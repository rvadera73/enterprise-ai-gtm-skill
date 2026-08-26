"""Validate a rendered demo video's actual spoken narration against the
known-good script, using Descript's API as an independent transcription
check the rest of the pipeline can't perform on itself.

Why this exists: our narration comes from TTS (Cartesia) with an
already-known, exact script -- so the value here isn't "generate a
transcript from scratch," it's "does an independent listener hear what we
think we said." This caught a real bug on the first real run: the TTS
voice's rendering of "RiskModelForgeIQ" was independently transcribed as
"Risk Model 4 IQ" -- a genuine pronunciation-clarity issue nothing else in
the pipeline (ffmpeg silence/click detection, our own narration_timing.json)
could ever catch, since none of it "listens" to the output.

Usage:
    python descript_validate.py --video path/to/final.mp4 --script path/to/narration_timing.json
    python descript_validate.py --video path/to/final.mp4 --text "plain expected transcript text"

Requires DESCRIPT_BEARER and DESCRIPT_SECRET in a .env.local file next to
this script (same convention generate_narration_unmaskiq.py uses for
CARTESIA_API_KEY) -- get these from a Descript account's API settings.

Cost, confirmed empirically (2026-08-26, see memory descript-api-integration
-facts): media-minute consumption is a clean 1:1 with real video duration
(a 144s video = 144 media-seconds used), billed against the account's
monthly minutes allowance (60 min/month on Free, renewing). Plain
import+transcribe consumes ZERO AI credits -- only AI-editing operations
(Underlord, Studio Sound, etc., not used here) touch the one-time,
non-renewing Free-tier AI-credit pool. At 3 videos/month this script's
usage is trivial (~15-20 min/month) against the Free tier.

Known API quirks baked into this script so you don't rediscover them:
- Auth: the bearer token is BOTH key halves joined with a colon
  (`dx_bearer_X:dx_secret_Y`), not either half alone -- undocumented,
  found by trial and error.
- A composition (needed before transcript export can return anything)
  MUST be declared in the SAME import call as the media itself
  (`add_compositions` alongside `add_media`). Omitting it succeeds (201)
  but leaves transcript export silently returning HTTP 200 with an EMPTY
  body -- no error. There's no way to attach a composition to
  already-uploaded media afterward; the whole import (including the
  upload) has to be redone.
"""
import argparse
import difflib
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

API_BASE = "https://descriptapi.com/v1"
_HERE = pathlib.Path(__file__).resolve().parent


def load_env_local():
    env_path = _HERE / ".env.local"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def auth_header():
    bearer = os.environ["DESCRIPT_BEARER"]
    secret = os.environ["DESCRIPT_SECRET"]
    return {"Authorization": f"Bearer {bearer}:{secret}"}


def api_request(method, path, body=None, extra_headers=None):
    url = f"{API_BASE}{path}"
    headers = {**auth_header(), **(extra_headers or {})}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def create_import_job(video_path: pathlib.Path, project_name: str):
    media_key = video_path.name
    body = {
        "project_name": project_name,
        "add_media": {
            media_key: {
                "content_type": "video/mp4",
                "file_size": video_path.stat().st_size,
            }
        },
        # Composition MUST be here, not added later -- see module docstring.
        "add_compositions": [
            {"name": "Main", "clips": [{"media": media_key}]}
        ],
    }
    status, raw = api_request("POST", "/jobs/import/project_media", body)
    if status != 201:
        raise RuntimeError(f"import job creation failed ({status}): {raw.decode()}")
    resp = json.loads(raw)
    return resp["job_id"], resp["project_id"], resp["upload_urls"][media_key]["upload_url"]


def upload_file(upload_url: str, video_path: pathlib.Path):
    req = urllib.request.Request(
        upload_url,
        data=video_path.read_bytes(),
        headers={"Content-Type": "application/octet-stream"},
        method="PUT",
    )
    with urllib.request.urlopen(req) as resp:
        if resp.status not in (200, 201):
            raise RuntimeError(f"upload failed: HTTP {resp.status}")


def poll_job(job_id: str, timeout_s: int = 180, interval_s: int = 10):
    waited = 0
    while waited < timeout_s:
        status, raw = api_request("GET", f"/jobs/{job_id}")
        data = json.loads(raw)
        if data["job_state"] == "stopped":
            return data
        time.sleep(interval_s)
        waited += interval_s
    raise TimeoutError(f"job {job_id} did not finish within {timeout_s}s")


def export_transcript(project_id: str, composition_id: str, fmt: str = "txt") -> str:
    body = {"project_id": project_id, "composition_id": composition_id, "format": fmt}
    status, raw = api_request("POST", "/export/transcript", body)
    if status != 200:
        raise RuntimeError(f"transcript export failed ({status}): {raw.decode()}")
    return raw.decode("utf-8")


def expected_text_from_script(script_path: pathlib.Path) -> str:
    data = json.loads(script_path.read_text())
    if "lines" in data:  # narration_timing.json shape
        return " ".join(line["text"] for line in data["lines"])
    raise ValueError(f"unrecognized script file shape: {script_path}")


_SPEAKER_LABEL_RE = re.compile(r"^\s*speaker\s*\d*\s*:\s*", re.IGNORECASE | re.MULTILINE)


def strip_speaker_labels(text: str) -> str:
    """Descript's txt export prefixes each turn with 'Speaker N: ' -- real
    structure for a human reading it, but pure noise for a word-level diff
    against a script that has no such labels. Strip before comparing."""
    return _SPEAKER_LABEL_RE.sub("", text)


def compare(expected: str, actual: str):
    """Word-level diff. Not fuzzy about punctuation/casing (ASR output
    normalizes both), but flags real word substitutions/omissions --
    exactly the class of thing that caught 'RiskModelForgeIQ' -> 'Risk
    Model 4 IQ' on the first real run."""
    actual = strip_speaker_labels(actual)
    norm = lambda s: [w.strip(".,!?—’'\"").lower() for w in s.split() if w.strip(".,!?—’'\"")]
    exp_words, act_words = norm(expected), norm(actual)
    sm = difflib.SequenceMatcher(None, exp_words, act_words)
    ratio = sm.ratio()
    diffs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        diffs.append({
            "type": tag,
            "expected": " ".join(exp_words[i1:i2]),
            "heard": " ".join(act_words[j1:j2]),
        })
    return ratio, diffs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--video", required=True, type=pathlib.Path)
    ap.add_argument("--script", type=pathlib.Path, help="narration_timing.json (or similar {lines:[{text}]} file)")
    ap.add_argument("--text", help="expected transcript text directly, instead of --script")
    ap.add_argument("--project-name", default=None)
    args = ap.parse_args()

    if not args.script and not args.text:
        ap.error("provide --script or --text so there's something to validate against")

    load_env_local()
    if "DESCRIPT_BEARER" not in os.environ or "DESCRIPT_SECRET" not in os.environ:
        print("ERROR: set DESCRIPT_BEARER and DESCRIPT_SECRET in .env.local next to this script.", file=sys.stderr)
        sys.exit(1)

    video_path = args.video.resolve()
    project_name = args.project_name or f"Validate: {video_path.stem}"

    print(f"[1/4] Creating import job for {video_path.name} ({video_path.stat().st_size / 1e6:.1f} MB)...")
    job_id, project_id, upload_url = create_import_job(video_path, project_name)

    print(f"[2/4] Uploading...")
    upload_file(upload_url, video_path)

    print(f"[3/4] Waiting for processing (job {job_id})...")
    result = poll_job(job_id)
    media_seconds = result["result"].get("media_seconds_used", "?")
    ai_credits = result["result"].get("ai_credits_used", 0)
    compositions = result["result"].get("created_compositions", [])
    if not compositions:
        print("ERROR: no composition created -- transcript export would return empty.", file=sys.stderr)
        sys.exit(1)
    composition_id = compositions[0]["id"]
    print(f"      media_seconds_used={media_seconds}  ai_credits_used={ai_credits}")

    print(f"[4/4] Exporting transcript...")
    actual_text = export_transcript(project_id, composition_id, fmt="txt")

    expected_text = args.text or expected_text_from_script(args.script)
    ratio, diffs = compare(expected_text, actual_text)

    print(f"\n=== Result: {ratio:.1%} word-level match ===")
    if not diffs:
        print("No discrepancies found -- transcript matches the script.")
    else:
        print(f"{len(diffs)} discrepanc{'y' if len(diffs) == 1 else 'ies'} found:\n")
        for d in diffs:
            print(f"  [{d['type']}] script: \"{d['expected']}\"  ->  heard: \"{d['heard']}\"")

    print(f"\nProject: https://web.descript.com/{project_id}")
    print("(Free tier renews media-minutes monthly; this run cost "
          f"~{int(media_seconds) / 60:.1f} of the 60 free minutes and 0 AI credits.)")


if __name__ == "__main__":
    main()
