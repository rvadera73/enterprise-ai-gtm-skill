# Brief Template — the input that produces a GTM asset

Fill this in; it produces a video spec (`content/<id>.json`) or a one-pager layout.
Everything downstream is derived from it, so vagueness here shows up as a weak asset.

Read `GTM-ASSET-PLAYBOOK.md` first. Rule 0 (`VIDEO-ASSET-TEMPLATES.md`) is mandatory.

---

## 1. What is this?

- **Asset:** video (hybrid — if a live, demoable UI exists, see `GTM-ASSET-PLAYBOOK.md`
  §1 / explain-only — if no demoable UI exists / feature-detail — narrower hybrid
  variant, for a warmer audience) · one-pager · post image
- **Product name, exactly as it must be said:** `______` (e.g. "Ask-AI MCP Service")
- **Length target:** `__` seconds → **word budget = seconds × 2.5** (≈150 wpm)
- **Where it will be published:** LinkedIn native · X · demo page · deck
- **Capture plan reference** (if this campaign supports a government pursuit):
  `______` — cite the `CAPTURE_PLAN_[opportunity].md` file from
  proposal-development's capture-management work here for positioning inputs
  (differentiators, proof points, competitor angle) rather than re-deriving them
  from scratch.

## 2. Audience

- **Who:** `______` (e.g. enterprise CIOs, CTOs, architects)
- **What they already know about us:** `______` (assume nothing unless it's a series)
- **What they have NO context for:** customer names, case IDs, regulation numbers,
  internal job titles → these must not appear in narration or copy

## 3. The single idea

One sentence. If it takes two, the asset is trying to do too much.

> `______`

## 4. The opening (BLUF)

A fact or tension, not a setup. BLUF passes the 3-line compression test
(`GTM-ASSET-PLAYBOOK.md` §13.4).

- **Verified figure:** `______`
- **Source + date checked:** `______`  ← **Rule 0. Web-search it. No exceptions.**
- **Is it a forecast for a period that has now elapsed?** If yes, find the outcome instead.
- **Is the source contested?** If yes, pick another.

## 5. The reframe

What the audience assumes, and what's actually true.

> They assume: `______`
> Actually: `______`

## 6. The ONE concrete contrast

Not a feature list. A single before/after, or same-input-different-output.

> `______`

## 7. The visible mechanism

What can the viewer *see working* that proves the claim? (Generated SQL on screen
beat every assertion we could have written.)

> `______`

## 8. Benefit — as consequence, not adjective

> `______`  (❌ "seamless, scalable, enterprise-ready")

## 9. Close

- **Question to leave them with:** `______`
- **CTA:** demo link goes in the **first comment**, never the body

## 10. Product mentions

- Target: **3–4×, functional** ("X writes the query"), never promotional
- Persistent brand rule on screen: yes / no

## 11. Claim boundaries — what we must NOT imply

> e.g. "duplicated infrastructure is ONE contributing factor to the cited failure
> causes — do not imply the product prevents AI project failure."

## 12. Visual

- **Explain-beat visual world** (pick ONE, never mix sketch and polished within the
  graphics themselves): brand-navy · sketch — alternating with real product-capture
  proof beats is the default archetype, not a violation of this (§4 rule 3)
- **Explain beats built as native Remotion components, not patched NotebookLM
  slides?** yes / no — if no, say why (§2.1)
- **Follows `DESIGN-SYSTEM.md`?** yes / no — if no, say why
- **Diagram inherits the layered-band structure?** yes / no
- **Capability names used verbatim from the taxonomy?** yes / no

## 13. Proof beats (skip only for a pure-explainer asset with no live capture at all)

- **Has someone confirmed the UI can actually show this?** ← the app-switcher lesson
- **Which real inputs / starter questions produce data?** `______`
- **Max two features.** Which two? `______`
- **Auth:** can it run gate-off locally? `______`
- **For each proof beat: what does a LATER action in this beat depend on that an
  earlier action (a domain/context switch, a data load) might not have settled yet?**
  Budget an explicit settle-wait, don't assume synchronous (§4 rule 15)

## 14. Narration

- **Voice:** `______` (male/female; multilingual neural voices carry better prosody)
- **Written for the ear?** no one-word sentences; commas/em-dashes inside a thought;
  numbers spelled as spoken; read aloud before generating
- **Unhedged and declarative?** caveats/scenarios go on an on-screen label if they
  must appear at all, never stacked into the voiceover line (§13.4)
- **Within word budget** (§1)? `______` words

---

## Definition of ready

- [ ] Single idea fits one sentence, and the BLUF passes the 3-line compression test
  (`GTM-ASSET-PLAYBOOK.md` §13.4)
- [ ] Opening figure **web-verified**, source + date recorded
- [ ] Claim boundaries written down
- [ ] Explain-beat visual world chosen, not mixing sketch/polished styles within it
  (alternating with proof beats is expected, not a violation)
- [ ] Proof-beat capability confirmed against the real UI, incl. settle-waits for any
  domain/context-dependent view
- [ ] Script within word budget
- [ ] **Storyboard reviewed and signed off before any code** ← the gate we skipped twice
