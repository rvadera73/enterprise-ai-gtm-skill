# Claude Code Skills - Enterprise AI GTM Skill

## Available Skills

### `/enterprise-gtm` — Enterprise AI GTM Skill
A comprehensive, framework-driven go-to-market skill that works for ANY enterprise product.

---

## How to Use `/enterprise-gtm`

### What It Does
Automatically:
1. **Selects the right framework** (based on product type × stage)
2. **Runs a 6-week positioning workshop** (9 discovery exercises)
3. **Generates 23 strategic artifacts** (positioning, personas, messaging, brand, sales)
4. **Creates content strategy** (customized by buyer type)
5. **Builds lead generation plan** (customized by product stage)
6. **Develops sales framework** (customized by buyer psychology)

### Quick Start

**Step 1: Invoke the skill**
```
/enterprise-gtm
```

**Step 2: Provide product information**
```
Product: Ask-AI Service
Type: Enterprise AI Service
Stage: Growth
Target Buyer: Sr. IT Executive (CTO, VP Engineering)
Problem: Knowledge fragmentation across 5+ systems
Differentiator: Conversational cross-system search in 28 days
Proof Points: IACP (95% reduction, 15-day setup), CBP (20-40x faster)
```

**Step 3: Get framework recommendation**
```
Primary Framework: Geoffrey Moore Template
Secondary Framework: STP (Segmentation, Targeting, Positioning)
Why: Enterprise AI Service at growth stage requires multi-stakeholder positioning
Timeline: 6 weeks
Artifacts: 23 pieces (positioning, personas, messaging, content, sales)
```

**Step 4: Execute the plan**
Follow the skill's guidance to run positioning workshop, create content, launch lead gen, close sales.

---

## Frameworks Included

### 1. JTBD (Jobs to Be Done)
**When to use**: Understanding customer motivation  
**Product types**: All (especially B2B SaaS)  
**Example**: Risk Scoring — What job is the customer trying to do? (Prevent fraud, reduce false positives)

### 2. April Dunford Canvas
**When to use**: Competing on differentiation  
**Product types**: DevTools, Infrastructure  
**Example**: Linear vs. Jira — What can you do that others can't?

### 3. Geoffrey Moore Template
**When to use**: Multi-stakeholder enterprise buying  
**Product types**: Enterprise SaaS, Enterprise AI Services  
**Example**: Ask-AI — Different messages for CTO (execution risk), CFO (cost), Operations (outcome)

### 4. Value Proposition Canvas
**When to use**: Understanding customer pains/gains  
**Product types**: B2B SaaS, Pre-launch products  
**Example**: eCourt — What are court administrators' pains? (Case overload, manual processes)

### 5. Category Design / Blue Ocean
**When to use**: Defining or redefining a category  
**Product types**: Mature products, emerging categories  
**Example**: "Enterprise AI for Modernization" — Define the category, own the mindshare

### 6. Lean Canvas
**When to use**: Early-stage, problem validation  
**Product types**: Pre-launch products, MVPs  
**Example**: Risk Scoring MVP — Validate fraud detection value before full build

---

## Product Type × Stage Matrix

### Enterprise AI Service (Like Ask-AI, Risk Scoring)
| Stage | Framework | Timeline | Use When |
|-------|-----------|----------|----------|
| **Pre-launch (MVP)** | Lean Canvas + JTBD + Value Prop | 3-4 weeks | Validating problem + solution fit |
| **Growth** | Geoffrey Moore + STP | 4-6 weeks | Product-market fit, scaling |
| **Mature** | Category Design + Blue Ocean | 6-8 weeks | Market leader, defending position |

### Government SaaS (Like eCourt)
| Stage | Framework | Timeline | Use When |
|-------|-----------|----------|----------|
| **Pre-launch** | Lean Canvas + Gov Psychology | 3-4 weeks | Validating compliance fit |
| **Deployment** | Moore (emphasize compliance) + Gov STP | 4-6 weeks | Scaling to agencies |
| **Mature** | Category Design (gov AI) | 6-8 weeks | Category leadership |

### B2B SaaS (Like Salesforce, HubSpot)
| Stage | Framework | Timeline | Use When |
|-------|-----------|----------|----------|
| **Pre-launch** | Lean Canvas + Value Prop | 2-3 weeks | MVP validation |
| **Growth** | Geoffrey Moore + STP | 4-6 weeks | Multi-stakeholder selling |
| **Mature** | Category Design + Blue Ocean | 6-8 weeks | Market leadership |

---

## Real Examples

### Example 1: Ask-AI Service

```
Input:
- Product: Ask-AI Service
- Type: Enterprise AI Service
- Stage: Growth
- Target Buyer: Sr. IT Executive
- Problem: Knowledge fragmentation (2-4 hours/day wasted)
- Differentiator: Conversational cross-system search, 28-day deployment
- Proof: IACP (95% reduction, 15 days), CBP (20-40x faster), Enterprise (92% accuracy)

Framework Selection:
- Primary: Geoffrey Moore Template
- Secondary: STP (Segment different messages by buyer role)
- Timeline: 6 weeks to full positioning

Output Positioning:
- Statement: "Ask-AI gives knowledge workers instant answers across 5+ systems, eliminating 2-4 hours/day of search time"
- For CTO: "Integrate with existing systems, 30-day deployment, zero disruption"
- For CFO: "$150K+ annual savings, ROI visible in 30 days"
- For Operations: "Help desk cost down 30%, team freed up for higher-value work"

Content Strategy:
- LinkedIn: "Knowledge systems fail because they're fragmented"
- Blog: "The $625K hidden cost of knowledge search"
- Case Study: "IACP: 95% Deficiency Reduction in 15 Days"
- Lead Magnet: "30-Day Implementation Roadmap"

Lead Gen Funnel:
- Stage 1 (Awareness): LinkedIn thought leadership (10K+ impressions)
- Stage 2 (Consideration): Lead magnet download (50+ qualified prospects)
- Stage 3 (Evaluation): Direct outreach to Sr. IT Execs
- Stage 4 (Decision): Pilot proposals (2-3 per month)
- Stage 5 (Expansion): Expand to Enterprise AI Foundry

Sales Script:
- Opening: "Most modernization projects take 18+ months. I help CTOs prove it can be done in 90 days."
- Problem: "How many legacy systems are you managing? What's the risk if this goes wrong?"
- Solution: "We've proven this pattern 3 times: 15-day clarity, 30-day proof, 60-day scale."
- Close: "Let's prove it on your priority system. 30 days. If it works, you scale."
```

### Example 2: Risk Scoring Platform

```
Input:
- Product: Risk Scoring Platform
- Type: Enterprise AI Service
- Stage: MVP
- Target Buyer: Chief Risk Officer + Finance VP
- Problem: False positive reduction in fraud detection
- Differentiator: Centralized risk model management, 30-day deployment
- Proof: Pilot results showing 70% false positive reduction

Framework Selection:
- Primary: Lean Canvas + JTBD + Value Prop Canvas
- Why: MVP stage requires problem validation + solution proof (different from Ask-AI which is growth)
- Timeline: 3-4 weeks (shorter than growth stage)

Output Positioning:
- Statement: "Risk Scoring enables institutions to deploy AI-powered fraud detection in 30 days"
- For CRO: "False positive reduction 70%, detect fraud faster"
- For CFO: "Model deployment in weeks, not 6 months"
- For Compliance: "Continuous compliance, audit-ready"

Key Difference from Ask-AI:
- Ask-AI is Growth (full GTM system)
- Risk Scoring is MVP (focus on proof of concept, waitlist)
- Same framework concepts, different stage = different emphasis
```

### Example 3: eCourt

```
Input:
- Product: eCourt
- Type: Government SaaS
- Stage: Pre-launch
- Target Buyer: Government CIO + Court Administrator
- Problem: Manual case management, compliance-heavy
- Differentiator: Government-hardened, 508-compliant, secure
- Proof: Design validation with 3 courts

Framework Selection:
- Primary: Lean Canvas + Government Buying Psychology
- Why: Government has unique buying criteria (compliance > speed, security > innovation)
- Timeline: 3-4 weeks (government-specific validation)

Output Positioning:
- Statement: "eCourt is a modern, accessible case management system that reduces judge and clerk workload"
- For CIO: "Government-hardened, 508-compliant, security-first"
- For Administrator: "Judges and clerks spend 30% less time on admin"
- For Justice: "Cases move faster, better information access"

Key Difference from Ask-AI & Risk Scoring:
- Different product category (Government vs. Enterprise)
- Different buyer psychology (compliance-first vs. outcome-first)
- Different framework (gov buying + Lean Canvas)
```

---

## 5 Buyer Customization

### Same Positioning, Different Emphasis

**Ask-AI positioning for different buyers**:

#### CTO Emphasis
- **Problem**: "Your legacy systems create integration nightmares when you try to modernize"
- **Solution**: "Ask-AI integrates without replacement, proven 30-day deployment"
- **Proof**: "IACP integrated in 15 days, CBP in 3 weeks, zero system replacement"
- **Fear Address**: "We handle compliance and governance built-in"

#### CFO Emphasis
- **Problem**: "Your help desk costs $150K+ annually just answering 'where do I find X' questions"
- **Solution**: "Ask-AI reduces help desk load by 30%, enables self-service"
- **Proof**: "Fortune 500 companies see ROI in 30 days, savings visible month 1"
- **Fear Address**: "Fixed cost, fixed timeline, $100K for proof, scale from there"

#### Operations Leader Emphasis
- **Problem**: "Your help desk is overwhelmed with knowledge questions, burning out the team"
- **Solution**: "Ask-AI enables self-service, frees up your team for higher-value work"
- **Proof**: "92% adoption in pilots, team satisfaction up 40%"
- **Fear Address**: "Works like Google, no training needed"

**Same Ask-AI positioning. Different opening depending on who you're talking to.**

---

## Stage-Based Lead Gen Customization

### Pre-Launch Stage Lead Gen
**Goal**: Build awareness + founder credibility + waitlist

```
Weeks 1-2: Founder credibility
- Founder LinkedIn thought leadership
- Problem validation posts
- Early customer testimonials

Weeks 3-4: Community engagement
- Industry communities (Product Hunt, etc.)
- Early adopter programs
- Beta sign-ups

Metrics:
- Waitlist: 500+ people
- Beta signups: 50+ companies
- Founder engagement: 10K+ impressions/week
```

### Growth Stage Lead Gen
**Goal**: Qualified leads → pilots → customers

```
Week 1-3: Awareness (LinkedIn, blog)
- Thought leadership on problem
- Competitive positioning
- Customer-specific content

Week 3-4: Consideration (lead magnet + webinar)
- "Decision framework" lead magnet
- Webinar: "How to Evaluate X"
- Email nurture sequence

Week 5-6: Evaluation (direct outreach)
- Sales development outreach
- Personalized messaging
- Qualification calls

Week 7-8: Decision (pilot proposals)
- Pilot agreement process
- Success metrics definition
- Kickoff planning

Metrics:
- 10K+ impressions/month
- 50+ lead magnet downloads
- 10+ qualified calls
- 2-3 pilots signed/month
```

### Mature Stage Lead Gen
**Goal**: Account-based marketing + expansion

```
Channels:
- Analyst relations (Gartner, Forrester)
- Strategic partnerships
- Executive outreach
- Industry events
- Thought leadership at scale

Messaging:
- "Here's how the category is evolving"
- "We're the leader in X"
- "Strategic partnerships with Y, Z"

Metrics:
- Enterprise deals: $500K+
- Expansion revenue: 30%+ of new
- Analyst coverage
- Partnership ecosystem
```

---

## 23 Strategic Artifacts Model

After 6 weeks of positioning, you have:

### Positioning Layer (5 artifacts)
1. Positioning statement
2. Differentiation statement
3. Value proposition (overall)
4. Brand promise
5. Brand guidelines

### Persona Layer (6 artifacts)
6. Persona 1 (detailed profile)
7. Persona 2
8. Persona 3
9. Their pain points + goals
10. Their objections
11. Proof that matters to each

### Messaging Layer (7 artifacts)
12. Primary message (Tier 1)
13. Secondary messages (Tier 2)
14. Handling objections (Tier 3)
15. Segment-specific message A
16. Segment-specific message B
17. Segment-specific message C
18. Proof point hierarchy

### Strategy Layer (5 artifacts)
19. Competitive positioning
20. Unique selling proposition
21. Category definition
22. Market positioning
23. Sales strategy

---

## How Frameworks Work Together

```
FRAMEWORK SELECTION ENGINE
(Product Type × Stage → Framework)
        ↓
GENERIC 6-WEEK POSITIONING PROCESS
(Same for all products)
        ↓
BUYER CUSTOMIZATION
(Different messaging for CTO, CFO, Ops, etc.)
        ↓
CONTENT STRATEGY
(Thought leadership customized by buyer type)
        ↓
LEAD GENERATION PLAN
(5-stage funnel customized by product stage)
        ↓
SALES FRAMEWORK
(Conversation scripts customized by buyer psychology)
        ↓
23 STRATEGIC ARTIFACTS
(Complete GTM foundation)
```

---

## Common Use Cases

### Use Case 1: "Which framework should I use?"
**Input**: Product type + stage  
**Output**: Framework recommendation (5 minutes)  
**Command**: `/enterprise-gtm [product-info]`

### Use Case 2: "I need full GTM system"
**Input**: Product details  
**Output**: 6-week positioning roadmap + 23 artifacts (6 weeks, guided)  
**Command**: `/enterprise-gtm [detailed-product-info]`

### Use Case 3: "I have positioning, need content calendar"
**Input**: Positioning brief + buyer profiles  
**Output**: 3-month content calendar + topic ideas (1 week)  
**Command**: `/enterprise-gtm content [positioning-brief]`

### Use Case 4: "I'm launching a new product"
**Input**: New product description  
**Output**: Framework selection + 30-day launch plan (2 weeks)  
**Command**: `/enterprise-gtm launch [new-product]`

### Use Case 5: "I'm expanding to a new market"
**Input**: Existing positioning + new market  
**Output**: Market-specific positioning + lead gen (1-2 weeks)  
**Command**: `/enterprise-gtm expand [product] [new-market]`

---

## Getting Started

### Right Now (5 minutes)
```
/enterprise-gtm
```
Provide your product information and get framework recommendation.

### This Week (2 hours)
```
1. Get framework recommendation
2. Read GENERIC-POSITIONING-PROCESS.md
3. Start 9 discovery exercises
4. Schedule customer interviews
```

### This Month (Full GTM)
```
1. Complete 6-week positioning workshop
2. Create 3-month content calendar
3. Launch lead generation
4. Build sales conversation scripts
5. Close first 30-day proof
```

---

## Documentation

### Essential Reading
- **GENERIC-GTM-SKILL-DEFINITION.md** — What this skill is (start here)
- **SKILL-MANIFEST.md** — Comprehensive skill documentation
- **FRAMEWORK-SELECTION-MATRIX.md** — Framework decision engine

### Deep Dives
- **GENERIC-POSITIONING-PROCESS.md** — 6-week workshop guide
- **GENERIC-CONTENT-LEADGEN-SALES.md** — Content, lead gen, sales execution

### Real Examples
- Ask-AI (Enterprise AI Service, Growth)
- Risk Scoring (Enterprise AI Service, MVP)
- eCourt (Government SaaS, Pre-launch)

---

## Success Metrics

| Week | Goal |
|------|------|
| Week 1 | Framework selected, positioning workshop started |
| Week 2-6 | 9 discovery exercises completed, positioning brief done |
| Week 7-8 | Content calendar created, lead magnet designed |
| Week 9 | Lead generation launched |
| Week 10 | Sales scripts completed, team trained |
| Week 11-12 | First customer conversations booked |
| Week 13+ | First proof projects signed |

---

## Limitations

### What This Skill Does
✅ Recommends framework  
✅ Guides positioning process  
✅ Creates content outlines  
✅ Plans lead generation  
✅ Provides sales scripts  

### What You Do
❌ Conduct customer interviews (skill guides, you interview)  
❌ Write detailed content (skill provides outline, you write)  
❌ Execute lead generation (skill plans, you execute)  
❌ Close deals (skill provides script, you sell)  
❌ Measure results (skill shows metrics, you track)  

**This is a guidance skill. You do the execution.**

---

## Advanced Features

### Feature 1: Multi-Buyer Customization
Use same framework with different messaging for CTO, CFO, Operations, User

### Feature 2: Stage Migration
"We're moving from MVP to Growth. How does positioning evolve?"

### Feature 3: Competitive Repositioning
"New competitor launched. How do we reposition?"

### Feature 4: Geographic Expansion
"We're expanding to Asia. How do we adapt positioning?"

### Feature 5: Product Portfolio
Apply to Ask-AI, then Risk Scoring, then eCourt — same skill, different outputs

---

## Next Steps

1. **Run the skill**:  
   `/enterprise-gtm [your-product-info]`

2. **Get framework recommendation**:  
   See which framework fits your product type × stage

3. **Read the positioning guide**:  
   `/frameworks/GENERIC-POSITIONING-PROCESS.md`

4. **Execute 6-week workshop**:  
   Run 9 discovery exercises, apply framework, validate

5. **Create content + lead gen + sales**:  
   Use skill outputs to execute GTM plan

---

**Ready to get started? Run `/enterprise-gtm` with your product information.**

