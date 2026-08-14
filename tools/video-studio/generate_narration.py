"""Generate Video 3's full narration track from the locked script
(docs/gtm/03-video/storyboard-video3-full-tour.md, storyboard v3, 2026-08-14).

Renders every line individually via Cartesia TTS (Rahul -> Sameer, Emma ->
stock Emma), concatenates them with silence gaps matching the script's
*(pause)* markers, and writes:
  - master_narration.wav        (the full track)
  - narration_timing.json       (start/end seconds per line + beat, for
                                  driving the Playwright recording off real
                                  cue timestamps, per this pipeline's
                                  established sequence)

Usage: .venv-voice/bin/python generate_narration.py
"""
import json
import os
import pathlib
import wave

from cartesia import Cartesia

_HERE = pathlib.Path(__file__).resolve().parent
_ENV_LOCAL = _HERE / ".env.local"
for _line in _ENV_LOCAL.read_text().splitlines():
    if "=" in _line and not _line.strip().startswith("#"):
        k, v = _line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())

client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])

VOICES = {
    "Rahul": "638efaaa-4d0c-442e-b701-3fae16aad012",  # Sameer - Problem Solver
    "Emma": "f6ff7c0c-e396-40a9-a70b-f7607edb6937",  # Emma - Customer Care Line
}

SAMPLE_RATE = 44100
STANDARD_PAUSE = 0.6
LONG_PAUSE = 2.0  # Beat 3's full-screen escalation graphic, explicitly "let it sit ~2s"

# (beat, speaker, text, pause_after_seconds)
SCRIPT = [
    # Beat 0
    ("0", "Emma", "Wait. Same case?", 0.2),
    ("0", "Rahul", "Same case. Same data. Two independently trained models — 25.09 versus 96.95.", STANDARD_PAUSE),
    ("0", "Emma", "So which one drives the decision?", 0.2),
    ("0", "Rahul", "Neither, by itself. The disagreement becomes a governed signal.", STANDARD_PAUSE),
    # Beat 1
    ("1", "Rahul", "So what happens underneath that decision?", 1.0),
    ("1", "Rahul", "The model is only one part of it. Signal Intelligence. Risk Intelligence. Decision Governance.", STANDARD_PAUSE),
    ("1", "Rahul", "Together, they form RiskModelForgeIQ's Decision Intelligence Layer.", 0.3),
    ("1", "Emma", "So this is more than MLOps?", 0.2),
    ("1", "Rahul", "Exactly. MLOps manages the model. DecisionOps governs what happens when the model actually makes a decision — the rules, the versions, human review, explainability, the evidence behind it.", 0.5),
    # Beat 2
    ("2", "Emma", "Why are they so different?", 0.2),
    ("2", "Rahul", "The champion sees this case as relatively routine. The challenger sees something materially different.", STANDARD_PAUSE),
    ("2", "Rahul", "RiskModelForgeIQ doesn't hide that disagreement behind a blended score. It makes the disagreement operational.", 0.3),
    ("2", None, "__VISUAL_71.86_POINT_DISAGREEMENT__", STANDARD_PAUSE),
    ("2", None, "__VISUAL_HUMAN_REVIEW_REQUIRED__", STANDARD_PAUSE),
    ("2", "Emma", "So the system doesn't pick a winner?", 0.2),
    ("2", "Rahul", "Right. When the models disagree this sharply, a human does.", 0.4),
    ("2", "Rahul", "We don't stop at explaining the score. We can trace the decision back through the model, the contributing signal, and the underlying evidence.", 0.5),
    ("2", None, "__VISUAL_DECISION_SCORE_RULE_FEATURE_SOURCE__", 0.3),
    ("2", "Rahul", "Real Medicare Part B claims, peer-grouped by specialty and region — not a synthetic example built to make a point.", 0.5),
    # Beat 3
    ("3", "Emma", "What about the rules underneath the models — are those just hardcoded somewhere?", 0.2),
    ("3", "Rahul", "The rule changes. The system creates a new version. The previous version is frozen.", STANDARD_PAUSE),
    ("3", "Rahul", "If the change doesn't perform, rollback is one switch.", STANDARD_PAUSE),
    ("3", "Rahul", "Every historical decision still points to the version that made it.", 0.3),
    ("3", "Emma", "Did that actually matter?", 0.2),
    ("3", "Rahul", "This is the surprising part.", STANDARD_PAUSE),
    ("3", None, "__VISUAL_2.8_TO_15.2_ESCALATION__", LONG_PAUSE),
    ("3", "Rahul", "Measured precision moved from 2.8 percent to 15.2 percent.", STANDARD_PAUSE),
    ("3", "Rahul", "The model didn't change.", STANDARD_PAUSE),
    ("3", "Rahul", "The decision rules did.", 0.5),
    # Beat 4
    ("4", "Emma", "Six months from now, if someone asks which model made this decision — can you prove it?", 0.2),
    ("4", "Rahul", "The registry answers that. Model. Version. Role. Status.", STANDARD_PAUSE),
    ("4", "Emma", "And can we reproduce the original decision?", 0.2),
    ("4", "Rahul", "Yes. It stays tied to the exact model, rule, and policy version that produced it.", 0.5),
    # Beat 5
    ("5", "Emma", "Does that same traceability hold model-wide, not just case by case?", 0.2),
    ("5", "Rahul", "It does. Ranked by real contribution — not a black-box weight.", 0.5),
    # Beat 7
    ("7", "Rahul", "The platform also watches the assumptions underneath the model.", 0.5),
    ("7", "Rahul", "When the distribution of an important feature changes, the system can surface that — before performance quietly degrades.", STANDARD_PAUSE),
    ("7", "Rahul", "On this demo, that's seeded traffic, not live trade data — but it's the same mechanism that would run in production.", 0.5),
    # Beat 8
    ("8", "Rahul", "These aren't separate features.", STANDARD_PAUSE),
    ("8", "Rahul", "They're one governed decision lifecycle.", STANDARD_PAUSE),
    ("8", "Rahul", "That's the difference between deploying a model and governing a decision.", 0.5),
    # Beat 9
    ("9", "Emma", "So the model is only part of the architecture.", 0.2),
    ("9", "Rahul", "Exactly.", STANDARD_PAUSE),
    ("9", "Rahul", "MLOps manages the model.", STANDARD_PAUSE),
    ("9", "Rahul", "DecisionOps governs the decision. That's RiskModelForgeIQ.", 0.4),
    ("9", "Rahul", "The demo link is in the comments.", 0.0),
]


def render_line(text: str, voice_id: str) -> bytes:
    chunks = client.tts.bytes(
        model_id="sonic-2",
        transcript=text,
        voice={"mode": "id", "id": voice_id},
        output_format={"container": "wav", "encoding": "pcm_s16le", "sample_rate": SAMPLE_RATE},
    )
    return b"".join(chunks)


def wav_bytes_to_frames(wav_bytes: bytes) -> tuple[bytes, int, int]:
    import io
    with wave.open(io.BytesIO(wav_bytes), "rb") as w:
        return w.readframes(w.getnframes()), w.getnchannels(), w.getsampwidth()


def silence_frames(seconds: float, channels: int, sampwidth: int) -> bytes:
    n_frames = int(seconds * SAMPLE_RATE)
    return b"\x00" * (n_frames * channels * sampwidth)


def main():
    out_dir = _HERE / "narration_lines"
    out_dir.mkdir(exist_ok=True)

    timing = []
    t = 0.0
    master_frames = b""
    channels = None
    sampwidth = None

    for i, (beat, speaker, text, pause_after) in enumerate(SCRIPT):
        if text.startswith("__VISUAL_"):
            # Silent visual-only beat: no speech, just the pause duration itself
            # counted as the "on-screen hold" — logged for recording timing.
            timing.append({"index": i, "beat": beat, "speaker": None, "text": text,
                            "start": round(t, 3), "end": round(t, 3)})
            if channels is not None:
                master_frames += silence_frames(pause_after, channels, sampwidth)
            t += pause_after
            continue

        print(f"[{i}] Beat {beat} {speaker}: {text[:60]}...")
        wav_bytes = render_line(text, VOICES[speaker])
        (out_dir / f"{i:03d}_{beat}_{speaker}.wav").write_bytes(wav_bytes)
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

    master_path = _HERE / "master_narration.wav"
    with wave.open(str(master_path), "wb") as w:
        w.setnchannels(channels)
        w.setsampwidth(sampwidth)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(master_frames)

    timing_path = _HERE / "narration_timing.json"
    timing_path.write_text(json.dumps({"total_duration_sec": round(t, 3), "lines": timing}, indent=2))

    print(f"\nMaster narration: {master_path} ({t:.1f}s)")
    print(f"Timing log: {timing_path}")


if __name__ == "__main__":
    main()
