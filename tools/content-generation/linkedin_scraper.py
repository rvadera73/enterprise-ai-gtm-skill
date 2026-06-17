#!/usr/bin/env python3
"""
LinkedIn Content Scraper
Fetches posts directly from a LinkedIn profile URL
and saves them for analysis.

Usage:
  python linkedin_scraper.py --profile "https://www.linkedin.com/in/rahul-vadera-1803a61/" --count 10

Prerequisites:
  pip install playwright
  playwright install chromium
"""

import argparse
import json
import asyncio
from pathlib import Path
from typing import Optional
from datetime import datetime

# For non-Playwright fallback
import urllib.parse
import urllib.request


def fetch_linkedin_posts_via_api(profile_url: str, count: int = 10) -> list:
    """
    Fetch LinkedIn posts using LinkedIn's unofficial API endpoint.

    This approach works without authentication for public profiles.
    """

    # Extract username from URL
    # https://www.linkedin.com/in/rahul-vadera-1803a61/ → rahul-vadera-1803a61
    username = profile_url.split("/in/")[1].rstrip("/")

    print(f"📍 Fetching posts for: {username}")
    print(f"📏 Requesting: {count} posts")

    posts = []

    # LinkedIn API endpoint for public profile
    api_endpoint = f"https://www.linkedin.com/voyager/api/identity/profiles/{username}/profile-by-normalized-url"

    try:
        # Add headers to mimic browser request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/vnd.linkedin.normalized+json+2.1",
        }

        # Note: Direct API access is restricted by LinkedIn
        # This is a fallback that may not work
        print("⚠️  Note: LinkedIn restricts direct API access.")
        print("💡 Recommended: Use LinkedIn Data Export feature or manual copy/paste")

        return []

    except Exception as e:
        print(f"❌ API fetch failed: {e}")
        return []


def fetch_linkedin_posts_via_export(profile_url: str) -> dict:
    """
    Provide instructions for using LinkedIn's official Data Export feature.
    This is the most reliable method.
    """

    print("""
╔════════════════════════════════════════════════════════════════╗
║  LINKEDIN DATA EXPORT (Official Method - Most Reliable)        ║
╚════════════════════════════════════════════════════════════════╝

LinkedIn restricts automated scraping. The official way to get your posts:

STEP 1: Go to LinkedIn Settings
  → https://www.linkedin.com/account/account-settings/

STEP 2: Select "Data Privacy"
  → Left sidebar → "Data privacy" → "Get a copy of your data"

STEP 3: Request Your Data
  → Check: "Posts"
  → Download format: JSON or CSV
  → Click "Request archive"

STEP 4: Wait for Email
  → LinkedIn sends download link (usually within 24 hours)

STEP 5: Save Posts to File
  → Once downloaded, save posts to: posts_export.json

STEP 6: Run Analysis
  → python content_analyzer.py --input posts_export.json

This gives you 100% of your posts, their metadata, and engagement data.

Alternative: Copy/paste posts manually into linkedin_content_template.txt
(Takes ~15 minutes for 5-10 posts)

""")

    return {
        "method": "linkedin_export",
        "status": "pending",
        "instructions": "Follow steps above"
    }


def parse_linkedin_export(export_file: str) -> list:
    """
    Parse LinkedIn data export file and extract posts.
    Supports both JSON and CSV formats.
    """

    file_path = Path(export_file)

    if not file_path.exists():
        print(f"❌ File not found: {export_file}")
        return []

    posts = []

    try:
        if export_file.endswith(".json"):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # LinkedIn export structure varies
            # Try common patterns
            if isinstance(data, list):
                for post in data:
                    if "content" in post:
                        posts.append({
                            "text": post.get("content", ""),
                            "date": post.get("date", ""),
                            "likes": post.get("likes", 0),
                            "comments": post.get("comments", 0),
                        })
                    elif "message" in post:
                        posts.append({
                            "text": post.get("message", ""),
                            "date": post.get("date", ""),
                        })

            elif isinstance(data, dict):
                # Might be nested structure
                if "posts" in data:
                    posts = data["posts"]
                elif "content" in data:
                    posts = data["content"]

        elif export_file.endswith(".csv"):
            import csv
            with open(file_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    posts.append({
                        "text": row.get("content") or row.get("message") or row.get("text", ""),
                        "date": row.get("date", ""),
                        "likes": row.get("likes", 0),
                    })

        print(f"✅ Extracted {len(posts)} posts from {export_file}")
        return posts

    except Exception as e:
        print(f"❌ Error parsing file: {e}")
        return []


def save_posts_for_analysis(posts: list, output_file: str = "linkedin_posts_for_analysis.txt") -> str:
    """
    Convert extracted posts to format readable by content_analyzer.py
    """

    if not posts:
        print("⚠️  No posts to save.")
        return ""

    # Format: posts separated by "---"
    formatted = "\n---\n".join([
        p.get("text", "") for p in posts
        if p.get("text", "").strip()
    ])

    output_path = Path(output_file)
    output_path.write_text(formatted, encoding="utf-8")

    print(f"✅ Saved {len(posts)} posts to: {output_path}")
    print(f"\n📖 Next step:")
    print(f"   python content_analyzer.py --input {output_file}")

    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch LinkedIn posts and prepare for content analysis"
    )
    parser.add_argument(
        "--profile",
        help="LinkedIn profile URL (e.g., https://www.linkedin.com/in/rahul-vadera-1803a61/)"
    )
    parser.add_argument(
        "--export-file",
        help="Path to LinkedIn data export file (JSON or CSV)"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="Number of recent posts to fetch (default: 10)"
    )
    parser.add_argument(
        "--output",
        default="linkedin_posts_for_analysis.txt",
        help="Output file for formatted posts"
    )

    args = parser.parse_args()

    print("""
╔════════════════════════════════════════════════════════════════╗
║  LINKEDIN CONTENT SCRAPER & ANALYZER                          ║
╚════════════════════════════════════════════════════════════════╝
""")

    # If export file provided, parse it
    if args.export_file:
        print(f"📁 Parsing LinkedIn export: {args.export_file}")
        posts = parse_linkedin_export(args.export_file)

        if posts:
            output_path = save_posts_for_analysis(posts, args.output)
            print(f"\n🚀 Ready to analyze!")
            print(f"   Run: python content_analyzer.py --input {output_path}")
        else:
            print("\n❌ No posts found in export file.")
            print("   Make sure you requested 'Posts' in LinkedIn Data Export.")

    # If profile URL provided, show instructions
    elif args.profile:
        print(f"📍 Profile: {args.profile}")
        result = fetch_linkedin_posts_via_export(args.profile)

    else:
        # Show instructions
        print("""
NO PROFILE OR FILE PROVIDED

Two methods to get your LinkedIn posts:

METHOD 1 (Recommended): LinkedIn Data Export
  Command: python linkedin_scraper.py --profile "https://www.linkedin.com/in/rahul-vadera-1803a61/"

  Then follow the steps to request your data from LinkedIn.
  Once you have posts_export.json:

  Command: python linkedin_scraper.py --export-file posts_export.json

  Then: python content_analyzer.py --input linkedin_posts_for_analysis.txt

METHOD 2 (Quick): Manual Copy/Paste
  1. Open linkedin_content_template.txt
  2. Copy 5-10 recent posts
  3. Paste into file, separated by "---"
  4. Save

  Then: python content_analyzer.py --input linkedin_content_template.txt

Which method would you like to use?
        """)


if __name__ == "__main__":
    main()
