#!/usr/bin/env python3
"""
Generate voiceover using edge-tts (free Microsoft neural voices).
Input: script text
Output: MP3 file with optional SRT subtitles
"""

import os
import sys
import subprocess
from pathlib import Path

def install_edge_tts():
    """Install edge-tts if not already installed."""
    try:
        import edge_tts
    except ImportError:
        print("Installing edge-tts...")
        subprocess.run([sys.executable, "-m", "pip", "install", "edge-tts"], check=True)

def get_available_voices():
    """List available voices from edge-tts."""
    try:
        result = subprocess.run(
            ["edge-tts", "--list-voices"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except Exception as e:
        print(f"Error listing voices: {e}")
        return None

def generate_voiceover(
    script_text: str,
    output_path: str,
    voice: str = "en-US-AriaNeural",
    rate: str = "+0%"
) -> bool:
    """
    Generate voiceover using edge-tts.

    Args:
        script_text: The text to convert to speech
        output_path: Output MP3 file path
        voice: Voice to use (default: Aria, female, natural)
        rate: Speech rate adjustment (e.g., "+10%", "-10%")

    Returns:
        True if successful, False otherwise
    """

    install_edge_tts()

    try:
        cmd = [
            "edge-tts",
            "--text", script_text,
            "--voice", voice,
            "--rate", rate,
            "--write-media", output_path,
            "--write-subtitles", output_path.replace(".mp3", ".vtt")
        ]

        print(f"Generating voiceover with {voice}...")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✓ Voiceover saved to: {output_path}")
        print(f"✓ Subtitles saved to: {output_path.replace('.mp3', '.vtt')}")
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error generating voiceover: {e}")
        print(f"Stderr: {e.stderr}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_voiceover.py '<script_text>' [--voice VOICE] [--rate RATE] [--output OUTPUT.mp3]")
        print("\nOptions:")
        print("  --voice VOICE    Voice name (default: en-US-AriaNeural)")
        print("  --rate RATE      Rate adjustment: +10%, -10%, etc. (default: +0%)")
        print("  --output OUTPUT  Output file path (default: voiceover.mp3)")
        print("\nAvailable voices:")

        voices = get_available_voices()
        if voices:
            print(voices[:1000])  # Print first 1000 chars
        sys.exit(1)

    script_text = sys.argv[1]

    # Parse optional arguments
    voice = "en-US-AriaNeural"
    rate = "+0%"
    output_path = "voiceover.mp3"

    if "--voice" in sys.argv:
        idx = sys.argv.index("--voice")
        if idx + 1 < len(sys.argv):
            voice = sys.argv[idx + 1]

    if "--rate" in sys.argv:
        idx = sys.argv.index("--rate")
        if idx + 1 < len(sys.argv):
            rate = sys.argv[idx + 1]

    if "--output" in sys.argv:
        idx = sys.argv.index("--output")
        if idx + 1 < len(sys.argv):
            output_path = sys.argv[idx + 1]

    print(f"Script length: {len(script_text)} characters")
    print(f"Voice: {voice}")
    print(f"Rate: {rate}")
    print(f"Output: {output_path}\n")

    success = generate_voiceover(script_text, output_path, voice, rate)

    if success:
        print("\n✓ Voiceover generation complete!")
        # Calculate approximate duration
        word_count = len(script_text.split())
        estimated_seconds = word_count / 150  # ~150 words per minute
        print(f"  Script: {word_count} words (~{estimated_seconds:.0f} seconds of audio)")
    else:
        print("\n✗ Voiceover generation failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
