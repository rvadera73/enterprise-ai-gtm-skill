# Storyboard — AI-Assisted Software Factory (internal, feature-detail)

Filled per `content/video/STORYBOARD-TEMPLATE.md`, against `BRIEF-internal-video.md` in
this same folder. Sign-off gate — review before any narration audio / capture work starts.

## Header

| | |
|---|---|
| Asset | video |
| Archetype | feature-detail (deeper on one capability, warmer internal audience) |
| Audience | Precise developers (primary), BD + sr. management (secondary) |
| Length target | ~150-170s spoken · word budget ~390-425 (150 wpm) |
| Visual world | **Deliberate divergence, recorded:** hybrid — graphic explainer beats + real product/pipeline capture, one continuous narration take. Supersedes this playbook's older "one visual world" rule per the 2026-08-14 hybrid-archetype standard. |
| Narrator | Two-voice, role-based (no invented personal names): **Developer** + **DevSecOps Engineer**, building turns (not strict Q&A alternation) — corrected 2026-08-27 after two rounds of the Developer voice reverting to one-liner cue-questions |
| Worked example (single thread throughout) | IACP-2.1 only — no other client repo mixed in |

## The beats

| # | Beat | On screen | Narration | Words |
|---|---|---|---|---|
| 1 | BLUF | Real IACP-2.1 repo tree → zoom into a terminal running a local health-check → real (locally-reproduced, honestly labeled) health-check evidence | **DEVSECOPS ENGINEER:** A developer hands over a repository and a Dockerfile, and the AI-Assisted Software Factory builds and deploys a real multi-cloud pipeline from that. You'd normally have a team writing that pipeline by hand — this doesn't. **DEVELOPER:** That's a lot riding on just a repo and a Dockerfile — most multi-cloud pipelines I've dealt with take a dedicated infrastructure team two sprints just to stand up and debug. | ~68 |
| 2 | reframe | Graphic: gap between "design" and "running in production" | **DEVSECOPS ENGINEER:** Right, and that's exactly the assumption people bring in — that something like this means more upfront work, new tooling, a new process to learn. **DEVELOPER:** That's usually how it goes, yeah — new AI angle, same old rewrite-everything tax. | ~38 |
| 3 | **contrast** | Before/after graphic: developer surrounded by "design, CI config, deploy scripts, infra" → developer surrounded by just "design, Docker packaging," build/deploy arrows pointing to the factory | **DEVELOPER:** Because normally that's the actual job, right — you design the service, sure, but then you're also the one writing the CI config, the deploy scripts, wiring up whatever infrastructure it needs. Half your sprint disappears into that before the thing even ships. **DEVSECOPS ENGINEER:** And now that whole second half isn't the developer's anymore. They design the architecture, package it properly in Docker, and the factory takes over build and deployment from there. | ~68 |
| 4 | mechanism | Real IACP-2.1 `project.factory.yaml`, `services:` block only — no branded comments visible (cropped); cursor-highlight tracks line-by-line with the narration so the still doesn't sit dead on screen | **DEVSECOPS ENGINEER:** Nobody's hand-typing this from scratch either — you point it at the repo, say what you're deploying, and it fills this in itself. If it can't tell something, it asks, and whatever comes back gets written straight into this. **DEVELOPER:** So if my config surface just shrank to one Dockerfile — what happens when a deployment actually fails, am I the one debugging the factory's generated pipeline, or is that shielded too? **DEVSECOPS ENGINEER:** Not you first, no — a failure routes back to the AI to diagnose and fix, same as any other failed gate. You only get pulled in for something that's actually your call — a breaking schema change, say, not a flaky retry. | ~112 |
| 5 | benefit | Graphic: developer's time → architecture/design; one real, honestly-labeled local health-check terminal (not dressed up as live AWS/GCP) | **DEVSECOPS ENGINEER:** Which is why a developer's actual week goes back to the service itself — the architecture, the design — not a Terraform diff, not a deploy script. **DEVELOPER:** And this isn't a thought experiment sitting in a deck somewhere — it's running for real, on IACP-2.1. That's the part that actually matters to me, honestly, versus a proposal. **DEVSECOPS ENGINEER:** It is — and the AI-Assisted Software Factory isn't stopping there. CBP Sentry's next, in the coming weeks — same factory model, same configuration structure, just pointed at a new repository. And it won't stay GitHub-only either — Jenkins and GitLab are next on the same model, just a different CI underneath. | ~101 |
| 6 | close/question | Condensed one-pager (compressed 4-stage flow + guardrails/outcomes strip) + small "Next" line, read not spoken: CBP Sentry (coming weeks) · GitLab & Jenkins adapters. Title "AI-Assisted Software Factory" | **DEVSECOPS ENGINEER:** A repository, a working Dockerfile, and the AI-Assisted Software Factory takes it the rest of the way. **DEVELOPER:** Fair trade — as long as that Dockerfile's actually right. **DEVSECOPS ENGINEER:** That's genuinely the only part still on you. Two sprints of infrastructure work, or the service you actually wanted to ship? | ~46 |

**Total words:** ~437 / budget ~410-450. **Real measured narration duration (Cartesia, sonic-3.5, 2026-08-27): 153.9s** — shorter than the 150wpm word-count estimate (~170-175s) predicted; this measured value is now the source of truth for visual timing, per GTM-ASSET-PLAYBOOK.md §3 ("derive visual timing from the audio"). Audio: `tools/video-studio/factory_output/master_narration.wav` + per-line cues in `factory_output/narration_timing.json` (also includes a `beats{}` map with each beat's real start/end, generated directly by `generate_narration_factory.py`).

## Review log (chronological)

### 1. External review — disposition (2026-08-27)

A second AI reviewed this storyboard. Accepted, rejected, and flagged below — see chat
log for full reasoning; this is the resolution record.

**Accepted:**
- Beat 1 Developer line tightened (sharper personal-experience framing)
- Beat 4 Developer line replaced — was drifting back to a passive cue-question; new
  version asks a real question ("what happens when a deployment fails") answered with a
  genuine, previously-unused verified fact (one-pager PIPELINE stage: "failures
  automatically return to the AI for diagnosis and remediation")
- Coverage-floor numbers: confirmed dropped (were never in the script, only an open
  checklist item)
- Cursor-highlight / line-by-line reveal for Beat 4's static YAML — valid craft note,
  carried into the on-screen column; full execution detail belongs in the shot-list phase

**Rejected:**
- Dropping "in the coming weeks" from Beat 5 — the user explicitly asked for that CBP
  Sentry timing to be included; kept it, adopted only the "pointed at a new repository"
  tightening around it
- Fixed shot timestamps (the reviewer's 0:00-0:25 / 0:25-1:05 / 1:05-1:35 / 1:35-2:15
  blueprint) — doesn't reconcile with this storyboard's actual 6 beats (skips the close),
  and conflicts with our own documented rule (GTM-ASSET-PLAYBOOK.md §3: derive visual
  timing from the real narration audio, not assign it up front)

**Flagged — disagree, will not do as proposed:**
- "Simulated local AWS/GCP routing tags" for the health-check visual — labeling two local
  ports as if they were real cloud endpoints is fabricating evidence, not reproducing it,
  and directly conflicts with the Brief's claim-boundaries section. Fix instead: show one
  real local health check, honestly labeled as local; the "two clouds" claim is carried
  by the already-real, dated Milestone 1 evidence, not a synthetic relabel.

### 2. Self-review, cold re-read (2026-08-27)

No external tool available for this pass (checked: Descript's API has no plain-text
script-review endpoint — see chat log). Self-critique instead, checked against the
playbook's own for-the-ear and narrative rules:

- Beat 6 had a real redundancy — Developer's "only lever left in a developer's hands"
  and the Engineer's very next line "that's the only part still on you" restated the
  same point twice in a row, killing the close's momentum. Trimmed Developer's line.
- Beat 4's Developer line had drifted back into two rapid-fire questions in a row —
  the exact cadence problem fixed elsewhere in this doc. Merged into one flowing
  question with an em-dash.
- Beat 2's Developer line opened on a dangling fragment ("Which is what I expected...")
  — awkward for spoken delivery. Smoothed into one complete sentence.
- Beat 5's GitLab/Jenkins line was ambiguous on timing (could read as already-true, not
  clearly future) compared to how the CBP Sentry line explicitly says "next." Added an
  explicit "next" for consistency with the Brief's §11 claim boundary.
- **Found a real cross-document bug:** `BRIEF-internal-video.md` §11 still carried a
  claim-boundary bullet about not overclaiming universal Docker multi-stage/non-root
  compliance — written for the old compliant-vs-noncompliant Dockerfile split-screen
  visual that beat 3 no longer uses (replaced by the job-scope contrast per later
  feedback). That bullet was orphaned; updated in the Brief to match the current script.

### 3. Third-party review, via Descript's Underlord chatbot in-app (2026-08-27)

User pasted the script into Descript's own chatbot and got emotional-naturalness/pacing
feedback. Applied nearly all of it — no conflicts with verified facts:

**Accepted:**
- Beat 1: "nobody writes that pipeline by hand" read as a slogan, not something an
  engineer says — reworded to "you'd normally have a team writing that pipeline by hand,
  this doesn't"
- Beat 2: Developer was conceding too fast (already agreeing by beat 2, undercutting the
  skepticism that makes beat 3's contrast land) — rewritten to stay skeptical
  ("same old rewrite-everything tax"), which also removes the weakest line in the
  script ("that's not actually where the line moved" — a written, not spoken, metaphor)
  and incidentally fixes the repeated "honestly" tic (was in both beats 2 and 5, now
  only beat 5)
- Beat 4: "genuinely needs your call" was too hand-wavy for a developer audience —
  added a concrete example (breaking schema change vs. a flaky retry), trimmed the
  opening line by the same amount to keep the beat's length flat
- Beat 6: closing question now callbacks to the Developer's own "two sprints" number
  from beat 1, instead of the more abstract "building all of this yourself" — reinforces
  retention, closes the loop
- Beat 5's roadmap detail was initially cut from spoken narration per this review's point
  that it undercut the strongest emotional beat — see round 4 below, since the user
  overrode this.

### 4. User override (2026-08-27)

User confirmed: wants the CBP Sentry timing + GitLab/Jenkins roadmap spoken in full,
**in addition to** the on-screen "Next" text on beat 6 — not one or the other — and is
fine with the added runtime. Restored beat 5's DevSecOps line to its fuller roadmap
version (kept the brief "it's not stopping there" landing line first, as a small nod to
the Underlord review's point about not cutting straight from the emotional beat into the
roadmap). Runtime moved back up to ~170-175s as a result; accepted deliberately, not an
oversight.

## Checks before sign-off

**Narrative**
- [x] Opens on a fact/tension, not a setup
- [x] Exactly ONE concrete contrast (developer job-scope before/after) — not a feature list
- [x] Visible mechanism the viewer can see working (real `project.factory.yaml` → real pipeline)
- [x] Benefit stated as consequence ("a developer's week goes back to the service"), not an adjective
- [x] Closes on a genuine question, not a CTA
- [x] Product named functionally 3× ("AI-Assisted Software Factory" — beats 1, 5, 6); "the factory" used as shorthand elsewhere

**Turn-taking (corrected 2026-08-27)**
- [x] Developer has ≥1 substantive, longer turn in beats 1, 3, 4, 5, 6 — not just short cue-questions
- [x] No line is a bare setup feeding the next answer
- [x] Read-aloud check done (review log §2, self-review, 2026-08-27) — found and fixed 3 cadence issues (beats 2, 4, 6); overall Developer/DevSecOps word split roughly even after the beat-5 roadmap restore, acceptable for an explainer archetype

**Truth**
- [x] `project.factory.yaml` confirmed real, exists for IACP-2.1 (read directly)
- [x] "ai-foundry" branding identified in both candidate config files — cropped out of the shot, not shown
- [x] IACP-2.1 GitHub Actions confirmed currently billing-blocked (checked live, 2026-08-26 runs failing in 3-6s) — live-URL proof will use local reproduction, not a live public URL claim
- [x] Docker examples (single-stage/root vs. multi-stage/non-root) verified against real files, not invented
- [x] Per-service coverage-floor numbers (80/70/68) — resolved: dropped, not used on screen or in narration

**Feasibility (capture)**
- [ ] Shot list not yet built — next step
- [x] Local repro path decided: one real, honestly-labeled local health check (docker-compose or local `kind`) — explicitly NOT relabeled/staged as live AWS/GCP endpoints; "two clouds" claim rests on the already-real, dated Milestone 1 evidence instead

**Sign-off:** _____ **Date:** _____
