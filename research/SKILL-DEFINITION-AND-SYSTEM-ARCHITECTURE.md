# GTM Marketing Skill: Definition, Frameworks, Tools, and Inputs
**Complete System Architecture**

---

## What is the Skill?

**Name**: GTM Marketing Skill (or Enterprise AI Foundry GTM Skill)

**What it does**: Takes a product concept and automatically generates:
- Strategic positioning aligned with industry frameworks
- 30+ professional marketing artifacts (posts, videos, emails, case studies, etc.)
- All artifacts branded, positioned, and segment-specific
- Ready to publish across channels (LinkedIn, email, blog, YouTube, sales)

**How it's different**:
- ❌ Traditional: Hire freelancer → guess at positioning → inconsistent assets
- ✅ GTM Skill: Define positioning using framework → automation generates 30+ aligned assets

**Who uses it**: Product managers, CTOs, founders launching products

**Time to result**: 6 weeks (positioning framework) + 25 min per campaign (automation)

---

## The Core Frameworks (What This Skill Is Built On)

The GTM Marketing Skill is built on **5 proven positioning frameworks** from companies like Stripe, Adobe, Salesforce:

### Framework 1: Jobs to Be Done (JTBD)
**What it does**: Identifies the actual job customers hire your product to do  
**When to use**: B2B SaaS, DevTools, any product-market fit stage  
**Example**: 
- Job: "Reduce issue triage time from 5+ hours to 30 minutes"
- Solution: Linear issue tracker

### Framework 2: April Dunford's Positioning Canvas
**What it does**: Maps competitive alternatives → unique features → benefits for target segment  
**When to use**: DevTools, high-growth B2B SaaS  
**Example**:
- Alternatives: Jira (bloated), GitHub Issues (limited)
- Unique: Speed + features + developer focus
- Benefit: Ship faster, team loves the tool

### Framework 3: Geoffrey Moore's Positioning Template
**What it does**: Maps buying persona journey → competitive differentiation → proof hierarchy  
**When to use**: Enterprise SaaS, multi-stakeholder sales cycles  
**Example**: "FOR Finance VPs, WHO are stuck with SAP's expensive implementation, Salesforce is the cloud CRM THAT cuts implementation from 24 months to 2 months"

### Framework 4: Value Proposition Canvas
**What it does**: Visual mapping of customer pains/gains vs. your pain relievers/gain creators  
**When to use**: MVP/Beta stage, discovery phase  
**Example**: Customer pain = manual invoicing; Your gain creator = automated AP workflow

### Framework 5: STP Framework (Segmentation, Targeting, Positioning)
**What it does**: Divides market into segments → selects target → positions for that segment  
**When to use**: Multi-segment strategy, scaling phase  
**Example**: Different messaging for CFO vs. AP clerk, even though they use same product

---

## Which Framework to Use?

**Decision Matrix** (The Skill automatically recommends based on these inputs):

| Product Type | Primary Framework | Secondary Framework | Example |
|---|---|---|---|
| **DevTools/Infrastructure** | April Dunford Canvas | JTBD | Stripe, Vercel, Linear |
| **B2B Application SaaS** | Geoffrey Moore Template | STP | Salesforce, HubSpot, Notion |
| **Marketplace/Platform** | JTBD | Category Design | Shopify, Twilio, Zapier |
| **Early-stage MVP** | Lean Canvas | JTBD | Pre-product validation |
| **High-growth SaaS** | STP + Perceptual Mapping | April Dunford | Series A-C companies |

---

## The Tools in the Skill

### Layer 1: Positioning & Strategy Tools

| Tool | What it does | Input | Output |
|---|---|---|---|
| **Discovery Workshop** | 9-exercise interactive session | Team + customer knowledge | Job definitions, personas, pain map |
| **Value Prop Canvas** | Visual customer-centric mapping | Customer interview data | Problem/solution clarity |
| **Perceptual Mapping** | 2D competitive positioning | Competitor analysis | Visual positioning clarity |
| **5-Second Clarity Test** | Validates messaging clarity | Positioning statement | % of customers who understand in <5 sec |
| **Brand Archetype Selector** | Assigns brand personality | Brand preferences | 2 primary archetypes (The Hero, The Sage, etc.) |

### Layer 2: Marketing Automation Tools

| Tool | What it does | Framework Input | Output |
|---|---|---|---|
| **LinkedIn Post Generator** | Creates positioning-aligned posts | Positioning brief + topic | 400-word post in brand voice |
| **Email Newsletter Generator** | Educational content | Value prop + audience | 600-word email, subtle CTA |
| **Blog Post Generator** | SEO-optimized content | Positioning + keywords | 2000+ word blog post |
| **Video Script Generator** | 30-sec and 60-sec scripts | Positioning statement | Professional voiceover script |
| **Case Study Generator** | Customer proof with metrics | Customer data + positioning | ROI-focused case study |
| **Email Sequence Generator** | 4-email nurture | Positioning + segment | Welcome → Educational → Proof → CTA |
| **Social Media Generator** | Multi-platform content | Positioning + topic | Instagram carousel, TikTok script, Reddit post |
| **Infographic Generator** | Visual data communication | Metrics + positioning | Timeline, comparison chart |
| **Image Generator** | Branded visuals | Visual brief + brand guidelines | 1200×628px LinkedIn image |
| **Voiceover Generator** | Professional narration | Script text | MP3 with multiple voice options |

### Layer 3: Technical Infrastructure

| Component | Technology | Purpose |
|---|---|---|
| **AI Engine** | Claude API (GPT-4 alternative) | Generate marketing copy |
| **Image Generation** | Google Gemini API or FAL.ai | Create branded visuals |
| **Voiceover** | edge-tts (free) or ElevenLabs | Professional narration |
| **Video Rendering** | Remotion (React → MP4) | Programmatic video creation |
| **Social Publishing** | Postiz (20+ networks) or Buffer | Publish to LinkedIn, Twitter, YouTube, Instagram |
| **Email Delivery** | Brevo API (300/day free) | Send email sequences |
| **Analytics** | Umami or Google Analytics | Measure performance |
| **Content Management** | Astro + GitHub Pages | Host blog, knowledge base |

---

## What Inputs Are Required?

### Input 1: Product Information
```
- Product name: Ask-AI
- What it does: Conversational knowledge platform
- Target customer: Enterprise knowledge workers at 500+ person companies
- Stage: Production-ready
- Key metrics: 92% accuracy, 300+ users
```

### Input 2: Product Type Classification
```
Select ONE:
[ ] DevTools/Infrastructure (Stripe, Vercel, Linear model)
[ ] B2B Application SaaS (Salesforce, HubSpot model)
[x] Marketplace/Platform (Shopify, Twilio model)
[ ] Early-stage MVP (pre-product validation)
[ ] High-growth (Series A-C)
```

### Input 3: Framework Recommendation
```
Based on product type, Skill recommends:
Primary framework: Geoffrey Moore Template
Secondary: STP (Segmentation)
```

### Input 4: Discovery Inputs (From Workshop)
```
Job Definition: "Find answers across company knowledge in 30 seconds"
Customer Segment: "Enterprise HR/Operations leaders at Fortune 500"
Pain Points: 
  - Current: Scattered knowledge across 5+ systems
  - Time cost: 2-4 hours/day searching
  - Money cost: $50K+ annually in lost productivity
Alternatives: Google Enterprise Search, Slack Search, SharePoint
Differentiation: Conversational + cross-system search
```

### Input 5: Brand Information
```
Brand Voice: Professional, knowledgeable, solution-focused
Brand Archetype: The Sage (clarity) + The Mentor (guidance)
Colors: Navy #013060, Teal #4AC4D3, Orange #E6800C
Brand Promise: "Find answers instantly. Everywhere."
```

### Input 6: Topic for Content Generation
```
Topic: "How Enterprise AI Foundry Reduced Knowledge Search Time by 80%"
Audience Segment: HR Leaders at mid-market companies
Proof Points: 92% accuracy, 300+ users, 28-day production timeline
```

---

## How the Skill Works (End-to-End Flow)

```
STEP 1: GATHER INPUTS (1-2 hours)
├─ Product information: what is it, who uses it, current stage
├─ Product type: DevTools, AppSaaS, Marketplace, etc.
├─ Framework recommendation: Based on product type
├─ Brand information: Voice, archetype, colors, promise
└─ Topic: What to create content about

                    ↓

STEP 2: POSITIONING FRAMEWORK (6 weeks)
├─ Run discovery workshop (9 exercises)
├─ Apply selected framework (April Dunford, Geoffrey Moore, JTBD, etc.)
├─ Validate with customer interviews (5-10 conversations)
├─ Create positioning statement (one sentence, crystal clear)
└─ Output: Positioning Brief (complete strategic foundation)

                    ↓

STEP 3: MARKETING AUTOMATION (25 minutes per topic)
├─ Input: Positioning Brief + Topic
├─ Trigger: Content generation across 15+ artifact types
├─ Process:
│  ├─ LinkedIn Post Generator → 400-word positioned post
│  ├─ Email Newsletter Generator → 600-word educational content
│  ├─ Blog Post Generator → 2000+ word SEO content
│  ├─ Video Script Generator → 30-sec and 60-sec scripts
│  ├─ Case Study Generator → ROI-focused customer proof
│  ├─ Email Sequence Generator → 4-email nurture campaign
│  ├─ Social Media Generator → Instagram, TikTok, Reddit variants
│  ├─ Infographic Generator → Visual data storytelling
│  ├─ Image Generator → Branded visuals (1200×628px)
│  ├─ Voiceover Generator → MP3 narration
│  └─ [10+ more artifact generators running in parallel]
└─ Output: 30+ professional marketing assets

                    ↓

STEP 4: PUBLISHING (Integrated)
├─ LinkedIn: Post with image, scheduled
├─ Email: Newsletter to subscriber list, nurture sequence queued
├─ Blog: Published to website, SEO indexed
├─ YouTube: Video uploaded with description
├─ Sales: One-pagers added to sales collateral
└─ Social: Posts scheduled across channels

                    ↓

STEP 5: MEASUREMENT (Ongoing)
├─ Analytics: Views, engagement, conversions tracked
├─ Feedback: Customer comments analyzed
├─ Iteration: Monthly positioning review
└─ Improvement: Adjust messaging based on performance
```

---

## How It's Tailored

### Tailoring Dimension 1: By Product Type

**DevTools/Infrastructure SaaS**
- Framework: April Dunford Canvas
- Focus: Competitive differentiation (what you can do that others can't)
- Messaging: Technical, speed-focused
- Audience: Tech leads, engineers
- Example: Linear (faster than Jira, for developers)

**B2B Application SaaS**
- Framework: Geoffrey Moore Template
- Focus: Buying journey + ROI
- Messaging: Business outcome, cost savings, implementation speed
- Audience: C-suite, operations teams, buyers
- Example: Salesforce (faster implementation than SAP)

**Marketplace/Platform**
- Framework: JTBD + Category Design
- Focus: Dual customer jobs (sellers + buyers)
- Messaging: Opportunity (for sellers) + Discovery (for buyers)
- Audience: Both sides of the market
- Example: Shopify (sellers: start business easily; buyers: discover products)

### Tailoring Dimension 2: By Stage

**Pre-launch (MVP)**
- Framework: Lean Canvas + JTBD
- Focus: Problem validation + founder credibility
- Messaging: "We're solving X. Want to be an early user?"
- Artifacts: 6 foundational pieces
- Timeline: 2-3 weeks

**Growth (Product-Market Fit)**
- Framework: April Dunford or Geoffrey Moore
- Focus: Competitive positioning + ROI quantification
- Messaging: Differentiation + business value
- Artifacts: 23 complete pieces
- Timeline: 4-6 weeks

**Mature (Market Leadership)**
- Framework: Category Design + Blue Ocean
- Focus: Own the category, shift perception
- Messaging: Thought leadership, industry vision
- Artifacts: 30+ pieces + research reports
- Timeline: 6-8 weeks

### Tailoring Dimension 3: By Customer Segment

Even within one product, messaging is tailored by buyer role:

**Ask-AI Example**:
```
Same product, different segments, different messaging:

FOR HR Leaders:
"Reduce onboarding time by 50%. New employees find answers independently."

FOR CIOs:
"Reduce help desk tickets by 30%. Fewer calls to IT."

FOR Individual Employee:
"Find answers in 30 seconds instead of 30 minutes."
```

---

## Input Requirements Checklist

Before the Skill can work, you need:

### Tier 1: Non-Negotiable (Must have)
- [ ] Product name
- [ ] What it does (1-2 sentences)
- [ ] Who uses it (customer role/company size)
- [ ] Product type (DevTools, AppSaaS, Marketplace, etc.)
- [ ] Current stage (MVP, growth, mature)

### Tier 2: Highly Valuable (Should have)
- [ ] Primary customer pain point (what problem it solves)
- [ ] Key metrics or proof points (accuracy %, time savings, cost reduction)
- [ ] Competitors or alternatives customers consider
- [ ] Brand voice preference (formal? playful? technical?)
- [ ] 2-3 customer segments (different buyer personas)

### Tier 3: Nice to Have (Optional, improves quality)
- [ ] Brand colors and visual guidelines
- [ ] Company values or mission statement
- [ ] Founder background (credibility)
- [ ] Customer success stories (quantified outcomes)
- [ ] Market size or opportunity

---

## Example: Complete Input for Ask-AI

```
PRODUCT INFORMATION:
- Name: Ask-AI Service
- What: Conversational knowledge platform for enterprises
- Users: Enterprise HR, Operations, Finance leaders at 500+ person companies
- Stage: Production-ready
- Type: B2B Application SaaS

FRAMEWORK SELECTION:
→ Skill recommends: Geoffrey Moore Template (enterprise multi-stakeholder)

DISCOVERY INPUTS:
- Job: "Find organizational answers in 30 seconds instead of 30 minutes"
- Pain: "Knowledge scattered across SharePoint, Confluence, email, case systems"
- Cost: "$50K+ annually per company in lost productivity searching"
- Alternatives: Google Enterprise, Slack Search, SharePoint native, do-nothing
- Differentiation: Conversational + cross-system + no setup required
- Proof: 92% accuracy, 300+ users in pilot, 28-day production timeline

BRAND:
- Voice: Professional, knowledgeable, solution-focused
- Archetype: The Sage (clarity) + The Mentor (guides success)
- Promise: "One conversational interface to your entire organization"

CONTENT TOPIC:
- Title: "How Enterprise AI Foundry Reduced Knowledge Search by 80%"
- Segment: HR Leaders at Fortune 500 companies
- Proof to highlight: 92% accuracy, 300+ active users, production-ready
```

**Output from Skill**: 30+ artifacts in 25 minutes, all:
- Using Geoffrey Moore positioning
- Targeted at HR Leaders
- Emphasizing 92% accuracy + time savings
- Ready to publish across LinkedIn, email, blog, YouTube

---

## The Relatable Comparison

Think of it like **Shipley methodology for proposals** (which you know):

| Shipley Proposal Model | GTM Marketing Skill |
|---|---|
| **Input**: RFQ/RFP requirements | **Input**: Product info + framework type |
| **Process**: Compliance matrix → Themes → Win strategy | **Process**: Discovery → Positioning framework → Messaging strategy |
| **Framework**: 7 Pillars (compliance, responsiveness, etc.) | **Framework**: 5 positioning frameworks (JTBD, Dunford, Moore, etc.) |
| **Output**: Proposal document | **Output**: 30+ marketing artifacts |
| **Artifact**: Win themes, compliance matrix, one-pagers | **Artifact**: Positioning statement, value props, brand guidelines, content |
| **Audit**: Does it follow the framework? | **Audit**: Is every asset positioned correctly? |

**Both are**: Systematic, repeatable, framework-driven, auditable.

---

## Summary: The Skill in One Picture

```
INPUT
(Product + Framework Selection)
         ↓
   [POSITIONING]
   (6-week framework process)
         ↓
   [BRIEF]
   (Strategic foundation:
    job, segment, differentiation,
    proof points, brand)
         ↓
   [AUTOMATION]
   (25 minutes)
         ↓
   [30+ ASSETS]
   (Posts, videos, emails, blogs,
    case studies, all positioned)
         ↓
   [PUBLISH]
   (LinkedIn, email, blog, YouTube)
         ↓
   [MEASURE]
   (Monthly iteration)
```

---

## Next: Apply to Your Products

For each product you want to market:

1. **Gather Tier 1 inputs** (5 items, 30 minutes)
2. **Get framework recommendation** (automated based on product type)
3. **Run positioning framework** (6 weeks, team workshop)
4. **Feed to automation** (30 min per topic)
5. **Publish and measure** (ongoing)

This is the skill. This is how it works. This is what frameworks it uses.

Ready to apply it to Ask-AI, Risk Scoring, or eCourt?

