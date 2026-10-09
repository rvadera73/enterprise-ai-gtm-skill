"""Generate narration audio for the "AI-Assisted Software Factory" internal
video (storyboard: examples/foundry/STORYBOARD-internal-video.md, approved
2026-08-27 after 3 review rounds -- external AI, self cold-read, Descript's
Underlord chatbot -- see that file's Review Log section for full history).

Reuses the exact voice setup and all the hard-won fixes from
generate_narration_unmaskiq.py: stock Cartesia voices (test_stock_voices.py),
sonic-3.5 model, the click-prevention edge-fade, real-duration-computed-from-
file-size (never trust Cartesia's streamed WAV header), and the
setparams()-without-stale-nframes fix for incremental wave writes.

Speaker -> voice mapping: DevSecOps Engineer (explaining voice, longer lines)
-> Sameer ("Rahul" slot); Developer (reactive/skeptical voice) -> Emma.

Outputs into factory_output/ (kept separate from other videos' output dirs):
  - factory_output/narration_lines/NNN_beatN_<Speaker>.wav  (per-line)
  - factory_output/master_narration.wav                     (concatenated)
  - factory_output/narration_timing.json                    (cue timestamps)
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
    "DevSecOps": "638efaaa-4d0c-442e-b701-3fae16aad012",  # Sameer - Problem Solver
    "Developer": "f6ff7c0c-e396-40a9-a70b-f7607edb6937",  # Emma - Customer Care Line
}

OUT_DIR = _HERE / "factory_output"
LINES_DIR = OUT_DIR / "narration_lines"
LINES_DIR.mkdir(parents=True, exist_ok=True)

STANDARD_GAP = 0.45   # seconds between lines within the same beat
BEAT_GAP = 0.70       # slightly longer pause at a beat boundary -- gives the
                       # eventual video-assembly step a clean cut point

# (beat, speaker, text, beat_boundary_after)
SCRIPT = [
    ("1", "DevSecOps", "A developer hands over a repository and a Dockerfile, and the AI-Assisted Software Factory builds and deploys a real multi-cloud pipeline from that. You'd normally have a team writing that pipeline by hand — this doesn't.", False),
    ("1", "Developer", "That's a lot riding on just a repo and a Dockerfile — most multi-cloud pipelines I've dealt with take a dedicated infrastructure team two sprints just to stand up and debug.", True),

    ("2", "DevSecOps", "Right, and that's exactly the assumption people bring in — that something like this means more upfront work, new tooling, a new process to learn.", False),
    ("2", "Developer", "That's usually how it goes, yeah — new AI angle, same old rewrite-everything tax.", True),

    ("3", "Developer", "Because normally that's the actual job, right — you design the service, sure, but then you're also the one writing the CI config, the deploy scripts, wiring up whatever infrastructure it needs. Half your sprint disappears into that before the thing even ships.", False),
    ("3", "DevSecOps", "And now that whole second half isn't the developer's anymore. They design the architecture, package it properly in Docker, and the factory takes over build and deployment from there.", True),

    ("4", "DevSecOps", "Nobody's hand-typing this from scratch either — you point it at the repo, say what you're deploying, and it fills this in itself. If it can't tell something, it asks, and whatever comes back gets written straight into this.", False),
    ("4", "Developer", "So if my config surface just shrank to one Dockerfile — what happens when a deployment actually fails, am I the one debugging the factory's generated pipeline, or is that shielded too?", False),
    ("4", "DevSecOps", "Not you first, no — a failure routes back to the AI to diagnose and fix, same as any other failed gate. You only get pulled in for something that's actually your call — a breaking schema change, say, not a flaky retry.", True),

    ("5", "DevSecOps", "Which is why a developer's actual week goes back to the service itself — the architecture, the design — not a Terraform diff, not a deploy script.", False),
    ("5", "Developer", "And this isn't a thought experiment sitting in a deck somewhere — it's running for real, on IACP-2.1. That's the part that actually matters to me, honestly, versus a proposal.", False),
    ("5", "DevSecOps", "It is — and the AI-Assisted Software Factory isn't stopping there. CBP Sentry's next, in the coming weeks — same factory model, same configuration structure, just pointed at a new repository. And it won't stay GitHub-only either — Jenkins and GitLab are next on the same model, just a different CI underneath.", True),

    ("6", "DevSecOps", "A repository, a working Dockerfile, and the AI-Assisted Software Factory takes it the rest of the way.", False),
    ("6", "Developer", "Fair trade — as long as that Dockerfile's actually right.", False),
    ("6", "DevSecOps", "That's genuinely the only part still on you. Two sprints of infrastructure work, or the service you actually wanted to ship?", False),
]


def synth_line(text: str, speaker: str, out_path: pathlib.Path) -> None:
    chunks = client.tts.bytes(
        model_id="sonic-3.5",
        transcript=text,
        voice={"mode": "id", "id": VOICES[speaker]},
        output_format={"container": "wav", "encoding": "pcm_s16le", "sample_rate": 44100},
    )
    with open(out_path, "wb") as f:
        for chunk in chunks:
            f.write(chunk)


FADE_MS = 8


def fade_edges(frames: bytes, framerate: int) -> bytes:
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

    for idx, (beat, speaker, text, beat_boundary) in enumerate(SCRIPT):
        out_path = LINES_DIR / f"{idx:03d}_beat{beat}_{speaker}.wav"
        print(f"[{idx:03d}] beat{beat} {speaker}: {text[:60]}...")
        synth_line(text, speaker, out_path)

        with wave.open(str(out_path), "rb") as w:
            if wav_params is None:
                wav_params = w.getparams()
            frame_size = w.getsampwidth() * w.getnchannels()
            framerate = w.getframerate()
        data_bytes = out_path.stat().st_size - 44
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

        gap = BEAT_GAP if beat_boundary else STANDARD_GAP
        silence_frames = int(wav_params.framerate * gap) * wav_params.sampwidth * wav_params.nchannels
        master_frames.append(b"\x00" * silence_frames)
        cursor = end + gap

    master_path = OUT_DIR / "master_narration.wav"
    with wave.open(str(master_path), "wb") as out:
        out.setnchannels(wav_params.nchannels)
        out.setsampwidth(wav_params.sampwidth)
        out.setframerate(wav_params.framerate)
        out.setcomptype(wav_params.comptype, wav_params.compname)
        for frames in master_frames:
            out.writeframesraw(frames)

    # beat-level start/end derived from the lines, for the video-assembly step
    beats = {}
    for line in timing_lines:
        b = line["beat"]
        beats.setdefault(b, {"start": line["start"], "end": line["end"]})
        beats[b]["end"] = line["end"]

    timing = {
        "total_duration_sec": round(cursor, 3),
        "lines": timing_lines,
        "beats": beats,
    }
    timing_path = OUT_DIR / "narration_timing.json"
    timing_path.write_text(json.dumps(timing, indent=2))

    print(f"\nDone. {len(SCRIPT)} lines, {cursor:.1f}s total.")
    print(f"  -> {master_path}")
    print(f"  -> {timing_path}")


if __name__ == "__main__":
    main()
