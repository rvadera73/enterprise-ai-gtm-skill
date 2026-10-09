"""Assemble the final "AI-Assisted Software Factory" internal video from the
real narration audio + timing (factory_output/) and the 6 rendered beat
images (../../examples/foundry/assets/). Pure ffmpeg -- no Remotion project,
per the loop instruction to keep this as simple/robust as time allows.

Approach:
  1. Segment the beat-start timestamps (not per-line) into image hold
     durations, so audio gaps between lines are absorbed into holding the
     current beat's image a little longer -- avoids a black-frame gap.
  2. Build a silent video via the concat demuxer (image2 + duration list).
  3. Generate an SRT from the per-line timing (short rolling captions, one
     cue per narration line -- matches the line boundaries exactly, not a
     guess).
  4. Burn the SRT onto the video with the subtitles filter.
  5. Mux against master_narration.wav (audio is already the correct total
     length; video built to match it exactly from the same timing file).
"""
import json
import pathlib
import subprocess

_HERE = pathlib.Path(__file__).resolve().parent
ASSETS = _HERE.parent.parent / "examples" / "foundry" / "assets"
OUT_DIR = _HERE / "factory_output"

timing = json.loads((OUT_DIR / "narration_timing.json").read_text())
beats = timing["beats"]
lines = timing["lines"]
total = timing["total_duration_sec"]

beat_starts = sorted(((float(b), k) for k, b in ((k, v["start"]) for k, v in beats.items())), key=lambda x: x[0])
beat_order = [k for _, k in beat_starts]

# beat -> segment duration = (next beat's start, or total) - this beat's start
segment_durations = {}
for i, b in enumerate(beat_order):
    start = beats[b]["start"]
    end = beats[beat_order[i + 1]]["start"] if i + 1 < len(beat_order) else total
    segment_durations[b] = round(end - start, 3)

print("Segment durations (beat -> seconds):", segment_durations)

# beat -> list of (image_path, duration) -- beat 1 splits into repo-tree then
# health-check; beat 5 reuses the health-check image (per storyboard's benefit
# beat calling for the same honest-local proof, not a new capture).
BEAT1_SPLIT = 10.0  # seconds on beat1-repotree.png before cutting to the health-check terminal
segments = []
for b in beat_order:
    dur = segment_durations[b]
    if b == "1":
        segments.append((ASSETS / "beat1-repotree.png", BEAT1_SPLIT))
        segments.append((ASSETS / "beat-healthcheck.png", round(dur - BEAT1_SPLIT, 3)))
    elif b == "2":
        segments.append((ASSETS / "beat2-reframe.png", dur))
    elif b == "3":
        segments.append((ASSETS / "beat3-contrast.png", dur))
    elif b == "4":
        segments.append((ASSETS / "beat4-mechanism.png", dur))
    elif b == "5":
        segments.append((ASSETS / "beat-healthcheck.png", dur))
    elif b == "6":
        segments.append((ASSETS / "beat6-close.png", dur))

for img, dur in segments:
    assert img.exists(), f"missing asset: {img}"
    assert dur > 0, f"non-positive duration for {img}: {dur}"

concat_list_path = OUT_DIR / "concat_list.txt"
with open(concat_list_path, "w") as f:
    for img, dur in segments:
        f.write(f"file '{img.as_posix()}'\n")
        f.write(f"duration {dur}\n")
    # concat demuxer quirk: the last listed file needs to be repeated without
    # a duration line, or its duration is ignored (well-documented ffmpeg gotcha)
    f.write(f"file '{segments[-1][0].as_posix()}'\n")

silent_video = OUT_DIR / "silent_video.mp4"
cmd = [
    "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list_path),
    "-vf", "scale=1600:900,fps=30,format=yuv420p",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", str(silent_video),
]
print("Building silent video:", " ".join(cmd))
subprocess.run(cmd, check=True)

# --- SRT captions, one cue per real narration line ---
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
        speaker = line["speaker"]
        f.write(f"{speaker}: {line['text']}\n\n")

print(f"Wrote {srt_path}")

captioned_video = OUT_DIR / "captioned_video.mp4"
srt_escaped = str(srt_path).replace("\\", "/").replace(":", "\\:")
subtitle_style = (
    "FontName=Arial,FontSize=16,PrimaryColour=&H00FFFFFF,"
    "OutlineColour=&H00000000,BorderStyle=3,Outline=1,Shadow=0,"
    "Alignment=2,MarginV=30"
)
cmd = [
    "ffmpeg", "-y", "-i", str(silent_video),
    "-vf", f"subtitles='{srt_escaped}':force_style='{subtitle_style}'",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", str(captioned_video),
]
print("Burning captions:", " ".join(cmd))
subprocess.run(cmd, check=True)

final_video = OUT_DIR / "AI-Assisted-Software-Factory-FINAL.mp4"
cmd = [
    "ffmpeg", "-y", "-i", str(captioned_video), "-i", str(OUT_DIR / "master_narration.wav"),
    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
    "-map", "0:v:0", "-map", "1:a:0", "-shortest",
    str(final_video),
]
print("Muxing final:", " ".join(cmd))
subprocess.run(cmd, check=True)

print(f"\nDone -> {final_video}")
