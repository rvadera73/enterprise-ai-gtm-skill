# Whitepaper Template — the long-form written asset, same spine as the one-pager

Companions: `../video/GTM-ASSET-PLAYBOOK.md` §7 (one-pager spine), `../video/DESIGN-SYSTEM.md`
(brand tokens + layered bands — this template inherits both rather than inventing new
visual structure), `../video/VIDEO-ASSET-TEMPLATES.md` (Rule 0, the web-verification
rule every figure in this doc is also bound by).

Raw example content exists at `examples/whitepapers/` (12+ HTML variants, several `.md`
drafts, a `README.md`, `WHITEPAPER_VERSIONS.md`, `WHITEPAPER_QUICK_SELECTION.md`). That
directory is reference material to learn tone and shape from — same rule this skill
already applies to NotebookLM output: **never copy it in verbatim.** It also predates
this template, so it doesn't yet reflect the Rule-0 verification gate or the
`DESIGN-SYSTEM.md` brand tokens below; treat its confident-sounding metrics (70% cost
reduction, 6x faster delivery, specific dollar figures) as **unverified drafting
examples, not pre-cleared numbers** — every figure still needs its own Rule-0 pass.

---

## 0. Which asset do you actually need? Decide this before filling anything in

**Full white paper** — broad public marketing collateral. No specific pursuit,
program, or customer relationship exists yet. Speaks to a category-level problem for
an audience type (e.g. "federal CTOs modernizing legacy case-management systems"), not
to one named opportunity. Long-form (6-10 pages, ~2,500-3,500 words), built for
gated download / LinkedIn extraction / cold outreach credibility. Use the **full
skeleton** in §2 below.

**Point paper** — a short, targeted document (6-7 slides/pages, ~600-1,000 words)
addressing a *specific audience's pain point* without naming any specific program,
solicitation, or pursuit. This is the right choice once a specific opportunity is
already forming (an RFI is out, a customer conversation has identified a real problem)
but before a formal capture or proposal effort exists — it's shaping material, not a
compliance document. Use the **condensed skeleton** in §2.1.

Do not conflate the two: a point paper that names a solicitation number or a specific
program has drifted into capture/proposal territory (see `capture-management` and
`proposal-drafting` skills) and is no longer a GTM asset built from this template. A
full white paper that narrows to name one customer's specific procurement has the
opposite problem — it stops being broad collateral and needs the capture skill's
tighter claim discipline instead.

---

## 1. Brief — fill this in first, before writing prose

Mirrors `../video/BRIEF-TEMPLATE.md`'s shape. Vagueness here shows up as a weak asset,
same as it does for video.

- **Asset:** full whitepaper / point paper (§0)
- **Product name, exactly as it must be said:** `{{PRODUCT_NAME}}`
- **Audience:** `{{AUDIENCE}}` (e.g. "federal CIOs and CTOs evaluating modernization
  vendors" — be specific; "enterprise leaders" is not an audience)
- **What they already know about us:** `{{PRIOR_CONTEXT}}` (assume nothing unless this
  is a follow-up to something they've already read)
- **What they have NO context for:** customer names, internal program names, case IDs,
  regulation numbers not yet defined → don't use these without a first mention that
  defines them
- **Length target:** `{{LENGTH_TARGET}}` (pages/words — see §2 budgets)
- **Where it will be published:** gated download · LinkedIn extract · email attachment
  · deck appendix
- **The single core claim (BLUF), one sentence:** `{{CORE_CLAIM}}` — if it takes two
  sentences, the asset is trying to do too much (same compression test as video's
  BLUF, `../video/GTM-ASSET-PLAYBOOK.md` §13.4)
- **The do-not-claim list:** `{{DO_NOT_CLAIM}}` (roadmap items, unshipped features —
  pulled from the product's own ADRs/roadmap docs, same source video's checklist uses)
- **Claim boundaries — what this must NOT imply:** `{{CLAIM_BOUNDARIES}}` (e.g. "X is
  one contributing factor to the cited industry failure rate — do not imply the
  product prevents it outright")

---

## 2. Section-by-section skeleton — full white paper (~2,500-3,500 words)

Each section maps onto one of `DESIGN-SYSTEM.md`'s layered bands (§3 below spells out
the mapping explicitly). Word budgets are targets, not hard caps — but if a section
runs 2x its budget, that's a sign it's trying to be two sections.

1. **Executive summary / BLUF** (150-250 words) — maps to the **header/BLUF band**.
   Lead with `{{CORE_CLAIM}}` as a fact or tension, not a setup — same rule as video's
   opening (`GTM-ASSET-PLAYBOOK.md` §3.1). Name `{{PRODUCT_NAME}}` in the first two
   sentences. No metrics-first framing — a headline stat is not a substitute for the
   claim itself.

2. **Problem framing** (400-600 words) — maps to the **application layer band** (who
   has this problem, in what context, doing what job). Name what's assumed vs. what's
   actually true (the reframe move, `GTM-ASSET-PLAYBOOK.md` §3.2). Domain-free where
   possible — avoid internal job titles or case IDs that make a general pattern read
   as a niche one (§3.7 of the same doc).

3. **The mechanism / approach** (600-900 words) — maps to **the service band** (what
   `{{PRODUCT_NAME}}` actually does, mechanically). Show the mechanism, don't just
   assert it — the written equivalent of video's "generated SQL on screen" rule
   (`GTM-ASSET-PLAYBOOK.md` §3.4). One concrete contrast beats a feature list here too.

4. **Proof points** (500-800 words, 2-4 examples) — maps to the **impact metrics
   band**. **Every figure in this section is Rule-0 territory — web-search-verify it,
   record the source and the date checked, same as video's mandatory step
   (`GTM-ASSET-PLAYBOOK.md` §4 rule 4, `VIDEO-ASSET-TEMPLATES.md` Rule 0).** This
   applies to the product's own claimed metrics as much as third-party statistics —
   `DESIGN-SYSTEM.md` §5 flags exactly this for the one-pager's own "100% secure"
   claim, and the same discipline applies here.

5. **Governance / compliance angle** (200-400 words, include only if relevant to the
   audience) — maps to the **governance band** (the defensibility/audit story: access
   control, compliance auditing, data handling). Skip this section entirely rather
   than padding it if the audience isn't compliance-sensitive; an empty-feeling
   governance section reads worse than no section.

6. **Close** (150-250 words) — a genuine synthesis, not a recap. End on a question or
   a clear next step, not generic "contact us for more information" boilerplate. If a
   CTA is included, keep it to one line — the substance should already have made the
   case.

**Total:** ~2,000-3,150 words core content, +appendix if proof points need supporting
detail tables (appendix word count doesn't count against the budget above).

## 2.1 Section-by-section skeleton — point paper (~600-1,000 words, 6-7 slides/pages)

Same six bands, compressed to one slide/page each, no program or pursuit named:

1. **Header/BLUF** (40-60 words, 1 slide) — the claim, ≤8 words as a headline
   (`DESIGN-SYSTEM.md` §2's header rule) plus 1-2 sentences of context.
2. **Problem framing** (80-120 words, 1 slide) — the specific pain point for
   `{{AUDIENCE}}`, no named program.
3. **The mechanism / approach** (100-150 words, 1-2 slides) — what `{{PRODUCT_NAME}}`
   does about it.
4. **Proof points** (100-150 words, 1 slide) — 1-2 verified figures max, Rule 0
   applies exactly as in §2.4 above; a point paper has less room to hedge a shaky
   number, not more.
5. **Governance angle** (60-100 words, 1 slide, optional) — only if the audience is
   compliance-sensitive.
6. **Close** (40-60 words, 1 slide) — one question or one clear next step.

---

## 3. Visual inheritance from `DESIGN-SYSTEM.md` — do not invent new structure

This template's six sections map directly onto the one-pager's canonical layered
bands (`DESIGN-SYSTEM.md` §3):

```
Executive Summary / BLUF   →  HEADER band (brand + tagline + one-line problem)
Problem framing            →  ANY APPLICATION LAYER band (who has this problem)
The mechanism / approach   →  {{PRODUCT_NAME}} SERVICE band (the product itself)
[implicit — data sources]  →  ANY CONNECTED ENTERPRISE DATA band (what it reads/writes)
Governance angle           →  GOVERNANCE & ACCESS CONTROL band
Proof points                →  ENTERPRISE BUSINESS IMPACT band (the metrics)
```

Any diagram used in the whitepaper (architecture figure, layer stack) should be
recognizably this same structure, not a new geometry invented for print. If the
document includes a laid-out PDF/HTML version rather than plain markdown, it inherits
`DESIGN-SYSTEM.md` §1's verified brand tokens directly:

- **Ground:** dark slate gradient (`slate-900 → slate-800 → slate-900`), not a new
  background color
- **Typeface:** Inter (vendor the actual font file if rendering outside a browser
  that already has Google Fonts access — a named-but-not-loaded font silently falls
  back to system sans, `GTM-ASSET-PLAYBOOK.md` §4 rule 13)
- **Accents:** 3-4 colors drawn from the existing blue/teal/purple/green family
  (§1's `label-blue`/`subtitle-teal`/`accent-purple`/`accent-green` tokens) — never a
  new hue invented per product (the "molten copper" mistake this doc already warns
  against)
- **Headers:** bold, uppercase, tight tracking, ≤8 words
- **Capability names:** if the whitepaper describes `{{PRODUCT_NAME}}`'s capabilities,
  use the exact taxonomy names from `DESIGN-SYSTEM.md` §4 rather than inventing new
  labels for the same five things

A plain-markdown/Word draft doesn't need to render these tokens directly, but its
prose structure and any diagrams should still assume this is where it's headed —
don't design around a different visual system that will need to be un-learned at
layout time.

---

## 4. Checklist gate — before this is published anywhere

Mirrors `../video/STORYBOARD-TEMPLATE.md`'s sign-off gate. Fill this in and get it
reviewed before the document goes out, not after.

**Truth**
- [ ] Every figure in the proof-points section (and anywhere else a number appears)
  is web-verified per Rule 0; source + date checked recorded next to each one
- [ ] No forecast or projection quoted for a period that has since elapsed
- [ ] Our own product metrics (adoption %, cost reduction, accuracy) are substantiated
  the same way a third-party stat would be — not exempted because "it's our number"
- [ ] `{{DO_NOT_CLAIM}}` items do not appear described as shipped/current capability
  anywhere in the document — label explicitly as roadmap/future if mentioned at all
- [ ] Claim boundaries (`{{CLAIM_BOUNDARIES}}`) are respected — nothing implied that
  can't be defended if a reader pushes back

**Read test**
- [ ] Read the whole document as if you are `{{AUDIENCE}}` seeing it for the first
  time, with zero prior context — does every term, acronym, and internal reference get
  defined before it's used, or does it assume context only an insider has?
- [ ] The executive summary / BLUF, read in isolation, compresses to a few sentences a
  stranger would understand without reading the rest of the document (same
  compression test video's BLUF line uses, `GTM-ASSET-PLAYBOOK.md` §13.4)
- [ ] No section is a restated version of another section — each of the six bands
  earns its place

**Structure**
- [ ] Section word counts are within roughly 1.5x of their §2/§2.1 budgets, or there's
  a deliberate reason one section is longer
- [ ] Diagrams (if any) inherit the layered-band structure (§3) rather than a
  bespoke geometry
- [ ] Brand tokens (if a laid-out version exists) match `DESIGN-SYSTEM.md` §1 exactly,
  or the divergence is deliberate and recorded
- [ ] Capability names, if used, match `DESIGN-SYSTEM.md` §4's taxonomy verbatim

**Scope discipline (§0)**
- [ ] If this is a point paper: confirm no specific program, solicitation number, or
  named pursuit appears anywhere in the document — if one does, this has become
  capture/proposal material and belongs with the `capture-management` or
  `proposal-drafting` skill instead, not this template
- [ ] If this is a full white paper: confirm it still speaks to a category/audience,
  not one narrowed-down customer relationship

**Sign-off:** `______`  **Date:** `______`
