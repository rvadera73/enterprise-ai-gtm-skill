# Enterprise AI GTM Skill — Definition & Usage

**A reusable skill for generating complete, production-ready B2B SaaS marketing and go-to-market systems.**

---

## Skill Summary

**Name:** Enterprise AI GTM + Marketing Skill  
**Purpose:** Generate professional marketing materials and execution playbooks for B2B SaaS products  
**Input:** Product details (name, problem, solution, target audience)  
**Output:** Whitepaper, one-pager, 2-week LinkedIn campaign, execution guides  
**Time to value:** 2 weeks (first customer conversations)  
**ROI:** $5-10M pipeline from <15 hours of execution  

---

## Skill Capabilities

### Core Capabilities

1. **Strategic Positioning** ✓
   - Market analysis (TAM/SAM/SOM)
   - Competitive positioning
   - Go-to-market motion design
   - Business strategy analysis

2. **Content Generation** ✓
   - Professional whitepaper (HTML/CSS, Tailwind, print-ready)
   - Visual one-pager (PDF-ready)
   - 14-day LinkedIn campaign (copy-paste ready)
   - Operational guides and playbooks

3. **Execution Planning** ✓
   - Daily task checklists
   - Engagement strategy per post
   - Success metrics and tracking
   - Follow-up playbooks

4. **Customization Support** ✓
   - Template-based approach
   - Adaptation guides
   - Industry-specific variations
   - Product-specific customization

---

## Skill Inputs

### Required
```yaml
Product Name: string
  - Example: "Enterprise Ask-AI Service", "Risk Scoring Platform"
  - Used in: Whitepaper, one-pager, LinkedIn posts, guides

Target Problem: string (specific, not generic)
  - Example: "Enterprises rebuild AI systems repeatedly instead of reusing infrastructure"
  - Example: "Organizations maintain inconsistent fraud rules across channels"
  - Used in: All marketing materials

Target Persona: string
  - Example: "Federal CIO", "Enterprise VP Engineering", "Healthcare CISO"
  - Used in: LinkedIn campaign targeting, messaging tone

Key Differentiators: array[string]
  - Example: ["Built for federal compliance", "Multi-tenant architecture", "Unified governance"]
  - Used in: Competitive positioning, one-pager
```

### Optional
```yaml
Industry: string
  - Options: "Federal", "Healthcare", "FinServ", "Enterprise"
  - Used in: Tone, emphasis, examples

Competitive Context: string
  - Example: "vs. SageMaker (vendor lock-in), vs. LangChain (no governance)"
  - Used in: Competitive positioning section

Use Cases: array[string]
  - Example: ["Conversational Knowledge", "Fraud Detection", "Case Management"]
  - Used in: Whitepaper examples, one-pager, LinkedIn posts
```

---

## Skill Outputs

### Deliverables

1. **Whitepaper.html** (4 pages)
   - Modern SaaS design (Tailwind CSS)
   - Embedded data visualizations
   - Print-to-PDF ready
   - ~32KB, renders in <1 sec

2. **OnePager.html** (1 page)
   - Problem | Solution | Impact format
   - Print-ready (8.5"x11")
   - LinkedIn document share-ready
   - ~12KB, prints beautifully

3. **LinkedIn-Campaign.md** (14 posts)
   - Day-by-day content calendar
   - Copy-paste ready (no editing needed)
   - Engagement hooks per post
   - Follow-up playbook
   - ~30KB, 14K words

4. **Operational Guides**
   - Quick-start checklist (daily tasks)
   - Execution playbook (how to run the campaign)
   - Marketing guide (asset reference)
   - Customization guide (adapt for your product)
   - Success metrics (what to track)

5. **Strategy Documents** (when provided)
   - Business strategy analysis
   - Market analysis (TAM/SAM/SOM)
   - Competitive positioning
   - Go-to-market motion design

---

## How to Use This Skill

### Path 1: Quick Start (Use Existing Example)

```bash
# Step 1: Navigate to example
cd examples/Enterprise-AI-Foundry/

# Step 2: Read quick start
cat quick-start-checklist.md

# Step 3: Execute (starting Monday)
# Open files, follow daily checklist for 2 weeks
```

**Time:** 5 minutes to start, 45 min/day for 2 weeks  
**Output:** 400+ followers, 5-10 conversations, 2-3 demo calls  

### Path 2: Adapt for Your Product

```bash
# Step 1: Read customization guide
cat docs/CUSTOMIZATION_GUIDE.md

# Step 2: Copy example files
mkdir products/Your-Product-GTM
cp examples/Enterprise-AI-Foundry/* products/Your-Product-GTM/

# Step 3: Customize materials (2 hours)
# Edit whitepaper.html, onepager.html, linkedin-campaign.md

# Step 4: Execute (starting Monday)
# Follow quick-start-checklist.md for 2 weeks
```

**Time:** 2 hours customization + 45 min/day for 2 weeks  
**Output:** Same as Path 1, but for your specific product  

### Path 3: Generate from Scratch

```bash
# Step 1: Provide product details (optional)
# See "Skill Inputs" above

# Step 2: Use templates (templates/ directory)
# Build custom strategy, whitepaper, campaign

# Step 3: Generate materials
# Customize for your specific positioning

# Step 4: Execute
# Follow playbook for 2 weeks
```

**Time:** 4-6 hours (building from templates) + 45 min/day for 2 weeks  

---

## Success Criteria

### Week 1
- [ ] 7 posts live on LinkedIn
- [ ] 50-100 new followers
- [ ] 2-3 inbound messages
- [ ] 1-2 hot leads identified (specific comments)

### Week 2
- [ ] 14 posts live
- [ ] 250-400+ new followers
- [ ] 5-10 inbound messages
- [ ] 2-3 discovery calls scheduled
- [ ] 20-30 whitepaper downloads

### Month 1
- [ ] 400-600 followers
- [ ] 5-10 conversations at various stages
- [ ] First customer discussion initiated

### Month 3
- [ ] 1000+ followers
- [ ] First customer signed or pilot launched
- [ ] $5-10M pipeline

---

## Integration Points

### Before Using This Skill

You should have:
- ✓ Clear understanding of your product's value prop
- ✓ Identified target customer (persona)
- ✓ Articulated the specific problem you solve
- ✓ (Optional) Business strategy document

### After Using This Skill

You'll have:
- ✓ Complete marketing system (materials + playbook)
- ✓ Professional thought leadership (whitepaper)
- ✓ Proven execution playbook (2-week campaign)
- ✓ Lead generation pipeline (qualified conversations)

---

## Variants & Customization

### By Product Type

**Enterprise AI Products** (Ask-AI, Risk Scoring, MLOps, Document Intelligence)
- Use as-is, adapt examples to your use cases
- Emphasis: Infrastructure, governance, scale

**Federal Government Products**
- Emphasize: Compliance, audit, security, governance
- Add: Federal context examples and references

**Healthcare Products**
- Emphasize: HIPAA, data residency, patient privacy
- Add: Healthcare industry examples

**Financial Services Products**
- Emphasize: Risk management, fraud prevention, regulatory
- Add: FinServ industry compliance references

### By Stage

**Pre-product** (Validating the problem)
- Focus: Problem exposition, thought leadership
- Use: Days 1-7 of campaign

**MVP** (Building credibility, early adoption)
- Focus: Problem + solution framework
- Use: All 14 days + whitepaper for credibility

**Production** (Driving adoption)
- Focus: Solution + case studies + ROI
- Use: All materials + add customer testimonials

**Scale** (Multiple products, expansion)
- Focus: Competitive positioning + thought leadership
- Use: Same playbook, iterate messaging

---

## Metrics & Measurement

### Daily Tracking
- LinkedIn followers (should grow 10-30/day)
- Post impressions (should grow over 2 weeks)
- Comments per post (should grow 3→20)
- Inbound messages (first expected by Day 3)

### Weekly Tracking
- Total new followers
- Engagement rate (comments / impressions)
- Conversation quality (generic vs. specific)
- Hot leads identified

### Monthly Tracking
- Total followers gained
- Total conversations started
- Qualified leads (fit your ICP)
- Pilots / partnerships initiated

### ROI Tracking
- Hours invested (execution time)
- Customer conversations generated
- Estimated pipeline value
- First customer acquisition cost

---

## Skill Performance Benchmarks

### Based on Enterprise AI Foundry Case Study

| Metric | Week 1 | Week 2 | Month 1 | Month 3 |
|--------|--------|--------|---------|---------|
| Followers | 50-100 | 250-400 | 400-600 | 1000+ |
| Comments | 30-50 | 100+ | 200+ | 500+ |
| Inbound messages | 1-2 | 5-10 | 5-10 | 20-30 |
| Demo calls booked | 0 | 2-3 | 3-5 | 10+ |
| Customers acquired | 0 | 0 | 0 | 1-2 |
| Pipeline value | $0 | $1-2M | $3-5M | $5-10M |

---

## Common Customizations

### By Audience

**CIOs/CTOs:** Emphasize architecture, scale, governance  
**CFOs/VPs:** Emphasize cost, ROI, time to value  
**Security/Compliance:** Emphasize governance, audit, regulatory  
**Product Managers:** Emphasize user experience, adoption, metrics  

### By Tone

**Formal/Enterprise:** More structured, data-driven  
**Startup/Conversational:** More casual, founder voice  
**Technical:** More architecture-focused  
**Business-focused:** More ROI and outcomes-focused  

### By Industry

**Federal:** Add compliance references, regulatory context  
**Healthcare:** Add HIPAA references, privacy context  
**FinServ:** Add risk/fraud references, regulatory context  
**Enterprise:** Add operational efficiency references  

---

## Troubleshooting

**Q: Posts aren't getting engagement?**
A: Check: Are you responding to comments? (This is 80% of the value)

**Q: Materials don't feel authentic?**
A: Check: Is the problem specific to your situation? Customize more.

**Q: Not sure what to customize?**
A: Start with copy, don't change structure. Same narrative arc works.

**Q: Can I skip parts of the campaign?**
A: Not recommended. All 14 days build momentum. Go all 2 weeks.

**Q: Can I run this for multiple products?**
A: Yes, but not simultaneously Week 1-2. Launch one, succeed, then next.

---

## Skill Evolution

### Current Version (v1.0)
- ✓ Enterprise AI Foundry case study (complete)
- ✓ 2-week LinkedIn campaign
- ✓ Professional whitepaper + one-pager
- ✓ Execution playbooks
- ✓ Customization guides

### Planned Enhancements (v1.1+)
- [ ] Additional industry examples (Healthcare, FinServ, Federal)
- [ ] Product-specific templates (Risk Scoring, MLOps, Document Intelligence)
- [ ] Video script generation (90-second explainer videos)
- [ ] Email sequence generation (follow-up drip campaigns)
- [ ] Blog post expansion (long-form content from LinkedIn posts)
- [ ] Automated metrics tracking (spreadsheet templates)
- [ ] A/B testing framework (post variations by audience)

---

## For Claude Code Integration

### Installation

```bash
# Clone the skill
git clone https://github.com/your-org/enterprise-ai-gtm-skill
cd enterprise-ai-gtm-skill

# Install (if using Node.js)
npm install
```

### Usage in Claude Code

```bash
# Generate for Enterprise AI Foundry (example provided)
claude-code skill:enterprise-ai-gtm-skill \
  --example "Enterprise-AI-Foundry"

# Generate for custom product
claude-code skill:enterprise-ai-gtm-skill \
  --product "Your Product Name" \
  --problem "Specific problem statement" \
  --persona "Target persona" \
  --output "./marketing-assets"
```

### As a Reusable Skill

This skill can be:
- ✓ Cloned and customized
- ✓ Extended with new templates
- ✓ Integrated into larger workflows
- ✓ Used repeatedly across products

---

## Licensing & Usage

- **License:** MIT (see LICENSE file)
- **Usage:** Free for internal use, customer engagements
- **Attribution:** Not required but appreciated
- **Sharing:** Encouraged (with attribution)

---

## Support & Documentation

| Document | Purpose |
|----------|---------|
| `README.md` | Skill overview |
| `docs/GETTING_STARTED.md` | 30-min quick start |
| `docs/CUSTOMIZATION_GUIDE.md` | How to adapt for your product |
| `examples/Enterprise-AI-Foundry/` | Complete working example |
| `examples/Enterprise-AI-Foundry/README.md` | Case study & lessons learned |

---

**Enterprise AI GTM Skill**  
**Version:** 1.0.0  
**Status:** Production Ready  
**Last Updated:** June 2026  
**Next Product:** Risk Scoring (Q4 2026)