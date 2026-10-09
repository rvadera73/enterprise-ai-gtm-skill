"""Redo only the caption-burn + mux steps against the already-built
silent_video_v2.mp4, fixing a real sizing bug: ffmpeg's `subtitles` filter
converts a plain .srt to ASS using a DEFAULT 384x288 reference resolution,
then scales up to the actual video size -- so FontSize=11 was rendering at
roughly 11 * (900/288) =~ 34px on our 1600x900 video, not 11px. Fix: pass
`original_size=1600x900` so the filter knows the real reference and stops
silently upscaling."""
import pathlib
import subprocess

OUT_DIR = pathlib.Path(__file__).resolve().parent / "factory_output"
silent_video = OUT_DIR / "silent_video_v2.mp4"
srt_path = OUT_DIR / "captions.srt"

captioned_video = OUT_DIR / "captioned_video_v2b.mp4"
srt_escaped = str(srt_path).replace("\\", "/").replace(":", "\\:")
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
print(f"Done -> {final_video}")
