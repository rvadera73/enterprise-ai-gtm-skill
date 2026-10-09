# Brief — AI-Assisted Software Factory (internal video)

Filled per `content/video/BRIEF-TEMPLATE.md`, retroactively (2026-08-27) — the storyboard
was drafted before this was locked, which is the actual root cause of several rounds of
scope drift (pipeline → secrets → config → Docker → CBP Sentry → CI roadmap) before this
converged. Fill the Brief BEFORE the storyboard on the next one.

---

## 1. What is this?

- **Asset:** video, **feature-detail** archetype (deeper on one capability, warmer
  internal audience — the previously-unbuilt third archetype)
- **Product name, exactly as it must be said:** "AI-Assisted Software Factory" —
  **no "AI Forge" / "ai-foundry" branding anywhere on screen or in narration**
- **Length target:** ~160s → word budget ≈ 400 (150 wpm)
- **Where published:** internal Precise session/recording — not LinkedIn/X, no public CTA

## 2. Audience

- **Who:** Precise developers (primary) — BD + senior management (secondary, observing
  to gauge this as a potential future Precise product)
- **What they already know about us:** first exposure to the "AI-Assisted Software
  Factory" name/framing specifically
- **What they have NO context for:** the "AI Forge"/"ai-foundry" internal codename (must
  not appear), IACP-2.1's legal/domain specifics beyond one descriptive line, CBP Sentry
  beyond "queued next"

## 3. The single idea

> Bring a properly containerized microservice, and the AI-Assisted Software Factory
> takes it the rest of the way to a real multi-cloud deploy.

## 4. The opening (BLUF)

Mechanism-based, not a stats claim — Rule 0's "web-verify" doesn't apply the same way,
but every underlying fact was verified against real files this session (2026-08-27):
`IACP-2.1/project.factory.yaml`, the fixed pipeline artifact, and real Dockerfiles
(`ask-ai-service/backend/Dockerfile`, `cbp-risk-engine/Dockerfile`). Not a forecast, not
contested.

## 5. The reframe

> They assume: adopting this means new tooling, more upfront process for the developer.
> Actually: the developer's own footprint *shrinks* — design + Docker packaging only —
> and everything else is generated.

## 6. The ONE concrete contrast

> A developer's job scope, before vs. after: before, design **+** CI config **+** deploy
> scripts **+** infrastructure. After, design **+** Docker packaging only — the factory
> owns build and deploy.

## 7. The visible mechanism

> Real `project.factory.yaml` (IACP-2.1, `services:` block) shown next to the real
> pipeline it drives.

## 8. Benefit — as consequence, not adjective

> "A developer's actual week goes back to the service itself — not a Terraform diff, not
> a deploy script." (Not "seamless," not "powerful.")

## 9. Close

- **Question to leave them with:** "What would take longer — building all of this
  yourself, or building the service you actually wanted to ship?"
- **CTA:** none. Informational close — internal audience, explicitly no ask (confirmed
  with the user).

## 10. Product mentions

- Target 3-4x functional: currently 3 ("AI-Assisted Software Factory" — beats 1, 5, 6),
  "the factory" as shorthand elsewhere.
- Persistent brand rule on screen: yes — condensed one-pager as the closing card.

## 11. Claim boundaries — what we must NOT imply

- Must **not** imply CBP Sentry is already running on the factory — roadmap / "coming
  weeks" only, confirmed internal, not shown as a proof beat.
- Must **not** imply the factory currently dispatches to GitLab/Jenkins — roadmap
  ("next"), not current capability.
- Must **not** show "ai-foundry" or "AI Forge" anywhere on screen — confirmed present in
  both `service.factory.yaml`'s header comment and `project.factory.yaml`'s inline
  comment; crop both out of any shot.
- Must **not** claim a live, currently-reachable public IACP-2.1 URL — GitHub Actions on
  that repo is confirmed billing-blocked as of 2026-08-26 (runs failing in 3-6s), and a
  "Reap Stale EKS Deployments" job runs on schedule, so staging may not even be up. Use
  local reproduction (docker-compose / local `kind`) or previously-verified evidence
  (Milestone 1 EKS proof, 2026-08-18), never a "watch it live right now" framing.
- ~~Must not claim every existing service already meets the multi-stage/non-root Docker
  pattern~~ — **stale, corrected 2026-08-27:** this was written for the earlier
  compliant-vs-noncompliant Dockerfile split-screen visual, which beat 3 no longer uses
  (replaced by the general job-scope contrast per later feedback). The current script
  makes no claim about which existing services do or don't comply, so this boundary no
  longer applies. Kept here, struck through, as a reminder: if a real Dockerfile
  screenshot is reintroduced at the shot-list stage, this same boundary needs to come
  back — `ask-ai-service/backend/Dockerfile` is still single-stage/root today,
  `cbp-risk-engine/Dockerfile` is still the real compliant example.
- Must **not** claim the "asks for missing info" config-generation behavior is a captured
  demo — it's spoken narration only, backed by the real files' "managed by / regenerate
  via factory generate" design intent, not a transcript of it actually happening. Flagged
  to the user; kept in the script by their call, not silently asserted as filmed proof.

## 12. Visual

- **Archetype's visual world:** hybrid — graphic explainer beats + real product/pipeline
  capture, one continuous narration take. **Deliberate, recorded divergence** from this
  playbook's default "one visual world" rule, per the 2026-08-14 standing hybrid-archetype
  decision (supersedes the older two-asset/single-world default).
- **Follows `DESIGN-SYSTEM.md`?** **Checked and resolved, 2026-08-27: deliberate divergence.**
  `content/video/DESIGN-SYSTEM.md` is Ask-AI's own system (dark slate ground,
  blue/teal/purple/green accents, Inter) — verified by reading it directly. Our product's
  actual one-pager (the real "AI-Assisted Software Factory" PNG this whole project is
  built around) is a different, already-shipped visual identity entirely: light
  background (`#EEF1F5`), dark navy header, blue/amber/green accent tokens matching
  real semantic meaning (GCP/AWS/shared-pipeline), Precise Software Solutions branding.
  Forcing Ask-AI's dark-slate palette onto an already-established different product's
  brand asset would be the wrong fix — this asset inherits from *its own* one-pager, not
  Ask-AI's, matching this doc's own stated principle (products get their own accent
  family) even though the doc's dark-slate ground assumption doesn't extend to a product
  with a genuinely different, pre-existing light-mode identity.
- **Diagram inherits layered-band structure?** Yes — the one-pager is the canonical
  diagram source (§6); the closing card is a condensed version of it, other graphic beats
  should reuse its palette/icon language rather than inventing new geometry.
- **Capability names used verbatim from taxonomy?** Yes — "AI-Assisted Software Factory"
  verbatim; stage names (PROMPT/REPO/PIPELINE/PRODUCTION) reserved for the closing card.

## 13. Demo-only

- **Has someone confirmed the assets can actually show this?** Partially. `project.factory.yaml`
  content confirmed real and screenshot-able. The Actions-run proof and "live" URL
  proof are NOT currently obtainable live (billing block, confirmed) — plan is local
  repro + the already-fixed pipeline artifact + the dated Milestone 1 evidence.
- **Real inputs used:** IACP-2.1's actual `project.factory.yaml`, actual Dockerfiles
  (two real repos, contrasted), the fixed pipeline artifact.
- **Max two proof points:** the Docker/job-scope contrast + the config-file mechanism —
  within the archetype's limit.
- **Auth:** n/a — no live gated interactive demo, static artifacts + local repro only.

## 14. Narration

- **Voice:** two-voice, role-based — **Developer** + **DevSecOps Engineer** (no invented
  personal names, per explicit user call)
- **Written for the ear:** building turns, not strict Q&A alternation (corrected
  2026-08-27 after two rounds of the Developer voice reverting to one-liner cue-questions)
- **Within word budget:** ~391 / ~400 words

---

## Definition of ready

- [x] Single idea fits one sentence
- [x] Underlying facts verified against real files/repos (not web stats — mechanism claims)
- [x] Claim boundaries written down (§11)
- [x] Visual world chosen — hybrid, **deliberately** diverging from "not hybridised" default,
      divergence recorded per §12
- [ ] Demo capability confirmed against the real, currently-live UI — **partial**: files
      confirmed, live URL/Actions run NOT currently obtainable, mitigation plan recorded
- [x] Script within word budget
- [ ] **Storyboard reviewed and signed off before any code** — see `STORYBOARD-internal-video.md`
      in this folder; still pending final sign-off
