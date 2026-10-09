"""v2 assembly: real artifact-page backdrops (crops of the actual approved
pipeline artifact, not invented flat mockups) with the real terminal/YAML
captures animating in as a fade-in overlay -- per user feedback 2026-08-27
("looks like cmd line everywhere", "last one is very basic", "use the
preview of this page as backdrop ... animating these cmd lines").

Per-beat segments (each its own short mp4, then concatenated):
  beat 1: real "Development + CI Pipeline" cards backdrop, health-check
          terminal fades in at t=4s
  beat 2: existing reframe card (unchanged)
  beat 3: existing contrast card (unchanged)
  beat 4: real "Dispatch Engine" card backdrop, real YAML fades in at t=3s
  beat 5: real "Live:" lines backdrop, health-check terminal fades in at t=3s
  beat 6: full real artifact page -- the complete reveal, static
"""
import json
import pathlib
import subprocess

_HERE = pathlib.Path(__file__).resolve().parent
ASSETS = _HERE.parent.parent / "examples" / "foundry" / "assets"
V2 = _HERE / "assets_v2"
V3 = _HERE / "assets_v3"
OUT_DIR = _HERE / "factory_output"

timing = json.loads((OUT_DIR / "narration_timing.json").read_text())
beats = timing["beats"]
lines = timing["lines"]
total = timing["total_duration_sec"]

beat_order = [str(i) for i in range(1, 7)]
segment_durations = {}
for i, b in enumerate(beat_order):
    start = beats[b]["start"]
    end = beats[beat_order[i + 1]]["start"] if i + 1 < len(beat_order) else total
    segment_durations[b] = round(end - start, 3)

print("Segment durations:", segment_durations)


def render_static(image_path, duration, out_path):
    cmd = [
        "ffmpeg", "-y", "-loop", "1", "-i", str(image_path), "-t", str(duration),
        "-vf", "scale=1600:900,fps=30,format=yuv420p",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", str(out_path),
    ]
    subprocess.run(cmd, check=True)


def render_fade_in_overlay(bg_path, inset_path, duration, fade_start, overlay_xy, out_path):
    """Backdrop held for `duration`; inset image fades in starting at
    `fade_start` seconds and stays visible for the rest of the segment."""
    x, y = overlay_xy
    fade_dur = 0.6
    filter_complex = (
        f"[0:v]scale=1600:900,fps=30,format=yuv420p[bg];"
        f"[1:v]format=rgba,"
        f"fade=in:st={fade_start}:d={fade_dur}:alpha=1[inset];"
        f"[bg][inset]overlay=x={x}:y={y}:format=auto[outv]"
    )
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(bg_path), "-t", str(duration),
        "-loop", "1", "-i", str(inset_path), "-t", str(duration),
        "-filter_complex", filter_complex,
        "-map", "[outv]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", str(out_path),
    ]
    subprocess.run(cmd, check=True)


segment_files = []

# Beat 1 -- real cards backdrop, health-check fades in partway through
seg = OUT_DIR / "seg1.mp4"
render_fade_in_overlay(V2 / "beat1-bg.png", V2 / "inset-healthcheck.png",
                       segment_durations["1"], fade_start=4.0, overlay_xy=(1040, 560), out_path=seg)
segment_files.append(seg)

# Beat 2 -- unchanged reframe card
seg = OUT_DIR / "seg2.mp4"
render_static(ASSETS / "beat2-reframe.png", segment_durations["2"], seg)
segment_files.append(seg)

# Beat 3 -- unchanged contrast card
seg = OUT_DIR / "seg3.mp4"
render_static(ASSETS / "beat3-contrast.png", segment_durations["3"], seg)
segment_files.append(seg)

# Beat 4 -- real dispatch-engine backdrop, real YAML fades in near the
# config-strip line it actually corresponds to
seg = OUT_DIR / "seg4.mp4"
render_fade_in_overlay(V2 / "beat4-bg.png", V2 / "inset-yaml.png",
                       segment_durations["4"], fade_start=3.0, overlay_xy=(1000, 40), out_path=seg)
segment_files.append(seg)

# Beat 5 -- real "Live:" lines backdrop, health-check fades in confirming "running for real"
seg = OUT_DIR / "seg5.mp4"
render_fade_in_overlay(V2 / "beat5-bg.png", V2 / "inset-healthcheck-big.png",
                       segment_durations["5"], fade_start=3.0, overlay_xy=(900, 520), out_path=seg)
segment_files.append(seg)

# Beat 6 -- the complete real page, full reveal (v3: corrected "Unified Case
# Management System" text, re-rendered from the fixed artifact source)
seg = OUT_DIR / "seg6.mp4"
render_static(V3 / "beat6-full-reveal.png", segment_durations["6"], seg)
segment_files.append(seg)

# --- concat all 6 real segments (re-encoded, not stream-copy, since filter
# chains differ per segment) ---
concat_list_path = OUT_DIR / "concat_list_v2.txt"
with open(concat_list_path, "w") as f:
    for seg in segment_files:
        f.write(f"file '{seg.as_posix()}'\n")

silent_video = OUT_DIR / "silent_video_v2.mp4"
cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list_path),
    "-c:v", "libx264", "-pix_fmt", "yuv420p", str(silent_video),
]
subprocess.run(cmd, check=True)


def srt_time(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int(round((t - int(t)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


srt_path = OUT_DIR / "captions.srt"
with open(srt_path, "w") as f:
    for i, line in enumerate(lines, start=1):
        f.write(f"{i}\n")
        f.write(f"{srt_time(line['start'])} --> {srt_time(line['end'])}\n")
        f.write(f"{line['speaker']}: {line['text']}\n\n")

captioned_video = OUT_DIR / "captioned_video_v2.mp4"
srt_escaped = str(srt_path).replace("\\", "/").replace(":", "\\:")
# Smaller font (was 16 -- "caption should be small, it's very big") + tighter
# margin so it reads as a caption, not a dominant on-screen block.
subtitle_style = (
    "FontName=Arial,FontSize=8,PrimaryColour=&H00FFFFFF,"
    "OutlineColour=&H00000000,BorderStyle=3,Outline=1,Shadow=0,"
    "Alignment=2,MarginV=18"
)
cmd = [
    "ffmpeg", "-y", "-i", str(silent_video),
    "-vf", f"subtitles='{srt_escaped}':force_style='{subtitle_style}'",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", str(captioned_video),
]
subprocess.run(cmd, check=True)

final_video = OUT_DIR / "AI-Assisted-Software-Factory-FINAL-v2.mp4"
cmd = [
    "ffmpeg", "-y", "-i", str(captioned_video), "-i", str(OUT_DIR / "master_narration.wav"),
    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
    "-map", "0:v:0", "-map", "1:a:0", "-shortest",
    str(final_video),
]
subprocess.run(cmd, check=True)

print(f"\nDone -> {final_video}")
