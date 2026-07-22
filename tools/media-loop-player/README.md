# media-loop-player

Unattended, looping media player for demo/kiosk use — cycles through videos, PDFs,
and images in filename order, no interaction required after launch. Built for
GTM booth/kiosk displays (conferences, lobby screens, sales demos).

## How it works

- `index.html` — the player. Loads `playlist.js`, plays videos to completion,
  shows PDFs/images for a fixed duration, then advances. Loops forever.
- `playlist.js` — ordered array of filenames in `media/`. Regenerate with
  `generate-playlist.ps1` after adding/renaming files.
- `generate-playlist.ps1` — scans `media/`, sorts by filename, writes `playlist.js`.
  Prefix files with `01_`, `02_`, `03_`, `04_`... to control play order.
- `launch.bat` — opens the player full-screen in Chrome kiosk mode with
  autoplay unrestricted (falls back to default browser if Chrome isn't found).

## Using it for a new project/campaign

1. Copy this whole folder to `examples/<vertical>/<project>/media-loop/`.
2. Drop your media files into `media/`, prefixed with `01_`, `02_`, ... for order.
3. Run `generate-playlist.ps1` (PowerShell, on Windows) to rebuild `playlist.js`.
4. Double-click `launch.bat` to run it unattended. Press `Esc` to stop/resume.

## Config

Edit the `CONFIG` block at the top of the `<script>` in `index.html`:
- `imageDurationMs` — how long each image is shown (default 8000ms)
- `pdfDurationMs` — how long each PDF is shown (default 15000ms)

Videos play through to their natural end regardless of these settings.

## Reference instance

`examples/federal/iacp-2.1/media-loop/` — IACP-2.1 (Intelligent Case Portal)
demo loop: two-pager PDF + highlight PNG today, 2 demo videos to be added.
