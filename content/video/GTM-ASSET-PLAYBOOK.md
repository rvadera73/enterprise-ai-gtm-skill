# GTM Asset Playbook — video & one-pager

What we learned building Ask-AI's first two videos (July 2026). Written as rules with
the evidence attached, so it can be argued with and iterated rather than obeyed.

Companions: `DESIGN-SYSTEM.md` (brand), `BRIEF-TEMPLATE.md` (input),
`STORYBOARD-TEMPLATE.md` (the gate), `VIDEO-ASSET-TEMPLATES.md` (scripts + Rule 0),
`DISTRIBUTION-PLAYBOOK.md` (publishing).

---

## 1. One hybrid archetype — not two videos, one video with two beat types

**Superseded 2026-08-14.** The original plan below shipped as two *separate* videos
(Video A argument, Video B proof) for Ask-AI, and worked. But building
RiskModelForgeIQ's Video 3 as one continuous hybrid — Remotion graphic beats
interleaved with real product capture inside a single ~3-minute cut — produced a
stronger, tighter asset than the two-video split, and the user's explicit retrospective
lesson was: **build this one type going forward, not two.** Treat the table below as
the two BEAT TYPES a single video alternates between, not two deliverables.

| | **Explain beat** | **Proof beat** |
|---|---|---|
| Job | Make them *understand* the idea | Make them *believe* it works |
| Material | Remotion graphic (native component, see §2.1) | Real product capture (Playwright, §9) |
| Opens on | The pattern or a verified figure | — (proof beats never open the video) |
| Failure mode | Feels theoretical | Feels like a feature tour |
| Length driver | Argument complexity | Real recorded/rendered duration (§13.2) |

**The spine is still argument → proof, just inside one script:** open on the BLUF
(explain beat), reframe what's assumed vs. true (explain beat), then alternate proof
beats (live capture of the actual mechanism) with short explain beats that name what
the viewer just saw. Video 3's beat sequence (`storyboard-video3-full-tour.md`,
`cbp-risk-engine`) is the reference implementation: 9 beats, 4 Remotion + 5 live,
75.3s of graphic runtime interleaved with ~115s of real capture, one continuous
narration take running underneath both.

**This retires the `STORYBOARD-TEMPLATE.md` / `BRIEF-TEMPLATE.md` "one visual world,
never hybridised" gate as originally worded** — that rule was written against a
different failure mode (rough programmatic sketches sitting next to polished CSS
*within the same graphic treatment*, reading as uncanny-valley). It still holds at
that grain: don't mix sketch-style and polished-style graphics in the same video.
It does NOT forbid alternating clean Remotion graphics with real product capture —
that alternation is now the default shape of the archetype itself. Both templates'
checklists are updated accordingly (§12 below still governs the graphic beats'
internal consistency).

**The gate — ask this first, every time, at brief time.** Does the subject actually
have a live, demoable UI that can be screen-captured? **If yes,** use the hybrid
archetype below (Remotion explain beats + Playwright live-capture proof beats, per
Video 3's reference implementation
`cbp-risk-engine/docs/gtm/03-video/storyboard-video3-full-tour.md`). **If no,** use
the **explain-only archetype**: Remotion/NotebookLM-sourced graphics only, narrated,
no live-capture beats and no Playwright pipeline at all — the same narration/BLUF/
accuracy rules as §2-§8 still apply, just without proof beats. This gate is the
correction to an earlier, wrong version of this rule that treated the hybrid
archetype as unconditional; it was written against one product (RiskModelForgeIQ)
that happens to have a demoable UI, and does not generalize to a subject that
doesn't. The table and reference below are the answer to **"yes"** — not the only
answer.

A narrower **feature-detail** variant remains available for a warmer, already-sold
audience (deeper on one capability, shorter runtime) — same hybrid rules apply, just
with a smaller beat count.

## 2. Sourcing raw material from NotebookLM — for any marketing or demo video

### 2.1 Default graphic-beat source: native Remotion component, not a patched NotebookLM slide

**Changed 2026-08-14, after Video 3.** Video 3's explain beats used two different
sourcing paths side by side, and the difference in downstream cost was stark:

- Beats reusing hand-exported NotebookLM slides needed: watermark removal (twice —
  the first attempt dragged in a red-glow artifact and had to be redone), a wrong
  CBP/CMS field-name fix, and an overclaiming column-header fix. All caught late,
  all manual, all per-slide.
- The one beat built as a native Remotion component from scratch
  (`PrecisionReveal` in `VideoC_Panel.jsx` — staged fade-in of a data-driven claim,
  built from theme tokens) needed none of that. No watermark to strip because
  nothing was exported from an external tool; no overclaim to catch because the
  copy was typed against the brief directly, not inherited from a source document
  that had its own agenda.

**New default for the hybrid archetype:** build explain beats as native Remotion
components with data passed as props (numbers, labels, claim text), not as images
sourced from NotebookLM and hand-patched. Reserve NotebookLM for what §2 already says
it's good for — tone/pacing/structure reference (the Chat-panel outline pass, the
Audio Overview transcript) — never as an image source for the hybrid archetype. If a
NotebookLM slide's layout genuinely earns reuse, redraw its structure in Remotion
rather than exporting and patching the PNG; the patching cost (watermark + overclaim
+ off-brand-color risk, §4 rules 4/14) recurs on every slide, every time, while a
component is written once and is correct by construction.

This does not apply to a pure architecture/explainer asset with no live capture at
all (still rare, and not what the hybrid default covers) — if one is ever built,
§2's original NotebookLM-slide-reuse guidance still applies there unchanged.

Once the archetype is picked (§1), NotebookLM (Google's document-to-podcast/deck tool)
is a genuinely useful SOURCE OF RAW MATERIAL — never the finished asset. First proven
on RiskModelForgeIQ Video A (§11 has the full worked example and production lessons);
generalized here so every future video starts from this, not from re-deriving it.

### What it's for, by archetype — this is the part that doesn't generalize blindly
- **Architecture/explainer**: use BOTH outputs. The Video Overview's slide deck
  becomes the video's actual visuals (after cleanup, step 4 below) — its diagrams are
  real presentation-quality assets, consistently better than hand-coded CSS/SVG or
  AI-image-generator output tried as alternatives. The Audio Overview's narration
  transcript becomes the basis for the script — its tone and pacing consistently beat
  scripts written from a blank page.
- **Demo/proof**: Audio Overview ONLY, as a narration-tone and argument-structure
  reference for the script — **never the Video Overview or deck.** §1's rule holds
  here without exception: a demo's job is to make the viewer believe the product
  works, which requires real product capture (§9's Playwright pipeline); a
  NotebookLM-generated slide can't substitute for that without producing exactly the
  "feels theoretical" failure mode §1 already warns about. Treat the Audio Overview
  transcript the same way §9/§10 treat narration — as tone/pacing reference, spliced
  against real capture, not against synthesized visuals.
- **Feature-detail** (the unbuilt third archetype): same treatment as demo/proof —
  narration reference only — since it's still built on real capture, just narrower.

### There is no API for this — it's a manual-but-scripted step, every time
Checked directly (2026-07-28): neither the free consumer NotebookLM
(`notebook.google.com/notebook/<id>`) nor the paid "Gemini Notebook Enterprise" API
gives programmatic control here. The Enterprise API is real and GA, but it's a
separate licensed GCP product, can't upload sources or generate Video Overviews at
all, and its only customization fields are `sourceIds`, `episodeFocus` (plain-text
topic string), and `languageCode` — no tone/length/style/font parameter exists in
either product tier. Stay manual, but make the manual step a fast, scripted checklist
rather than freehand improvising in the UI each time, and automate everything
downstream (already the case).

The consumer UI's real customization fields, verified current as of this session:
- **Video Overview**: **Format** (Explainer / Brief), **Visual style** — 16 presets
  (Classic, Whiteboard, Watercolor, Retro Print, Heritage, Paper-craft, Kawaii, Anime,
  Sketch Note, Professional, Scientific, Clay, Editorial, Instructional, Bento Grid,
  Bricks) or **Custom** with a free-text style description, plus a **Focus** field
  ("what should the AI host focus on").
- **Audio Overview**: a tone/focus customization instruction field (freeform text).

### The checklist — run this for every video, either archetype
0. **Positioning brief** (before touching NotebookLM). One page: product name +
   tagline verbatim, the single BLUF claim to open on, 3-5 terms that must repeat, a
   **do-not-claim list** (pulled from the product's own "not yet implemented"
   ADRs/roadmap docs), and the target final runtime.
1. **Curate the source bundle.** Upload only accuracy-safe sources: PRD, architecture
   docs, ADRs (with status fields), the brief itself. If a source overclaims a roadmap
   item as shipped, fix that doc first or exclude it — NotebookLM faithfully amplifies
   whatever it's given.
1.5. **Ask for alternative slide structures BEFORE generating the Video Overview** —
   use NotebookLM's **Chat** panel (a free-text question against the uploaded sources),
   not a full Video Overview generation. This is a cheap outline/brainstorm pass,
   same spirit as §6's "storyboard first" gate, and it's much faster to iterate on a
   text outline than to regenerate a full video 2-3 times to compare structures. See
   the prompt shape below. Pick one structure, THEN move to step 2.
2. **Generate with a steering prompt, not defaults** — in the Video Overview's Focus
   field (explainer only), now referencing the chosen structure from step 1.5, and the
   Audio Overview's tone field (always). See the prompt shape below. Don't accept the
   first unguided pass; regenerate with a tightened Focus string rather than
   proceeding and fixing it in post.
3. **Export + flatten.** Slide deck → PDF → PNG per slide (150dpi, PyMuPDF/pdf2image).
   Audio/Video Overview → download the audio → transcribe once with Whisper for a
   CONTENT/TONE reference only (never trust its literal text for brand-name spelling —
   it mangles product names; cross-check spelling against the PRD instead).
4. **Clean every slide mechanically** (architecture/explainer only — demo videos skip
   this entirely, see above). Run `tools/video-studio/scripts/clean_notebooklm_slides.py`
   over the exported PNGs — auto-detects and removes the NotebookLM watermark.
5. **Accuracy pass — mandatory regardless of archetype.** For every slide (explainer)
   or script beat (either archetype), grep the product's own ADRs/design docs for "not
   yet implemented" / "accepted, not shipped" language; strip or soften anything that
   fails, on BOTH the script and any reused slide image.
6. **Write the final script from the transcript + the brief — never from a blank
   page, never verbatim.** Compress/restructure for the target runtime, insert the
   mandated product-name repetitions, remove metrics-first framing, keep the source's
   tone and confidence.
7. **Map scenes/beats to assets up front** — a table of scene key → visual (a specific
   cleaned slide file for explainer; a specific capture step for demo) → narration
   lines — before writing any composition or automation code. Deciding this
   mid-iteration cost real time on Video A.
8. **Voice + timing.** edge-tts (or a cloned voice) per line → ffmpeg
   normalize/concat/loudnorm → compute scene/caption timing arithmetically from known
   clip durations. Never re-derive timing via Whisper — it mangles brand names in the
   transcript it produces.
9. **Composition.** Explainer archetype reuses the `SlideImage`
   Ken-Burns-over-real-slide Remotion component (`VideoA_Panel.jsx`) rather than
   hand-coding new CSS diagrams. Demo archetype uses the Playwright capture pipeline
   (§9) — no Remotion needed unless hybridizing with a drawn intro/outro (§10).
10. **Render + verify.** Render, pull stills (explainer) or frames (demo) at several
    timestamps, read them back and check each against its narration line for
    disagreement — this is the step that caught real accuracy bugs on Video A. Do this
    BEFORE declaring done, not after a user catches it.
11. **Deliver.** Copy to Downloads via WSL, then re-verify the file exists via a native
    PowerShell `Get-ChildItem` after a short sleep — a WSL-side copy has silently
    failed to persist before despite `ls -la` succeeding on the WSL side.

### Prompt shape — fill in per product (§11 has a fully worked RiskModelForgeIQ example)

**Chat panel — alternative slide structures (step 1.5, ask this BEFORE generating):**
> Based on the uploaded sources, propose 3 alternative slide-by-slide structures for
> a [N]-second video about [TOPIC]. For each option, give: (1) slide count and a
> one-line description of what each slide shows, (2) the single idea that option
> leads with, (3) the tradeoff versus the other two options (e.g. more before/after
> contrast vs. more mechanism detail vs. more proof-point emphasis). Do not generate
> the video yet — this is an outline review only. Flag any slide in any option that
> would require describing [ROADMAP ITEM / DO-NOT-CLAIM ITEM] and note that as a risk
> specific to that option.

**Video Overview Focus field** (explainer archetype):
> Open directly on [PRODUCT]'s core claim: [BLUF]. Do not open on generic industry
> framing — name the product in the first slide. Mention [PRODUCT] and "[TAGLINE]" by
> name on at least 4 slides. Treat [KEY METRIC] as supporting evidence, not a
> headline. Do not describe [ROADMAP ITEM] as a current capability — label it
> explicitly as roadmap/future if shown at all. Close on an invitation to try the
> product, not a summary slide.

**Audio Overview tone field** (both archetypes):
> Same constraints as above. Confident and conversational, not a dry corporate read.
> Target roughly [N] minutes; if you can't hit that, prioritize [MUST-KEEP BEATS] over
> [WHAT CAN BE CUT] so compression afterward is straightforward.

NotebookLM has no reliable hard runtime control today — budget a manual compression
pass regardless of what length is requested.

### One-pager content — also feasible, with a real caveat: copy only, not the design

NotebookLM's **Reports** feature (confirmed current, March 2026 update) can draft the
one-pager's COPY: it has a **Custom** format option where you set Objective, Audience,
and Tone and describe the structure you want, plus suggested formats (Briefing Doc,
Technical White Paper, Explanatory Article, Concept Overview) it'll adapt on request.
**It cannot produce the finished visual one-pager** — Reports render as a plain text/
doc output, not a laid-out graphic with `DESIGN-SYSTEM.md`'s bands, brand colors, or
typography. Treat it exactly like the Audio Overview: raw copy to compress and edit
into the real template, never pasted in as the finished asset.

**Reports → Custom prompt, filled in per product:**
> Objective: draft the copy for a one-page sales one-pager for [PRODUCT], structured
> in exactly these six bands, one short block each: (1) header/BLUF — the single
> claim, ≤8 words; (2) the application layer — who's using it and for what; (3) the
> service — what [PRODUCT] actually does; (4) connected data — what it reads/writes
> and where; (5) governance — the defensibility/audit story; (6) impact — verified
> figures only, no unsubstantiated stats. Audience: a technical buyer evaluating
> [CATEGORY] tools. Tone: confident, concrete, no adjectives doing the work a fact
> should do. Do not describe [ROADMAP ITEM] as shipped — label it explicitly as
> roadmap if mentioned at all. Keep every section to bullet-length copy, not
> paragraphs — this is a page, not a memo.

Then build the actual one-pager from that copy against `DESIGN-SYSTEM.md`'s spec (§7)
— the same accuracy pass from step 5 above still applies to whatever NotebookLM
drafts, since it will amplify an unverified figure exactly as readily in a report as
in a script.

## 3. The narrative spine (video AND one-pager)

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

## 4. Rules that actually moved quality — ranked by observed impact

**1. One continuous narration take.** The single biggest lever. Generating each beat
separately and stitching them *is* what made v1 sound like someone reading slides —
every clip starts cold and ends flat. Nothing else came close.

**2. Derive visual timing from the audio.** Extract cue times from the narration's own
subtitle output and drive scenes off them. Sync becomes structural, not hand-tuned.

**3. Commit to ONE visual world — within each graphic beat.** The worst failure was
the uncanny valley — neither rough sketch nor polished design, described by the
reviewer as "poorly drawn flowcharts". Pick a world; irregularity then becomes the
aesthetic, not a defect. This governs a graphic beat's own internal style consistency,
not whether graphic beats may alternate with real product capture — §1's hybrid
archetype does exactly that by design, and is a different axis from this rule.

**4. Web-verify every figure (Rule 0).** A recalled Gartner number was ~2× off.

**5. Check what the UI can actually show before scripting.** A script assuming an
app-switcher that doesn't exist had to be rebuilt around what the demo really does.

**6. Don't narrate what's already on screen.** Reading a five-item list the slide
displayed burned 22 seconds of a 90-second budget.

**7. Domain-free narration.** Case IDs, regulation numbers and internal job titles
make a general pattern look like a niche tool. Say "someone in day-to-day operations".

**8. Hold stills; never slow-motion UI.** Slowed interface footage reads as broken.

**9. Two features maximum in a demo.** More than two and nothing lands.

**10. Match the canvas aspect ratio to the source material's aspect ratio — pick
the format from the content, not a habit.** RiskModelForgeIQ Video 2 forced ~1.79:1
deck slides into a 1080x1080 square canvas, producing large dead-space bars above
and below every slide. Verified against real production guidance: 16:9 is the
recommended format specifically for slide/presentation-led content, because it
preserves layout and readability — this isn't a style preference, it's the correct
default for this content type. Before picking a canvas size, size the content area so
its own aspect ratio nearly matches the source material's (compute it — don't
eyeball it); a few px of residual pillar/letterbox is invisible, tens of px reads as
a defect. Square/vertical formats are still right for other content (talking-head,
UI capture) — the format follows what's actually being shown, every time.

**11. A recurring brand mark is a quiet footer, not a floating header.** Real
presentation templates put a recurring logo/tagline in the footer or a corner, sized
to recede into the background on content slides — never a large floating element
disconnected from the content frame with its own dead space around it. Only a title
or closing moment earns a bigger, more prominent brand treatment. Build this into the
shared frame/panel component itself so every scene gets it for free, rather than
per-scene brand code.

**12. Caption/subtitle overlays need a full-width, opaque bar — not a pill sized to
the text.** A pill narrower than the full frame lets whatever's behind it (real slide
content, in a video with a real background) peek out at the edges once a mismatch
occurs, reading as a glitch or a cut-off sentence rather than a deliberate overlay.
The standard broadcast/subtitle-bar convention — full width, fully opaque, fixed
position — always fully occludes whatever's behind it, so it reads as intentional
regardless of what the underlying content happens to be. Re-run frame-sample QA
across ALL scenes after any layout change, not a handful — this exact bug was only
caught because a fuller pass followed a narrower one that missed it.

**13. Verify a font is actually loading before claiming it in the font stack.** Naming
a typeface (e.g. "Inter") first in a CSS font stack without loading it anywhere
silently falls back to system sans — the claim becomes false without any visible
error. If matching a real brand asset's typography, vendor the actual font file and
add a real `@font-face`, then confirm the render actually uses it.

**14. Verify a recorded/rendered segment at a MID-window checkpoint, not just the
final frame.** Video 3's Beat 5 and Beat 7 both passed a final-frame check (page had
finished loading by the last frame) while still failing in the middle — the settled,
usable portion of the window was only 4.2s of 15.0s and 5.9s of 17.0s. A final-frame
check only proves the segment *ends* in a good state; it says nothing about how much
of the window is actually usable. Check a frame at roughly the midpoint of every
recorded/rendered segment before accepting its duration as correct — this is what
caught both real shortfalls, and a final-frame-only check missed them twice.

**15. Any UI action that changes what a LATER action depends on needs an explicit
settle-wait longer than the app's own async resolution — don't assume synchronous.**
A real bug class, not specific to one app: switching a domain/context selector and
immediately clicking a dependent tab raced the parent's own data resolution, leaving
a child view stuck on a loading spinner indefinitely. The fix was a flat post-switch
wait (2000ms) before the next interaction — cheap, but only after the race was found
by inspecting a hung recording, not by design. Treat any selector/dropdown/context
switch in a recording script as a suspect boundary and verify settle time empirically
before trusting a hold-and-hope duration.

**16. Absorb real-world recording overshoot as inserted silence in the audio track,
not by re-timing the visuals to fit a fixed script.** When a live-capture beat needs
more real time than its narration window (page load, settle-waits), extend that
beat's window and insert matching silence into the already-generated narration WAV
at the corresponding splice point, shifting every later timestamp by the same amount.
Two gotchas from doing this twice in sequence on Video 3: (a) a second insertion's
splice point must be computed against the ALREADY-shifted position from the first
insertion, not the original pre-shift value, or the boundary is off by the first
insertion's length; (b) track a running total against whatever slack budget was
pre-approved (Video 3 used 13.4s of a 30s pool) so extensions stay inside it instead
of silently compounding.

**17. Run a stitch-plan verification pass before assembling the final cut, not after.**
A 3.78s audio/video mismatch on Video 3's first assembly was initially misdiagnosed
as an ffmpeg seek-accuracy bug (real, and worth fixing — `-ss` belongs after `-i` for
frame-accurate trims) but the actual cause was a stale file: the stitch script was
reading an old, broken recording from one temp path while the corrected version had
been saved to a different one. `tools/video-studio/scripts/verify_stitch_plan.py`
(added 2026-08-14) checks every segment's probed duration against its planned target
before any concatenation happens, and flags exactly this class of stale-input bug
mechanically instead of after a failed assembly.

**18. Never invent a product's accent color from a metaphor — verify it against the
real, current brand asset, and check the doc's word isn't stale.** RiskModelForgeIQ's
video used an invented "molten copper" accent (from the product name's "Forge"),
never checked against either the product's real one-pager or the portfolio's design-
system doc. Worse: the design-system doc itself turned out to be stale (documented an
earlier version of Ask-AI's one-pager that no longer matched what's shipped) — caught
only by reading the actual current one-pager HTML/PNG directly, not trusting the
doc's word. Before choosing any brand color: (a) read the product's own real, current
one-pager/marketing asset directly if one exists, (b) cross-check the portfolio
design-system doc against that same real asset rather than assuming the doc is
current, (c) fix the doc immediately if it's stale, so the next product doesn't
repeat the same ad hoc pick.

## 5. Writing narration for the ear, not the page

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

## 6. The gate we were missing

Both videos were rebuilt after being coded, because we jumped script → code with no
review in between. **Storyboard first** (`STORYBOARD-TEMPLATE.md`): beat, on-screen
content, narration line, and what the viewer should understand. Text only, reviewed
before any build. It would have caught the missing app-switcher and the sparse slides
at zero cost.

## 7. One-pager — same spine, static

Follow `DESIGN-SYSTEM.md` layered bands: header/BLUF → application layer → the service
→ connected data → governance → impact metrics. Same rules apply: verified figures,
bounded claims, benefit as consequence, ≤8 words per header.

The one-pager is also the **canonical source for diagram structure** — videos should
inherit it rather than invent new geometry.

NotebookLM can draft the six bands' COPY via its Reports/Custom feature — see §2's
one-pager subsection for the exact prompt. It cannot produce the finished visual;
build that from the drafted copy against this section's spec, same accuracy pass as
everything else NotebookLM touches.

## 8. Still open

- **No measurement loop.** We never learn which hook worked; distribution tracks leads
  but nothing feeds back into the next script.
- **Composition is code, not config** — a scene-type library would make the next
  video a brief rather than a build.
- **Videos don't yet match brand palette** (see DESIGN-SYSTEM divergence note).
- **Our own metrics unverified** — the one-pager's 60–80% / 40–60% / "100% secure"
  need substantiation before reuse.

## 9. Addendum — longer-form "product capture" demos, no Remotion (IACP, 2026-07-21)

Second worked example, a different archetype from Ask-AI's: two 2–2.5 min
**feature-detail** demos (not 90s proof reels), **100% real screen capture** — no
hand-drawn intro/outro, so no Remotion needed at all. Full write-up:
`IACP-2.1/docs/gtm/03-video/LESSONS-LEARNED.md`. What's new here, not already covered
above:

1. **When the archetype is pure product capture, skip Remotion entirely.**
   `edge-tts` (free, local, no key) + `ffmpeg-static` is the whole pipeline: generate
   narration → drive a Playwright recording off the narration's own cue timestamps →
   pad the canvas with a caption bar → burn in rolling captions → mux audio. Remotion
   only earns its keep when part of the video is hand-drawn (Ask-AI's hybrid).

2. **Record timeline-first, not hold-and-hope.** Generate the narration audio BEFORE
   finalizing the recording script, extract its cue timestamps, and drive the
   automation off an elapsed-time `waitUntil(cueEndSeconds)` clock. A first-draft
   recording built on guessed `hold(ms)` pauses came out at roughly half the actual
   narration length.

3. **Burn captions into a bar below the capture, in short rolling phrases — not
   full sentences overlaid on the product.** Full-sentence cues sit on screen for
   15-20s and cover the UI; both are wrong for a product demo. `edge-tts`'s CLI only
   emits one cue per sentence — use its Python API directly and interpolate per-word
   timing across each sentence's real duration (this version has no true
   `WordBoundary` events) to build ~5-word rolling cues instead.

4. **The "pivot to real-data proof" move.** If a live interaction won't reliably
   complete after genuine diagnostic effort (screenshots, DOM inspection, not just
   selector guessing), don't keep patching — rebuild that beat to prove the same
   capability against real, already-existing data instead of a live transaction. Make
   this a standing option from early on, not a last resort after a huge time sink.

5. **Screenshot the second a selector misbehaves, not the fifth attempt.** Text-only
   `innerText()` dumps flatten native `<select>` options into plain text
   indistinguishable from real clickable rows — this cost the most debugging time in
   the whole session. A screenshot + `elementFromPoint()` check resolves DOM ambiguity
   that repeated selector guessing can't.

## 10. Addendum — Video B v2, cloned voice + Remotion hybrid (Ask-AI, 2026-07-27)

Second pass at Video B: real cloned narration (OpenVoice V2 + MeloTTS, see
`~/tools/OpenVoice/`) over the same hybrid Remotion composite (hand-drawn intro/outro +
real capture) as v1. User feedback on the result, plus one new bug class this surfaced:

1. **`recordVideo` + an app's own `scrollIntoView({behavior:'smooth'})` is a silent
   trap — scroll to the CONTENT, never to a peripheral anchor.** A real backend answer
   rendered correctly in the DOM every time (confirmed via `page.evaluate()` reading
   `body.innerText`), yet was invisible in the actual recording. Root cause, found via
   `getBoundingClientRect()` logging: the recording script's own "fix" scrolled to the
   *input box* (bottom of a scrollable panel) to guarantee it was reachable — for a
   short answer, that scrolls the page almost to max scrollY, pushing the Q&A pair
   ~24px above the fold. The app's own animated `smooth` scroll made this worse under
   `recordVideo`'s extra CPU load (multiple scroll calls in quick succession settling
   mid-animation). Fix: after confirming an answer exists, scroll directly to an answer
   marker with `el.scrollIntoView({ block: 'center', behavior: 'instant' })` — never
   assume "scroll the input into view" also reveals content sitting above it in a tall
   panel. Diagnose this class of bug with `page.evaluate()` geometry (`scrollY`,
   `getBoundingClientRect()`), not repeated screenshot guessing — screenshots proved
   *that* it was invisible, only geometry proved *why*.
2. **Background reads as generic.** Flat pale cream + a barely-visible dot-grid is too
   plain for a "professional" bar. Next time: a slow, subtle animated gradient mesh
   (pure CSS/canvas, no external asset, zero licensing risk) reads more premium than a
   flat fill without competing with foreground content.
3. **Programmatic rough.js figures read as crude at full-screen scrutiny**, even
   though they're fine as small inline sketch accents. For next time, evaluate two
   alternatives rather than hand-tuning more `SkFigure` seeds: (a) Excalidraw/
   Excalimate-authored diagrams (hand-drawn look, designed once in the Excalidraw UI,
   exported and animated — not procedurally generated per-frame), or (b) a curated
   open-license illustration set (unDraw, Storyset — MIT/permissive) for any figure
   that isn't literally the product UI. Reserve rough.js for small sketch accents
   (underlines, arrows, frame highlights) where its texture is a feature, not the main
   illustration.
4. **Pacing ran fast.** Both the narration speaking rate and the visual beat timing
   (derived from narration cues) need to slow ~15-20% next time. Since scene timing is
   whisper-cue-derived, the single lever that moves both together is MeloTTS's own
   synthesis `speed` parameter (default ~1.0) — try ~0.82-0.85 at generation time rather
   than post-hoc slowing the video (which would desync lip-less-but-still-cued visuals)
   or padding hold times manually scene-by-scene.
5. **The "caption band" in `VideoB.jsx` is NOT a subtitle track** — it's a handful of
   scene-headline strings (`'Day-to-day operations' / 'What do I have to act on?'`)
   keyed to narration scene boundaries, not a word-synced transcript. This reads fine
   as a design accent but doesn't satisfy an actual captions/accessibility expectation.
   We already extract word-level timestamps via Whisper (`extract_timing.py`,
   `word_timestamps=True`) for cue markers — the same data supports real rolling
   captions; reuse the IACP pattern (§9.3 above: short ~5-word rolling phrases in a
   dedicated bar, not full sentences) rather than treating scene headlines as captions.
6. **Voice-clone fidelity was the weakest link — OpenVoice V2 didn't read as the
   user's own voice.** Researched 2026 comparisons: OpenVoice is tuned for fast
   zero-shot tone/style conversion, not maximum speaker-identity fidelity. RVC
   (Retrieval-based Voice Conversion) is the stronger pick specifically for "sounds
   like *this* person" — needs only ~1-5 minutes of clean reference audio (we already
   have that) and is reported to rival paid services on voice-match accuracy, at the
   cost of a heavier local setup (real-time capable, GPU-friendlier) than OpenVoice's
   simpler pipeline. Recommend trying RVC for the RiskModelForgeIQ video before
   accepting cloned-voice quality as "good enough."
7. **"OpenMonet" is not a real, findable tool** (checked directly — no such project
   surfaces in 2026 tooling searches). Likely a mishearing/mixup of OpenVoice, which
   we already evaluated and found wanting on fidelity (see #6). Treat RVC as the actual
   next candidate rather than continuing to search for "OpenMonet" by that name.

## 11. Addendum — RiskModelForgeIQ Video A, NotebookLM proof-of-concept (2026-07-28)

First production to use NotebookLM-generated assets (a slide-deck "Overview" PDF and a
spoken "Audio Overview" video) as source material, and the first two-voice panel
(interviewer "Emma" + cloned "architect" voice). Took 7 script/visual iterations to
close — the generalized process this run produced now lives in **§2** as the standing
rule for every future video; this addendum keeps the production-specific lessons and
the fully worked RiskModelForgeIQ prompt example.

### What NotebookLM got right — the basis for §2's archetype split
- **Visual polish.** The PDF deck's slides (isometric architecture diagrams, JSON
  schema cards, version timelines) are real presentation-quality assets — better than
  anything hand-coded in CSS/SVG this round, and better than AI-image-generator output
  we also tried. Reusing the ACTUAL slide images (after cleanup) beat rebuilding them.
- **Narration tone and confidence.** The Audio Overview's spoken narration had genuine
  marketing energy and pacing our first several from-scratch script drafts lacked.
  Compressing ITS actual transcript — not rewriting from a blank page — is what
  finally produced a script with real excitement per the user's own read.

### What NotebookLM got wrong — why §2's checklist has an accuracy-pass step
1. **Generic industry framing as the opening hook, not the product.** Both the deck
   and the video opened on category-level scene-setting instead of the product name or
   its core claim.
2. **Thin, inconsistent product-name repetition.** Needs an explicit minimum-repetition
   instruction — NotebookLM won't self-impose this.
3. **Metrics-first instinct.** NotebookLM defaults to leading with a stat slide (e.g.
   "0.995 correlation") as if the number were the pitch. When the actual positioning is
   the architecture/platform, say so explicitly or it keeps proposing stat-forward
   slides as the headline.
4. **Overclaims capabilities that aren't shipped yet.** The deck asserted a
   "Multi-Model Arbitration" mechanism as live when the repo's own ADR
   (`cbp-risk-engine/docs/design/adr/0002-...md`) labels it "Accepted, not yet
   implemented." NotebookLM synthesizes confidently from whatever source material it's
   given — if the uploaded sources themselves overclaim (product docs describing
   roadmap items as current), it repeats and amplifies the overclaim as fact. Fix this
   BEFORE upload (scrub or flag roadmap language in the source bundle), not after —
   catching it after the fact cost two separate rounds of image surgery this session
   (once on the script's own visual, once again on a reused deck slide's JSON field
   that had the identical overclaim baked in).
5. **Length mismatch, no reliable control.** An 8-minute Audio Overview had to be
   manually compressed to ~2:30. NotebookLM has no dependable hard-length setting —
   budget a compression pass into the plan rather than expecting the requested runtime.
6. **Its own watermark on every exported slide.** Needs mechanical removal before
   reuse — see tooling below.

### Lessons that generalize beyond NotebookLM specifically
- **Verify every claim against the product's own source of truth (ADRs / design docs /
  test-results) before it lands in a script OR stays on a reused slide.** This caught
  the OR-gate arbitration overclaim in the script draft, and — independently — the
  *same* overclaim resurfacing on a reused deck slide's JSON schema field
  (`model_score_challenger` sitting beside `requires_human_review`, implying the
  shadow/challenger model already drives live decisions). Make this a mandatory
  pipeline step, not a one-off catch.
- **Cross-check every scene against its paired visual once assembled, not just each in
  isolation.** A script line and a slide image can each be individually accurate and
  still disagree once put together — the challenger-model JSON field spoiling a later
  scene's reveal is the concrete example.
- **Ad hoc, coordinate-guessed image edits are slow and error-prone.** Two botched
  attempts on the shadow slide and one on the evidence slide before getting them right,
  all from hand-measuring pixel boxes off a scaled screenshot. Replaced with a reusable
  script (below) that auto-detects the watermark region and picks its fill strategy
  from the surrounding pixels instead of guessing coordinates by eye every time.

### Worked example — RiskModelForgeIQ, technical-architecture follow-up video

Use this directly for the next video rather than re-deriving it from §2's placeholders:

**Video Overview Focus field:**
> Open directly on RiskModelForgeIQ's architecture claim: a shared Decision
> Intelligence Layer, not a single model. Do not open on generic industry framing —
> name the product in the first slide. Structure around the three-pillar architecture
> (Rules Engine / Probabilistic Risk Model / Governance Layer) as the spine, going one
> level deeper into each pillar than the first video did. Say "RiskModelForgeIQ" and
> "Decision Intelligence Layer" by name on at least 4 slides. Do not describe
> multi-model arbitration or disagreement-triggered referral as a current capability —
> it is accepted design, not yet implemented; if shown, label it explicitly as
> roadmap. Treat any correlation/accuracy figures as supporting evidence, not a
> headline. Close on an invitation to try the product, not a summary slide.

**Audio Overview tone field:**
> Same constraints as above. Confident, conversational, technical-but-not-dry —
> explain the architecture like a founder walking an engineer through the design, not
> reading a spec. Target roughly 3 minutes; if you can't hit that, prioritize the
> three-pillar breakdown and the versioning/rollback story over any one specific
> numeric example.

**Visual style**: try **Custom** with `dark graphite background, molten-copper and
steel-blue accents, isometric technical diagrams, monospace labels for code/JSON` to
match the existing `theme-riskforge.js` palette already built for this product line —
if the output doesn't match well, fall back to the **Professional** preset and let the
Remotion composition's own dark-forge theme carry brand consistency instead.

### Tooling update

Added `tools/video-studio/scripts/clean_notebooklm_slides.py`: auto-detects the
NotebookLM watermark's bounding box in the bottom-right corner of an exported slide PNG
instead of hand-measuring pixel coordinates per slide (which produced two visibly
botched edits this round before getting them right), and adapts its fill strategy —
solid-color fill when the surrounding region is flat, blur-and-stretch when it's
textured/decorative. Usage: `python clean_notebooklm_slides.py <input_dir>
<output_dir>`. Does not attempt automated overclaim detection (OCR-based content
review is a bigger, separately-scoped tool) — §2 step 5 (grep the ADRs by hand)
remains the accuracy gate.

## 12. Addendum — RiskModelForgeIQ Video 2, editorial-quality pass (2026-07-31)

Video 2 (Policy & Decision Intelligence Framework) shipped with accurate content on
the first pass, but took 6 further iterations on editorial quality alone before it
read as coming from "a quality video publishing shop" (user's words) rather than a
correct-but-rough first cut. §4 rules 10-13 and 18 above are the durable, generalized
version of what follows — this section is the specific story and evidence.

**What went wrong, in the order it surfaced:**
1. Narration accuracy: the TTS silently mispronounced "2.8% to 15.2%" as "Two, eight
   percent to 15. Two percent" (decimal "point" dropped) — caught by transcribing the
   *actual delivered audio* with Whisper, not by re-reading the input script (which
   looked correct). **Lesson: verify narration by transcribing the output, not by
   proofreading the input text — TTS can silently mispronounce numbers.**
2. Brand bar: too small/low-contrast to read as branding, floating above the content
   panel with dead space between them — looked disconnected rather than designed.
3. Root layout defect: ~1.79:1 deck slides forced into a 1080x1080 square canvas
   produced large dead-space bars above/below every slide. First fix attempt (bigger
   footer text) was correctly rejected by the user as a band-aid on the wrong problem
   — the real fix was the canvas/aspect-ratio mismatch itself (§4 rule 10).
4. Ad hoc color: the "molten copper" accent was invented from the product name's
   "Forge" metaphor and never checked against the product's real one-pager or the
   portfolio design-system doc — which itself turned out to be stale (§4 rule 18).
5. A fix introduced a new bug: switching to 16:9 fixed the dead space, but the first
   attempt's caption pill let real slide content peek out from behind it on a slide
   whose content ran close to the bottom, reading as a glitch. Caught by re-running
   frame-sample QA across ALL scenes after the layout change, not reusing the smaller
   sample from the previous round.

**What generalizes:** none of these were one-off mistakes specific to this video —
each is now a numbered rule in §4, and the underlying components (`Panel`,
`Captions`, the footer) live in `VideoB2_Panel.jsx` as the reference implementation
to copy from (or, once the shared-component refactor in `DESIGN-SYSTEM.md` §7
happens, to import from directly) for the next video rather than re-deriving.

## 13. Addendum — RiskModelForgeIQ Video 3, hybrid-archetype consolidation + the
sync methodology (2026-08-14)

Video 3 (the full-tour hybrid demo) took two full editorial review rounds to script
and roughly a full production day to record/stitch, and produced the retrospective
that triggered §1's archetype consolidation. This section is the specific story, the
reusable procedure, and the storytelling-technique research the user asked for.

### 13.1 The hybrid archetype was the right call, once
Two 90s single-mode videos (pure argument, pure proof) had been the standing plan.
One ~3-minute hybrid — Remotion explain beats interleaved with real Playwright
capture, one continuous narration take underneath both — read stronger and is now
the only archetype to build going forward (§1). The evidence: nothing about the
hybrid felt like a compromise between two weaker forms; it read as a single
deliberate format once the beat-type alternation (§1's table) was treated as the
default shape rather than a special case.

### 13.2 The voice/screen sync procedure — do this in this order, every time
This generalizes what had been ad hoc across three separate timing-patch scripts on
Video 3. As a repeatable procedure:

1. **Generate the full narration as one continuous take first** (§4 rule 1), and get
   its real per-line `[start, end]` timestamps out of the TTS call directly — don't
   derive timing from a transcript tool (Whisper mangles brand names, §2 step 3).
2. **Map every beat's narration window directly onto either a Remotion composition
   duration (explain beat) or a live-capture recording target (proof beat).** The
   narration timing file is the single source of truth both sides read from — never
   hand-tune a visual duration independent of it.
3. **Treat every proof beat's narration window as a target for the recording script
   to hit, not a guarantee it will.** Real page loads and settle-waits (§4 rule 15)
   are load-bearing time that the narration-derived window may not have budgeted for.
4. **Verify each recorded/rendered segment against its target duration AND at a
   mid-window checkpoint before accepting it** (§4 rule 14) — run
   `tools/video-studio/scripts/verify_stitch_plan.py` (new, this session) against the
   full segment manifest before assembling anything. It probes every segment's real
   duration against its planned target and flags mismatches mechanically; it does
   NOT replace the manual mid-window frame-sample check, which is the only thing that
   catches "technically the right length, but stuck on a spinner for most of it."
5. **If a proof beat needs more real time than its narration window has, extend the
   window and insert matching silence into the narration WAV at that beat's boundary**
   (§4 rule 16), tracked against a pre-approved slack budget, rather than compressing
   the recording or letting drift accumulate unaudited.
6. **Run a stitch-plan verification pass (step 4's tool) immediately before the final
   concatenation**, not just once during recording — this is what would have caught
   the stale-file bug (§4 rule 17) mechanically instead of after a failed assembly.

### 13.3 Slide/graphic-beat mechanism — see §2.1
The native-Remotion-component default for explain beats (§2.1) is the direct fix for
"need to polish or better slide mechanism" — it removes the entire watermark/
overclaim/off-brand-color patch cycle by not exporting an image from an external tool
in the first place. `PrecisionReveal` (`VideoC_Panel.jsx`) is the reference
component to copy from for the next video's data-driven explain beats.

### 13.4 Storytelling/BLUF research — Sandeep Swadia ("TheMITMonk")
Researched directly per the user's reference (youtube.com/@SandeepSwadia) — first
attempted under a misheard spelling ("Sandeep Sadia") which surfaced no real match;
the correct name is **Sandeep Swadia**, MIT Sloan MBA, ex-Chief Data & Trust Officer
at The Trade Desk, YouTube channel "TheMITMonk." His most directly relevant public
piece is a newsletter post, *"How to Become a Better Communicator"*
(sandeepswadia.beehiiv.com) — the framework itself (a "3A Pyramid Principle") is
paywalled past the intro and is NOT reproduced here since it wasn't actually read;
what follows is only the material that was publicly visible.

**The concrete technique, extractable from the public portion:**
- **"Employees explain. Leaders decide."** — a CEO gave a 3-line answer (margins,
  investment focus, one named risk) to a question a CFO had answered with 60 slides
  of scenarios and caveats. The 3-line version was the more credible one, not the
  less rigorous one. **"Bury your lead, and you bury your credibility."**
- **Practical test for a script's BLUF line:** compress the single idea to 3 lines
  before writing anything longer. If it can't compress, the idea isn't settled yet —
  don't paper over that with more runtime.
- **Unhedged, declarative delivery reads as more authoritative than a hedge-and-
  caveat delivery of the same facts.** Applies directly to narration: push caveats/
  scenarios to an on-screen label if they must appear at all, never stack them into
  the voiceover line itself.
- A cited claim that story-wrapped information recalls far better than an
  equivalent bullet list (a specific Stanford figure was quoted in secondary
  coverage) is explicitly flagged here as **UNVERIFIED — do not cite this figure in
  any published asset without independently web-verifying it first (Rule 0)**; only
  the qualitative direction (story beats a list) is used above, and that direction
  already matches this doc's own §3 rule 3 and STORYBOARD-TEMPLATE.md's contrast
  check, independent of the unverified number.

**New storyboard-gate check, added to `STORYBOARD-TEMPLATE.md`:** read the BLUF line
in isolation — would a stranger with zero context understand the single claim from
that line alone, in 3 lines or fewer? If it takes a paragraph to set up, the beat
needs restructuring before it's a video problem.

### Tooling update
Added `tools/video-studio/scripts/verify_stitch_plan.py`: takes a stitch manifest
(list of `{kind, target_duration, src?}`, the same shape as `stitch_video3.py`'s
`SEGMENTS`) plus the narration timing JSON, probes every real source file's duration
with ffprobe, and reports PASS/FAIL per segment against its planned target (default
tolerance 0.15s) plus a total-duration check against the narration's own total. Does
NOT replace the manual mid-window frame-sample check (§4 rule 14) — duration matching
a target says nothing about whether the middle of that duration is actually usable.
Usage: `python verify_stitch_plan.py <manifest.json> <narration_timing.json>`.
