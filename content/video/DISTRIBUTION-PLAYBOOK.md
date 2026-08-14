# Distribution Playbook (enterprise-gtm)

Product-agnostic plan for publishing a video launch set. LinkedIn primary, X
secondary. Replace `{{PLACEHOLDERS}}`.

---

## 0. Channel strategy — where the effort goes

| Channel | Role | Effort | Audience |
|---|---|---|---|
| **LinkedIn** | **Primary — the revenue channel** | ~80% | The actual buyers (CIOs, VPs, architects, program owners) |
| **X** | Secondary — credibility + peer reach | ~20% | Builders, technical community, potential hires |

**Do not split 50/50.** Enterprise buyers are on LinkedIn. X compounds slowly and
pays off in credibility and recruiting, not near-term pipeline.

**Reframe per channel — same video, different hook:**
- **LinkedIn** → the *business/operating-model* story.
- **X** → the *technical* story (the protocol, the architecture, the hard part).
  The business-value framing lands flat with a builder audience.

---

## 1. LinkedIn (primary)

### 1.1 Post vs. comment — the decision
**Hybrid: a new native post is primary; a comment on your existing related post is
the feeder.**

- **Only a new native post gets feed distribution.** Comments get none — just people
  who visit that post.
- So: publish the video as **its own native post**, then **comment on the earlier
  related post** linking to the new one. That catches people who find the old post
  later and gently reactivates the thread.

**Three pieces of copy, in this order:**
1. **New post body** — the story + video attached natively. **No link in the body.**
2. **First comment on the new post** (post it yourself, immediately) — the demo/product
   link lives here: *"Live demo if you want to poke at it: {{URL}}"*.
3. **Comment on the existing post** (~1–2h later) — one line tying back to that
   post's actual point + link to the new post. Must add a thought, not read as
   drive-by self-promotion.

### 1.2 Sequencing
- **Hybrid archetype (the common case now):** publish as a single asset, one native
  post. There is no separate "why" video and "proof" video to sequence — the explain
  and proof beats already live in the same continuous video (`GTM-ASSET-PLAYBOOK.md`
  §1).
- **Fallback — genuinely separate assets (real but less common):** only when the
  archetype gate (`GTM-ASSET-PLAYBOOK.md` §1) produces a real explain-only video
  *plus* a separate proof asset published later, sequence explain-only ("why") → wait
  **3–7 days** → the proof asset ("proof").
- **Minimum 24–48h between any two posts, either case** — closer together and they
  compete for the same audience.

### 1.3 The first 90 minutes (matters more than the copy)
- Publish only when you can **reply for ~90 minutes**. Early reply velocity is the
  strongest signal you control.
- **Reply with substance**, not "thanks!" — real answers create threads, and threaded
  replies count far more than reactions.
- **Don't edit the post in the first hour** — widely reported (never officially
  confirmed) to reset distribution. Proofread before publishing.
- Tag only people who'd genuinely want to respond.

### 1.4 Don'ts
- No "link in comments!!" theatrics; ≤3 hashtags, or none.
- No sales CTA — end on a genuine question.
- Don't repost the same video later; cut a new angle.

---

## 2. X (secondary)

### 2.1 Set expectations honestly
**A new X account has effectively zero organic distribution.** The first post reaches
almost nobody. That is normal, not a signal to quit — X rewards consistent presence
and *replies into other people's conversations*. Judging post #1 by its numbers leads
to the wrong conclusion.

### 2.2 Phase 1 — Profile (before posting anything)
- Bio: what you build, plain words, no "thought leader" language.
- **Product URL in the profile link field** (profile links are free; in-post links
  cost reach).
- Header + real avatar — an empty profile kills follow-through from replies.

### 2.3 Phase 2 — Warm up (~2 weeks, before your first post)
- **Reply substantively into existing conversations** in your technical niche. This
  is how cold accounts get discovered.
- Follow the builders you'd want reading your work.
- Goal: a few hundred profile visits from replies *before* post #1, so it lands on a
  non-zero audience.

### 2.4 Phase 3 — First thread (use the demo video, technical framing)
Keep links to a later tweet — links suppress reach on X too.

> **1/** {{PROBLEM_IN_ONE_LINE}}
> {{THE_DUPLICATION_OR_HARD_PART}}
> We built it once. 90s of it working ↓ *[native video]*
>
> **2/** {{THE_NON-OBVIOUS_TECHNICAL_POINT}}
>
> **3/** {{THE_ARCHITECTURE/PROTOCOL_HOOK — the bit builders care about}}
>
> **4/** Live demo: {{URL}}

- **Pin the thread.** Keep replying to it as questions come in.

### 2.5 Cadence
2–4 posts/week + daily replies beats one big launch. Repurpose each LinkedIn post as
an X thread ~a week later, reframed technical.

---

## 3. Cross-channel sequencing
**Run LinkedIn first and let it breathe for a week.** The comments tell you which
line actually resonates — write the X copy with that knowledge instead of guessing.
Never launch both channels the same day.

---

## 4. Asset rules (both platforms)
- **Burned-in captions, always** — both autoplay muted.
- **Pick the aspect ratio per `GTM-ASSET-PLAYBOOK.md` §4 rule 10** — match the source
  content's actual aspect ratio, usually 16:9 for slide/hybrid content. Cut a 9:16 or
  1:1 version only if the specific platform/placement genuinely needs it, rather than
  defaulting to a fixed 1:1 master.
- MP4 / H.264, <200MB. **Native upload** — never a YouTube link as the primary post.

---

## 5. Measurement — track the funnel, not the vanity

If the product has a sign-in/lead capture, the funnel is measurable end-to-end:

```
impressions -> profile/product clicks -> sign-in -> CAPTURED LEAD
```

| Track | Ignore |
|---|---|
| **Captured leads** (the real metric) | Impressions |
| Comments + reply depth | Likes |
| Profile views after a post | Follower count (early X) |
| Sign-ins in the 48h after a post | "Engagement rate" |

**Rule of thumb: a post producing 3 real conversations beats one with 10k
impressions and no comments.**
