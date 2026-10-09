#!/usr/bin/env python3
"""
Shared 3-tier LLM fallback chain for enterprise-ai-gtm tooling:

    1. Qwen Singapore   (subscription / Token Plan)  - primary
    2. Qwen Virginia     (pay-as-you-go)              - fallback
    3. Gemini            (text or image)              - third-tier fallback

Rationale: this skill's scripts previously called the Anthropic API directly
with a separate paid key (ANTHROPIC_API_KEY), which duplicates the existing
Claude Code / Claude subscription spend. Per established policy (see
personal-assistant's architecture docs), reasoning tasks should ride the
existing subscription path rather than pay per-token for a second API. Since
these scripts run outside a Claude Code session (plain Python, invoked
directly), they can't use the Claude subscription itself — so they're moved
onto the Qwen-first chain instead of direct-Anthropic, which is the other
piece of the same policy: don't pay a second vendor per-token when a
cheaper/already-paid-for path exists.

Credentials:
    Reads QWEN_API_KEY, QWEN_BASE_URL, QWEN_API_KEY_VIRGINIA_BACKUP,
    QWEN_BASE_URL_VIRGINIA_BACKUP, QWEN_MODEL, GEMINI_API_KEY from the
    process environment first. If any are missing there, falls back to
    reading them from ~/personal-assistant/.env directly (same user/same
    machine, already the canonical home for these creds — see
    ~/.claude/CLAUDE.md "Reusable pattern" note and
    ~/.claude/projects/.../memory/MEMORY.md). This means these scripts need
    no separate credential setup of their own; they ride on the credentials
    already configured for personal-assistant. If that's ever undesirable
    (e.g. this skill is used on a different machine), set the six env vars
    directly before running and the .env fallback is simply never consulted.

Failure-vs-fallback policy:
    Only fall back to the next tier on a REAL failure: connection error,
    timeout, non-2xx HTTP status, or (for image tasks) an explicit
    task_status of FAILED/CANCELED/UNKNOWN. A merely terse or unsatisfying
    response from a working tier is NOT a failure and is returned as-is.
"""

import json
import os
import time
import urllib.parse as up
from pathlib import Path
from typing import List, Dict, Optional

import requests

_PA_ENV_PATH = Path.home() / "personal-assistant" / ".env"

_ENV_KEYS = [
    "QWEN_API_KEY",
    "QWEN_BASE_URL",
    "QWEN_API_KEY_VIRGINIA_BACKUP",
    "QWEN_BASE_URL_VIRGINIA_BACKUP",
    "QWEN_MODEL",
    "GEMINI_API_KEY",
]


class LLMFallbackError(RuntimeError):
    """Raised when every tier in the chain has genuinely failed."""


def _parse_dotenv(path: Path) -> Dict[str, str]:
    out: Dict[str, str] = {}
    if not path.exists():
        return out
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def load_credentials() -> Dict[str, Optional[str]]:
    """Env vars win; ~/personal-assistant/.env fills in anything missing."""
    creds: Dict[str, Optional[str]] = {k: os.environ.get(k) for k in _ENV_KEYS}
    if any(v is None for v in creds.values()):
        dotenv = _parse_dotenv(_PA_ENV_PATH)
        for k in _ENV_KEYS:
            if creds.get(k) is None and k in dotenv:
                creds[k] = dotenv[k]
    return creds


def _root_from_base_url(base_url: str) -> str:
    """Strip the '/compatible-mode/v1' (or any) suffix to get the bare host,
    which is where the native DashScope-style task endpoints live (verified
    live 2026-10-09: the OpenAI-compatible base_url and the native
    image-generation task endpoints share the same host/key, just different
    paths)."""
    p = up.urlparse(base_url)
    return f"{p.scheme}://{p.netloc}"


# ---------------------------------------------------------------------------
# Text completion chain (used by generate_post.py, content_analyzer.py)
# ---------------------------------------------------------------------------

def _qwen_chat_completion(base_url: str, api_key: str, model: str,
                           messages: List[Dict], max_tokens: int,
                           temperature: float) -> str:
    url = base_url.rstrip("/") + "/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    body = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    resp = requests.post(url, headers=headers, json=body, timeout=90)
    resp.raise_for_status()  # non-2xx -> real failure -> caller falls back
    data = resp.json()
    return data["choices"][0]["message"]["content"]


def _gemini_text_completion(api_key: str, prompt: str, max_tokens: int,
                             temperature: float,
                             model: str = "gemini-2.5-flash") -> str:
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent"
    )
    headers = {"Content-Type": "application/json", "x-goog-api-key": api_key}
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens,
        },
    }
    resp = requests.post(url, headers=headers, json=body, timeout=90)
    resp.raise_for_status()
    data = resp.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def chat_completion(prompt: str, max_tokens: int = 1024,
                     temperature: float = 0.7,
                     system: Optional[str] = None) -> str:
    """Run `prompt` through Qwen-SG -> Qwen-VA -> Gemini-text, in order.
    Returns the first successful response. Raises LLMFallbackError only if
    all three tiers genuinely fail."""
    creds = load_credentials()
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    errors = []

    # Tier 1: Qwen Singapore
    if creds.get("QWEN_API_KEY") and creds.get("QWEN_BASE_URL"):
        try:
            return _qwen_chat_completion(
                creds["QWEN_BASE_URL"], creds["QWEN_API_KEY"],
                creds.get("QWEN_MODEL") or "qwen3.8-max",
                messages, max_tokens, temperature,
            )
        except Exception as e:
            errors.append(f"Qwen Singapore: {e}")
    else:
        errors.append("Qwen Singapore: QWEN_API_KEY/QWEN_BASE_URL not set")

    # Tier 2: Qwen Virginia
    if creds.get("QWEN_API_KEY_VIRGINIA_BACKUP") and creds.get("QWEN_BASE_URL_VIRGINIA_BACKUP"):
        try:
            return _qwen_chat_completion(
                creds["QWEN_BASE_URL_VIRGINIA_BACKUP"],
                creds["QWEN_API_KEY_VIRGINIA_BACKUP"],
                creds.get("QWEN_MODEL") or "qwen3.8-max",
                messages, max_tokens, temperature,
            )
        except Exception as e:
            errors.append(f"Qwen Virginia: {e}")
    else:
        errors.append("Qwen Virginia: backup creds not set")

    # Tier 3: Gemini (text)
    if creds.get("GEMINI_API_KEY"):
        full_prompt = (f"{system}\n\n{prompt}" if system else prompt)
        try:
            return _gemini_text_completion(
                creds["GEMINI_API_KEY"], full_prompt, max_tokens, temperature,
            )
        except Exception as e:
            errors.append(f"Gemini: {e}")
    else:
        errors.append("Gemini: GEMINI_API_KEY not set")

    raise LLMFallbackError(
        "All 3 tiers failed:\n  - " + "\n  - ".join(errors)
    )


# ---------------------------------------------------------------------------
# Image generation chain (used by generate_image.py)
# ---------------------------------------------------------------------------

def _wan_image_generate(base_url: str, api_key: str, prompt: str,
                         size: str = "1K", poll_timeout_s: int = 120) -> bytes:
    """Submit + poll a wan2.7-image-pro task against a Qwen/DashScope-style
    host (same account/key as the OpenAI-compatible base_url, native task
    endpoints live at the bare host). Verified live 2026-10-09 against the
    Qwen Singapore account: real task_id -> SUCCEEDED -> real image bytes."""
    root = _root_from_base_url(base_url)
    create_url = root + "/api/v1/services/aigc/image-generation/generation"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "X-DashScope-Async": "enable",
    }
    body = {
        "model": "wan2.7-image-pro",
        "input": {
            "messages": [
                {"role": "user", "content": [{"text": prompt}]}
            ]
        },
        "parameters": {"size": size, "n": 1},
    }
    resp = requests.post(create_url, headers=headers, json=body, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    task_id = data.get("output", {}).get("task_id")
    if not task_id:
        raise RuntimeError(f"No task_id in create-task response: {data}")

    poll_url = f"{root}/api/v1/tasks/{task_id}"
    poll_headers = {"Authorization": f"Bearer {api_key}"}
    deadline = time.time() + poll_timeout_s
    while time.time() < deadline:
        time.sleep(3)
        r = requests.get(poll_url, headers=poll_headers, timeout=30)
        r.raise_for_status()
        d = r.json()
        status = d.get("output", {}).get("task_status")
        if status == "SUCCEEDED":
            choices = d.get("output", {}).get("choices", [])
            if not choices:
                raise RuntimeError(f"SUCCEEDED but no choices in response: {d}")
            content = choices[0].get("message", {}).get("content", [])
            image_url = next((c["image"] for c in content if "image" in c), None)
            if not image_url:
                raise RuntimeError(f"SUCCEEDED but no image URL found: {d}")
            img_resp = requests.get(image_url, timeout=60)
            img_resp.raise_for_status()
            return img_resp.content
        if status in ("FAILED", "CANCELED", "UNKNOWN"):
            raise RuntimeError(f"Task ended with status={status}: {d}")
        # PENDING / RUNNING -> keep polling
    raise TimeoutError(f"Task {task_id} did not finish within {poll_timeout_s}s")


def _gemini_image_generate(api_key: str, prompt: str,
                            model: str = "gemini-2.5-flash-image") -> bytes:
    """Last-resort tier. Requires billing enabled on the Gemini project (the
    free tier returns 429 RESOURCE_EXHAUSTED with limit:0 for this model —
    confirmed live 2026-09-04, see color-team-review/proposal-drafting
    SKILL.md). That 429 counts as a real failure here and propagates up so
    the caller knows every tier is exhausted, rather than being swallowed."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    headers = {"Content-Type": "application/json", "x-goog-api-key": api_key}
    body = {"contents": [{"parts": [{"text": prompt}]}]}
    resp = requests.post(url, headers=headers, json=body, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    parts = data["candidates"][0]["content"]["parts"]
    inline = next((p for p in parts if "inlineData" in p), None)
    if not inline:
        raise RuntimeError(f"No inlineData image part in Gemini response: {data}")
    import base64
    return base64.b64decode(inline["inlineData"]["data"])


def generate_image(prompt: str, size: str = "1K") -> bytes:
    """Run image generation through Qwen-SG (wan2.7-image-pro) -> Qwen-VA
    (wan2.7-image-pro) -> Gemini (gemini-2.5-flash-image), in order. Returns
    raw image bytes from the first tier that genuinely succeeds. Raises
    LLMFallbackError only if all three tiers genuinely fail."""
    creds = load_credentials()
    errors = []

    if creds.get("QWEN_API_KEY") and creds.get("QWEN_BASE_URL"):
        try:
            return _wan_image_generate(creds["QWEN_BASE_URL"], creds["QWEN_API_KEY"], prompt, size)
        except Exception as e:
            errors.append(f"Qwen Singapore (wan2.7-image-pro): {e}")
    else:
        errors.append("Qwen Singapore: QWEN_API_KEY/QWEN_BASE_URL not set")

    if creds.get("QWEN_API_KEY_VIRGINIA_BACKUP") and creds.get("QWEN_BASE_URL_VIRGINIA_BACKUP"):
        try:
            return _wan_image_generate(
                creds["QWEN_BASE_URL_VIRGINIA_BACKUP"],
                creds["QWEN_API_KEY_VIRGINIA_BACKUP"], prompt, size,
            )
        except Exception as e:
            errors.append(f"Qwen Virginia (wan2.7-image-pro): {e}")
    else:
        errors.append("Qwen Virginia: backup creds not set")

    if creds.get("GEMINI_API_KEY"):
        try:
            return _gemini_image_generate(creds["GEMINI_API_KEY"], prompt)
        except Exception as e:
            errors.append(f"Gemini (gemini-2.5-flash-image): {e}")
    else:
        errors.append("Gemini: GEMINI_API_KEY not set")

    raise LLMFallbackError(
        "All 3 image-generation tiers failed:\n  - " + "\n  - ".join(errors)
    )


# ---------------------------------------------------------------------------
# CLI entry point - lets a Windows-side Claude Code session (which can't
# import this module directly) call the chain via
# `wsl -e bash -lc "python3 ~/enterprise-ai-gtm-skill/tools/llm_common/qwen_fallback.py ..."`
# instead of re-implementing fallback logic as a raw PowerShell snippet.
# See color-team-review/SKILL.md and proposal-drafting/SKILL.md "Technical
# Graphics" sections, which call this.
# ---------------------------------------------------------------------------

def _cli():
    import argparse

    parser = argparse.ArgumentParser(
        description="Qwen-first (SG -> VA -> Gemini) LLM fallback chain CLI"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_img = sub.add_parser("image", help="Generate an image from a prompt")
    p_img.add_argument("prompt")
    p_img.add_argument("output_path")
    p_img.add_argument("--size", default="1K")

    p_txt = sub.add_parser("text", help="Generate text from a prompt")
    p_txt.add_argument("prompt")
    p_txt.add_argument("--max-tokens", type=int, default=1024)

    args = parser.parse_args()

    if args.command == "image":
        try:
            data = generate_image(args.prompt, size=args.size)
        except LLMFallbackError as e:
            print(f"FAILED: {e}", file=__import__("sys").stderr)
            raise SystemExit(1)
        with open(args.output_path, "wb") as f:
            f.write(data)
        print(f"OK: wrote {len(data)} bytes to {args.output_path}")
    elif args.command == "text":
        try:
            out = chat_completion(args.prompt, max_tokens=args.max_tokens)
        except LLMFallbackError as e:
            print(f"FAILED: {e}", file=__import__("sys").stderr)
            raise SystemExit(1)
        print(out)


if __name__ == "__main__":
    _cli()
