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
| Archetype | hybrid (if a live, demoable UI exists — see `GTM-ASSET-PLAYBOOK.md` §1) / explain-only (if no demoable UI exists) / feature-detail (narrower hybrid variant, for a warmer audience) |
| Length target | `__`s · word budget `__` (seconds × 2.5) |
| Explain-beat visual world | brand-navy / sketch — **one only, within explain beats** |
| Narrator | `______` |

## The beats

One row per beat. Keep narration in the row so length is visible as you write. Mark
each beat's **type** — explain (Remotion graphic) or proof (live capture) — per the
alternation pattern in `GTM-ASSET-PLAYBOOK.md` §1: open on an explain beat, then
alternate proof beats with short explain beats that name what was just shown.

| # | Beat | Type | On screen | Narration (verbatim) | Words | What the viewer should now understand |
|---|---|---|---|---|---|---|
| 1 | BLUF | explain | | | | |
| 2 | reframe | explain | | | | |
| 3 | contrast | explain | | | | |
| 4 | mechanism | proof | | | | |
| 5 | benefit | explain | | | | |
| 6 | close/question | explain | | | | |

**Total words:** `____` / budget `____`

## Checks before sign-off

**Narrative**
- [ ] Opens on a fact or tension, not a setup
- [ ] BLUF passes the 3-line compression test (`GTM-ASSET-PLAYBOOK.md` §13.4)
- [ ] Exactly ONE concrete contrast — not a feature list
- [ ] There is a *visible mechanism* the viewer can see working
- [ ] Benefit stated as consequence, not adjective
- [ ] Narration is unhedged and declarative — caveats/scenarios live on an on-screen
  label if they must appear at all, never stacked into the voiceover line itself
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
- [ ] Explain beats share one visual world (not a mix of sketch and polished styles
  within the graphics themselves — alternating explain/proof beat TYPES is the
  default archetype, not a violation of this, `GTM-ASSET-PLAYBOOK.md` §4 rule 3)
- [ ] Explain-beat graphics are native components (props/data-driven), not exported
  and hand-patched NotebookLM slide images (§2.1) — unless this is a pure explainer
  asset with no proof beats at all
- [ ] Follows `DESIGN-SYSTEM.md` (or divergence is deliberate and recorded)
- [ ] Diagrams inherit the layered-band structure
- [ ] Capability names verbatim from the taxonomy
- [ ] No beat is just a headline with empty space beneath it
- [ ] The pivotal transformation *animates* rather than cutting

**Sync (proof beats only)**
- [ ] Each proof beat's narration window is the recording target, not a guarantee —
  settle-waits for any dependent UI state change are budgeted in (§4 rule 15)
- [ ] Plan to verify each recording at a mid-window checkpoint, not just the final
  frame, before accepting its duration (§4 rule 14)

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
| BLUF compression test | A 60-slide answer was less credible than a 3-line one (CEO vs. CFO example) |
| Native component over patched slide | Two watermark-removal attempts + a wrong-field fix + an overclaim fix, all on ONE reused NotebookLM slide |
| Mid-window check, not just final frame | A recorded beat passed at its last frame while ~2/3 of its middle was stuck on a spinner |
