# Storyboard Template — the review gate

**Fill this in and get it signed off BEFORE writing any composition code.**

Both Ask-AI videos were built, reviewed, and then substantially rebuilt — once
because the script assumed a UI capability that didn't exist, once because the visuals
were "neither rough sketch nor polished design". A text storyboard costs minutes and
would have caught both. Code costs hours.

---

## Header

| | |
|---|---|
| Asset | `______` |
| Archetype | architecture / demo / feature-detail |
| Length target | `__`s · word budget `__` (seconds × 2.5) |
| Visual world | brand-navy / sketch / product capture — **one only** |
| Narrator | `______` |

## The beats

One row per beat. Keep narration in the row so length is visible as you write.

| # | Beat | On screen | Narration (verbatim) | Words | What the viewer should now understand |
|---|---|---|---|---|---|
| 1 | BLUF | | | | |
| 2 | reframe | | | | |
| 3 | contrast | | | | |
| 4 | mechanism | | | | |
| 5 | benefit | | | | |
| 6 | close/question | | | | |

**Total words:** `____` / budget `____`

## Checks before sign-off

**Narrative**
- [ ] Opens on a fact or tension, not a setup
- [ ] Exactly ONE concrete contrast — not a feature list
- [ ] There is a *visible mechanism* the viewer can see working
- [ ] Benefit stated as consequence, not adjective
- [ ] Closes on a question, not a CTA
- [ ] Product named 3–4×, functionally

**Truth**
- [ ] Every figure web-verified; source + date recorded (Rule 0)
- [ ] No forecast quoted for a period that has elapsed
- [ ] Claim boundaries respected — nothing implied that we can't defend
- [ ] Our own marketing metrics substantiated before reuse

**Feasibility (demo assets)**
- [ ] Someone has confirmed the UI can show each beat **in the real product**
- [ ] Named starter inputs that actually return data
- [ ] Two features maximum
- [ ] Auth path settled (gate-off local vs signed-in)

**For the ear**
- [ ] No one-word sentences
- [ ] Commas/em-dashes inside a thought; full stops only between thoughts
- [ ] Numbers spelled as spoken; screen carries the numeral
- [ ] Read aloud end-to-end without running out of breath
- [ ] Within word budget

**Visual**
- [ ] One visual world, not a hybrid
- [ ] Follows `DESIGN-SYSTEM.md` (or divergence is deliberate and recorded)
- [ ] Diagrams inherit the layered-band structure
- [ ] Capability names verbatim from the taxonomy
- [ ] No beat is just a headline with empty space beneath it
- [ ] The pivotal transformation *animates* rather than cutting

**Sign-off:** `______`  **Date:** `______`

---

## Why each check exists

| Check | The failure it prevents |
|---|---|
| UI can show each beat | Scripted an app-switcher that didn't exist; click-path rebuilt |
| One visual world | "Neither architect style nor UX designer — poorly drawn flowcharts" |
| Word budget | Both videos overran their target |
| Don't narrate the screen | 22s spent reading a list already displayed |
| Rule 0 | Recalled figure was ~2× off the verified one |
| No one-word sentences | Terminal pauses → flat, gappy delivery |
| No empty-space beats | Three versions shipped with content stranded in the top third |
