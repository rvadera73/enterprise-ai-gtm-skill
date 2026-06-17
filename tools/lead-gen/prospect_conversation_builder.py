#!/usr/bin/env python3
"""
Prospect Conversation Builder
Generates a closing conversation framework based on your messaging profile
and the specific prospect's pain points.

Usage:
  python prospect_conversation_builder.py
"""

from anthropic import Anthropic

client = Anthropic()
conversation_history = []

def send_message(user_message: str) -> str:
    """Send message to Claude and maintain conversation history."""
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=2000,
        system="""You are an expert GTM strategist helping build closing conversations for B2B enterprise sales.

Your job is to help structure a prospect conversation based on:
1. The prospect's specific pain point
2. The seller's authentic messaging (tone, themes, value props)
3. The buyer's implicit concerns

Always ask clarifying questions to understand the prospect better. Then generate a conversation framework that:
- Opens with something that resonates with the buyer's world (not your world)
- Addresses their implicit concern early
- Shows how you solve their specific problem
- Uses their language/tone, not jargon
- Closes with a clear next step (prove it in 30 days, pilot, evaluate, etc.)

Keep responses practical and direct. No fluff.""",
        messages=conversation_history
    )

    assistant_message = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


def main():
    """Interactive conversation builder."""

    print("""
╔════════════════════════════════════════════════════════════════╗
║     PROSPECT CONVERSATION BUILDER                              ║
║     Build closing conversations that actually work             ║
╚════════════════════════════════════════════════════════════════╝

This tool helps you structure a conversation with a prospect based on:
1. Their specific pain point
2. Your authentic messaging
3. Their implicit concerns

Let's start. I'll ask you about the prospect, then generate a framework
for your conversation.

(Type 'done' at any time to exit)

""")

    # Initial prompt
    initial = send_message("""
I want to build a closing conversation framework with a prospect.

Please ask me about:
1. The prospect's company, role, and specific pain point
2. What product/solution we're offering (Ask-AI, Enterprise AI Foundry, etc.)
3. What the buyer's implicit concern is (timeline? cost? risk? complexity?)
4. What we want them to do (evaluate in 30 days, pilot, schedule demo, etc.)

Start by asking about the prospect.
""")

    print(f"Assistant: {initial}\n")

    # Multi-turn conversation
    turn = 1
    while True:
        user_input = input(f"You (turn {turn}): ").strip()

        if user_input.lower() == "done":
            print("\nConversation saved. Use the framework above to structure your pitch.")
            break

        if not user_input:
            continue

        response = send_message(user_input)
        print(f"\nAssistant: {response}\n")
        turn += 1

        # Check if assistant is ready to generate the framework
        if "framework" in response.lower() or "here's your" in response.lower() or "conversation" in response.lower():
            save_choice = input("\nWould you like to save this framework? (yes/no): ").strip().lower()
            if save_choice == "yes":
                save_framework()
                break


def save_framework():
    """Save the conversation history as a framework document."""

    # Extract the final framework from conversation
    framework_prompt = send_message("""
Based on our conversation, please generate a COMPLETE CONVERSATION FRAMEWORK document that includes:

## PROSPECT PROFILE
- Company/Role/Pain Point
- Implicit Concern
- Current Situation

## CONVERSATION OPENING (30 seconds)
- What you lead with (not your product, but their world)
- Goal: Get them to lean in and care

## PROBLEM EXPLORATION (2-3 minutes)
- 3-4 questions that reveal their pain
- Your themes that connect to their pain
- Example: "So you're saying X takes Y time and costs Z?"

## SOLUTION NARRATIVE (3-5 minutes)
- How you solve this specific problem
- Your proof (Ask-AI in IACP? CBP? Other?)
- Why they should believe you (speed, flexibility, fail-fast)

## BUYING SIGNAL & OBJECTION HANDLING (1-2 minutes)
- What buying signals to listen for
- Common objections + your response (based on your authentic voice)
- How to address their implicit concern

## CLOSING & NEXT STEP (1 minute)
- Clear ask: "Let's prove this in 30 days with [specific thing]"
- Why 30 days? What you'll show them?
- If yes → Pilot agreement
- If no → What's the concern?

Format as a document with exact words to say where helpful.
""")

    output_path = "/home/rahulvadera/enterprise-ai-gtm-skill/prospect_frameworks/closing_conversation_framework.md"

    # Create output directory if it doesn't exist
    from pathlib import Path
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        f.write("# CLOSING CONVERSATION FRAMEWORK\n\n")
        f.write(framework_prompt)

    print(f"\n✅ Framework saved to: {output_path}")


if __name__ == "__main__":
    main()
