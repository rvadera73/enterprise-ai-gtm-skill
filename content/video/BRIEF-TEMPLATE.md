# Brief Template — the input that produces a GTM asset

Fill this in; it produces a video spec (`content/<id>.json`) or a one-pager layout.
Everything downstream is derived from it, so vagueness here shows up as a weak asset.

Read `GTM-ASSET-PLAYBOOK.md` first. Rule 0 (`VIDEO-ASSET-TEMPLATES.md`) is mandatory.

---

## 1. What is this?

- **Asset:** video (architecture / demo / feature-detail) · one-pager · post image
- **Product name, exactly as it must be said:** `______` (e.g. "Ask-AI MCP Service")
- **Length target:** `__` seconds → **word budget = seconds × 2.5** (≈150 wpm)
- **Where it will be published:** LinkedIn native · X · demo page · deck

## 2. Audience

- **Who:** `______` (e.g. enterprise CIOs, CTOs, architects)
- **What they already know about us:** `______` (assume nothing unless it's a series)
- **What they have NO context for:** customer names, case IDs, regulation numbers,
  internal job titles → these must not appear in narration or copy

## 3. The single idea

One sentence. If it takes two, the asset is trying to do too much.

> `______`

## 4. The opening (BLUF)

A fact or tension, not a setup.

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

- **Archetype's visual world** (pick ONE, never between): brand-navy · sketch · product capture
- **Follows `DESIGN-SYSTEM.md`?** yes / no — if no, say why
- **Diagram inherits the layered-band structure?** yes / no
- **Capability names used verbatim from the taxonomy?** yes / no

## 13. Demo-only (skip for architecture assets)

- **Has someone confirmed the UI can actually show this?** ← the app-switcher lesson
- **Which real inputs / starter questions produce data?** `______`
- **Max two features.** Which two? `______`
- **Auth:** can it run gate-off locally? `______`

## 14. Narration

- **Voice:** `______` (male/female; multilingual neural voices carry better prosody)
- **Written for the ear?** no one-word sentences; commas/em-dashes inside a thought;
  numbers spelled as spoken; read aloud before generating
- **Within word budget** (§1)? `______` words

---

## Definition of ready

- [ ] Single idea fits one sentence
- [ ] Opening figure **web-verified**, source + date recorded
- [ ] Claim boundaries written down
- [ ] Visual world chosen, not hybridised
- [ ] Demo capability confirmed against the real UI (demo assets)
- [ ] Script within word budget
- [ ] **Storyboard reviewed and signed off before any code** ← the gate we skipped twice
