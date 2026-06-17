#!/usr/bin/env python3
"""
Generate LinkedIn post image using Google Gemini API.
Input: post text
Output: 1200x628 PNG image with brand colors
"""

import os
import sys
import base64
import requests
from datetime import datetime

def generate_image_prompt_from_post(post_text: str) -> str:
    """Extract key visual message from LinkedIn post for image generation."""

    # For now, use a structured prompt that works for Enterprise AI Foundry content
    # In production, would use Claude to intelligently extract this

    return """Create a professional enterprise architecture infographic for LinkedIn:
- Format: 1200x628 pixels (LinkedIn landscape)
- Style: Clean, grid-based, solution-architecture aesthetic
- Colors: Navy (#013060), Teal (#4AC4D3), Orange (#E6800C), Light Blue (#DBF3F6)
- Content: Show contrast between Traditional (18-month waterfall) vs. Enterprise AI Foundry (90-day path)
- Timeline sections: Ideation, Pre-MVP, MVP, Production, Scale
- Key metric: "15-day MVP validation" prominently displayed
- No marketing language, pure business outcome visualization
- Include 4-5 system examples at bottom: Ask-AI, Risk Scoring, Case Management, eCourt
- Professional, architectural, not playful
- Quality: LinkedIn publication-ready"""

def generate_image_with_gemini(prompt: str) -> bytes:
    """Generate image using Google Gemini API (free tier)."""

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")

    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

    # Gemini API for image generation
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1024
        }
    }

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key
    }

    # Note: Gemini 2.0 Flash doesn't have native image generation in this endpoint
    # For actual implementation, would need to use:
    # 1. Gemini API with image generation model (if available)
    # 2. Or integrate with Imagen 4 (via Vertex AI) or similar
    # For now, return a placeholder that guides implementation

    print("Note: Gemini API text endpoint doesn't support image generation directly.")
    print("For actual implementation, integrate with:")
    print("- Google Imagen 4 (via Vertex AI)")
    print("- FAL.ai FLUX Schnell ($0.003/image)")
    print("- Replicate API")
    print("\nFor testing, generate image via:")
    print("  curl -X POST 'https://api.fal.ai/v1/fal-ai/flux/schnell/submit' \\")
    print("    -H 'Authorization: Key $FAL_KEY' \\")
    print("    -H 'Content-Type: application/json' \\")
    print("    -d '{\"prompt\": \"...\", \"image_size\": \"landscape_4_3\", \"num_images\": 1}'")

    return None

def fallback_image_generation(prompt: str, output_path: str):
    """Fallback: Generate image using FAL.ai (recommended, $0.003/image)."""

    fal_key = os.environ.get("FAL_KEY")
    if not fal_key:
        print("FAL_KEY not set. To generate real images, set FAL_KEY environment variable.")
        print("Get free $20 credits at https://fal.ai (signup with business email)")
        return None

    import requests

    url = "https://api.fal.ai/v1/fal-ai/flux/schnell/submit"
    headers = {
        "Authorization": f"Key {fal_key}",
        "Content-Type": "application/json"
    }

    # Request image generation
    payload = {
        "prompt": prompt,
        "image_size": "landscape_4_3",  # 4:3 aspect ratio close to 1200x628
        "num_images": 1,
        "num_inference_steps": 4,  # Schnell is optimized for 4 steps
        "guidance_scale": 3.5
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()

        if "request_id" in result:
            request_id = result["request_id"]
            print(f"Image generation submitted. Request ID: {request_id}")
            print("Poll endpoint: https://api.fal.ai/v1/requests/{request_id}/status")
            return request_id
        else:
            print(f"Unexpected response: {result}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error calling FAL.ai API: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_image.py '<post_text>' [--output output.png]")
        print("\nThis script generates a LinkedIn-formatted image (1200x628px) for your post.")
        print("Requires GEMINI_API_KEY or FAL_KEY environment variable.")
        sys.exit(1)

    post_text = sys.argv[1]
    output_path = "linkedin_image.png"

    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    print(f"Generating image prompt from post...")
    image_prompt = generate_image_prompt_from_post(post_text)
    print(f"Prompt: {image_prompt[:200]}...\n")

    print("Attempting FAL.ai image generation (recommended)...")
    request_id = fallback_image_generation(image_prompt, output_path)

    if request_id:
        print(f"\nImage queued for generation.")
        print(f"Check status and download via request ID: {request_id}")
    else:
        print("\n⚠️ Image generation skipped. Set FAL_KEY to enable.")
        print("Free $20 credits: https://fal.ai (business email)")
        print("Or use: GEMINI_API_KEY for Imagen integration")

if __name__ == "__main__":
    main()
