#!/usr/bin/env python3
"""Strip the NotebookLM watermark from exported slide-deck PNGs.

Replaces the hand-measured-pixel-box approach used for RiskModelForgeIQ Video A
(see content/video/GTM-ASSET-PLAYBOOK.md addendum #10): that produced two
visibly botched edits before getting them right, because the watermark box was
guessed off a scaled screenshot instead of detected from the actual image.

This scans the bottom-right corner for the watermark's actual ink cluster,
picks it out from any real slide text that might share the same row (e.g. a
full-width banner sentence ending near the same corner), and fills it with
either a solid color (flat background) or a blurred nearby patch (textured
background) -- whichever the surrounding pixels call for.

Does NOT attempt overclaim/content detection -- that remains a manual step
(grep the product's ADRs/design docs; see the playbook's step 5).

Known limitations -- always visually spot-check the bottom-right corner of
every slide, not just a full-page glance (a small watermark logo is easy to
miss at a scaled-down preview size):
1. Slides where body text runs flush to the same corner as the watermark (a
   full-bleed banner whose last line ends within ~20px of the watermark) can
   share near-identical letter/word spacing at this resolution, making them
   hard to tell apart by gap size alone -- detection is biased toward the
   rightmost plausible cluster to avoid clipping real text.
2. Slides with a subtle gradient/vignette across the whole bottom band (seen
   on RiskModelForgeIQ Video 2's more atmospheric/glowing slides) break the
   "sample one flat background color" assumption: nearly every column reads
   as "ink" versus a single sample point, the resulting cluster exceeds
   MAX_CLUSTER_WIDTH_FRAC, and detection returns None (no-op, watermark left
   untouched) rather than a wrong box. 3 of 8 slides failed silently this way
   in one real run. If a slide comes back unchanged, don't assume it had no
   watermark -- check the corner directly, then fall back to a manual
   local-patch (sample a small crop immediately left of the known ~x:[2600,
   2867] y:[1520,1600]-at-2867x1600 watermark position, blur, paste) rather
   than trusting the whole-row bg-color assumption on that slide.

Usage:
    python clean_notebooklm_slides.py <input_dir> <output_dir>
    python clean_notebooklm_slides.py one_slide.png cleaned_slide.png
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

# Watermark historically sits in the last ~25% of width, last ~4% of height.
SEARCH_X_FRAC = 0.60
SEARCH_Y_FRAC = 0.96
INK_DIFF_THRESHOLD = 30
MIN_CLUSTER_GAP = 12  # px of background between ink runs before treating them as separate clusters
MAX_CLUSTER_WIDTH_FRAC = 0.30  # a cluster wider than this is probably body text, not the watermark
MIN_CLUSTER_WIDTH = 30  # px -- rejects 1-3px anti-aliasing/JPEG-corner noise as a false "cluster"
PADDING = 6
FLAT_STD_THRESHOLD = 9.0


def _most_common_color(arr: np.ndarray) -> tuple[int, int, int]:
    flat = arr.reshape(-1, arr.shape[-1])
    colors, counts = np.unique(flat, axis=0, return_counts=True)
    return tuple(int(c) for c in colors[np.argmax(counts)])


def _find_watermark_box(img: Image.Image) -> tuple[int, int, int, int] | None:
    w, h = img.size
    arr = np.array(img.convert('RGB'))

    y0 = int(h * SEARCH_Y_FRAC)
    x0 = int(w * SEARCH_X_FRAC)
    region = arr[y0:h, x0:w]
    if region.size == 0:
        return None

    # Sample background from the bottom-most few rows only, not the whole
    # search band -- a band this close to the edge can still straddle a
    # banner/margin boundary on some slides, and the absolute bottom rows
    # are reliably pure background (the watermark itself sits a few px
    # above the true edge) regardless of what's above them in the band.
    bg_strip = arr[h - 4:h, x0:w]
    bg = np.array(_most_common_color(bg_strip)) if bg_strip.size else np.array(_most_common_color(region))
    diff = np.abs(region.astype(int) - bg).sum(axis=2)
    ink_cols = (diff > INK_DIFF_THRESHOLD).any(axis=0)

    # Segment into clusters of contiguous (gap-tolerant) ink columns.
    clusters: list[list[int]] = []
    gap = MIN_CLUSTER_GAP + 1
    for i, has_ink in enumerate(ink_cols):
        if has_ink:
            if gap > MIN_CLUSTER_GAP:
                clusters.append([i, i])
            else:
                clusters[-1][1] = i
            gap = 0
        else:
            gap += 1

    if not clusters:
        return None

    # Prefer the rightmost cluster narrow enough to plausibly be a logo, not
    # a sentence -- if the rightmost is too wide, it's likely body text with
    # no separate watermark cluster in view (nothing to remove).
    max_width = (w - x0) * MAX_CLUSTER_WIDTH_FRAC
    for start, end in reversed(clusters):
        width = end - start
        if MIN_CLUSTER_WIDTH <= width <= max_width:
            local_box_x0, local_box_x1 = start, end
            break
    else:
        return None

    # Tighten the y-range to the actual ink extent within that column range.
    col_slice = region[:, local_box_x0:local_box_x1 + 1]
    row_diff = np.abs(col_slice.astype(int) - bg).sum(axis=2)
    ink_rows = np.where((row_diff > INK_DIFF_THRESHOLD).any(axis=1))[0]
    if len(ink_rows) == 0:
        return None
    local_y0, local_y1 = ink_rows.min(), ink_rows.max()

    box = (
        max(0, x0 + local_box_x0 - PADDING),
        max(0, y0 + local_y0 - PADDING),
        min(w, x0 + local_box_x1 + PADDING),
        min(h, y0 + local_y1 + PADDING),
    )
    return box


def clean_slide(img: Image.Image) -> Image.Image:
    img = img.convert('RGB')
    box = _find_watermark_box(img)
    if box is None:
        return img

    bx0, by0, bx1, by1 = box
    box_w, box_h = bx1 - bx0, by1 - by0

    sample_box = (max(0, bx0 - box_w - 10), by0, max(0, bx0 - 10), by1)
    if sample_box[2] <= sample_box[0]:
        sample_box = (bx0, by0, bx1, by1)  # degenerate fallback, rare
    patch_src = img.crop(sample_box)

    patch_arr = np.array(patch_src)
    is_flat = patch_arr.reshape(-1, 3).std(axis=0).mean() < FLAT_STD_THRESHOLD

    out = img.copy()
    if is_flat:
        color = tuple(int(c) for c in patch_arr.reshape(-1, 3).mean(axis=0))
        fill = Image.new('RGB', (box_w, box_h), color)
    else:
        fill = patch_src.filter(ImageFilter.GaussianBlur(8)).resize((box_w, box_h))
    out.paste(fill, (bx0, by0))
    return out


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__)
        return 1

    src, dst = Path(argv[1]), Path(argv[2])

    if src.is_dir():
        dst.mkdir(parents=True, exist_ok=True)
        pngs = sorted(src.glob('*.png'))
        if not pngs:
            print(f'No PNGs found in {src}')
            return 1
        for path in pngs:
            cleaned = clean_slide(Image.open(path))
            out_path = dst / path.name
            cleaned.save(out_path)
            print(f'{path.name} -> {out_path}')
    else:
        cleaned = clean_slide(Image.open(src))
        dst.parent.mkdir(parents=True, exist_ok=True)
        cleaned.save(dst)
        print(f'{src} -> {dst}')

    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
