"""Render test lines from Video 3's actual script using stock Cartesia voices
(cloning is gated behind a paid tier we haven't upgraded to yet). Persona
names stay "Rahul" and "Emma" in the script/storyboard regardless of which
underlying stock voice is used. Picks: Rahul -> Sameer ("Problem Solver"),
Emma -> Emma ("Customer Care Line").
"""
import os
import pathlib

from cartesia import Cartesia

_HERE = pathlib.Path(__file__).resolve().parent
_ENV_LOCAL = _HERE / ".env.local"
for line in _ENV_LOCAL.read_text().splitlines():
    if "=" in line and not line.strip().startswith("#"):
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())

client = Cartesia(api_key=os.environ["CARTESIA_API_KEY"])

VOICES = {
    "rahul": "638efaaa-4d0c-442e-b701-3fae16aad012",  # Sameer - Problem Solver
    "emma": "f6ff7c0c-e396-40a9-a70b-f7607edb6937",  # Emma - Customer Care Line
}

LINES = {
    "rahul": (
        "Measured precision moved from 2.8 percent to 15.2 percent. "
        "The model didn't change. The decision rules did."
    ),
    "emma": "Six months from now, if someone asks which model made this decision — can you prove it?",
}

for key, voice_id in VOICES.items():
    print(f"Rendering {key} ...")
    chunks = client.tts.bytes(
        model_id="sonic-3.5",  # sonic-2 sunsets 2026-10-20
        transcript=LINES[key],
        voice={"mode": "id", "id": voice_id},
        output_format={"container": "wav", "encoding": "pcm_f32le", "sample_rate": 44100},
    )
    out_path = _HERE / f"test_{key}.wav"
    with open(out_path, "wb") as f:
        for chunk in chunks:
            f.write(chunk)
    print(f"  -> {out_path}")
