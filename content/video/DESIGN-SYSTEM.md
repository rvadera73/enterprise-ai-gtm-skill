# GTM Design System — Ask-AI (source of truth: the one-pager)

Derived from `ask-ai-service/linkedin/Ask-AI-Service-OnePager.png`. Every GTM asset —
video, one-pager, deck, post image — should inherit from this so the brand reads as
one system.

> ⚠️ **Known divergence:** the first two videos (July 2026) use a paper/teal/amber
> hand-drawn palette that does **not** match this brand. They work as standalone
> assets, but future videos should move to the palette below, or the sketch style
> should be recoloured into it (navy ink on warm paper, gold marker accents).

---

## 1. Palette

| Token | Hex (approx) | Use |
|---|---|---|
| `navy` | `#1B2A4A` | Header band, primary text, RAG card |
| `navy-deep` | `#132038` | Header gradient, borders |
| `gold` | `#C9922E` | Brand accent, the "ASK-AI SERVICE" emphasis, Graph card |
| `blue` | `#2E7DC4` | Analytics card, service-band tint |
| `purple` | `#5B4C9E` | Workflow card |
| `orange` | `#D2691E` | Orchestrate card |
| `panel` | `#F0F1F3` | Band backgrounds |
| `panel-alt` | `#E4E7EB` | Alternating band |
| `ink` | `#1F2937` | Body text |
| `ink-soft` | `#5A6472` | Secondary text |

**Rule:** navy + gold carry the brand. The five capability colours are *only* for the
five capability cards — never decorative.

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

## 6. Applying this to video

- Ground: navy or warm paper — pick one per asset, never mid-gradient.
- Accent: gold for emphasis (the marker/highlighter gesture already fits).
- Capability cards keep their five colours; everything else stays navy/gold/neutral.
- Diagrams inherit the layered-band structure rather than inventing new geometry.
- Brand rule persists on screen for the full runtime (already the practice).
