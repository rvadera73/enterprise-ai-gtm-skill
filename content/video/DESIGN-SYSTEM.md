# GTM Design System — Ask-AI (source of truth: the one-pager)

Derived from `ask-ai-service/linkedin/Ask-AI-Service-OnePager.png`. Every GTM asset —
video, one-pager, deck, post image — should inherit from this so the brand reads as
one system.

> ⚠️ **Known divergence:** the first two videos (July 2026) use a paper/teal/amber
> hand-drawn palette that does **not** match this brand. They work as standalone
> assets, but future videos should move to the palette below, or the sketch style
> should be recoloured into it.

> **CORRECTED 2026-07-31**: the palette below was stale — it documented an earlier
> version of the one-pager that no longer matches what's actually shipped. Verified
> directly against the current `Ask-AI-Service-OnePager.html`/`.png` (source HTML
> read in full; Tailwind classes quoted below are the literal ground truth, not a
> approximation) before correcting this. **RiskModelForgeIQ's own one-pager
> (`cbp-risk-engine` branch `docs/rmf-onepager`) already correctly derived from this
> real palette — its header comment says so explicitly, and it checks out — so it's
> the second confirming data point, not just this doc's word.**

---

## 1. Palette — verified current, 2026-07-31

| Token | Value | Use |
|---|---|---|
| `ground` | Tailwind gradient `slate-900 → slate-800 → slate-900` (`#0F172A`-ish) | Full-page background |
| `label-blue` | Tailwind `blue-400` (`~#60A5FA`) | Eyebrow label (e.g. "ASK-AI SERVICE"), first capability card accent |
| `subtitle-teal` | Tailwind `teal-300` (`~#5EEAD4`, RiskModelForgeIQ's sampled `#2DD4BF` is the same family) | Subtitle/tagline emphasis, second capability card accent |
| `accent-purple` | Tailwind `purple-400`-ish (`~#A78BFA`) | Third capability card accent |
| `accent-green` | Tailwind `emerald`/`green-400`-ish (`~#34D399`) | Used where a fourth accent is needed (RiskModelForgeIQ's card left-bars) |
| `body` | Tailwind `gray-300` (`~#D1D5DB`) | Body text on dark ground |
| `muted` | Tailwind `gray-400` (`~#9CA3AF`) | Secondary/meta text (type/category/audience block) |
| `card-bg` | `slate-800`/`900`-ish translucent panel | Capability card backgrounds, "plugs in" tag backgrounds |

Font: **Inter** (Google Fonts in Ask-AI's HTML; RiskModelForgeIQ's HTML vendors it
locally as `InterVariable.woff2` for offline-safe rendering — same typeface either
way).

**Rule (corrected): dark slate ground + Inter carry the brand across the whole
portfolio. Each product's capability cards get 3-4 accent colors drawn from the same
blue/teal/purple/green family — never a new hue invented per product, and never used
decoratively outside the capability cards.** This directly resolves an ad hoc accent
color (`#E08D3C`, "molten copper," invented independently for a video pipeline
without checking this doc) — that color should be retired in favor of this real,
verified family.

## 2. Typography

- **Band headers:** bold, UPPERCASE, tight tracking (`ANY APPLICATION LAYER`)
- **Card titles:** bold, uppercase, smaller
- **Body:** regular sans, sentence case, 2–3 lines max per card
- **Metrics:** very large bold numerals with a small caption beneath
- Never more than ~8 words in any on-screen header.

## 3. The canonical diagram — layered bands

The one-pager's structure IS the argument, top to bottom:

```
┌ HEADER ─ brand + tagline + one-line problem ──────────────┐
├ ANY APPLICATION LAYER ─ CRM/ERP · Legacy · Software ·     │
│                          Energy · Digital · Enterprise    │
├ ASK-AI AGENTIC AI SERVICE ─ the 5 capability cards ───────┤  ← the product
├ ANY CONNECTED ENTERPRISE DATA / SYSTEM ─ docs · DBs ·     │
│                          knowledge · systems · APIs       │
├ SINGLE PATHWAY … GOVERNANCE & ACCESS CONTROL ─ 4 controls │
└ ENTERPRISE BUSINESS IMPACT / BENEFITS ─ the metrics ──────┘
```

Applications on top, data underneath, **Ask-AI as the tier between them**, governance
across the whole pathway. Any diagram in any asset should be recognisably this.

## 4. Capability taxonomy — use these names exactly

**Five service capabilities** (the coloured cards):

| Capability | One-line |
|---|---|
| **RAG Agent** | AI agents for data sources, context windows, large documents |
| **Analytics** | Agents to analyse data, find patterns, provide insights |
| **Graph Agent** | Knowledge graphs for structuring, navigating, query-answering |
| **Workflow** | Workflow automation, connecting tools, orchestrating complex tasks |
| **Orchestrate** | Orchestrate actions, tasks and data flows into agentic service |

**Four governance controls** (separate band — do not mix into the five):
Role-Based Access Control · Prompt/Data Policy · Compliance Auditing · Rate/Cost Control

> Video B flattened all nine into a single ring. That was wrong — the separation
> between *capabilities* and *governance* is part of the architecture story.

## 5. Claimed metrics — handle with care

The one-pager states **60–80% faster deployment**, **40–60% lower OpEx**,
**100% secure/compliant/audited**, and portfolio scale.

**Before reusing any of these in a video, post, or deck:** confirm what they are
derived from and whether they are defensible publicly. "100% secure" in particular is
an absolute claim that invites challenge. Per Rule 0, no figure ships unverified —
this applies to our own numbers, not just third-party ones.

## 6. Applying this to video — corrected 2026-07-31

- Ground: the dark slate gradient (§1), not navy or warm paper — that was the stale
  version. Every product's video shares this ground; don't invent a new one per
  product.
- Accent: blue/teal for primary emphasis (label + tagline), matching the real
  one-pager's actual hierarchy — not gold, which no longer exists in the current
  brand.
- Capability cards get 3-4 accents from the blue/teal/purple/green family (§1);
  everything else stays on the dark ground + `body`/`muted` neutrals.
- A recurring product-name/tagline mark (a "brand bar") should sit as a **quiet
  footer band inside the content frame**, not a large floating header disconnected
  from it — matches real presentation-template convention (logo recedes into the
  background as a quiet mark on content slides; only a title/opening or closing
  moment earns a bigger, more prominent brand treatment).
- Diagrams inherit the layered-band structure rather than inventing new geometry.
- Brand rule persists on screen for the full runtime (already the practice) — just
  quieter than a full-size header, per the point above.

## 7. Portfolio-wide component reuse (added 2026-07-31)

Both Ask-AI's and RiskModelForgeIQ's video pipelines currently duplicate the same
`BrandBar`/`Panel`/`Captions` component code per product (`VideoA_Panel.jsx`,
`VideoB2_Panel.jsx` in `enterprise-ai-gtm-skill/tools/video-studio/src/`), each with
its own hand-copied styles. **Going forward, these should be ONE shared component set
that takes a per-product theme object as config** (ground/accent tokens from §1,
product name + tagline, capability-card colors) — not reinvented per video. This is
the same three-tier pattern (shared structure + component tokens + per-product
semantic tokens) real multi-product design systems (e.g. Atlassian's) use to scale
across a portfolio without either forcing one rigid look or letting every product
drift into its own bespoke, undocumented palette (which is how `#E08D3C` "molten
copper" happened in the first place — invented in a video file, never checked
against this doc or the real one-pager).
