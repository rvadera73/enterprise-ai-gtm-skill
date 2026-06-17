#!/bin/bash
# Direct LinkedIn Profile Post Fetcher
# Uses browser automation to fetch posts from your LinkedIn profile

# Configuration
PROFILE_URL="https://www.linkedin.com/in/rahul-vadera-1803a61/"
OUTPUT_FILE="linkedin_posts_from_profile.txt"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  LINKEDIN POST FETCHER (Direct)                               ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "🔗 Profile: $PROFILE_URL"
echo "📁 Output: $OUTPUT_FILE"
echo ""

# Check if playwright is installed
if ! python3 -c "import playwright" 2>/dev/null; then
    echo "⚠️  Playwright not installed"
    echo "Install with: pip install playwright && playwright install chromium"
    echo ""
    echo "Then run this script again."
    exit 1
fi

# Python script to fetch posts
python3 << 'EOF'
import asyncio
from playwright.async_api import async_playwright
import re
from pathlib import Path

async def fetch_posts():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("🌐 Opening LinkedIn profile...")
        await page.goto("https://www.linkedin.com/in/rahul-vadera-1803a61/", wait_until="networkidle")

        # Wait for page to load
        await page.wait_for_timeout(3000)

        # Check if logged in (look for profile header)
        try:
            await page.wait_for_selector("[data-test-id='profile-posts-feed']", timeout=5000)
            print("✅ Profile loaded")
        except:
            print("⚠️  You may not be logged in. Please log in to LinkedIn, then run again.")
            await browser.close()
            return []

        # Scroll to load more posts
        posts_text = []

        for i in range(3):  # Scroll 3 times to load ~10 posts
            print(f"📜 Scrolling... ({i+1}/3)")
            await page.evaluate("window.scrollBy(0, 2000)")
            await page.wait_for_timeout(2000)

            # Extract post text
            posts = await page.query_selector_all(".feed-share-update__description, [data-test-id='feed-share-text']")

            for post in posts:
                text = await post.inner_text()
                if text and len(text) > 20:  # Filter out short/empty posts
                    posts_text.append(text)

        # Remove duplicates
        posts_text = list(dict.fromkeys(posts_text))

        print(f"✅ Extracted {len(posts_text)} posts")

        # Save to file
        with open("linkedin_posts_from_profile.txt", "w", encoding="utf-8") as f:
            f.write("\n---\n".join(posts_text))

        print(f"💾 Saved to: linkedin_posts_from_profile.txt")

        await browser.close()

# Run the fetch
asyncio.run(fetch_posts())
EOF

echo ""
echo "✅ Posts fetched!"
echo ""
echo "📖 Next step: Analyze the posts"
echo "   python content_analyzer.py --input $OUTPUT_FILE"
