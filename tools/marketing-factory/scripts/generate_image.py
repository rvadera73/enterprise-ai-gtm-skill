#!/usr/bin/env python3
"""
Generate LinkedIn post image via the Qwen-first fallback chain:
  1. Qwen Singapore (wan2.7-image-pro) - primary
  2. Qwen Virginia   (wan2.7-image-pro) - fallback
  3. Gemini          (gemini-2.5-flash-image) - third-tier fallback

Input: post text
Output: PNG image (default 1200x628-ish brand-colored infographic, actual
        pixel size is whatever the generating tier returns - wan2.7 returns
        square 1024x1024 by default; resize downstream if an exact 1200x628
        crop is required)

Replaces a previous version of this script that called the Gemini text
endpoint (gemini-2.0-flash:generateContent) for image generation. That
endpoint does not do image generation at all (its own code comments said so)
and this script had apparently never produced a real image. The new chain
was verified live on 2026-10-09: real wan2.7-image-pro task submitted,
polled to SUCCEEDED, and a real PNG downloaded from the Qwen Singapore
account. See tools/llm_common/qwen_fallback.py for the shared implementation
and credential-sourcing notes.
"""

import os
import sys

_TOOLS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, _TOOLS_DIR)
from llm_common.qwen_fallback import generate_image, LLMFallbackError


def generate_image_prompt_from_post(post_text: str) -> str:
    """Extract key visual message from LinkedIn post for image generation."""

    # For now, use a structured prompt that works for Enterprise AI Foundry content
    # In production, would use an LLM to intelligently extract this from post_text

    return """Create a professional enterprise architecture infographic for LinkedIn:
- Format: landscape, solution-architecture aesthetic
- Colors: Navy (#013060), Teal (#4AC4D3), Orange (#E6800C), Light Blue (#DBF3F6)
- Content: Show contrast between Traditional (18-month waterfall) vs. Enterprise AI Foundry (90-day path)
- Timeline sections: Ideation, Pre-MVP, MVP, Production, Scale
- Key metric: "15-day MVP validation" prominently displayed
- No marketing language, pure business outcome visualization
- Include 4-5 system examples at bottom: Ask-AI, Risk Scoring, Case Management, eCourt
- Professional, architectural, not playful
- Quality: LinkedIn publication-ready"""


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_image.py '<post_text>' [--output output.png]")
        print("\nThis script generates a LinkedIn infographic image for your post.")
        print("Credentials: reads QWEN_API_KEY/QWEN_BASE_URL (+ Virginia backup,")
        print("+ GEMINI_API_KEY) from the environment, falling back to")
        print("~/personal-assistant/.env if not set. See tools/llm_common/qwen_fallback.py.")
        sys.exit(1)

    post_text = sys.argv[1]
    output_path = "linkedin_image.png"

    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    print("Generating image prompt from post...")
    image_prompt = generate_image_prompt_from_post(post_text)
    print(f"Prompt: {image_prompt[:200]}...\n")

    print("Generating image (Qwen Singapore -> Qwen Virginia -> Gemini)...")
    try:
        image_bytes = generate_image(image_prompt)
    except LLMFallbackError as e:
        print(f"\nImage generation failed on all 3 tiers:\n{e}")
        sys.exit(1)

    with open(output_path, "wb") as f:
        f.write(image_bytes)
    print(f"\nImage saved to: {output_path} ({len(image_bytes)} bytes)")


if __name__ == "__main__":
    main()
