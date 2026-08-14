"""Beat 5's recorded video clip is 15.0s (extended from its original
narration-derived 8.6s window to fix a real loading-race bug, see
cbp-risk-engine issue #206/PR #209). Insert the difference as silence in
master_narration.wav right after Beat 5's last spoken line, and shift every
subsequent beat's timestamps in narration_timing.json accordingly, so the
audio track and the final concatenated video stay in sync.
"""
import json
import pathlib
import wave

_HERE = pathlib.Path(__file__).resolve().parent
TIMING_PATH = _HERE / "narration_timing.json"
AUDIO_PATH = _HERE / "master_narration.wav"

NEW_BEAT5_DURATION = 15.0
OLD_BEAT5_DURATION = 140.237 - 131.642  # next beat's original start - this beat's start
INSERT_SECONDS = NEW_BEAT5_DURATION - OLD_BEAT5_DURATION
SPLICE_AFTER = 139.737  # end of beat 5's last spoken line (index 34)

data = json.loads(TIMING_PATH.read_text())
for line in data["lines"]:
    if line["start"] >= SPLICE_AFTER:
        line["start"] = round(line["start"] + INSERT_SECONDS, 3)
        line["end"] = round(line["end"] + INSERT_SECONDS, 3)
data["total_duration_sec"] = round(data["total_duration_sec"] + INSERT_SECONDS, 3)
TIMING_PATH.write_text(json.dumps(data, indent=2))
print(f"Shifted all beats after t={SPLICE_AFTER} by +{INSERT_SECONDS:.3f}s in {TIMING_PATH}")
print(f"New total duration: {data['total_duration_sec']}s")

with wave.open(str(AUDIO_PATH), "rb") as r:
    params = r.getparams()
    frames = r.readframes(r.getnframes())

splice_byte = int(SPLICE_AFTER * params.framerate) * params.nchannels * params.sampwidth
silence = b"\x00" * (int(INSERT_SECONDS * params.framerate) * params.nchannels * params.sampwidth)
new_frames = frames[:splice_byte] + silence + frames[splice_byte:]

with wave.open(str(AUDIO_PATH), "wb") as w:
    w.setparams(params)
    w.writeframes(new_frames)

new_duration = len(new_frames) / (params.nchannels * params.sampwidth) / params.framerate
print(f"Patched {AUDIO_PATH}, new audio duration: {new_duration:.3f}s")
