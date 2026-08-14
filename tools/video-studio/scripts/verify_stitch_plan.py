"""Verify a stitch manifest's real segment durations against their planned targets,
BEFORE any concatenation happens.

Added 2026-08-14 after Video 3's stitch process caught two real bugs the hard way:
a stale-file bug (one segment silently read an old, broken recording from a
different temp path than the corrected one) and two rounds of a beat's recorded
window being too short despite passing at the final frame. Both would have been
caught mechanically by this check instead of by a failed/wrong assembly.

This does NOT replace the manual mid-window frame-sample check (GTM-ASSET-PLAYBOOK.md
§4 rule 14) -- a segment can have the exact right duration and still spend most of
that duration stuck on a loading spinner. Duration matching is necessary, not
sufficient.

Usage:
    python verify_stitch_plan.py <manifest.json> <narration_timing.json>

manifest.json shape (same fields as stitch_video3.py's SEGMENTS, as objects):
[
  {"label": "seg00", "kind": "graphic", "target_duration": 16.275},
  {"label": "seg02", "kind": "live", "target_duration": 35.5, "src": "/tmp/.../beat2.webm"},
  ...
]
"graphic" segments have no `src` -- they're trusted to the render step and skipped
here (nothing external to go stale). "live" and "live_partial" segments must have
`src` pointing at the real recorded file being assembled.

narration_timing.json shape: {"total_duration_sec": <float>, "lines": [...]}
"""
import json
import pathlib
import subprocess
import sys

TOLERANCE_SEC = 0.15

FFPROBE_CANDIDATES = [
    pathlib.Path.home() / "enterprise-ai-gtm-skill/tools/video-studio/node_modules/@remotion/compositor-linux-x64-gnu/ffprobe",
    pathlib.Path("ffprobe"),
]


def find_ffprobe():
    for candidate in FFPROBE_CANDIDATES:
        path = str(candidate)
        try:
            subprocess.run([path, "-version"], capture_output=True, check=True)
            return path
        except (FileNotFoundError, subprocess.CalledProcessError):
            continue
    raise RuntimeError("no working ffprobe found -- checked: " + ", ".join(str(c) for c in FFPROBE_CANDIDATES))


def probe_duration(ffprobe, path):
    out = subprocess.run(
        [ffprobe, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    manifest = json.loads(pathlib.Path(sys.argv[1]).read_text())
    narration = json.loads(pathlib.Path(sys.argv[2]).read_text())
    ffprobe = find_ffprobe()

    ok = True
    planned_total = 0.0
    for seg in manifest:
        label = seg.get("label", "?")
        target = seg["target_duration"]
        planned_total += target
        src = seg.get("src")

        if seg["kind"] == "graphic" or not src:
            print(f"  {label:12s} [{seg['kind']:12s}] target {target:6.2f}s  (rendered, not probed)")
            continue

        src_path = pathlib.Path(src)
        if not src_path.exists():
            print(f"  {label:12s} [{seg['kind']:12s}] MISSING FILE: {src}")
            ok = False
            continue

        actual = probe_duration(ffprobe, src_path)
        # segments trim/skip within a longer raw file, so `actual` (the raw
        # source's full length) only needs to be >= target, not equal to it.
        if actual + TOLERANCE_SEC < target:
            print(f"  {label:12s} [{seg['kind']:12s}] target {target:6.2f}s  raw {actual:6.2f}s  "
                  f"FAIL -- raw source is shorter than the planned trim")
            ok = False
        else:
            print(f"  {label:12s} [{seg['kind']:12s}] target {target:6.2f}s  raw {actual:6.2f}s  OK")

    narration_total = narration["total_duration_sec"]
    print(f"\nPlanned segment total:   {planned_total:.3f}s")
    print(f"Narration total:         {narration_total:.3f}s")
    if abs(planned_total - narration_total) > TOLERANCE_SEC:
        print(f"FAIL -- segment plan and narration total differ by "
              f"{abs(planned_total - narration_total):.3f}s (tolerance {TOLERANCE_SEC}s)")
        ok = False

    print("\n" + ("PASS -- safe to stitch" if ok else "FAIL -- fix the above before stitching"))
    print("Reminder: this checks duration only. Still do a manual mid-window frame-sample "
          "check on every live segment (GTM-ASSET-PLAYBOOK.md §4 rule 14) -- a segment can "
          "be the right length and still be stuck on a spinner for most of it.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
