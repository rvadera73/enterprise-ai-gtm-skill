"""Manifest-driven final-assembly pipeline, generalized from stitch_video3.py
(which hard-coded one specific video's beat list, durations, and paths).

Takes a single JSON manifest describing an ordered list of segments --
Remotion-rendered "graphic" ranges extracted from a rendered composition
(e.g. SharedVideoPanel.jsx's output), plus Playwright-recorded "live" or
"live_partial" clips -- normalizes them all to a common 1920x1080/30fps
format, concatenates them in order, then muxes a narration track over the
result. Any future video's stitch becomes a new manifest, not a new script.

Usage:
    python stitch_pipeline.py <manifest.json>

Manifest shape:
{
  "videoc_path": "out/videoC.mp4",              # rendered graphic composition
  "narration_wav": "master_narration.wav",
  "narration_timing_json": "narration_timing.json",  # optional: sanity-checks total duration, doesn't block the stitch
  "output_path": "video3_FINAL.mp4",
  "segments": [
    {"kind": "graphic", "start": 0.0, "end": 16.275, "target_duration": 16.275},
    {"kind": "live", "src": "beats/beat2.webm", "target_duration": 35.5},
    {"kind": "live_partial", "src": "beats/beat3.webm", "target_duration": 20.937, "full_duration": 31.649},
    ...
  ]
}

All relative paths in the manifest (videoc_path, narration_wav,
narration_timing_json, output_path, and each segment's "src") resolve
against the MANIFEST FILE's own directory -- not the caller's cwd -- so a
manifest is portable. Absolute paths (e.g. downloaded recording artifacts
living outside the repo) pass through unchanged.

See stitch_video3.manifest.json for a worked example: Video 3's actual
segment list from stitch_video3.py, encoded as manifest data so this
pipeline is proven against real data, not just a theoretical schema.

Preserves stitch_video3.py's exact ffmpeg mechanics:
  - "-ss" placed AFTER "-i" for frame-accurate (not nearest-keyframe) seeking
  - PAD_COLOR pillarboxing so pad bars tonally match the graphic beats
  - the live_partial special case: front-trim to the beat's own FULL target
    duration first (not the partial one), then keep only the first
    `target_duration` seconds -- the pre-cutaway portion, not the settled tail
"""
import json
import pathlib
import subprocess
import sys

FFMPEG = str(pathlib.Path.home() / "enterprise-ai-gtm-skill/tools/video-studio/node_modules/ffmpeg-static/ffmpeg")
PAD_COLOR = "0x0B1220"  # RF.bgDeep -- so pillarbox bars tonally match the graphic beats


def probe_duration(path):
    out = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True).stderr
    for line in out.splitlines():
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"could not probe duration of {path}")


def resolve(base_dir, value):
    """Relative paths resolve against the manifest file's own directory;
    absolute paths pass through unchanged."""
    p = pathlib.Path(value)
    return p if p.is_absolute() else (base_dir / p)


def normalize_live(src, target_dur, out_path):
    raw_dur = probe_duration(src)
    skip = max(0.0, raw_dur - target_dur)
    # -ss AFTER -i (not before) -- frame-accurate seeking, not
    # nearest-keyframe. These clips are short so decode-from-start cost is
    # negligible; accuracy matters far more since drift compounds across
    # many concatenated segments. "Take the tail" rule: Playwright's
    # recordVideo has a small, consistent startup overhead, so skipping that
    # amount off the FRONT keeps the settled, fully-loaded state at the end.
    subprocess.run([
        FFMPEG, "-y", "-i", str(src), "-ss", f"{skip:.3f}", "-t", f"{target_dur:.3f}",
        "-vf", f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color={PAD_COLOR},fps=30",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-an", str(out_path),
    ], check=True)


def normalize_live_partial(src, target_dur, full_dur, out_path):
    # "take the tail" rule doesn't apply here -- we want the FRONT portion of
    # the beat (before its graphic cutaway), not the settled tail. The skip
    # is computed against the beat's own FULL target duration (`full_dur`,
    # i.e. what the beat's complete recording window was meant to be), then
    # only the first `target_dur` seconds of that result are kept.
    raw_dur = probe_duration(src)
    skip = max(0.0, raw_dur - full_dur)
    subprocess.run([
        FFMPEG, "-y", "-i", str(src), "-ss", f"{skip:.3f}", "-t", f"{target_dur:.3f}",
        "-vf", f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color={PAD_COLOR},fps=30",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-an", str(out_path),
    ], check=True)


def extract_graphic(videoc_path, start, end, out_path):
    subprocess.run([
        FFMPEG, "-y", "-i", str(videoc_path), "-ss", f"{start:.3f}", "-t", f"{end - start:.3f}",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-an", str(out_path),
    ], check=True)


def main(manifest_arg):
    manifest_path = pathlib.Path(manifest_arg).resolve()
    base_dir = manifest_path.parent
    manifest = json.loads(manifest_path.read_text())

    videoc_path = resolve(base_dir, manifest["videoc_path"])
    narration_wav = resolve(base_dir, manifest["narration_wav"])
    output_path = resolve(base_dir, manifest["output_path"])
    narration_timing_json = manifest.get("narration_timing_json")

    work_dir = output_path.parent / f"{output_path.stem}_stitch_work"
    work_dir.mkdir(parents=True, exist_ok=True)

    clip_paths = []
    for i, seg in enumerate(manifest["segments"]):
        kind = seg["kind"]
        out_path = work_dir / f"seg{i:02d}.mp4"
        if kind == "graphic":
            extract_graphic(videoc_path, seg["start"], seg["end"], out_path)
        elif kind == "live":
            normalize_live(resolve(base_dir, seg["src"]), seg["target_duration"], out_path)
        elif kind == "live_partial":
            normalize_live_partial(
                resolve(base_dir, seg["src"]), seg["target_duration"], seg["full_duration"], out_path
            )
        else:
            raise ValueError(f"unknown segment kind: {kind!r}")
        clip_paths.append(out_path)
        print(f"seg{i:02d} ({kind}, target {seg['target_duration']:.2f}s) -> {out_path}")

    concat_list = work_dir / "concat.txt"
    concat_list.write_text("\n".join(f"file '{p.resolve()}'" for p in clip_paths))

    silent_video = work_dir / "silent.mp4"
    subprocess.run([
        FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
        "-c", "copy", str(silent_video),
    ], check=True)
    print(f"Concatenated silent video: {silent_video}")

    # Optional sanity check against the narration timing log -- doesn't block
    # the stitch, just flags drift before publishing rather than after.
    if narration_timing_json:
        timing_path = resolve(base_dir, narration_timing_json)
        if timing_path.exists():
            timing = json.loads(timing_path.read_text())
            expected = timing.get("total_duration_sec")
            actual = sum(seg["target_duration"] for seg in manifest["segments"])
            if expected is not None and abs(expected - actual) > 1.0:
                print(
                    f"WARNING: segment total ({actual:.2f}s) differs from "
                    f"narration timing total ({expected:.2f}s) by more than 1s"
                )

    subprocess.run([
        FFMPEG, "-y", "-i", str(silent_video), "-i", str(narration_wav),
        "-c:v", "copy", "-c:a", "aac", "-shortest", str(output_path),
    ], check=True)
    print(f"\nFinal video: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python stitch_pipeline.py <manifest.json>")
        sys.exit(1)
    main(sys.argv[1])
