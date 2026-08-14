"""Manifest-driven narration generator, generalized from generate_narration.py (which
hard-coded Video 3's specific script as a Python literal -- reusable only by editing
the file directly). Same generalization pattern as stitch_video3.py -> stitch_pipeline.py:
the old file stays as Video 3's reference implementation; this is what a NEW video's
narration stage (via produce_video.py) actually calls.

Preserves generate_narration.py's exact TTS/silence/timing logic:
  - one Cartesia TTS call per line (sonic-2, pcm_s16le -- NOT pcm_f32le, which
    Python's stdlib wave module can't parse)
  - "__VISUAL_..." text entries are silent visual-only beats: no speech, just the
    pause duration counted as an on-screen hold
  - silence gaps inserted after each line per its own pause_after value
  - a full per-line timing log (start/end seconds) for driving downstream recording

Usage:
    python generate_narration_pipeline.py <script.json> <voices.json> <output_dir>

script.json: a list of {"beat": "0", "speaker": "Rahul"|"Emma"|null, "text": "...",
"pause_after": 0.6} objects, in narration order. A `text` starting with "__VISUAL_"
is a silent visual-only beat (speaker should be null).

voices.json: {"Rahul": "<cartesia voice id>", "Emma": "<cartesia voice id>"} -- maps
every speaker name used in script.json to a real Cartesia voice ID.

Writes <output_dir>/master_narration.wav and <output_dir>/narration_timing.json.
"""
import io
import json
import os
import pathlib
import sys
import wave

from cartesia import Cartesia

_HERE = pathlib.Path(__file__).resolve().parent
SAMPLE_RATE = 44100


def _load_env_local():
    env_path = _HERE / ".env.local"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def render_line(client, text: str, voice_id: str) -> bytes:
    chunks = client.tts.bytes(
        model_id="sonic-2",
        transcript=text,
        voice={"mode": "id", "id": voice_id},
        output_format={"container": "wav", "encoding": "pcm_s16le", "sample_rate": SAMPLE_RATE},
    )
    return b"".join(chunks)


def wav_bytes_to_frames(wav_bytes: bytes) -> tuple[bytes, int, int]:
    with wave.open(io.BytesIO(wav_bytes), "rb") as w:
        return w.readframes(w.getnframes()), w.getnchannels(), w.getsampwidth()


def silence_frames(seconds: float, channels: int, sampwidth: int) -> bytes:
    n_frames = int(seconds * SAMPLE_RATE)
    return b"\x00" * (n_frames * channels * sampwidth)


def generate(script, voices, out_dir: pathlib.Path):
    _load_env_local()
    client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])

    lines_dir = out_dir / "narration_lines"
    lines_dir.mkdir(parents=True, exist_ok=True)

    timing = []
    t = 0.0
    master_frames = b""
    channels = None
    sampwidth = None

    for i, entry in enumerate(script):
        beat = entry["beat"]
        speaker = entry.get("speaker")
        text = entry["text"]
        pause_after = entry.get("pause_after", 0.0)

        if text.startswith("__VISUAL_"):
            timing.append({"index": i, "beat": beat, "speaker": None, "text": text,
                            "start": round(t, 3), "end": round(t, 3)})
            if channels is not None:
                master_frames += silence_frames(pause_after, channels, sampwidth)
            t += pause_after
            continue

        if speaker not in voices:
            raise KeyError(f"line {i} uses speaker {speaker!r}, not present in voices.json ({list(voices)})")

        print(f"[{i}] Beat {beat} {speaker}: {text[:60]}...")
        wav_bytes = render_line(client, text, voices[speaker])
        (lines_dir / f"{i:03d}_{beat}_{speaker}.wav").write_bytes(wav_bytes)
        frames, ch, sw = wav_bytes_to_frames(wav_bytes)
        if channels is None:
            channels, sampwidth = ch, sw
        assert (ch, sw) == (channels, sampwidth), "inconsistent audio format across lines"

        duration = len(frames) / (channels * sampwidth) / SAMPLE_RATE
        timing.append({"index": i, "beat": beat, "speaker": speaker, "text": text,
                        "start": round(t, 3), "end": round(t + duration, 3)})
        master_frames += frames
        t += duration

        if pause_after > 0:
            master_frames += silence_frames(pause_after, channels, sampwidth)
            t += pause_after

    master_path = out_dir / "master_narration.wav"
    with wave.open(str(master_path), "wb") as w:
        w.setnchannels(channels)
        w.setsampwidth(sampwidth)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(master_frames)

    timing_path = out_dir / "narration_timing.json"
    timing_path.write_text(json.dumps({"total_duration_sec": round(t, 3), "lines": timing}, indent=2))

    print(f"\nMaster narration: {master_path} ({t:.1f}s)")
    print(f"Timing log: {timing_path}")
    return master_path, timing_path


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)

    script = json.loads(pathlib.Path(sys.argv[1]).read_text())
    voices = json.loads(pathlib.Path(sys.argv[2]).read_text())
    out_dir = pathlib.Path(sys.argv[3])
    out_dir.mkdir(parents=True, exist_ok=True)

    generate(script, voices, out_dir)


if __name__ == "__main__":
    main()
