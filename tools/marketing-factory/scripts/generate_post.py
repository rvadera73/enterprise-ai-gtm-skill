#!/usr/bin/env python3
"""
Generate LinkedIn post from topic using Claude API.
Input: topic string
Output: LinkedIn post (400 words, brand voice)
"""

import os
import sys
import json
import anthropic

def load_brand_guidelines():
    """Load brand voice guidelines."""
    return {
        "brand_voice": "Solution architect perspective, technical depth, authentic, no marketing fluff",
        "tone": "Professional, thought-leader, pragmatic",
        "structure": "Hook (problem) → Insight → Proof → CTA",
        "length": "400 words max",
        "hashtags": ["EnterpriseAI", "SoftwareModernization", "TechnicalDebt", "AIServices", "AgenticAI", "FederalTech", "DigitalTransformation"],
    }

def generate_linkedin_post(topic: str) -> str:
    """Generate LinkedIn post from topic."""

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    brand = load_brand_guidelines()

    prompt = f"""You are writing a LinkedIn post for a solution architect discussing enterprise AI and modernization.

TOPIC: {topic}

BRAND VOICE & GUIDELINES:
- Voice: {brand['brand_voice']}
- Tone: {brand['tone']}
- Structure: {brand['structure']}
- Max length: {brand['length']}
- Reference existing successful posts about Enterprise AI Foundry, ASF (Agile Software Fabric), AEF (Agentic Engineering Factory)
- Focus on: Customer problems (not features), business outcomes (not technical details), paradigm shifts (not incremental improvements)
- No emojis, no marketing language, no buzzwords

EXAMPLES OF GOOD POSTS:
1. "For years, enterprise modernization has relied on the wrong metric: how fast we can build an MVP. But as a Solution Architect, my experience has taught me the real question is: 'How quickly can we determine if it's worth building?'"
2. "By shifting from project-based engineering to product-based value creation, we successfully accelerated delivery across four major enterprise systems."

WRITE A LINKEDIN POST NOW:
- Start with a hook that challenges status quo or asks a question
- Include 1-2 examples or proof points
- End with a clear, specific CTA (not generic "let's talk")
- Add 6-8 relevant hashtags at the end
- DO NOT use markdown formatting, keep it as plain text with line breaks
- Total: 300-400 words"""

    message = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_post.py '<topic>'")
        sys.exit(1)

    topic = sys.argv[1]

    print(f"Generating LinkedIn post for topic: {topic}\n")
    print("=" * 80)

    post = generate_linkedin_post(topic)
    print(post)
    print("=" * 80)

    # Also save to file
    output_file = f"linkedin_post_{topic.lower().replace(' ', '_')}.txt"
    with open(output_file, "w") as f:
        f.write(post)
    print(f"\nPost saved to: {output_file}")

if __name__ == "__main__":
    main()
