# LinkedIn Graphic Style Framework (paired thought-leadership image)

Derived 2026-08-28 from the author's own published post, "Frontier Today.
Commodity Tomorrow: Rethinking AI Model Tokenomics"
(linkedin.com/feed/update/urn:li:activity:7499080296554782720), paired with
the image `Tokenomics_ Smarter Models, Lower Costs.png`. Governs the
**graphic** that accompanies a LinkedIn thought-leadership post — distinct
from `LINKEDIN-POST-STYLE-FRAMEWORK.md` (short-form post mechanics) and
`LINKEDIN-ARTICLE-STYLE-FRAMEWORK.md` (long-form article voice). The three
coexist: this one governs the paired image only.

## The real pattern this example revealed

The published post text is calm, institutional, third-person — no
accusatory hook, no emoji bullets, no punchy one-liners in the body. That's
a deliberate register (matches `LINKEDIN-ARTICLE-STYLE-FRAMEWORK.md` rule 1,
institutional voice). The graphic is where the punchy, provocative,
memorable version of the same idea lives instead: the accusatory headline
("Your Smartest AI Model Is Doing the Mundane Work"), the habit-vs-smarter
contrast, the rhyme close. **The graphic and the text post are not the same
voice twice — they're a deliberate two-register pair.** Don't flatten the
image into a literal illustration of the post's calm argument; let it carry
the sharper hook the text post itself is choosing not to lead with.

## 1. Comic-book/graphic-novel painterly style, not flat vector
Semi-realistic character illustration with halftone dot shading and bold
"pow"-style comic lettering for the headline — not the flat-silhouette
vector style a first attempt at this defaulted to. The painterly,
higher-production-value comic look reads as more scroll-stopping and more
like a real editorial infographic than a simple satirical strip. When
prompting an image generator, say so explicitly ("comic-book/graphic-novel
style, halftone shading, dynamic comic lettering") — flat vector is the
default an image model will otherwise reach for.

## 2. Two-panel color-coded contrast
A left panel (habit/expensive/wrong, in a warm red header band) beside a
right panel (deliberate/smarter/right, in a green header band). The color
coding alone communicates the argument before anyone reads a word — this is
the single highest-leverage structural choice in the image. Use red/green
(or another clearly opposed pair) as the header bands, not just as accent
details.

## 3. A data band that makes the image stand alone
A footer strip beneath the panels with 3 icon + short-claim pairs, each
pulling one real supporting number or fact from the post's own research
(not generic stats). This is what elevates the image from "a joke that
needs the caption" to a standalone shareable infographic — a viewer who
never reads the post text still gets the argument's substance. Pull these
directly from whatever real, sourced facts backed the post — never invent
placeholder statistics for this band.

## 4. One consistent punchline, echoed from the post
The image's closing line should be the exact same rhyme/punchline the post
text closes on (here, "Frontier Today. Commodity Tomorrow.") — this is what
visibly ties the two assets together as one artifact rather than two
independently-made pieces, the same principle
`LINKEDIN-POST-STYLE-FRAMEWORK.md` rule 5 applies to video pairs.

## 5. Proofread text-in-image before publishing
The published image shipped with a typo ("smarterst" instead of "smartest")
in a speech bubble — invisible until someone reads closely, and not
correctable after the fact once posted. AI image generators do not spell-
check their own rendered text. Read every word of text baked into the image
at full resolution before publishing, not just at thumbnail size.

## Reusable prompt shape (loose, story-only — let the model stage it)
```
A comic-book/graphic-novel style illustration, halftone shading, bold
dynamic comic-style headline lettering. Two panels side by side: a left
panel with a red header band showing [the habit / expensive default], and
a right panel with a green header band showing [the deliberate / smarter
alternative]. Below the panels, a data band with 3 icon + short-claim pairs
summarizing [the post's actual supporting facts — name them]. Close on the
line "[the post's own closing punchline]." Professional tone for a
business/tech LinkedIn audience — polished editorial infographic, not a
cartoonish joke.
```
Let the model decide exact character poses/staging within that structure —
per the "don't over-specify panel choreography" lesson from the earlier
Dilbert-style draft, name the two states and the data, not the blocking.

## How to apply
Draft the image brief against all five points before generating. If a
draft comes back flat-vector/minimalist, explicitly push back toward the
painterly comic-book direction — that upgrade, plus the two-panel color
contrast and the data band, is what separated this published result from
the earlier flat-vector attempt in the same session.
