"""The video-production orchestrator: one entry point that runs the pipeline this
skill previously documented as prose steps ("generate narration, then render, then
record, then verify, then stitch") as actual enforced code instead.

Why this exists: every video built with this pipeline so far was produced by
manually running separate scripts in the right order, remembering the rules from
GTM-ASSET-PLAYBOOK.md's prose each time. That's a process a tool should own, not a
document a human/agent has to re-read and follow correctly every time. This does not
replace GTM-ASSET-PLAYBOOK.md -- it replaces the PROCEDURAL parts of it (what order,
what command). The judgment-requiring parts (brand voice, narrative rules, Rule 0
claim verification) still need a human/LLM to read and apply; they can't be
mechanically enforced, and stay in the doc.

Stages (run one at a time, in order -- each is idempotent so a failed `verify` does
not force re-running `narration`/`render`):

    python produce_video.py <spec.json> --stage narration
    python produce_video.py <spec.json> --stage render
    python produce_video.py <spec.json> --stage await-recording
        # STOPS here. This stage cannot proceed further itself: the live-capture
        # recording runs in the PRODUCT's own repo (e.g. cbp-risk-engine), using
        # Playwright against the real running app -- this orchestrator has no
        # reach into a different repo and should not pretend to. It writes the
        # recording target manifest and prints what to do next.
    python produce_video.py <spec.json> --stage verify [--override-qa-suspect]
        # Runs verify_stitch_plan.py (duration -- a real FAIL always blocks, no
        # override) and qa_frame_sample.py (the stuck-frame heuristic -- a SUSPECT
        # flag requires --override-qa-suspect to proceed past, an explicit
        # acknowledgment, never a silent skip).
    python produce_video.py <spec.json> --stage stitch
    python produce_video.py <spec.json> --stage quality-package
        # Extracts a frame at each beat's start from the FINAL stitched video and
        # writes review-prompt.md -- the handoff to an agent-driven qualitative
        # review of engagement/professionalism/brand consistency, which is a
        # judgment call no numeric heuristic in this pipeline can make.

spec.json shape (all paths resolve against the spec file's own directory, same
portability convention as stitch_pipeline.py's manifest):
{
  "narration_script": "narration_script.json",   // generate_narration_pipeline.py input
  "voices": "voices.json",                        // generate_narration_pipeline.py input
  "composition_id": "RiskForgeVideoXPanel",        // Remotion composition id (see src/Root.jsx)
  "render_output": "out/videoX.mp4",
  "stitch_manifest": "stitch_manifest.json",       // stitch_pipeline.py's manifest shape;
                                                     // its narration_wav/narration_timing_json
                                                     // fields should point at work_dir's outputs
  "recording_manifest_out": "recording_targets.json",
  "qa_output_dir": "qa_frames",
  "work_dir": "work"                                // narration outputs land here
}
"""
import argparse
import json
import pathlib
import subprocess
import sys

_HERE = pathlib.Path(__file__).resolve().parent
SCRIPTS = _HERE / "scripts"


def resolve(base_dir, value):
    p = pathlib.Path(value)
    return p if p.is_absolute() else (base_dir / p)


def load_spec(spec_path):
    spec_path = pathlib.Path(spec_path).resolve()
    base_dir = spec_path.parent
    raw = json.loads(spec_path.read_text())
    paths = {
        "narration_script": resolve(base_dir, raw["narration_script"]),
        "voices": resolve(base_dir, raw["voices"]),
        "render_output": resolve(base_dir, raw["render_output"]),
        "stitch_manifest": resolve(base_dir, raw["stitch_manifest"]),
        "recording_manifest_out": resolve(base_dir, raw["recording_manifest_out"]),
        "qa_output_dir": resolve(base_dir, raw["qa_output_dir"]),
        "work_dir": resolve(base_dir, raw["work_dir"]),
    }
    return raw, paths


def run(cmd, **kwargs):
    print(f"  $ {' '.join(str(c) for c in cmd)}")
    return subprocess.run(cmd, **kwargs)


def stage_narration(raw, paths):
    paths["work_dir"].mkdir(parents=True, exist_ok=True)
    result = run([
        sys.executable, str(_HERE / "generate_narration_pipeline.py"),
        str(paths["narration_script"]), str(paths["voices"]), str(paths["work_dir"]),
    ])
    result.check_returncode()


def stage_render(raw, paths):
    composition_id = raw["composition_id"]
    paths["render_output"].parent.mkdir(parents=True, exist_ok=True)
    result = run(
        ["npx", "remotion", "render", composition_id, str(paths["render_output"])],
        cwd=str(_HERE),
    )
    result.check_returncode()
    if not paths["render_output"].exists():
        raise RuntimeError(f"render reported success but {paths['render_output']} is missing")


def stage_await_recording(raw, paths):
    manifest = json.loads(paths["stitch_manifest"].read_text())
    targets = [
        {
            "label": seg.get("label", f"seg{i:02d}"),
            "kind": seg["kind"],
            "target_duration": seg["target_duration"],
            **({"full_duration": seg["full_duration"]} if "full_duration" in seg else {}),
            "src": seg.get("src"),
        }
        for i, seg in enumerate(manifest["segments"])
        if seg["kind"] in ("live", "live_partial")
    ]
    paths["recording_manifest_out"].parent.mkdir(parents=True, exist_ok=True)
    paths["recording_manifest_out"].write_text(json.dumps(targets, indent=2))

    print(f"\nWrote recording targets: {paths['recording_manifest_out']}")
    print(f"  {len(targets)} live-capture segment(s) needed:")
    for t in targets:
        print(f"    {t['label']:12s} {t['kind']:12s} target {t['target_duration']:.2f}s"
              + (f" (full window {t['full_duration']:.2f}s)" if "full_duration" in t else ""))
    print(
        "\nThis orchestrator cannot record these itself -- the live capture runs against\n"
        "the real product in ITS OWN repo, via Playwright. Next steps:\n"
        "  1. In the product repo's recording script, copy the poll-until-ready pattern\n"
        f"     from {SCRIPTS / 'recording_helpers.mjs'} (waitUntilSettled / waitUntilSpinnerGone)\n"
        "     in place of any fixed-sleep settle wait.\n"
        "  2. Record each beat listed above to the `src` path its stitch_manifest.json\n"
        "     segment expects (fill in `src` there if not already set).\n"
        f"  3. Re-run: python produce_video.py <spec.json> --stage verify\n"
    )


def stage_verify(raw, paths, override_qa_suspect):
    narration_timing = paths["work_dir"] / "narration_timing.json"
    duration_check = run([
        sys.executable, str(SCRIPTS / "verify_stitch_plan.py"),
        str(paths["stitch_manifest"]), str(narration_timing),
    ])
    if duration_check.returncode != 0:
        print("\nBLOCKED: duration check failed. This never has an override -- fix the "
              "underlying issue (missing file, stale path, real duration mismatch) and re-run.")
        sys.exit(1)

    paths["qa_output_dir"].mkdir(parents=True, exist_ok=True)
    qa_check = run([
        sys.executable, str(SCRIPTS / "qa_frame_sample.py"),
        str(paths["stitch_manifest"]), str(paths["qa_output_dir"]),
    ])
    if qa_check.returncode != 0:
        if override_qa_suspect:
            print(
                "\nProceeding past SUSPECT-flagged segment(s) per --override-qa-suspect -- "
                "reviewed and accepted. This acknowledgment is logged, not silent."
            )
        else:
            print(
                "\nBLOCKED: one or more segments flagged SUSPECT (possibly stuck on a "
                f"loading state). Open the frames in {paths['qa_output_dir']} and decide:\n"
                "  - real defect -> fix and re-record that beat, then re-run --stage verify\n"
                "  - false positive (e.g. a legitimately static beat) -> re-run with "
                "--override-qa-suspect to proceed"
            )
            sys.exit(1)

    print("\nverify stage PASSED -- safe to run --stage stitch")


def stage_stitch(raw, paths):
    result = run([
        sys.executable, str(_HERE / "stitch_pipeline.py"), str(paths["stitch_manifest"]),
    ])
    result.check_returncode()


def stage_quality_package(raw, paths):
    manifest = json.loads(paths["stitch_manifest"].read_text())
    output_path = resolve(paths["stitch_manifest"].parent, manifest["output_path"])
    if not output_path.exists():
        raise RuntimeError(f"final video not found at {output_path} -- run --stage stitch first")

    ffmpeg = str(_HERE / "node_modules/ffmpeg-static/ffmpeg")
    review_dir = paths["qa_output_dir"].parent / "quality_review"
    review_dir.mkdir(parents=True, exist_ok=True)

    cumulative = 0.0
    beat_frames = []
    for i, seg in enumerate(manifest["segments"]):
        label = seg.get("label", f"seg{i:02d}")
        # A couple seconds into the beat, not the exact cut point, to avoid an
        # in-transition/blend frame at the boundary.
        probe_time = cumulative + min(2.0, seg["target_duration"] / 2)
        frame_path = review_dir / f"{label}_start.png"
        subprocess.run([
            ffmpeg, "-y", "-i", str(output_path), "-ss", f"{probe_time:.3f}",
            "-frames:v", "1", str(frame_path),
        ], check=True, capture_output=True)
        beat_frames.append({
            "label": label, "kind": seg["kind"],
            "start_sec": round(cumulative, 2), "frame": str(frame_path),
        })
        cumulative += seg["target_duration"]

    narration_script_text = "(narration script not found -- see spec.json's narration_script path)"
    if paths["narration_script"].exists():
        raw_text = paths["narration_script"].read_text()
        try:
            script_entries = json.loads(raw_text)
            lines = []
            for entry in script_entries:
                text = entry["text"]
                if text.startswith("__VISUAL_"):
                    lines.append(f"[Beat {entry['beat']}] (visual only: {text})")
                else:
                    lines.append(f"[Beat {entry['beat']}] {entry.get('speaker')}: {text}")
            narration_script_text = "\n".join(lines)
        except (json.JSONDecodeError, KeyError, TypeError):
            # Not the script.json shape (e.g. an older video's plain-text script) --
            # fall back to showing it verbatim rather than failing the whole stage.
            narration_script_text = raw_text

    beat_table = "\n".join(
        f"| {b['label']} | {b['kind']} | {b['start_sec']:.1f}s | `{b['frame']}` |"
        for b in beat_frames
    )

    prompt = f"""# Quality review — {output_path.name}

An agent should read every frame listed below alongside this narration script and
score the final video against these dimensions. Report SPECIFIC findings tied to a
beat/timestamp, not a bare pass/fail — this is the check no mechanical heuristic in
this pipeline can do; the duration and stuck-frame checks (verify stage) already
passed before this package was built, so this is purely a judgment/engagement pass.

## Dimensions to score (see content/video/GTM-ASSET-PLAYBOOK.md for the full rules)

1. **BLUF / opening strength** — does the first beat compress to 3 lines or fewer and
   land as a fact/tension a stranger would understand cold (§13.4's compression test)?
2. **Narrative pacing and engagement** — does the sequence read as argument -> proof,
   alternating explain/proof beats per §1, or does any stretch feel like a feature
   tour / theoretical lecture (the two failure modes §1 names explicitly)?
3. **Brand and visual consistency** — do the explain beats match DESIGN-SYSTEM.md's
   verified tokens (dark slate ground, Inter, blue/teal/purple/green accent family),
   and is there a consistent visual world within each beat (§4 rule 3)?
4. **The "quality video publishing shop" bar** — read literally from the Video 2
   editorial-pass addendum (§12): does this look correct-but-rough, or does it read
   as coming from a shop that does this professionally? Call out anything that reads
   as an AI-generated first draft rather than a finished asset.

## Beats (in final playback order)

| Beat | Kind | Starts at | Frame |
|---|---|---|---|
{beat_table}

## Narration script (source of truth for what each beat is supposed to say)

```
{narration_script_text}
```
"""
    (review_dir / "review-prompt.md").write_text(prompt)
    print(f"\nQuality-review package written: {review_dir}")
    print(f"  {len(beat_frames)} beat-start frames + review-prompt.md")
    print("  Have an agent read review-prompt.md (it embeds the frame paths and the "
          "narration script) before declaring this video done.")


STAGES = {
    "narration": stage_narration,
    "render": stage_render,
    "await-recording": stage_await_recording,
    "verify": stage_verify,
    "stitch": stage_stitch,
    "quality-package": stage_quality_package,
}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("spec", help="path to spec.json")
    parser.add_argument("--stage", required=True, choices=list(STAGES.keys()))
    parser.add_argument("--override-qa-suspect", action="store_true",
                         help="acknowledge and proceed past a SUSPECT frame-QA flag (verify stage only)")
    args = parser.parse_args()

    raw, paths = load_spec(args.spec)
    print(f"=== stage: {args.stage} ===")

    if args.stage == "verify":
        stage_verify(raw, paths, args.override_qa_suspect)
    else:
        STAGES[args.stage](raw, paths)


if __name__ == "__main__":
    main()
