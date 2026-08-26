"""One-time setup: clone Rahul's voice on Cartesia from the existing reference
clip, save it as a persistent named voice, and render a short test line from
Video 3's actual script (Beat 3's climax) so the identity/quality can be
judged against real content, not filler text.

Usage: .venv-voice/bin/python clone_voice.py
"""
import os
import pathlib

from cartesia import Cartesia

_HERE = pathlib.Path(__file__).resolve().parent
_ENV_LOCAL = _HERE / ".env.local"
if _ENV_LOCAL.exists():
    for line in _ENV_LOCAL.read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

REFERENCE_CLIP = pathlib.Path.home() / "enterprise-ai-gtm-skill/tools/video-studio/public/narration-VideoB-myvoice.wav"
TEST_LINE = (
    "Measured precision moved from 2.8 percent to 15.2 percent. "
    "The model didn't change. The decision rules did."
)
VOICE_ID_FILE = _HERE / "rahul_voice_id.txt"

client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])

print(f"Cloning from {REFERENCE_CLIP} ...")
with open(REFERENCE_CLIP, "rb") as f:
    voice = client.voices.clone(
        clip=f,
        language="en",
        name="Rahul - RiskModelForgeIQ Video 3",
        description="Cloned from narration-VideoB-myvoice.wav for Video 3 narration.",
    )
voice_id = voice.id
VOICE_ID_FILE.write_text(voice_id)
print(f"Voice ID: {voice_id} (saved to {VOICE_ID_FILE})")

print("Rendering test line ...")
chunks = client.tts.bytes(
    model_id="sonic-3.5",  # sonic-2 sunsets 2026-10-20
    transcript=TEST_LINE,
    voice={"mode": "id", "id": voice_id},
    output_format={"container": "wav", "encoding": "pcm_f32le", "sample_rate": 44100},
)
out_path = _HERE / "test_rahul_voice.wav"
with open(out_path, "wb") as f:
    for chunk in chunks:
        f.write(chunk)
print(f"Test clip written to {out_path}")
