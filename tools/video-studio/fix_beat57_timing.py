"""Second timing correction: real page-load time was consuming most of Beat
5's and Beat 7's windows even after the domain-switch race fix (measured
settled-margin: 4.2s/15.0s and 5.9s/17.0s -- both well under a safe floor of
~8s of real settled time). Extends both further, using the user-approved
extra-runtime slack (already used 6.405s on Beat 5's first extension; this
adds 4.0s more to Beat 5 and 2.982s to Beat 7 -- 13.385s of the 30s pool
total, comfortably within budget).

Applies two sequential silence insertions to the ALREADY-once-patched
master_narration.wav / narration_timing.json (from fix_beat5_timing.py).
"""
import json
import pathlib
import wave

_HERE = pathlib.Path(__file__).resolve().parent
TIMING_PATH = _HERE / "narration_timing.json"
AUDIO_PATH = _HERE / "master_narration.wav"

INSERTIONS = [
    (139.737, 4.000),   # after beat 5's last line -- extends beat 5's window 15.0 -> 19.0s
    # beat 7's last line currently ends at 163.160, but the FIRST insertion
    # above shifts it (and everything after beat 5) by +4.0s before this one
    # applies -- must target the post-shift position (163.160 + 4.000), not
    # the pre-shift value, or this would double-catch/miss the boundary.
    (163.160 + 4.000, 2.982),  # after beat 7's last line -- extends beat 7's window 17.0 -> 20.0s
]

data = json.loads(TIMING_PATH.read_text())

with wave.open(str(AUDIO_PATH), "rb") as r:
    params = r.getparams()
    frames = r.readframes(r.getnframes())

for splice_after, insert_seconds in INSERTIONS:
    for line in data["lines"]:
        if line["start"] >= splice_after + 0.001:  # already-shifted lines only
            line["start"] = round(line["start"] + insert_seconds, 3)
            line["end"] = round(line["end"] + insert_seconds, 3)
    data["total_duration_sec"] = round(data["total_duration_sec"] + insert_seconds, 3)

    splice_byte = int(splice_after * params.framerate) * params.nchannels * params.sampwidth
    silence = b"\x00" * (int(insert_seconds * params.framerate) * params.nchannels * params.sampwidth)
    frames = frames[:splice_byte] + silence + frames[splice_byte:]
    print(f"Inserted {insert_seconds}s after t={splice_after}")

TIMING_PATH.write_text(json.dumps(data, indent=2))
with wave.open(str(AUDIO_PATH), "wb") as w:
    w.setparams(params)
    w.writeframes(frames)

new_duration = len(frames) / (params.nchannels * params.sampwidth) / params.framerate
print(f"New total duration: {new_duration:.3f}s (timing.json says {data['total_duration_sec']}s)")
