"""SUPERSEDED for future videos by stitch_pipeline.py (manifest-driven) --
kept as reference/fallback; see stitch_video3.manifest.json for this video's
segment list re-encoded as the new manifest format.

Final assembly for Video 3: normalizes the 5 recorded live-capture clips
and the 4 Remotion graphic segments to a common 1920x1080/30fps format,
concatenates them in the correct order, then muxes the (already beat-5-
corrected) narration track over the result.

Trim math for each live clip uses the "take the tail" rule established
during recording verification: Playwright's recordVideo has a small,
consistent startup overhead (each raw clip runs ~1.2-2.6s longer than its
target), so skipping that amount off the FRONT (not the back) keeps the
settled, fully-loaded state that sits at the end of every clip.
"""
import pathlib
import subprocess

_HERE = pathlib.Path(__file__).resolve().parent
FFMPEG = str(pathlib.Path.home() / "enterprise-ai-gtm-skill/tools/video-studio/node_modules/ffmpeg-static/ffmpeg")
BEATS_DIR = pathlib.Path("/tmp/video3beats/video3-live-beats")  # downloaded recording artifacts
VIDEOC = _HERE / "out/videoC.mp4"
WORK_DIR = _HERE / "out/stitch"
WORK_DIR.mkdir(parents=True, exist_ok=True)

PAD_COLOR = "0x0B1220"  # RF.bgDeep -- so pillarbox bars tonally match the graphic beats

def probe_duration(path):
    out = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True).stderr
    for line in out.splitlines():
        if "Duration:" in line:
            h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    raise RuntimeError(f"could not probe duration of {path}")

def normalize_live(src, target_dur, out_path):
    raw_dur = probe_duration(src)
    skip = max(0.0, raw_dur - target_dur)
    # -ss AFTER -i (not before) -- frame-accurate seeking, not
    # nearest-keyframe. These clips are short (<40s) so the decode-from-start
    # cost is negligible; accuracy matters far more here since drift
    # compounds across 9 concatenated segments.
    subprocess.run([
        FFMPEG, "-y", "-i", str(src), "-ss", f"{skip:.3f}", "-t", f"{target_dur:.3f}",
        "-vf", f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color={PAD_COLOR},fps=30",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-an", str(out_path),
    ], check=True)

def extract_graphic(start, end, out_path):
    subprocess.run([
        FFMPEG, "-y", "-i", str(VIDEOC), "-ss", f"{start:.3f}", "-t", f"{end - start:.3f}",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-an", str(out_path),
    ], check=True)

# (kind, args, target_duration) in final playback order
SEGMENTS = [
    ("graphic", (0.0, 16.275), 16.275),
    ("graphic", (16.275, 44.835), 28.56),
    ("live", (BEATS_DIR / "beat2.webm",), 35.5),
    ("live_partial", (BEATS_DIR / "beat3.webm", 20.937), 20.937),  # only the pre-graphic portion
    ("graphic", (44.835, 55.547), 10.712),
    ("live", (BEATS_DIR / "beat4.webm",), 19.658),
    ("live", (BEATS_DIR / "beat5.webm",), 19.0),
    ("live", (BEATS_DIR / "beat7.webm",), 20.0),
    ("graphic", (55.547, 75.301), 75.301 - 55.547),  # beats 8 + 9, contiguous in videoC
]

clip_paths = []
for i, (kind, args, dur) in enumerate(SEGMENTS):
    out_path = WORK_DIR / f"seg{i:02d}.mp4"
    if kind == "graphic":
        start, end = args
        extract_graphic(start, end, out_path)
    elif kind == "live":
        (src,) = args
        normalize_live(src, dur, out_path)
    elif kind == "live_partial":
        src, partial_dur = args
        # "take the tail" rule doesn't apply here -- we want the FRONT portion
        # of the beat (before the graphic cutaway), not the settled tail, so
        # just take the clip's own front after skipping the startup overshoot.
        raw_dur = probe_duration(src)
        # beat3's own full target was 31.649s; skip is computed against THAT,
        # then we take only the first `partial_dur` seconds of the result.
        full_target = 111.984 - 80.335
        skip = max(0.0, raw_dur - full_target)
        subprocess.run([
            FFMPEG, "-y", "-i", str(src), "-ss", f"{skip:.3f}", "-t", f"{partial_dur:.3f}",
            "-vf", f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color={PAD_COLOR},fps=30",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-an", str(out_path),
        ], check=True)
    clip_paths.append(out_path)
    print(f"seg{i:02d} ({kind}, target {dur:.2f}s) -> {out_path}")

concat_list = WORK_DIR / "concat.txt"
concat_list.write_text("\n".join(f"file '{p.resolve()}'" for p in clip_paths))

silent_video = WORK_DIR / "video3_silent.mp4"
subprocess.run([
    FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list),
    "-c", "copy", str(silent_video),
], check=True)
print(f"Concatenated silent video: {silent_video}")

final_out = _HERE / "video3_FINAL.mp4"
subprocess.run([
    FFMPEG, "-y", "-i", str(silent_video), "-i", str(_HERE / "master_narration.wav"),
    "-c:v", "copy", "-c:a", "aac", "-shortest", str(final_out),
], check=True)
print(f"\nFinal video: {final_out}")
