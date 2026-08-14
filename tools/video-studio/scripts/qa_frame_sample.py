#!/usr/bin/env python3
"""Multi-checkpoint frame sampling for live/live_partial segments, closing the gap
verify_stitch_plan.py already flags in its own docstring: duration matching says
nothing about whether a segment spends most of its window stuck on a loading state.

This session's two most expensive real bugs (a domain-switch race condition, and two
rounds of a recording window being too short) were both caught by ad hoc, one-off
manual frame checks during live debugging -- never by a reusable tool. This
generalizes "check mid-window, not just the final frame" (GTM-ASSET-PLAYBOOK.md §4
rule 14) into full, repeatable coverage: 5 evenly-spaced checkpoints per segment
instead of one manual spot-check.

Heuristic, not a guarantee: computes a pixel-difference "possibly stuck" signal
between consecutive checkpoints, using the same PIL/numpy stack already established
in clean_notebooklm_slides.py. A SUSPECT flag means "a human (or an agent, via the
quality-review package produce_video.py builds) should actually look at these saved
frames" -- it does not mean the segment is provably broken, and a clean report does
not mean the segment is provably fine (a slow-panning but otherwise static beat can
legitimately have low frame-to-frame variance). This is a triage tool: it turns
"eyeball the whole video" into "look at these N flagged frames."

Usage:
    python qa_frame_sample.py <manifest.json> <output_dir>

manifest.json: same shape as verify_stitch_plan.py's manifest (a list of
{"label", "kind", "target_duration", "src"} objects) -- "graphic" segments and
segments with no `src` are skipped (nothing live to get stuck).

Output: <output_dir>/qa_report.json plus <output_dir>/<label>_<pct>pct.png for every
checkpoint frame, so a reviewer (or produce_video.py's quality-package stage) can
pull them up directly rather than re-extracting.
"""
import json
import pathlib
import subprocess
import sys

import numpy as np
from PIL import Image

CHECKPOINT_FRACTIONS = [0.10, 0.30, 0.50, 0.70, 0.90]
# Threshold on EDGE-MAP mean absolute difference (see _edge_magnitude below), not
# raw pixel values. Empirically necessary: tested against Video 3's 5 real, known-
# good, already-shipped segments, a raw-pixel mean-abs-diff between a genuine
# "Loading model registry..." spinner frame and a fully different, fully-loaded
# tab (real content, not a defect) scored only 3.64 -- BELOW a 6.0 raw-pixel
# threshold, a false SUSPECT flag -- because both frames share a large, dominant
# flat-white background that swamps the raw-pixel average even though the actual
# foreground content is completely different. Light, text/table-heavy dashboard
# UI (exactly this pipeline's typical subject) is the worst case for a raw-pixel
# metric for this reason. Edge-magnitude diffing is far more sensitive to real
# structural/content change (text strokes, table lines, a spinner glyph) and far
# less dominated by a shared flat background -- recalibrate this threshold again
# if a future video's false-positive/false-negative rate suggests it needs it.
STUCK_DIFF_THRESHOLD = 3.0
DOWNSAMPLE_SIZE = (384, 216)  # upsized from an initial 192x108 -- edge detection
                              # needs more resolution than a raw-pixel average did

# Calibration note, honestly: this threshold is set against 5 known-GOOD Video 3
# segments only (edge-diff scores 5.05-9.12) -- there was no known-stuck/defective
# recording still available to calibrate the other side. 3.0 sits well below every
# observed good-segment score, on the assumption that a genuinely frozen frame
# scores near 0. If a future video's actual stuck-frame bug is missed (or a good
# segment gets a new false positive), that's real evidence to retune this number --
# don't treat 3.0 as settled science.

FFMPEG_CANDIDATES = [
    pathlib.Path.home() / "enterprise-ai-gtm-skill/tools/video-studio/node_modules/ffmpeg-static/ffmpeg",
    pathlib.Path("ffmpeg"),
]


def find_ffmpeg():
    for candidate in FFMPEG_CANDIDATES:
        path = str(candidate)
        try:
            subprocess.run([path, "-version"], capture_output=True, check=True)
            return path
        except (FileNotFoundError, subprocess.CalledProcessError):
            continue
    raise RuntimeError("no working ffmpeg found -- checked: " + ", ".join(str(c) for c in FFMPEG_CANDIDATES))


def extract_checkpoint_frame(ffmpeg, src, timestamp_sec, out_path):
    subprocess.run([
        ffmpeg, "-y", "-i", str(src), "-ss", f"{timestamp_sec:.3f}",
        "-frames:v", "1", str(out_path),
    ], check=True, capture_output=True)


def _edge_magnitude(arr: np.ndarray) -> np.ndarray:
    """Simple gradient-magnitude edge map: robust to a shared flat background
    dominating a raw pixel-value comparison, sensitive to text/table/UI-element
    structure -- exactly the discriminator a raw mean-pixel-diff lacks (see the
    threshold comment above for the real false-positive this fixed)."""
    gray = arr.mean(axis=2)
    gx = np.abs(np.diff(gray, axis=1, prepend=gray[:, :1]))
    gy = np.abs(np.diff(gray, axis=0, prepend=gray[:1, :]))
    return gx + gy


def mean_abs_diff(path_a, path_b):
    a = np.array(Image.open(path_a).convert("RGB").resize(DOWNSAMPLE_SIZE), dtype=np.float32)
    b = np.array(Image.open(path_b).convert("RGB").resize(DOWNSAMPLE_SIZE), dtype=np.float32)
    return float(np.abs(_edge_magnitude(a) - _edge_magnitude(b)).mean())


def sample_segment(ffmpeg, label, src, target_duration, out_dir):
    frame_paths = []
    for frac in CHECKPOINT_FRACTIONS:
        timestamp = target_duration * frac
        out_path = out_dir / f"{label}_{int(frac * 100)}pct.png"
        extract_checkpoint_frame(ffmpeg, src, timestamp, out_path)
        frame_paths.append((frac, out_path))

    diffs = []
    for (frac_a, path_a), (frac_b, path_b) in zip(frame_paths, frame_paths[1:]):
        diffs.append(mean_abs_diff(path_a, path_b))

    # First-vs-last, not "most consecutive pairs are flat": a beat that loads
    # early and then legitimately HOLDS STILL for the rest of its window (the
    # desired pattern per GTM-ASSET-PLAYBOOK.md's "hold stills; never
    # slow-motion UI" rule) will show near-zero variance across its back half
    # by design -- penalizing that as "most pairs flat" produced false
    # positives on every one of Video 3's actual, known-good shipped segments
    # in testing. A genuinely stuck segment never visibly progresses AT ALL,
    # which shows up as low variance between the FIRST checkpoint and the
    # LAST one -- that's the signature this heuristic now targets.
    first_last_diff = mean_abs_diff(frame_paths[0][1], frame_paths[-1][1])
    suspect = first_last_diff < STUCK_DIFF_THRESHOLD

    return {
        "label": label,
        "frames": [str(p) for _, p in frame_paths],
        "consecutive_diffs": diffs,
        "first_last_diff": round(first_last_diff, 2),
        "verdict": "SUSPECT" if suspect else "OK",
        "note": (
            "near-zero variance between the first and last checkpoint -- the segment may "
            "never have visibly progressed past its initial state; look at the saved "
            "frames before accepting this segment"
            if suspect else
            "visible progression between first and last checkpoint -- still spot-check the "
            "frames, this is a heuristic, not a guarantee"
        ),
    }


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    manifest_data = json.loads(pathlib.Path(sys.argv[1]).read_text())
    # Accept either a bare segment list or the richer object shape
    # stitch_pipeline.py's manifest uses -- see verify_stitch_plan.py's identical
    # handling; both scripts share one manifest format via produce_video.py.
    manifest = manifest_data["segments"] if isinstance(manifest_data, dict) else manifest_data
    out_dir = pathlib.Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg = find_ffmpeg()

    results = []
    for seg in manifest:
        label = seg.get("label", "?")
        src = seg.get("src")
        if seg["kind"] == "graphic" or not src:
            continue
        src_path = pathlib.Path(src)
        if not src_path.exists():
            print(f"  {label:12s} SKIP -- source file missing: {src}")
            continue
        result = sample_segment(ffmpeg, label, src_path, seg["target_duration"], out_dir)
        results.append(result)
        marker = "!! SUSPECT !!" if result["verdict"] == "SUSPECT" else "OK"
        print(f"  {label:12s} {marker}  first-vs-last={result['first_last_diff']}  "
              f"diffs={[round(d, 1) for d in result['consecutive_diffs']]}")

    report_path = out_dir / "qa_report.json"
    report_path.write_text(json.dumps(results, indent=2))

    suspects = [r for r in results if r["verdict"] == "SUSPECT"]
    print(f"\n{len(results)} segments sampled, {len(suspects)} flagged SUSPECT.")
    print(f"Report + frames: {out_dir}")
    if suspects:
        print("Reminder: SUSPECT is a heuristic trigger, not proof of a defect -- open the "
              "saved frames for each flagged segment before deciding whether to re-record.")
    sys.exit(1 if suspects else 0)


if __name__ == "__main__":
    main()
