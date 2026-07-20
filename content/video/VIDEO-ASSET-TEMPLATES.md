# Video Asset Templates (enterprise-gtm)

Product-agnostic templates for producing a two-video launch set for any enterprise
product, plus the distribution plan. Replace `{{PLACEHOLDERS}}`.

> **Scope:** GTM assets live in **this skill (`enterprise-gtm`)**. The `ai-foundry`
> engineering skill builds and ships the product; this skill positions and markets
> it. Do not put GTM templates in ai-foundry.

**Worked reference implementation:** `ask-ai-service` →
`docs/gtm/03-video/{voiceover-scripts,demo-click-path,distribution-playbook}.md`
and `docs/gtm/01-linkedin/post-4-*`, `post-5-*`.

---

## The two-video set

| | Video A — "Why" | Video B — "Proof" |
|---|---|---|
| Format | Narrated slideshow (NotebookLM) | Screen recording + AI voiceover |
| Length | ~75s | ~90s |
| Job | Explain the problem + the shift | Show the live product working |
| Ends on | "here's what it looks like" | a genuine question + demo |

---

## Rule 0 — WEB-SEARCH EVERY CITED FIGURE BEFORE IT SHIPS

**Never publish a statistic from recall.** Search it, confirm the current number and
the exact wording, and record the source + date you checked in the spec.

This is not theoretical. Building Ask-AI's Video B, the recalled figure was
"Gartner: ~30% of GenAI projects abandoned after proof of concept by end-2025."
A search showed that 30% was Gartner's **2024 forecast**, and the **actual outcome
exceeded 50%**. Quoting the remembered number would have understated reality by
nearly half — in front of the exact audience most likely to know the real one.

Two failure modes to check for specifically:
1. **Stale forecasts.** A prediction for a period that has since elapsed reads as
   dated, and may have been overtaken by the outcome. Prefer the measured result, or
   a forecast whose horizon is still in the future.
2. **Contested figures.** Some widely-shared statistics are methodologically
   disputed (e.g. the "95% of GenAI pilots fail" study). Punchy is not worth
   defending a weak source in the comments.

Also bound the claim: name the statistic's *cited causes*, and connect your product
to the one it actually addresses. Do not imply it solves all of them.

## Two hard rules (learned the expensive way)

1. **Narration must be DOMAIN-FREE.** The viewer is a buyer scrolling a feed with
   zero context for your customers' case IDs, regulation citations, internal job
   titles, or agency names. Leaning on them makes a *general* pattern look like a
   *niche* tool. The screen may show specifics as texture; the voiceover and post
   copy must never depend on them. Say "someone in day-to-day operations", never the
   real job title.
2. **Cap the demo at TWO features.** More than two and nothing lands in 90 seconds.
   Pick the two that prove the core positioning claim.

**Also check what the UI can actually show, before scripting.** A first draft that
assumes a capability the demo doesn't have (e.g. an app switcher that doesn't exist)
has to be rebuilt from scratch. Script against reality.

---

## Video A template — narrated slideshow (~75s, 7 beats)

**[Slide 1 — Title: "{{CORE_POSITIONING_LINE}}"]**
"There's a problem hiding inside most {{CATEGORY}} efforts."

**[Slide 2 — "{{N}} × the same rebuild"]**
"{{THE_DUPLICATION_PROBLEM_IN_PLAIN_WORDS}} — {{TIME_COST}}, every single time."

**[Slide 3 — "You can only run one at a time."]**
"So you can only run one project at a time. {{X}} get approved; one ships. That
isn't a budget problem — it's a sequencing problem."

**[Slide 4 — "Build it once."]**
"So build {{THE_SHARED_THING}} once, and stop rebuilding it."

**[Slide 5 — "Each {{UNIT}} just describes its own world."]**
"Then each new {{UNIT}} only has to describe {{WHAT_VARIES}}. That description is
the only part a team writes."

**[Slide 6 — metric cards]**
"{{PROOF_POINT_1}}. {{PROOF_POINT_2}}. {{PROOF_POINT_3}}."

**[Slide 7 — CTA + URL]**
"{{ONE_LINE_PAYOFF}}. Here's what that looks like."

### NotebookLM "Customize" prompt template
```
AUDIENCE: {{BUYER_TITLES}} scrolling a professional feed. They have ZERO context
about our customers, their industry, or any internal job titles.

GOAL: Explain ONE idea — {{THE_SINGLE_IDEA}}.

LENGTH: About 75 seconds, roughly 7 beats.

STRUCTURE (follow this order):
1..7  {{PASTE THE 7 BEATS ABOVE}}

TONE AND HARD RULES:
- One neutral narrator. Calm, precise, conversational. No excitement, no hype.
- NEVER mention: case numbers, regulation citations, customer names, or internal
  job titles. Say "someone in day-to-day operations", never a specific title.
- NEVER use: "seamless", "enterprise-ready", "revolutionary", "game-changing",
  "unlock", "empower", "platform", "solution".
- Lead with the problem, not the product. Use specific numbers, not vague
  comparatives like "faster".
- End with curiosity, not a sales call-to-action.
```
**Caveat:** NotebookLM treats this as *steering*, not a contract. It drifts on
length and re-introduces jargon from the source documents — review every output for
leaked domain terms. If it drifts badly, build the slides manually and run the lines
through TTS for exact control.

---

## Video B template — screen demo (~90s, 6 VO lines)

Spine: **same record, different user, different answer** → then one more capability.

1. (0:00–0:12) Problem — "{{DUPLICATION_PROBLEM}}. {{COST}}. Every time."
2. (0:12–0:22) Shift — "So we built {{SHARED_THING}} once. Each new {{UNIT}} just
   describes its own world."
3. (0:22–0:42) Feature 1a — "{{USER_TYPE_A}} asks {{QUESTION}}, and gets {{ANSWER_A}}
   — what they need to do their job."
4. (0:42–1:02) Feature 1b — "Now the same {{RECORD}}, but {{USER_TYPE_B}} asks. Same
   system — and it returns {{ANSWER_B}}. The person's job changes the answer, not
   just what they're allowed to see."
5. (1:02–1:18) Feature 2 — "{{SECOND_CAPABILITY_IN_PLAIN_WORDS}}."
6. (1:18–1:30) Close — "{{PAYOFF_LINE}}. If your teams keep {{THE_WASTE}} — what
   would they ship if they didn't have to?"

### Demo click-path checklist (before recording)
- [ ] **Warm the service** (hit `/health`) — scale-to-zero means a cold start on camera
- [ ] **Sign in through any access gate** — protected APIs 401 without a token
- [ ] **Blur/crop personal account chip + email**
- [ ] Clean browser: no bookmarks, extensions, or extra tabs
- [ ] Zoom 110–125% so text survives cropping
- [ ] Use the product's **own starter/sample questions** — guarantees seeded data returns
- [ ] Record 1080p+/30fps; plan to speed up "thinking" pauses in post

---

## Captions — burn them in (both videos, both platforms)

**Burned-in** (hard/open) captions are rendered into the pixels: always visible,
cannot be toggled off. Closed captions (`.srt`/platform CC) can be switched off and
often default to off.

**Why it's non-negotiable:** LinkedIn and X both **autoplay muted**. A message that
lives only in the audio reaches almost nobody.

Two distinct on-screen text types — **burn in both**:

| Type | Example | Purpose |
|---|---|---|
| **Subtitles** | the voiceover, transcribed | muted viewers read the narration |
| **Title cards** | `Day-to-day operations → "what do I act on?"` | short labels framing each shot |

**Tools:** CapCut (Auto-captions → export; burned in by default), Descript
(transcript → captions → export), Premiere/Final Cut ("burn in" on export).
Platform auto-CC is **not** burned in.

**Settings:** large high-contrast text (white + dark outline/box), 1–2 lines max,
out of the bottom ~15% (platform UI overlays there), never covering the product.

**Export one 1:1 (1080×1080) master** — serves both LinkedIn feed and X.

---

## Distribution
See `DISTRIBUTION-PLAYBOOK.md` in this folder for the LinkedIn-primary / X-secondary
plan, post-vs-comment decision, first-90-minutes protocol, and what to measure.
