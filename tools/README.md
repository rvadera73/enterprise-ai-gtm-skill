# Tools & Automation

Automation scripts and tools to support GTM execution.

## Folders

### `/content-generation/`
Tools for analyzing and generating content.

**Files**:
- `content_analyzer.py` — Analyze your posts for messaging patterns
- `linkedin_scraper.py` — Fetch LinkedIn content (official export support)
- `CONTENT_ANALYZER_GUIDE.md` — How to use the analyzer
- `WORKFLOW_GUIDE.md` — Complete content analysis workflow

**Use for**: Understanding your authentic messaging and content patterns.

### `/lead-gen/`
Tools for generating and managing leads.

**Files**:
- `prospect_conversation_builder.py` — Interactive framework for building sales conversations
- (Future) `decision_framework_generator.py` — Auto-generate decision frameworks

**Use for**: Building conversation frameworks for specific prospects.

### `/marketing-factory/`
Automated marketing asset generation (legacy).

**Files**:
- `generate_post.py` — LinkedIn post generator
- `generate_image.py` — Image generation
- `generate_voiceover.py` — Voiceover generation
- Supporting files

**Note**: These are lower priority. Focus on positioning and lead gen first.

---

## Quick Start

### Analyze Your Messaging
```bash
cd tools/content-generation
python content_analyzer.py --interactive
```
Paste your LinkedIn posts, get messaging profile.

### Build Prospect Conversations
```bash
cd tools/lead-gen
python prospect_conversation_builder.py
```
Answer questions about prospect, get conversation framework.

---

## Which Tool Should I Use?

**If you want to**:
- Understand your messaging → `/content-generation/content_analyzer.py`
- Build sales conversation frameworks → `/lead-gen/prospect_conversation_builder.py`
- Generate marketing assets at scale → `/marketing-factory/` (future)

---

## Next Steps

1. Review `/content-generation/QUICK_START.md`
2. Run content analyzer to confirm your messaging
3. Use prospect_conversation_builder for your first prospect
4. Archive or revisit marketing factory later

---

## Related Documentation
- `/documentation/TOOL-USAGE-GUIDE.md` — Complete tool documentation
- `/strategy/LEAD-GENERATION-STRATEGY.md` — How tools fit into GTM
