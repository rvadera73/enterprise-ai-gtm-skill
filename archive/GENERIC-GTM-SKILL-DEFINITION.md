# Enterprise AI GTM Skill - Generic Definition

**The Real Skill**: A framework-driven go-to-market system that works for ANY enterprise product, tailored by product type and stage.

---

## What This Skill IS (Not What We Had)

**NOT**: A campaign for Ask-AI and Enterprise AI Foundry

**ACTUALLY**: A reusable, configurable GTM framework that you can apply to:
- Ask-AI Service
- Enterprise AI Foundry
- Risk Scoring Model
- eCourt Document Management
- Fraud Detection System
- Any enterprise product you build

And can be used by:
- Your team (for all your products)
- Other organizations (licensing the framework)
- Sales teams in different verticals

---

## Core Architecture

### Layer 1: Framework Selection (Generic)

**Input**: Product type + Stage

**Process**: Automated framework recommendation

**Output**: Which positioning framework to use

```
Product Type × Stage Matrix:
├─ DevTools (API, SDK, Infrastructure)
│  ├─ Pre-launch → Lean Canvas + JTBD
│  ├─ Growth → April Dunford Canvas
│  └─ Mature → Category Design
│
├─ B2B Application SaaS (CRM, Finance, HR)
│  ├─ Pre-launch → Lean Canvas + Value Prop
│  ├─ Growth → Geoffrey Moore Template
│  └─ Mature → Blue Ocean
│
├─ Platform/Marketplace (Shopify, Twilio model)
│  ├─ Pre-launch → Platform Canvas + JTBD
│  ├─ Growth → Category Design + STP
│  └─ Mature → Network Effects
│
└─ Enterprise AI Service (Ask-AI, Risk Scoring)
   ├─ Pre-launch → Service Canvas + JTBD
   ├─ Growth → Geoffrey Moore + STP
   └─ Mature → Category Design
```

### Layer 2: Generic Positioning Process (Reusable)

**Input**: Product details + Framework type

**Process**: 6-week discovery + positioning workshop

**Output**: 23 strategic artifacts (positioning statement, personas, messaging, etc.)

Framework-independent process:
1. **Week 1-2**: Discovery workshop (9 exercises)
2. **Week 2-3**: Framework application (tailored by type)
3. **Week 3-4**: Validation (customer interviews, competitive analysis)
4. **Week 4-5**: Messaging hierarchy (for different buyers)
5. **Week 5-6**: Operationalization (brand guidelines, selling assets)

### Layer 3: Generic Content Strategy (Configurable)

**Input**: Positioning brief + Buyer profile + Stage

**Process**: Generate thought leadership for your target buyer

**Output**: LinkedIn posts, blog articles, case studies, etc.

Different for each buyer type:
- Sr. IT Executive (focus: execution risk, ROI, timeline)
- Individual User (focus: ease of use, time savings, job fit)
- Finance Buyer (focus: cost, ROI, business impact)
- Technical Buyer (focus: integration, architecture, scalability)

### Layer 4: Generic Lead Generation (By Product Stage)

**Input**: Target buyer + Product stage + Sales motion

**Process**: 5-stage funnel customized to buyer journey

**Output**: Lead generation playbook

Different for each stage:
- Pre-launch: Build waitlist + founder credibility
- Growth: Demand gen + product-led growth
- Mature: Account-based marketing + expansion

### Layer 5: Generic Sales Framework (By Buyer Type)

**Input**: Buyer profile + Product category + Buying decision type

**Process**: Sales conversation framework

**Output**: Scripts, objection handling, closing strategy

Different for each buyer:
- Technical buyer: Focus on architecture, integration, proof
- Business buyer: Focus on ROI, timeline, cost
- Executive buyer: Focus on strategic fit, risk, competitive advantage

---

## How This Differs From What We Had

### What We Built (Product-Specific)
```
Ask-AI Positioning
    ↓
Ask-AI Thought Leadership Posts
    ↓
Sr. IT Executive Lead Gen
    ↓
Enterprise AI Foundry Sales
```

**Problem**: Only works for Ask-AI + Enterprise AI Foundry + Sr. IT Execs

### What We Should Have (Generic)
```
Framework Selection Engine
    ↓ (Choose framework based on product type × stage)
Generic Positioning Process
    ↓ (Works for any product)
Generic Content Strategy
    ↓ (Customized by buyer type)
Generic Lead Generation
    ↓ (Customized by product stage)
Generic Sales Framework
    ↓ (Customized by buying decision type)
```

**Then Apply To**:
- Ask-AI (Enterprise Service, Growth stage, Sr. IT Exec buyer)
- Risk Scoring (Enterprise Service, Growth stage, Data Science + Finance buyer)
- eCourt (Government SaaS, Pre-launch stage, Government buyer)
- Future products...

---

## File Structure (Generic Skill)

```
/frameworks/
├── README.md                           (Framework overview)
├── FRAMEWORK-SELECTION-MATRIX.md       (Which framework for which product)
├── JTBD-FRAMEWORK-GUIDE.md            (How to apply JTBD)
├── DUNFORD-FRAMEWORK-GUIDE.md         (How to apply Dunford)
├── MOORE-FRAMEWORK-GUIDE.md           (How to apply Moore)
├── VALUE-PROP-FRAMEWORK-GUIDE.md      (How to apply Value Prop Canvas)
└── CATEGORY-DESIGN-FRAMEWORK-GUIDE.md (How to apply Category Design)

/positioning/
├── README.md
├── GENERIC-POSITIONING-PROCESS.md      (6-week workshop - works for any product)
├── DISCOVERY-EXERCISES.md              (9 exercises - generic)
├── ARTIFACTS-23-PIECE-MODEL.md         (What to produce)
└── VALIDATION-CHECKLIST.md             (How to validate)

/content-strategy/
├── README.md
├── THOUGHT-LEADERSHIP-BY-BUYER.md      (Different for each buyer type)
├── CONTENT-CALENDAR-TEMPLATE.md        (Generic calendar)
├── POST-STRUCTURE-BY-STAGE.md          (Different for pre-launch vs. growth)
└── EXAMPLES/
    ├── DEVTOOLS-EXAMPLES.md            (Example posts for DevTools)
    ├── SAAS-EXAMPLES.md                (Example posts for B2B SaaS)
    └── PLATFORM-EXAMPLES.md            (Example posts for Platforms)

/lead-generation/
├── README.md
├── FUNNEL-BY-PRODUCT-STAGE.md          (Different for each stage)
├── BUYER-JOURNEY-MAPPING.md            (Generic process)
└── EXAMPLES/
    ├── PRELAUNCH-LEAD-GEN.md           (For pre-launch products)
    ├── GROWTH-LEAD-GEN.md              (For growth stage)
    └── MATURE-LEAD-GEN.md              (For mature products)

/sales/
├── README.md
├── SALES-FRAMEWORK-BY-BUYER.md         (Different for each buyer type)
├── CONVERSATION-SCRIPTS-TEMPLATE.md    (Generic structure)
└── EXAMPLES/
    ├── TECHNICAL-BUYER-SCRIPT.md       (For engineers, architects)
    ├── BUSINESS-BUYER-SCRIPT.md        (For CFO, VP Ops)
    └── EXECUTIVE-BUYER-SCRIPT.md       (For CTO, VP Engineering)

/applications/
├── README.md
├── /ask-ai/
│   ├── POSITIONING-BRIEF.md            (Ask-AI application of framework)
│   ├── CONTENT-CALENDAR.md             (Ask-AI content)
│   ├── LEAD-GEN-PLAN.md                (Ask-AI lead gen)
│   └── SALES-SCRIPTS.md                (Ask-AI sales)
├── /risk-scoring/
│   └── (Same structure for Risk Scoring)
├── /ecourt/
│   └── (Same structure for eCourt)
└── /template-new-product/
    └── (Blank template to fill for new products)

/tools/
├── FRAMEWORK-SELECTOR.py               (Recommends framework based on inputs)
├── DISCOVERY-WORKSHOP-GUIDE.md         (How to run 6-week process)
├── ARTIFACTS-GENERATOR.md              (Generate the 23 pieces)
└── CONTENT-CUSTOMIZER.py               (Customize content by buyer)

/documentation/
├── GETTING-STARTED.md                  (How to use skill for any product)
├── APPLY-TO-NEW-PRODUCT.md             (Steps to apply to Risk Scoring, eCourt, etc.)
├── FRAMEWORK-SELECTION-GUIDE.md        (How to choose right framework)
├── POSITIONING-PROCESS-GUIDE.md        (How to run 6-week workshop)
├── CONTENT-STRATEGY-GUIDE.md           (How to create thought leadership)
└── SALES-FRAMEWORK-GUIDE.md            (How to sell any product)
```

---

## The Real Skill: Step-by-Step

### Step 1: Select Framework (Automated)
```
Input:
- Product type: "Enterprise AI Service"
- Stage: "Growth"
- Target buyer: "Sr. IT Executive"

Output:
→ Recommended framework: Geoffrey Moore Template + STP Framework
→ Process: 6-week positioning workshop
→ Artifacts to produce: 23 pieces
```

### Step 2: Run Positioning Process (Same for Any Product)
```
Week 1-2: Discovery Workshop
├─ Exercise 1: Future State Headlines
├─ Exercise 2: Problem Definition
├─ Exercise 3: Customer Persona
├─ Exercise 4: Competitive Positioning
├─ Exercise 5: Differentiation Statement
├─ Exercise 6: Value Proposition Mapping
├─ Exercise 7: Messaging Hierarchy
├─ Exercise 8: Brand Archetype
└─ Exercise 9: Brand Promise

Week 2-3: Framework Application (Tailored by type)
├─ For Ask-AI: Apply Geoffrey Moore template
├─ For Risk Scoring: Apply Geoffrey Moore template
├─ For eCourt: Apply Geoffrey Moore template

Week 3-4: Validation
├─ Customer interviews (5-10)
├─ Competitive analysis
├─ Market research

Week 4-5: Messaging
├─ Segment-specific messaging
├─ Buyer-specific value props
├─ Proof point prioritization

Week 5-6: Operationalization
├─ Brand guidelines
├─ Sales playbook
├─ Content calendar
```

### Step 3: Create Content Strategy (Customized by Buyer)
```
Input:
- Positioning brief (from Step 2)
- Target buyer: "Sr. IT Executive"
- Product stage: "Growth"

Output:
→ LinkedIn content strategy (for Sr. IT Execs)
→ Blog content strategy (for Sr. IT Execs)
→ Sales email sequences (for Sr. IT Execs)
→ Webinar outlines (for Sr. IT Execs)

Different if buyer was "Technical User" or "Finance Buyer"
```

### Step 4: Build Lead Generation (Customized by Stage)
```
Input:
- Product stage: "Growth"
- Target buyer: "Sr. IT Executive"
- Target market: "Federal + Commercial"

Output:
→ 5-stage funnel (for growth stage)
→ Awareness tactics (LinkedIn, blog, etc.)
→ Consideration tactics (lead magnet, webinar, etc.)
→ Decision tactics (direct outreach, sales calls, etc.)
```

### Step 5: Build Sales Framework (Customized by Buyer)
```
Input:
- Target buyer: "Sr. IT Executive" (CTO, VP Engineering, Chief Architect)
- Buying decision: "Modernization + AI enablement"
- Product: Ask-AI Service

Output:
→ Sales conversation framework
→ Objection handling (by buyer type)
→ Closing strategy
→ Proof methodology (30-day pilot)
```

---

## Apply To Any Product

### Ask-AI Application
```
Product Type: Enterprise AI Service
Stage: Growth
Target Buyer: Sr. IT Executive
Target Market: Federal + Commercial

→ Framework: Geoffrey Moore Template + STP
→ Process: 6-week positioning (same as any product)
→ Content: Thought leadership for Sr. IT Execs
→ Lead Gen: Growth stage funnel
→ Sales: Sr. IT Exec buying psychology
```

### Risk Scoring Application
```
Product Type: Enterprise AI Service (same as Ask-AI)
Stage: MVP (earlier stage)
Target Buyer: Data Science Lead + Finance VP
Target Market: Commercial (fraud, credit, insurance)

→ Framework: Geoffrey Moore Template + JTBD
→ Process: 6-week positioning (same process, different inputs)
→ Content: Thought leadership for Data Science + Finance
→ Lead Gen: MVP stage funnel (different from growth)
→ Sales: Data Science buyer psychology + Finance buyer psychology
```

### eCourt Application
```
Product Type: Government SaaS
Stage: Pre-launch
Target Buyer: Government CIO + Judiciary
Target Market: Federal + State Courts

→ Framework: Lean Canvas + JTBD + Value Prop Canvas
→ Process: 6-week positioning (same process, different inputs)
→ Content: Thought leadership for Government buyers
→ Lead Gen: Pre-launch stage funnel
→ Sales: Government buyer psychology + risk aversion patterns
```

---

## Why This Is The Real Skill

### 1. Generic (Works for Any Product)
- Same positioning process works for Ask-AI, Risk Scoring, eCourt, future products
- Same content strategy works for any buyer type
- Same sales framework works for any buying decision

### 2. Framework-Based (Proven Methodologies)
- Built on JTBD, Dunford, Moore, Value Prop Canvas, etc.
- Not theoretical templates, but established frameworks

### 3. Reusable (Across Products)
- Apply to Ask-AI this quarter
- Apply to Risk Scoring next quarter
- Apply to eCourt next quarter
- Apply to future products automatically

### 4. Scalable (Can Be Offered as Service)
- Could be productized and sold to other organizations
- Could be licensed to consulting firms
- Could be taught to your sales team for any product

### 5. Configurable (By Product Type + Stage + Buyer)
- Framework selection is automatic (not manual guessing)
- Content is customized to buyer type
- Sales scripts are customized to buying decision

---

## What We Need To Build

### Phase 1: Generic Framework Guides
- [ ] FRAMEWORK-SELECTION-MATRIX.md (decision engine)
- [ ] JTBD-FRAMEWORK-GUIDE.md (how to apply JTBD)
- [ ] DUNFORD-FRAMEWORK-GUIDE.md (how to apply Dunford)
- [ ] MOORE-FRAMEWORK-GUIDE.md (how to apply Moore)
- [ ] VALUE-PROP-FRAMEWORK-GUIDE.md (how to apply Value Prop Canvas)
- [ ] CATEGORY-DESIGN-FRAMEWORK-GUIDE.md (how to apply Category Design)

### Phase 2: Generic Positioning Process
- [ ] GENERIC-POSITIONING-PROCESS.md (6-week workshop template)
- [ ] DISCOVERY-EXERCISES.md (9 exercises - works for any product)
- [ ] ARTIFACTS-23-PIECE-MODEL.md (what to produce)

### Phase 3: Generic Content Strategy
- [ ] THOUGHT-LEADERSHIP-BY-BUYER.md (different for each buyer type)
- [ ] CONTENT-CALENDAR-TEMPLATE.md (how to plan content)
- [ ] POST-STRUCTURE-BY-STAGE.md (different for each stage)

### Phase 4: Generic Lead Generation
- [ ] FUNNEL-BY-PRODUCT-STAGE.md (different for each stage)
- [ ] BUYER-JOURNEY-MAPPING.md (process for any buyer)

### Phase 5: Generic Sales Framework
- [ ] SALES-FRAMEWORK-BY-BUYER.md (different for each buyer type)
- [ ] CONVERSATION-SCRIPTS-TEMPLATE.md (structure for any script)

### Phase 6: Applications (Examples)
- [ ] Ask-AI application (positioning brief, content, lead gen, sales)
- [ ] Risk Scoring application
- [ ] eCourt application
- [ ] Template for new products

---

## Summary

**The Real Skill**: A reusable GTM framework that works for ANY enterprise product

**Core Idea**: Framework selection (based on product type × stage) + generic process (same for all) + customization (by buyer type and stage)

**Reusability**: Apply to Ask-AI, Risk Scoring, eCourt, future products, or other organizations

**Intellectual Property**: Defensible, valuable methodology that scales

**Current State**: We built a campaign. We need to build the skill.

---

**This is the right approach. Ready to build it?**
