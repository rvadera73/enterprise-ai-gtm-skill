# Enterprise AI GTM Skill - Proposed Structure

## Current Issues
- 20+ markdown files in root directory (cluttered)
- Tools scattered in `/tools/` without clear organization
- Examples in `/examples/` but not linked from main docs
- No clear navigation/hierarchy

## Proposed Enhanced Structure

```
enterprise-ai-gtm-skill/
│
├── README.md                              # Main entry point
├── .gitignore
├── package.json
│
├── /positioning/                          # Core positioning frameworks
│   ├── README.md                          # How to use positioning
│   ├── POSITIONING-FRAMEWORK.md           # THE main framework (Ask-AI + Foundry together)
│   ├── ASK-AI-POSITIONING.md              # Ask-AI specific details
│   ├── ENTERPRISE-AI-FOUNDRY-POSITIONING.md # Foundry specific details
│   ├── AUTHENTIC-MESSAGING-PROFILE.md     # Your actual voice & themes
│   └── MENTAL-MODELS-POSITIONING.md       # Mental model framework for Sr. IT Execs
│
├── /content/                              # All marketing content
│   ├── README.md                          # Content guidelines
│   ├── /linkedin/                         # LinkedIn posts
│   │   ├── README.md                      # Post strategy & schedule
│   │   ├── ASK-AI-THOUGHT-LEADERSHIP-1.md # High-quality Ask-AI post
│   │   ├── FOUNDRY-THOUGHT-LEADERSHIP-1.md # Foundry post (to create)
│   │   └── (future posts)
│   ├── /blog/                             # Long-form blog articles
│   ├── /whitepapers/                      # Full whitepapers
│   └── /case-studies/                     # Customer case studies
│
├── /strategy/                             # GTM strategies
│   ├── README.md                          # Strategy overview
│   ├── LEAD-GENERATION-STRATEGY.md        # 5-stage lead funnel
│   ├── DECISION-FRAMEWORK.md              # Lead magnet framework
│   ├── DISCOVERY-WORKSHOP.md              # 6-week discovery process
│   ├── CUSTOMER-JOURNEY-MAP.md            # Ask-AI to Foundry progression
│   └── (supporting strategy docs)
│
├── /research/                             # Research & discovery
│   ├── README.md
│   ├── STRATEGIC-DISCOVERY-BRIEF.md       # Initial research synthesis
│   ├── ENTERPRISE-AI-FOUNDRY-RESEARCH.md  # Product research
│   ├── ASK-AI-RESEARCH.md                 # Ask-AI specific research
│   ├── COMPETITOR-ANALYSIS.md             # Market analysis
│   └── (supporting research)
│
├── /tools/                                # Automation tools & scripts
│   ├── README.md                          # Tool overview
│   ├── /content-generation/               # Content creation tools
│   │   ├── content_analyzer.py            # Analyze posts for messaging
│   │   ├── linkedin_scraper.py            # Fetch LinkedIn content
│   │   ├── CONTENT_ANALYZER_GUIDE.md      # How to use analyzer
│   │   └── WORKFLOW_GUIDE.md              # Complete workflow
│   ├── /lead-gen/                         # Lead generation tools
│   │   ├── prospect_conversation_builder.py # Build conversation frameworks
│   │   ├── decision_framework_generator.py  # Generate decision framework
│   │   └── LEAD_GEN_TOOLS_GUIDE.md        # Tool usage guide
│   ├── /marketing-factory/                # Marketing automation (legacy)
│   │   ├── generate_post.py
│   │   ├── generate_image.py
│   │   ├── generate_voiceover.py
│   │   └── README.md
│   └── QUICK_START.md                     # Quick start for all tools
│
├── /examples/                             # Reference materials
│   ├── README.md
│   ├── /ask-ai/                           # Ask-AI examples
│   │   ├── BUSINESS-CASE.md               # Ask-AI ROI calculation
│   │   ├── DEPLOYMENT-TIMELINE.md         # 28-day deployment plan
│   │   └── CUSTOMER-OUTCOMES.md           # Proof points
│   ├── /foundry/                          # Foundry examples
│   │   ├── BUSINESS-CASE.md               # Foundry ROI (3 systems)
│   │   ├── 120-DAY-ROADMAP.md             # Full deployment timeline
│   │   ├── COST-BREAKDOWN.md              # Pricing model
│   │   └── (supporting examples)
│   ├── /federal/                          # Federal-specific examples
│   │   ├── DOL-OALJ-CASE-STUDY.md        # IACP case study
│   │   ├── CBP-CASE-STUDY.md              # CBP Sentry case study
│   │   └── COMPLIANCE-FRAMEWORK.md        # Federal compliance approach
│   └── /whitepapers/                      # Reference whitepapers
│
├── /documentation/                        # How-to guides
│   ├── README.md
│   ├── GETTING-STARTED.md                 # First 30 days
│   ├── POSITIONING-GUIDE.md               # How to use frameworks
│   ├── CONTENT-CREATION-GUIDE.md          # How to create posts
│   ├── LEAD-GENERATION-GUIDE.md           # How to generate leads
│   ├── SALES-CONVERSATION-GUIDE.md        # How to close deals
│   └── CUSTOMIZATION-GUIDE.md             # How to tailor for your org
│
└── /archive/                              # Old/obsolete files
    ├── BRAND-DISCOVERY-FRAMEWORK.md       # (archived - superseded by positioning)
    ├── MARKETING-FACTORY-*.md             # (archived - old approach)
    └── (other obsolete docs)
```

---

## File Organization Plan

### Phase 1: Create Folders (Today)
```bash
mkdir -p /positioning /content/{linkedin,blog,whitepapers,case-studies} \
  /strategy /research /tools/{content-generation,lead-gen,marketing-factory} \
  /examples/{ask-ai,foundry,federal,whitepapers} /documentation /archive
```

### Phase 2: Move & Organize Files

**To `/positioning/`:**
- POSITIONING-FRAMEWORK-ASK-AI-ENTERPRISE-AI-FOUNDRY.md → POSITIONING-FRAMEWORK.md
- YOUR-AUTHENTIC-MESSAGING-PROFILE.md → AUTHENTIC-MESSAGING-PROFILE.md
- MENTAL-MODELS-POSITIONING.md (stays as-is)
- Create: ASK-AI-POSITIONING.md
- Create: ENTERPRISE-AI-FOUNDRY-POSITIONING.md

**To `/content/linkedin/`:**
- ASK-AI-THOUGHT-LEADERSHIP-POST.md → ASK-AI-THOUGHT-LEADERSHIP-1.md
- Create: LINKEDIN-STRATEGY.md

**To `/strategy/`:**
- LEAD-GENERATION-STRATEGY.md (stays)
- STRATEGIC-DISCOVERY-BRIEF.md (stays)
- ENTERPRISE-AI-FOUNDRY-ASK-AI-INPUTS.md → DISCOVERY-INPUTS.md
- Create: CUSTOMER-JOURNEY-MAP.md
- Create: DECISION-FRAMEWORK.md

**To `/research/`:**
- SKILL-DEFINITION-AND-SYSTEM-ARCHITECTURE.md (stays)
- Create: ENTERPRISE-AI-FOUNDRY-RESEARCH.md
- Create: ASK-AI-RESEARCH.md
- Create: COMPETITOR-ANALYSIS.md

**To `/tools/content-generation/`:**
- content_analyzer.py
- linkedin_scraper.py
- CONTENT_ANALYZER_GUIDE.md
- WORKFLOW_GUIDE.md
- linkedin_content_template.txt

**To `/tools/lead-gen/`:**
- prospect_conversation_builder.py
- Create: decision_framework_generator.py

**To `/examples/ask-ai/`:**
- Extract from ask-ai-campaign-artifacts.md

**To `/examples/foundry/`:**
- Create from research and proof points

**To `/documentation/`:**
- GETTING_STARTED.md (from /docs/)
- Create: POSITIONING-GUIDE.md
- Create: CONTENT-CREATION-GUIDE.md
- Create: others

**To `/archive/`:**
- BRAND-DISCOVERY-FRAMEWORK.md
- MARKETING-FACTORY-*.md
- LINKEDIN-POSTS-ENTERPRISE-AI-FOUNDRY.md (old template posts)
- (other superseded files)

### Phase 3: Create Navigation Files

Create README files for each folder that:
- Explain the folder's purpose
- List what's inside
- Link to related folders
- Show where to start

---

## Master README Structure

```markdown
# Enterprise AI GTM Skill

## Quick Start (30 minutes)
- Read: /positioning/POSITIONING-FRAMEWORK.md
- Read: /content/linkedin/ASK-AI-THOUGHT-LEADERSHIP-1.md
- Next: Post on LinkedIn

## For Different Roles

### If you're the GTM Lead:
- Start: /documentation/GETTING-STARTED.md
- Then: /strategy/LEAD-GENERATION-STRATEGY.md
- Then: /content/linkedin/

### If you're the Sales Lead:
- Start: /positioning/POSITIONING-FRAMEWORK.md
- Then: /documentation/SALES-CONVERSATION-GUIDE.md
- Then: /examples/

### If you're the Content Lead:
- Start: /content/linkedin/LINKEDIN-STRATEGY.md
- Then: /documentation/CONTENT-CREATION-GUIDE.md
- Then: /strategy/

## Full Map
- Positioning → Content → Strategy → Tools → Examples
- [link to folder structure diagram above]
```

---

## Benefits of This Structure

1. **Clear Navigation**: Everything has a place
2. **No Root Clutter**: 20+ files organized into folders
3. **Self-Documenting**: README in each folder explains purpose
4. **Scalable**: Easy to add new posts, cases, examples
5. **Role-Based**: Easy for different people to find what they need
6. **Archive**: Old files don't clutter active workspace

---

## Implementation

Should I:
1. Create all folders and README files? ✅
2. Move all existing files? ✅
3. Update master README for navigation? ✅
4. Create any missing files? ✅

Confirm and I'll execute the reorganization now.
