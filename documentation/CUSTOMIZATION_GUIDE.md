# Customization Guide

**How to adapt the Enterprise AI Foundry materials for your own product.**

---

## Overview

The Enterprise AI Foundry example is a **complete, working system**. To adapt it for your product, you need to customize:

1. **Whitepaper** (change examples, problem statement)
2. **One-Pager** (change positioning, use cases)
3. **LinkedIn posts** (change problem, solution, examples)
4. **Execution guides** (update CTAs, timelines)

**What to keep:** Narrative structure, format, design. These are proven.

---

## Step 1: Whitepaper Customization

### What to Change

**Title & Intro (Line 30-50)**
```html
<!-- CHANGE THIS -->
<h1>Enterprise AI Foundry</h1>
<p>From Fragmentation to Scale: Building Repeatable AI Products Across Your Enterprise</p>

<!-- TO THIS (your product) -->
<h1>Risk Scoring Platform</h1>
<p>From Manual Rules to AI-Driven Fraud Detection at Scale</p>
```

**Problem Statement (Search for "Fragmentation Pattern")**
```markdown
CURRENT:
"Most large enterprises now have multiple AI systems addressing similar problems"

YOUR VERSION:
"Most organizations have multiple fraud detection rules, inconsistent across channels"
```

**Case Examples (Look for "EXAMPLE 1:", "EXAMPLE 2:", "EXAMPLE 3:")**
```markdown
CURRENT:
- Conversational Knowledge System
- Multi-Layer Fraud Detection
- Case Adjudication

YOUR VERSION (if Risk Scoring):
- Transaction Fraud Detection
- Claims Fraud Detection
- Account Takeover Detection
```

**Infrastructure Layers (Search for "Governance Layer")**
Keep the concept, change the context:

CURRENT (generic):
```
Governance Layer — Who can ask what? What gets logged? How do we audit?
```

YOUR VERSION (Risk Scoring):
```
Governance Layer — Who can request scores? Which data sources? Audit trail for compliance?
```

**Conclusion & CTA (End of document)**
```markdown
CURRENT:
"The organizations that solve this problem early will deploy 10 AI systems..."

YOUR VERSION:
"The organizations that move first to unified fraud detection will reduce fraud by..."
```

### What to Keep

- **Structure** (6 sections are proven)
- **Narrative arc** (problem → insight → solution → futures)
- **Design** (Tailwind CSS, color scheme)
- **Visuals** (if using Chart.js or SVGs, keep them)

### How to Edit

1. Open `whitepaper.html` in a text editor (not browser)
2. Find sections above
3. Replace content between tags
4. Keep tags and structure intact
5. Save
6. Test in browser (open file, check it renders)

**Estimated time:** 20-30 minutes

---

## Step 2: One-Pager Customization

### Three-Column Layout

```
LEFT COLUMN          | MIDDLE COLUMN    | RIGHT COLUMN
The Problem          | The Solution     | The Impact
```

### What to Change

**Left Column (The Problem)**
```html
<!-- CURRENT (search for "Fragmentation") -->
<p>Fragmentation</p>
<p>Each team builds its own Ask-AI system independently</p>

<!-- CHANGE TO (your problem) -->
<p>Manual Rule Explosion</p>
<p>Each channel has its own fraud rules (inconsistent, high false positives)</p>
```

**Middle Column (The Solution)**
```html
<!-- CURRENT (the 5 stages) -->
1. Idea & Validation
2. Prototype
3. MVP Development
4. Production
5. Scale

<!-- CHANGE TO (your 5-stage framework) -->
1. Define Fraud Patterns
2. Build Detection Model
3. Multi-channel Testing
4. Production Deployment
5. Continuous Improvement
```

**Right Column (The Impact)**
```html
<!-- CURRENT -->
Cost: Deploy 10 systems for cost of 2
Speed: 3-4 weeks per system

<!-- CHANGE TO (your metrics) -->
Cost: Reduce fraud team by 50%
Speed: Detect fraud in real-time
```

**Use Cases (find "Typical Use Cases")**
```markdown
CURRENT:
- Ask-AI
- Fraud Detection
- Case Management
- Document Intelligence

YOUR VERSION (if Risk Scoring):
- Transaction Fraud Detection
- Claims Fraud Detection
- Account Takeover Detection
- Synthetic Identity Detection
```

### Estimated time: 15 minutes

---

## Step 3: LinkedIn Posts Customization

### The Campaign Structure

All 14 posts follow this pattern:
- **Days 1-7:** Problem exposition + credibility
- **Days 8-14:** Solution introduction + action

### What to Change

**Day 1 (The Hook)**
```markdown
CURRENT:
"Most enterprises believe their AI fragmentation problem is a 'tool selection' issue."

YOUR VERSION:
"Most enterprises believe their fraud problem is a 'rule tuning' issue. They're wrong."
```

**Day 2 (The Evidence)**
```markdown
CURRENT:
"15 separate compliance approvals" → Cost of fragmentation
"15-20x the cost of a single system"

YOUR VERSION:
"Manual rules across 5 channels" → Cost of fragmentation
"5-10x the false positive rate"
```

**Day 3 (The Stories)**
Replace the three examples with your use cases:

CURRENT:
```
EXAMPLE 1: Conversational Knowledge System
EXAMPLE 2: Multi-Layer Fraud Detection
EXAMPLE 3: Case Adjudication
```

YOUR VERSION (Risk Scoring):
```
EXAMPLE 1: Transaction Fraud Detection
EXAMPLE 2: Claims Fraud Detection
EXAMPLE 3: Account Takeover Detection
```

**Days 8-14 (The Solution)**
Change framework names, layer names, and examples to match your solution.

### What to Keep

- **Narrative structure** (problem → evidence → stories → tension → solution)
- **Posting cadence** (1 per day, Monday-Sunday)
- **Engagement hooks** (questions at the end of each post)
- **Tone** (thoughtful, specific, expert-level)

### Quick Find & Replace

```bash
# If adapting in a text editor
Replace all "Ask-AI" with your product name
Replace all "fragmentation" with your problem
Replace all "system" with "domain" (or your term)
```

### Estimated time: 45 minutes (one hour for careful customization)

---

## Step 4: Execution Guides

### Quick-Start Checklist
- Update Monday 8 AM reminder
- Update CTAs in follow-up sections
- Update discovery call pitch

**Estimated time:** 10 minutes

### Marketing Guide
- Update product name in headers
- Update use cases in tables
- Update CTA messaging

**Estimated time:** 15 minutes

---

## Timeline: Full Customization

| Task | Time | Difficulty |
|------|------|------------|
| Copy template files | 5 min | Easy |
| Whitepaper | 25 min | Medium |
| One-Pager | 15 min | Easy |
| LinkedIn posts | 60 min | Medium |
| Execution guides | 25 min | Easy |
| **Total** | **2 hours** | **Moderate** |

---

## Before You Start Posting

1. **Read everything once** (whitepaper + posts) — Does the narrative make sense for your product?
2. **Test HTML files** — Open in browser, check rendering
3. **Read first week of posts** (Days 1-7) — Does the problem exposition feel authentic?
4. **Do final edits** — Fix anything that doesn't sound like you

---

## Common Adaptation Scenarios

### Scenario 1: Federal/Government Product
**Add emphasis on:** Compliance, audit, security, governance
**Posts should mention:** Regulatory requirements, audit trails, federal standards

Example:
```markdown
"In federal agencies, the governance problem is even more acute.
You need audit trails, role-based access, compliance automation.
Most systems skip this layer. That's why they fail at scale."
```

### Scenario 2: Enterprise (Non-Federal)
**Add emphasis on:** Cost optimization, operational efficiency, speed to market
**Posts should mention:** ROI, time to market, operational overhead

Example:
```markdown
"For enterprises, the real constraint is operational cost.
Each system requires a team. Multiply by 10 domains, and you've got 
half your engineering team just maintaining AI infrastructure."
```

### Scenario 3: Healthcare
**Add emphasis on:** HIPAA compliance, data residency, patient privacy
**Posts should mention:** Regulatory requirements, data governance, security

Example:
```markdown
"In healthcare, you can't just build one Ask-AI and roll it out.
You need data residency rules, audit logging, HIPAA compliance
built into every layer."
```

### Scenario 4: Financial Services
**Add emphasis on:** Risk management, fraud prevention, regulatory compliance
**Posts should mention:** Risk metrics, compliance requirements, audit

Example:
```markdown
"In financial services, the cost of getting AI wrong is measured in millions.
That's why governance, versioning, and evaluation aren't optional—
they're your insurance policy against regulatory problems."
```

---

## Style Guide for Customization

### Tone
- **Professional but conversational** (not stiff, not sales-y)
- **Specific over generic** (actual examples, not vague statements)
- **Systems thinking** (how it scales, not why feature is cool)
- **Problem-focused** (what's broken, not what we built)

### What Not to Do
❌ Replace problem with "we built a better product"
❌ Replace examples with feature lists
❌ Change narrative structure (keep 7-day + 7-day arc)
❌ Make it too salesy (week 1-2 are about expertise, not sales)

### What to Do
✅ Keep problem-first positioning
✅ Use real examples from your industry
✅ Maintain systems thinking
✅ Be authentic (use your voice)

---

## Validation Checklist

After customization:

- [ ] Whitepaper reads as coherent narrative
- [ ] HTML renders properly in browser
- [ ] One-Pager looks visually correct
- [ ] LinkedIn posts feel authentic
- [ ] Problem statement is specific (not generic)
- [ ] Examples are industry-relevant
- [ ] Solution framework maps to your product
- [ ] CTAs point to correct discovery process
- [ ] You'd be comfortable posting this content

---

## Example: Complete Customization (Risk Scoring)

If you were adapting for a Risk Scoring product:

**Problem statement:**
```
ORIGINAL: "Enterprises rebuild AI systems repeatedly"
ADAPTED: "Enterprises maintain separate fraud rules across channels, 
         leading to inconsistent detection and high false positives"
```

**Solution framework:**
```
ORIGINAL: Idea → Validation → Prototype → MVP → Production → Scale
ADAPTED: Pattern Discovery → Model Development → Multi-Channel Testing 
         → Unified Deployment → Continuous Optimization
```

**Key metrics:**
```
ORIGINAL: Cost savings, speed, operations
ADAPTED: Detection accuracy, false positive rate, fraud reduction %, 
         operational cost per review
```

**Use cases:**
```
ORIGINAL: Ask-AI, Fraud Detection, Case Management
ADAPTED: Transaction Fraud, Claims Fraud, Account Takeover, 
         Synthetic Identity Detection
```

This is what a full customization looks like.

---

## Tools for Customization

**Text Editor** (for HTML/Markdown):
- VS Code (recommended)
- Sublime Text
- Notepad++ (Windows)
- nano/vim (command line)

**Find & Replace:**
- Most editors have this (Ctrl+H or Cmd+H)
- Use to swap product names, terminology

**Browser Testing:**
- Open HTML files in Chrome, Firefox, Safari
- Check rendering on mobile (device or dev tools)

---

## Get Help

If you get stuck:

1. **Narrative doesn't make sense?** → Reread original (understand the logic first)
2. **HTML won't render?** → Check you didn't accidentally delete closing tags
3. **Not sure what to change?** → Keep the original next to your version, compare
4. **Tone doesn't feel right?** → Read it aloud, adjust for your voice

---

## Next Steps After Customization

1. **Proofread** once (full read-through)
2. **Set up tracking** (get a simple spreadsheet ready)
3. **Schedule Day 1 post** (Monday 8 AM)
4. **Plan engagement** (clear 30 min on Day 1 to respond to comments)
5. **Execute** (follow the daily checklist)

---

**Customization Guide**
**Read time:** 15 minutes
**Customization time:** 2 hours
**Ready to deploy:** Same day as customization