"""Generate narration audio for the UnmaskIQ demo (storyboard v5,
cbp-sentry/docs/gtm/03-video/storyboard-traceforge-demo.md).

v5, 2026-08-25: corrected from "three hops back" to "one hop back" (Beat 0
and Beat 2 lines) to match what the resolution pipeline can actually show
-- cbp-sentry commit 5d6c5c4 fixed a real gap so a curated demo entity's
own OFAC status is detected one hop back in the ownership chain, but no
2-3-hop case exists in the dataset. Recording the old v4 script would have
shown a screen that contradicted its own narration.

Reuses the exact voice setup already locked for the RiskModelForgeIQ/Video 3
pipeline (see test_stock_voices.py): stock Cartesia voices, persona names
"Rahul"/"Emma" regardless of the underlying voice name. Outputs, mirroring
Video 3's schema, into unmaskiq_output/ (kept separate from Video 3's own
master_narration.wav/narration_timing.json so neither overwrites the other):
  - unmaskiq_output/narration_lines/NNN_<beat>_<Speaker>.wav  (per-line)
  - unmaskiq_output/master_narration.wav                       (concatenated)
  - unmaskiq_output/narration_timing.json                      (cue timestamps)
"""
import json
import os
import pathlib
import struct
import wave

from cartesia import Cartesia

_HERE = pathlib.Path(__file__).resolve().parent
_ENV_LOCAL = _HERE / ".env.local"
for line in _ENV_LOCAL.read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())

client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])

VOICES = {
    "Rahul": "638efaaa-4d0c-442e-b701-3fae16aad012",  # Sameer - Problem Solver
    "Emma": "f6ff7c0c-e396-40a9-a70b-f7607edb6937",  # Emma - Customer Care Line
}

OUT_DIR = _HERE / "unmaskiq_output"
LINES_DIR = OUT_DIR / "narration_lines"
LINES_DIR.mkdir(parents=True, exist_ok=True)

STANDARD_GAP = 0.45  # seconds between ordinary lines
DRAMATIC_PAUSE = 1.4  # seconds after the two marked *(pause)* beats

# (beat, speaker, text, pause_after)
SCRIPT = [
    ("0", "Emma", "That name right there — flagged. Government sanctions list. You can't do business with it.", False),
    ("0", "Rahul", "And one hop back, that same party's hiding behind a name that looks completely clean on one of thousands of shipping manifests that cross every day.", False),
    ("0", "Emma", "So how did anyone even find it?", False),
    ("0", "Rahul", "That's what this is.", False),

    ("1", "Emma", "So you start with the raw manifest.", False),
    ("1", "Rahul", "Every shipment starts as a messy file. This breaks it into its actual parts — shipper, value, vessel.", False),
    ("1", "Emma", "But the name on here is clean.", False),
    ("1", "Rahul", "The name on here is clean. That's the point — it's supposed to be. Same pipeline's built to handle claims, transactions, whatever you throw at it. Right now it's a shipment.", False),
    ("1", "Emma", "Okay. So what do you do with a clean name?", False),

    ("2", "Rahul", "You trace it. The name on the form is a starting point. We follow who's behind that name — owned by whom — and we keep going until we hit the real thing.", False),
    ("2", "Emma", "That's not the name on the manifest.", False),
    ("2", "Rahul", "One hop back. And that's the one from the beginning. Already flagged.", True),
    ("2", "Emma", "So if nobody traces it back—", False),
    ("2", "Rahul", "—a sanctioned party does business through a name that looks clean on paper. The sanction exists, and it does nothing.", False),
    ("2", "Emma", "Whoever's actually behind this shipment — it's not even the name on the paperwork.", False),
    ("2", "Rahul", "Right. A name-only check stops at the first name, looks fine, moves on. It never gets to hop two.", False),

    ("3", "Emma", "So does it just block it now?", False),
    ("3", "Rahul", "It doesn't decide on its own. It takes the chain, the hit, scores the shipment, and builds it all into one case file.", False),
    ("3", "Emma", "Somebody still has to look at it.", False),
    ("3", "Rahul", "Somebody still puts their name on the decision. They're just not spending half a day reconstructing what we just watched happen in seconds.", False),

    ("4", "Emma", "How do I trust that score? Or that flag?", False),
    ("4", "Rahul", "That's what this tab's for. Every rule that made that call is versioned. Every model's registered with a status. And if two signals disagree — which happens — a person looks at it. It doesn't get averaged out and forgotten.", False),
    ("4", "Emma", "So it's not just that you caught something.", False),
    ("4", "Rahul", "Somebody's putting their name on this call. If it's wrong, that can't be 'the system said so.' They need to point to exactly why, months later.", True),
    ("4", "Rahul", "And everything you just watched — the ingest, the chain, the score, this tab — it's all the same two interfaces underneath. REST API, MCP.", False),
    ("4", "Emma", "So next week it's a claim, a transaction—", False),
    ("4", "Rahul", "Config change. That's kind of the whole point.", False),
    ("4", "Rahul", "That's UnmaskIQ, running on RiskModelForgeIQ's Decision Intelligence Layer. Demo link's in the comments.", False),
]


def synth_line(text: str, speaker: str, out_path: pathlib.Path) -> None:
    chunks = client.tts.bytes(
        model_id="sonic-2",
        transcript=text,
        voice={"mode": "id", "id": VOICES[speaker]},
        output_format={"container": "wav", "encoding": "pcm_s16le", "sample_rate": 44100},
    )
    with open(out_path, "wb") as f:
        for chunk in chunks:
            f.write(chunk)


def wav_duration_sec(path: pathlib.Path) -> float:
    with wave.open(str(path), "rb") as w:
        return w.getnframes() / float(w.getframerate())


FADE_MS = 8  # short enough to be inaudible, long enough to kill the click


def fade_edges(frames: bytes, framerate: int) -> bytes:
    """Ramp each line's clip to/from zero at its head/tail before it gets
    spliced against silence padding. Cartesia's raw TTS output starts and
    ends mid-waveform (never at a zero crossing), so pasting it directly
    against silence is a hard sample-level discontinuity -- audible as a
    click at every single line boundary (confirmed: found identical-
    magnitude jumps at all 28 line-start timestamps in a prior render)."""
    samples = list(struct.unpack(f"<{len(frames)//2}h", frames))
    n = min(int(framerate * FADE_MS / 1000), len(samples) // 2)
    for i in range(n):
        g = i / n
        samples[i] = int(samples[i] * g)
        samples[-(i + 1)] = int(samples[-(i + 1)] * g)
    return struct.pack(f"<{len(samples)}h", *samples)


def main() -> None:
    timing_lines = []
    cursor = 0.0
    wav_params = None
    master_frames = []

    for idx, (beat, speaker, text, pause_after) in enumerate(SCRIPT):
        out_path = LINES_DIR / f"{idx:03d}_{beat}_{speaker}.wav"
        print(f"[{idx:03d}] {speaker} ({beat}): {text[:60]}...")
        synth_line(text, speaker, out_path)

        with wave.open(str(out_path), "rb") as w:
            if wav_params is None:
                wav_params = w.getparams()
            frame_size = w.getsampwidth() * w.getnchannels()
            framerate = w.getframerate()
        # Don't trust the WAV header's declared frame count -- Cartesia's
        # streamed WAV appears to write a placeholder/streaming size field,
        # not the real one (getnframes() returned values corresponding to
        # hours of audio for a two-second line). Compute the real duration
        # from the actual bytes on disk instead.
        data_bytes = out_path.stat().st_size - 44  # standard WAV header size
        n_frames = data_bytes // frame_size
        frames = out_path.read_bytes()[44:44 + n_frames * frame_size]
        frames = fade_edges(frames, framerate)
        duration = n_frames / float(framerate)

        start = cursor
        end = cursor + duration
        timing_lines.append({
            "index": idx, "beat": beat, "speaker": speaker, "text": text,
            "start": round(start, 3), "end": round(end, 3),
        })
        master_frames.append(frames)

        gap = DRAMATIC_PAUSE if pause_after else STANDARD_GAP
        silence_frames = int(wav_params.framerate * gap) * wav_params.sampwidth * wav_params.nchannels
        master_frames.append(b"\x00" * silence_frames)
        cursor = end + gap

    master_path = OUT_DIR / "master_narration.wav"
    with wave.open(str(master_path), "wb") as out:
        # Set format fields only -- NOT wav_params.nframes (captured from the
        # first line's short WAV). Passing that stale nframes through
        # setparams() corrupts wave's frame-count accumulation across the
        # many writeframesraw() calls below, producing a garbage datasize on
        # close() that overflows struct.pack's 32-bit field.
        out.setnchannels(wav_params.nchannels)
        out.setsampwidth(wav_params.sampwidth)
        out.setframerate(wav_params.framerate)
        out.setcomptype(wav_params.comptype, wav_params.compname)
        for frames in master_frames:
            out.writeframesraw(frames)

    timing = {"total_duration_sec": round(cursor, 3), "lines": timing_lines}
    timing_path = OUT_DIR / "narration_timing.json"
    timing_path.write_text(json.dumps(timing, indent=2))

    print(f"\nDone. {len(SCRIPT)} lines, {cursor:.1f}s total.")
    print(f"  -> {master_path}")
    print(f"  -> {timing_path}")


if __name__ == "__main__":
    main()
