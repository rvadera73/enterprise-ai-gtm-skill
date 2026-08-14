# Enterprise AI GTM Skill

**Purpose:** Framework-driven, go-to-market strategy and positioning for ANY enterprise product.

---

## Overview

This skill delivers a complete GTM strategy in minutes:
- **Automated framework selection** based on product type × stage
- **6-week positioning workshop** with 9 discovery exercises
- **23 strategic artifacts** (positioning, personas, messaging, strategy)
- **Buyer-type customization** (CTO, CFO, Business Leader, User)
- **Stage-based content** (Pre-launch, Growth, Mature)
- **Sales conversation scripts** with objection handling

---

## Quick Start

### Invoke the Skill

```bash
/enterprise-gtm [product-name], [product-type], [product-stage], [target-buyer]
```

### Examples

- `/enterprise-gtm Ask-AI Service, Enterprise AI Service, Growth, Sr. IT Executive`
- `/enterprise-gtm Risk Scoring Platform, Enterprise AI Service, MVP, Chief Risk Officer`
- `/enterprise-gtm eCourt, Government SaaS, Pre-launch, Government CIO`

---

## Input Parameters

### Required
| Parameter | Type | Example |
|-----------|------|---------|
| **product_name** | string | Ask-AI Service, Risk Scoring Platform |
| **product_type** | enum | Enterprise AI Service, Government SaaS, B2B SaaS |
| **product_stage** | enum | Pre-launch, Growth, Mature |
| **target_buyer** | string | Sr. IT Executive, Chief Risk Officer, Government CIO |

### Optional
- `problem_statement` — What problem does your product solve?
- `key_differentiator` — What makes your product different?
- `proof_points` — Existing customers, metrics, deployments
- `target_market` — Geographic or vertical focus
- `company_size` — Enterprise, Mid-market, SMB
- `customer_industry` — Finance, Healthcare, Government, etc.

---

## Output / Deliverables

The skill generates:

1. **Framework Selection** - Primary + secondary framework with rationale
2. **Positioning Brief** - 1-page positioning statement + differentiation
3. **Content Strategy** - 3-month calendar + topic ideas + lead magnet
4. **Lead Generation Plan** - 5-stage funnel + messaging + tactics + metrics
5. **Sales Framework** - Conversation scripts by buyer type + objection handling
6. **GTM Plan Summary** - 6-week positioning roadmap + 90-day execution plan
7. **Artifacts Checklist** - 23 strategic artifacts model

---

## Frameworks Included

| Framework | Best For |
|-----------|----------|
| **JTBD** (Jobs to Be Done) | Understanding customer motivation |
| **April Dunford Canvas** | DevTools and infrastructure at growth |
| **Geoffrey Moore Template** | Enterprise SaaS and AI services |
| **Value Proposition Canvas** | B2B SaaS and pre-launch products |
| **Category Design / Blue Ocean** | Mature products and new categories |
| **Lean Canvas** | Pre-launch and early-stage products |

---

## Five Workflow Options

### 1. Quick Framework Selection (5 minutes)
Get framework recommendation + rationale based on your product type and stage.

```
/enterprise-gtm [product], [type], [stage], [buyer] --framework-only
```

### 2. Full 6-Week Positioning Workshop
Run all 9 discovery exercises → apply framework → generate 23 artifacts.

```
/enterprise-gtm [product], [type], [stage], [buyer] --full-positioning
```

### 3. Content Strategy Only (1-2 weeks)
Assume existing positioning → build 3-month content calendar + lead magnet.

```
/enterprise-gtm [product], [type], [stage], [buyer] --content-only
```

### 4. Lead Generation Plan (1-2 weeks)
Map 5-stage funnel → messaging + tactics + 30-day launch plan.

```
/enterprise-gtm [product], [type], [stage], [buyer] --leadgen-only
```

### 5. Sales Framework Only (1 week)
Build sales scripts by buyer psychology + objection handling guide.

```
/enterprise-gtm [product], [type], [stage], [buyer] --sales-only
```

---

## Real Examples Included

### Example 1: Ask-AI Service
- **Product Type:** Enterprise AI Service
- **Stage:** Growth
- **Framework:** Geoffrey Moore + Segment-Target-Position
- **Description:** Conversational knowledge platform for enterprises

### Example 2: Risk Scoring Platform
- **Product Type:** Enterprise AI Service
- **Stage:** MVP
- **Framework:** Lean Canvas + JTBD + Value Proposition Canvas
- **Description:** AI-powered fraud detection and risk scoring

### Example 3: eCourt
- **Product Type:** Government SaaS
- **Stage:** Pre-launch
- **Framework:** Lean Canvas + Government Buyer Psychology
- **Description:** Modern, accessible case management for courts

---

## Key Features

✓ Automated framework selection (15 configurations: 5 product types × 3 stages)  
✓ 6-week positioning workshop (same process for all products)  
✓ 23 strategic artifacts model (positioning, personas, messaging, strategy)  
✓ Buyer-type customization (CTO, CFO, Business Leader, User)  
✓ Stage-based lead generation (Pre-launch, Growth, Mature)  
✓ Buyer psychology sales scripts (Technical, Financial, Business, Executive)  
✓ Content strategy by buyer type (not by product)  
✓ Real product examples with complete frameworks  
✓ Framework selection rationale (why this framework for you)  
✓ Integration with proven methodologies (Moore, Dunford, JTBD, etc.)

---

## Success Metrics

| Phase | Success Metric | Measurement |
|-------|----------------|-------------|
| **Framework Selection** | Framework selected correctly | Customer validates framework match |
| **Positioning** | Positioning clarity | Buyer understands in < 30 seconds |
| **Content** | Content execution | Marketing team executes immediately |
| **Lead Gen** | Lead volume accuracy | Expected leads match real results |
| **Sales** | Conversation effectiveness | Sales team wins with scripts |

---

## Product Types Supported

- DevTools/Infrastructure
- B2B Application SaaS
- Platform/Marketplace
- Enterprise AI Service
- Government SaaS

---

## When to Use This Skill

✓ Launching a new product and need positioning framework  
✓ Entering a new market and need customized GTM  
✓ Building content strategy and lead generation plan  
✓ Creating sales conversation scripts for buyer types  
✓ Validating positioning with customer interviews  
✓ Planning 6-month GTM roadmap and 90-day execution  

---

## Files in This Skill

- `SKILL.md` — This documentation
- `.claude/skills/enterprise-gtm.yaml` — Skill definition and metadata
- `frameworks/` — Framework templates and examples
- `content/` — Content strategy templates
- `examples/` — Real product examples (Ask-AI, Risk Scoring, eCourt)
- `positioning/` — Positioning workshop materials
- `strategy/` — Sales and lead gen strategy templates

---

## Next Steps

1. **Invoke the skill** with your product info
2. **Select your workflow** (full positioning, framework-only, content-only, etc.)
3. **Review framework recommendation** and rationale
4. **Run discovery exercises** (if full positioning)
5. **Customize content** for your target buyers
6. **Launch GTM execution** within 30 days

---

## Questions?

For detailed framework guidance, examples, or custom configurations, invoke the skill with your product information and the skill will guide you through the entire process.
