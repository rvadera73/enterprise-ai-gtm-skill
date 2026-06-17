# Marketing Factory Setup Guide
**Zero-Cost, Fully Automated GTM Content Production**

---

## Overview

This is a complete marketing automation system that generates professional-grade GTM content (LinkedIn posts, images, voiceovers, videos, blog posts, emails) from a single topic input. Zero human team required after setup.

**What You Get**: One command → LinkedIn post + image + voiceover + video + blog + email, all published automatically.

---

## Prerequisites

### Required
- Python 3.9+
- Node.js 18+
- Git
- FFmpeg (for video optimization)

### API Keys (All Free)
1. **Google Gemini API** (for image generation)
   - Free: 500 API requests/day, no credit card required
   - Sign up: https://ai.google.dev
   - Get API key from Google AI Studio

2. **FAL.ai** (alternative image generation)
   - Free: $20 credits for new business email signups
   - $0.003 per image with FLUX.1 Schnell
   - Sign up: https://fal.ai

3. **Brevo** (for email automation)
   - Free: 300 emails/day
   - Full API access included
   - Sign up: https://www.brevo.com

4. **Postiz** (for social publishing)
   - Free: Self-hosted via Docker
   - Supports 20+ platforms
   - GitHub: https://github.com/gitroomhq/postiz-app

5. **Anthropic API** (for Claude)
   - Required if not using Claude Code
   - Pay-as-you-go (optional)

---

## Installation

### 1. Clone and Setup Repository

```bash
cd enterprise-ai-gtm-skill

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r marketing-factory/requirements.txt
```

### 2. Install System Dependencies

```bash
# macOS (using Homebrew)
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows (using Chocolatey)
choco install ffmpeg
```

### 3. Setup Node.js Project (for Remotion video)

```bash
cd marketing-factory/video
npm install
cd ../..
```

### 4. Setup Environment Variables

Create `.env` file in `marketing-factory/` directory:

```bash
# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# FAL.ai (for image generation)
FAL_KEY=your_fal_key_here

# Anthropic Claude API
ANTHROPIC_API_KEY=your_anthropic_key_here

# Brevo (email)
BREVO_API_KEY=your_brevo_api_key_here

# Postiz (optional, if self-hosting)
POSTIZ_API_URL=http://localhost:3000/api

# Analytics (Umami or similar)
UMAMI_API_KEY=your_umami_api_key_here
```

---

## Quick Start

### Generate Content (All-in-One)

```bash
# Simple: Just provide topic
python marketing-factory/scripts/gtm_factory.py "Enterprise AI Foundry MVP in 15 Days"

# This will:
# 1. Generate LinkedIn post
# 2. Create branded image
# 3. Generate voiceover script
# 4. Render video
# 5. Publish to Postiz
# 6. Send email digest
```

### Individual Steps

**Generate LinkedIn Post**
```bash
python marketing-factory/scripts/generate_post.py "Your Topic Here"
```
Output: `linkedin_post_your_topic_here.txt`

**Generate Image**
```bash
python marketing-factory/scripts/generate_image.py "Your post text"
```
Requires: `GEMINI_API_KEY` or `FAL_KEY`

**Generate Voiceover**
```bash
python marketing-factory/scripts/generate_voiceover.py "Your script text" --output voiceover.mp3
```
No API key required (uses Microsoft edge-tts)

**Render Video**
```bash
cd marketing-factory/video
npm run render:linkedin
npm run render:youtube
```
Outputs: `out/LinkedInPost.mp4`, `out/YouTubeIntro.mp4`

---

## Setup Details by Component

### Component 1: LinkedIn Post Generation

**Script**: `marketing-factory/scripts/generate_post.py`  
**Tech**: Claude API (Opus 4.8)  
**Input**: Topic string  
**Output**: 400-word post in your brand voice  
**Cost**: ~$0.01 per post  
**Speed**: ~5 seconds

The post generator uses Claude to write in your brand voice. It:
- Challenges the status quo (poses a question)
- Includes proof points (data, examples)
- Ends with specific CTA
- Adds relevant hashtags

**Example Output**:
```
For years, enterprise modernization has relied on the wrong metric...

By shifting from project-based engineering to product-based value creation...

The results? 5 systems delivered in 90 days, $1.33M total investment...

If your organization is asking "why does this take 18 months"...
```

### Component 2: Image Generation

**Options**:
1. **Google Gemini API** (Free: 500/day)
2. **FAL.ai** (Free: $20 credits, then $0.003/image)
3. **Local ComfyUI** (Free, runs on your GPU)

**Implementation**:
```python
# generate_image.py handles all three options
# Set GEMINI_API_KEY or FAL_KEY in .env
python marketing-factory/scripts/generate_image.py "post text" --output image.png
```

**Output**: 1200×628px PNG (LinkedIn landscape format)  
**Specs**: Navy (#013060), Teal (#4AC4D3), Orange (#E6800C)  
**Speed**: ~30 seconds (FAL.ai)

### Component 3: Voiceover Generation

**Script**: `marketing-factory/scripts/generate_voiceover.py`  
**Tech**: edge-tts (Microsoft neural voices)  
**Input**: Script text  
**Output**: MP3 + VTT subtitle file  
**Cost**: $0 (completely free)  
**Speed**: ~5 seconds per 1 minute of audio  
**Quality**: Human-quality, multiple voices available

**Available Voices**:
- `en-US-AriaNeural` (Female, professional)
- `en-US-GuyNeural` (Male, warm)
- `en-US-JennyNeural` (Female, conversational)
- Plus 50+ other languages/accents

**Example**:
```bash
python marketing-factory/scripts/generate_voiceover.py \
  "Enterprise modernization takes 18 months. But does it have to?" \
  --voice en-US-AriaNeural \
  --rate "+5%" \
  --output voiceover.mp3
```

### Component 4: Video Rendering

**Framework**: Remotion (React → MP4)  
**Tech**: TypeScript/React components  
**Input**: Topic, voiceover MP3, image  
**Output**: MP4 video (optimized)  
**Cost**: $0 (free for ≤3 person teams)  
**Speed**: ~2 minutes for 30-second video

**Compositions**:
- `LinkedInPost.tsx` — 30-second vertical video
- `YouTubeIntro.tsx` — 60-second landscape video

**Structure**:
1. Title card with topic (2-3 sec)
2. Problem statement with animation (10 sec)
3. Solution framework explanation (10 sec)
4. Proof with data visualization (5 sec)
5. Call-to-action (2-3 sec)

**Render**:
```bash
cd marketing-factory/video
npm run render:linkedin
# Output: out/LinkedInPost.mp4 (1280×1080, H.264)
```

**Video Optimization**:
```bash
ffmpeg -i raw.mp4 -crf 28 -preset slow optimized.mp4
# Reduces file size by 80% with minimal quality loss
```

### Component 5: Social Publishing

**Platform**: Postiz (self-hosted)  
**Support**: 20+ networks (LinkedIn, Twitter, YouTube, Instagram, TikTok, etc.)  
**Cost**: $0 (self-hosted), or $0.01/render on Automators plan  
**Speed**: <1 second per post

**Setup Postiz** (Docker):
```bash
# Clone Postiz
git clone https://github.com/gitroomhq/postiz-app.git
cd postiz-app

# Deploy via Docker Compose
docker-compose up -d

# Access at http://localhost:3000
```

**Publish via API**:
```python
# publish_postiz.py
import requests

def publish_to_postiz(post_text, image_path, video_path):
    """Queue post to Postiz (which handles all 20+ networks)."""
    headers = {"Authorization": f"Bearer {POSTIZ_API_TOKEN}"}
    
    payload = {
        "text": post_text,
        "images": [image_path],
        "videos": [video_path],
        "platforms": ["linkedin", "twitter", "youtube"],
        "scheduledAt": "2026-06-16T09:00:00Z"
    }
    
    response = requests.post(
        "http://localhost:3000/api/posts",
        json=payload,
        headers=headers
    )
    return response.json()
```

### Component 6: Email Automation

**Platform**: Brevo  
**Cost**: $0 (300 emails/day free)  
**Speed**: <1 second per email

**Setup**:
1. Sign up: https://www.brevo.com
2. Get API key from settings
3. Add `BREVO_API_KEY` to `.env`

**Send Email Digest**:
```python
# publish_brevo.py
import requests

def send_email_digest(recipient_email, post_text, video_link):
    """Send content digest to subscriber."""
    response = requests.post(
        "https://api.brevo.com/v3/smtp/email",
        headers={"api-key": BREVO_API_KEY},
        json={
            "sender": {"name": "Enterprise AI GTM", "email": "gtm@your-domain.com"},
            "to": [{"email": recipient_email}],
            "subject": "Weekly Enterprise AI Insights",
            "htmlContent": f"""
            <h2>{post_text[:100]}...</h2>
            <p><a href="{video_link}">Watch the video</a></p>
            """
        }
    )
    return response.json()
```

### Component 7: Analytics

**Platform**: Umami (self-hosted) or Umami Cloud  
**Cost**: $0 (self-hosted) or $0 (1M events/month free tier)  
**Speed**: Real-time

**Setup Umami on Cloudflare**:
```bash
# Clone and deploy
git clone https://github.com/umami-software/umami.git
cd umami

# Deploy to Cloudflare Pages (free)
npm run build
wrangler pages deploy dist
```

**Track Content Performance**:
```javascript
// Embed in your Astro/Hugo site
<script async defer src="https://your-umami-domain.com/script.js" 
  data-website-id="YOUR_WEBSITE_ID"></script>

// Track events
umami.track('linkedin-post-click', { topic: 'Enterprise AI' })
```

---

## Complete Workflow

### Daily Automation

**Schedule via GitHub Actions** (`.github/workflows/generate-content.yml`):

```yaml
name: Daily Content Generation
on:
  schedule:
    - cron: '0 8 * * 1-5'  # 8 AM Mon-Fri

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r marketing-factory/requirements.txt
          sudo apt-get install ffmpeg
      
      - name: Generate content
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          BREVO_API_KEY: ${{ secrets.BREVO_API_KEY }}
        run: |
          python marketing-factory/scripts/gtm_factory.py "$(cat today_topic.txt)"
      
      - name: Commit blog post
        run: |
          git config user.name "GTM Bot"
          git config user.email "gtm@your-domain.com"
          git add marketing-factory/blog/src/content/posts/
          git commit -m "Add blog post: $(date +%Y-%m-%d)"
          git push
```

### Weekly Performance Report

**Schedule via GitHub Actions**:

```yaml
name: Weekly Analytics Report
on:
  schedule:
    - cron: '0 9 * * 1'  # 9 AM Mondays

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - name: Pull analytics
        env:
          UMAMI_API_KEY: ${{ secrets.UMAMI_API_KEY }}
        run: |
          python marketing-factory/scripts/analytics_pull.py
      
      - name: Generate report
        run: |
          python marketing-factory/scripts/generate_report.py
      
      - name: Send report
        run: |
          python marketing-factory/scripts/send_report.py
```

---

## Verification Checklist

After setup, verify each component:

- [ ] **Post Generation**: `python marketing-factory/scripts/generate_post.py "Test Topic"` produces 400-word post
- [ ] **Image Generation**: Image appears in 1200×628 format with brand colors
- [ ] **Voiceover**: MP3 file created with clear audio and matching SRT subtitles
- [ ] **Video Render**: 30-second LinkedIn video renders to MP4
- [ ] **Publishing**: Postiz shows scheduled post in dashboard
- [ ] **Email**: Test email delivered from Brevo
- [ ] **Analytics**: Umami dashboard shows tracking code active
- [ ] **Blog**: New markdown file appears in Astro site

---

## Cost Analysis

**Monthly Cost Estimate** (for 20 posts/month):

| Component | Cost/Month | Notes |
|-----------|-----------|-------|
| Post generation (Claude) | $0.20 | $0.01 × 20 posts |
| Image generation (FAL.ai) | $0.06 | $0.003 × 20 images |
| Voiceover (edge-tts) | $0 | Completely free |
| Video rendering (Remotion) | $0 | Free for ≤3 person teams |
| Email (Brevo) | $0 | 300/day free tier |
| Social publishing (Postiz) | $0 | Self-hosted Docker |
| Analytics (Umami) | $0 | Self-hosted or 1M free tier |
| **Total** | **$0.26** | Less than a coffee |

---

## Troubleshooting

### Issue: "ANTHROPIC_API_KEY not found"
**Solution**: Set environment variable
```bash
export ANTHROPIC_API_KEY=sk-your-key-here
```

### Issue: "FAL_KEY not set / FAL API error"
**Solution**: 
1. Get free $20 credits at https://fal.ai (business email signup)
2. Paste API key in `.env`

### Issue: "edge-tts not found"
**Solution**: 
```bash
pip install edge-tts
```

### Issue: "Remotion render timeout"
**Solution**:
- Reduce video complexity
- Lower resolution (720p instead of 1080p)
- Use FFmpeg optimization post-render

### Issue: "Cannot connect to Postiz API"
**Solution**: 
```bash
# Check if Postiz container is running
docker ps | grep postiz

# If not, start it
docker-compose up -d
```

---

## Next Steps

1. **Set up daily automation**: Configure GitHub Actions to generate content daily
2. **Create content calendar**: Plan topics for next 4 weeks
3. **Configure Postiz**: Set up LinkedIn, Twitter, YouTube, email accounts
4. **Test end-to-end**: Run full pipeline once, verify all outputs
5. **Monitor performance**: Set up Umami analytics, weekly reports
6. **Iterate**: Adjust prompts, images, voice based on engagement data

---

## Support

For issues or questions:
- ComfyUI MCP: https://github.com/artokun/comfyui-mcp
- Postiz: https://github.com/gitroomhq/postiz-app
- Remotion: https://remotion.dev/docs
- FAL.ai: https://fal.ai/docs
- Brevo: https://developers.brevo.com

---

**Ready to launch?** Run:
```bash
python marketing-factory/scripts/gtm_factory.py "Your First Topic"
```

This will be your fully automated GTM content factory. ✨
