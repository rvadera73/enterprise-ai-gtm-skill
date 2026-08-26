# GTM Asset Playbook — video & one-pager

What we learned building Ask-AI's first two videos (July 2026). Written as rules with
the evidence attached, so it can be argued with and iterated rather than obeyed.

Companions: `DESIGN-SYSTEM.md` (brand), `BRIEF-TEMPLATE.md` (input),
`STORYBOARD-TEMPLATE.md` (the gate), `VIDEO-ASSET-TEMPLATES.md` (scripts + Rule 0),
`DISTRIBUTION-PLAYBOOK.md` (publishing).

---

## 1. Pick the archetype first — they are not variations

| | **Architecture / explainer** | **Demo / proof** |
|---|---|---|
| Job | Make them *understand* the idea | Make them *believe* it works |
| Material | Drawn diagrams, no product | Real product capture |
| Opens on | The pattern or a verified figure | A verified figure |
| Failure mode | Feels theoretical | Feels like a feature tour |
| Length driver | Argument complexity | Available footage |

**They pair: argument, then proof.** The second opens with an explicit callback
("In the last video…"), which is what makes them a series rather than two assets.

A third archetype exists but is unbuilt: **feature detail** — deeper on one
capability, for a warmer audience.

## 2. The narrative spine (video AND one-pager)

1. **BLUF — a fact or tension, not a setup.** Video A opened on the problem; Video B
   opened on *"50%+ of GenAI projects abandoned after PoC."* The second is markedly
   stronger. Lead with something true and surprising.
2. **Name what isn't the answer.** *"Notice what isn't on that list. The model."*
   Reframing outperforms asserting.
3. **Explain with ONE concrete contrast**, never a feature list. "Same record,
   different person, different answer" carried more than any capability enumeration.
4. **Show the mechanism.** The generated SQL visible on screen proved NL→SQL better
   than any claim could. Find the equivalent "you can see it working" moment.
5. **Benefit as consequence, not adjective.** "Each application keeps its own logic
   and data" — not "seamless and scalable".
6. **Close on a question**, never a CTA. The demo link lives in the first comment.
7. **Name the product 3–4×, functionally.** "Ask-AI MCP Service writes the query,"
   never "Ask-AI MCP Service is a powerful platform." Plus a persistent brand rule so
   it is *present* without being *pitched*.

## 3. Rules that actually moved quality — ranked by observed impact

**1. One continuous narration take.** The single biggest lever. Generating each beat
separately and stitching them *is* what made v1 sound like someone reading slides —
every clip starts cold and ends flat. Nothing else came close.

**2. Derive visual timing from the audio.** Extract cue times from the narration's own
subtitle output and drive scenes off them. Sync becomes structural, not hand-tuned.

**3. Commit to ONE visual world.** The worst failure was the uncanny valley — neither
rough sketch nor polished design, described by the reviewer as "poorly drawn
flowcharts". Pick a world; irregularity then becomes the aesthetic, not a defect.

**4. Web-verify every figure (Rule 0).** A recalled Gartner number was ~2× off.

**5. Check what the UI can actually show before scripting.** A script assuming an
app-switcher that doesn't exist had to be rebuilt around what the demo really does.

**6. Don't narrate what's already on screen.** Reading a five-item list the slide
displayed burned 22 seconds of a 90-second budget.

**7. Domain-free narration.** Case IDs, regulation numbers and internal job titles
make a general pattern look like a niche tool. Say "someone in day-to-day operations".

**8. Hold stills; never slow-motion UI.** Slowed interface footage reads as broken.

**9. Two features maximum in a demo.** More than two and nothing lands.

## 4. Writing narration for the ear, not the page

Flat, gappy delivery is usually **punctuation, not the engine**. Every full stop
forces a terminal pause with falling pitch.

- ❌ *"Rarely because the model was wrong. Usually because of everything built around
  it. Cost. Governance. Unclear value."* — five stops, three of them fragments.
- ✅ *"Rarely because the model was wrong — usually because of everything built around
  it: cost, governance, unclear value."* — one breath, one arc.

Rules:
- **No one-word sentences.** Punchy in text, dead in audio.
- Prefer **commas, em-dashes and colons** inside a thought; full stops only between them.
- **Spell numbers as spoken** ("more than half", not "50%+"); let the *screen* carry
  the numeral.
- **~150 words per minute.** Budget the script: 90s ≈ 225 words. Both videos overran
  because nobody budgeted.
- Read it aloud before generating. If you run out of breath, so will the narrator.
- For finer control, use **SSML** via the edge-tts Python API (`<break>`,
  `<emphasis>`, `<prosody>`) — the CLI only exposes global rate/pitch/volume.

## 5. The gate we were missing

Both videos were rebuilt after being coded, because we jumped script → code with no
review in between. **Storyboard first** (`STORYBOARD-TEMPLATE.md`): beat, on-screen
content, narration line, and what the viewer should understand. Text only, reviewed
before any build. It would have caught the missing app-switcher and the sparse slides
at zero cost.

## 6. One-pager — same spine, static

Follow `DESIGN-SYSTEM.md` layered bands: header/BLUF → application layer → the service
→ connected data → governance → impact metrics. Same rules apply: verified figures,
bounded claims, benefit as consequence, ≤8 words per header.

The one-pager is also the **canonical source for diagram structure** — videos should
inherit it rather than invent new geometry.

## 7. Validate the render — an independent listener, not just your own ffmpeg checks

Run `tools/video-studio/descript_validate.py --video <final.mp4> --script <narration_timing.json>`
on every finished render, before calling it done. It uploads the real video to Descript
(API, Free tier — costs a few minutes of the 60/month free allowance, ~$0), gets an
independent transcript back, and diffs it word-for-word against the script that actually
generated the narration. This catches a class of bug nothing else in the pipeline can:
whether the TTS voice's pronunciation of something is genuinely *ambiguous to a listener*,
not just present in the audio. First real run caught exactly this — "RiskModelForgeIQ"
came back independently transcribed as "Risk Model 4 IQ" / "Risk Model For IQ" across two
separate passes, meaning that word doesn't reliably land, even though the audio itself
plays back fine mechanically (no clipping, no silence, no click). ffmpeg-based checks
(silence/click detection) verify the audio is *structurally* correct; this verifies it's
*understandable*. Run both — neither replaces the other.

Read the script's own docstring before touching the API by hand — it documents two real,
undocumented API quirks (the auth token format, and that a composition must be created in
the same call as the media upload or transcript export silently returns empty) found the
hard way, so you don't have to rediscover them.

## 8. Still open

- **No measurement loop.** We never learn which hook worked; distribution tracks leads
  but nothing feeds back into the next script.
- **Composition is code, not config** — a scene-type library would make the next
  video a brief rather than a build.
- **Videos don't yet match brand palette** (see DESIGN-SYSTEM divergence note).
- **Our own metrics unverified** — the one-pager's 60–80% / 40–60% / "100% secure"
  need substantiation before reuse.
