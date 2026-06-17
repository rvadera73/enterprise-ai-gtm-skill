# Content Analyzer Tool - Quick Start Guide

**Purpose**: Extract your messaging patterns from LinkedIn posts, articles, and content to generate an authentic messaging profile for GTM strategy.

**Why This Matters**: Instead of guessing what messaging will resonate, we analyze what's *actually* working in your existing content.

---

## Setup

### Prerequisites
```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-...
```

### Files Included
- `content_analyzer.py` — Main analysis tool
- `linkedin_content_template.txt` — Template for collecting posts
- This guide

---

## Option 1: Interactive Mode (Easiest)

### Step 1: Paste Your Content
```bash
cd /home/rahulvadera/enterprise-ai-gtm-skill/tools
python content_analyzer.py --interactive
```

### Step 2: Follow Prompts
```
🚀 Content Analyzer - Interactive Mode
=====================================
Paste your LinkedIn posts, articles, or content below.
Separate multiple posts with '---' on its own line.
Type 'DONE' when finished, then 'ANALYZE' to generate profile.

[Paste your content here]
---
[Next post]
---
[Next post]

DONE
```

### Step 3: Review Results
Tool generates `messaging_profile_generated.md` with:
- Core themes you emphasize
- Your tone & voice
- Value propositions you stress
- Buyer persona you speak to
- Implied differentiation
- Call-to-action patterns

---

## Option 2: File Mode (For Bulk Content)

### Step 1: Collect Your Content
Use the template provided: `linkedin_content_template.txt`

Or create a plain text file with your posts separated by `---`:

```txt
Your first LinkedIn post text here
---
Your second LinkedIn post text here
---
Your article or whitepaper content here
```

### Step 2: Run Analysis
```bash
python content_analyzer.py --input your_posts.txt --output messaging_profile.md
```

### Step 3: Review Results
Check `messaging_profile.md` for full analysis

---

## What the Tool Analyzes

### 1. **THEMES** (What You Keep Coming Back To)
Identifies 3-5 recurring narratives across your content.

Examples: "speed", "risk reduction", "proof vs. promise", "flexibility", "compliance"

**Why it matters**: These are your authentic differentiators. Use them in positioning.

### 2. **TONE & VOICE** (How You Sound)
Extracts formality level, emotional tone, audience assumptions, confidence level.

**Why it matters**: Your pitch to prospects should match this tone. Authenticity closes deals.

### 3. **VALUE PROPOSITIONS** (What You Claim Matters)
Lists business outcomes, user outcomes, and institutional outcomes you emphasize.

**Why it matters**: These are what actually resonates with your buyers. Prioritize them.

### 4. **BUYER FRAMING** (Who You're Speaking To)
Identifies primary buyer persona, their implicit concerns, and how you address them.

**Why it matters**: Understand who decides and what they worry about (even if they don't say it).

### 5. **DIFFERENTIATION** (What Makes You Different)
Uncovers assumptions you challenge and capabilities you treat as obvious.

**Why it matters**: Your competitive moat isn't what you say, it's what you assume is obvious.

### 6. **CALL-TO-ACTION** (What You're Asking For)
Maps explicit and implicit CTAs throughout your content.

**Why it matters**: Understand what action you drive people toward (learning? evaluating? committing?).

---

## Example Output

Here's what a generated messaging profile looks like:

```markdown
# Your Messaging Profile

## 1. YOUR CORE THEMES

- **Speed / Acceleration** (appears 15+ times)
  Quote: "From 7 years to 90 days"
  Why it matters: Your differentiator is velocity, not features

- **Proof vs. Promise** (appears 8 times)
  Quote: "We show, not tell"
  Why it matters: You build credibility through demonstration

- **Flexibility / Customization** (appears 12 times)
  Quote: "Fail fast, iterate quickly"
  Why it matters: Your real moat is adaptability, not rigid features

## 2. YOUR TONE & VOICE

**Formality**: Executive + Technical (not academic, not conversational)
**Emotional Tone**: Confident, pragmatic, slightly urgent
**Audience**: Government/Enterprise CTOs and business leaders
**Confidence**: High (you state things as facts, not opinions)

Best quote: "This isn't theoretical. We've done it three times."

## 3. VALUE PROPOSITIONS YOU EMPHASIZE

1. **Speed to deployment** (Primary: $, Timeline)
   - CTO cares: 90 days vs. 7 years
   - User cares: Works on day 1

2. **Flexibility to customize** (Primary: Risk, Flexibility)
   - CTO cares: Can tailor without re-engineering
   - User cares: Adapts to their workflow

3. **Compliance included** (Secondary: Risk, Governance)
   - CISO cares: Audit trails, governance built-in
   - CTO cares: No custom compliance work

...
```

---

## Tips for Best Results

### Collect Sufficient Content
- **Minimum**: 3-5 LinkedIn posts (300-500 words each)
- **Ideal**: 8-10 posts + 1-2 articles + any speaking engagements
- **Why**: More data = more accurate pattern detection

### Include Different Content Types
- Posts (quick, punchy)
- Articles (longer, detailed)
- Comments on others' posts (your unfiltered perspective)
- Why: Tone varies by format; we need both

### Recent Content Preferred
- Last 3-6 months ideally
- Your messaging evolves; we want current
- If older content is particularly important, include it too

### Include "Failures" or Challenges
- Posts where you discuss problems, not just wins
- These reveal what you actually care about
- Don't just cherry-pick your best posts

---

## What to Do With Results

### For Ask-AI Positioning
- **Themes** → Core messaging pillars
- **Tone** → How to write case studies, emails, sales docs
- **Value Props** → What to emphasize for HR leaders vs. CTOs
- **Buyer Framing** → How to address CTO's concerns

### For Enterprise AI Foundry Positioning
- **Differentiation** → What makes it different from consulting firms, AWS, point solutions
- **Themes** → Speed, flexibility, fail-fast become part of narrative
- **Tone** → How to position it (pragmatic, proven, not hype)
- **CTA** → What action to ask from prospects (evaluate, pilot, discuss)

### For Closing Conversation with Prospect
- **Tone** → Mirror this in your pitch
- **Buyer Framing** → Address their implicit concerns
- **Value Props** → Lead with what resonates (speed, flexibility, proof)
- **Themes** → Reinforce these throughout conversation

---

## Running the Analysis

### Quick Command
```bash
# Interactive (easiest)
python content_analyzer.py --interactive

# From file
python content_analyzer.py --input posts.txt --output profile.md
```

### What Gets Generated
```
messaging_profile_generated.md (or messaging_profile.md)
├─ Themes (what you keep saying)
├─ Tone (how you sound)
├─ Value Propositions (what you claim matters)
├─ Buyer Framing (who you're talking to)
├─ Differentiation (what makes you different)
├─ CTA (what you ask for)
└─ Synthesis (what it all means)
```

---

## Next Steps After Analysis

1. **Review the generated profile** — Does it match how you see yourself?
2. **Adjust if needed** — If something doesn't feel right, add more content and re-run
3. **Use for GTM** — Feed this profile to prospect conversations, content creation, positioning
4. **Track what works** — As you close deals, note which themes/messages resonated most
5. **Refine** — Re-run analysis quarterly as your messaging evolves

---

## Troubleshooting

### "API key not found"
```bash
export ANTHROPIC_API_KEY=sk-your-key-here
```

### "No content provided"
Make sure you're pasting actual post text, not just links. Include full content.

### "Analysis seems off"
Add more content (more posts = better accuracy). Re-run.

### "Want to customize the analysis?"
Edit `content_analyzer.py` and modify the `prompts` dictionary to ask different questions.

---

## Cost
- ~$0.05-0.15 per full analysis (6 Claude API calls)
- Includes all analyses: themes, tone, value props, buyer, differentiation, CTA
- Rerun as often as you want for different content sets

---

## Ready?

### Step 1: Collect Your Content
Copy 5-10 recent LinkedIn posts into `linkedin_content_template.txt`

### Step 2: Run Analysis
```bash
python content_analyzer.py --interactive
```

### Step 3: Review Results
Open `messaging_profile_generated.md`

### Step 4: Share Results
Send profile to team + use for positioning Ask-AI + Enterprise AI Foundry

**Let's go.** 🚀
