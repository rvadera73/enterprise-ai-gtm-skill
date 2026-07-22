# IACP-2.1 demo loop

Unattended kiosk/demo player for IACP-2.1 (Intelligent Case Portal). Built from
the reusable [`tools/media-loop-player`](../../../../tools/media-loop-player) template.

## Current media (`media/`)

- `03_Unified-Case-Management.pdf` — two-pager
- `04_IACP-2.1-AI-Engineering-Highlight.png` — highlight image

## Adding the 2 videos

1. Drop the two video files into `media/`, named `01_<name>.mp4` and
   `02_<name>.mp4` so they play first (before the PDF/PNG).
2. Re-run `generate-playlist.ps1` in this folder (PowerShell) to rebuild
   `playlist.js`.
3. Double-click `launch.bat` — it opens full-screen in Chrome, autoplays with
   sound, and loops forever with no further interaction. Press `Esc` to
   stop/resume.

## Notes

- This folder is self-contained (own copy of `index.html`/`launch.bat`), so it
  can be zipped/copied to another machine or a USB drive as-is.
- Default display time: images 8s, PDF 15s — adjust in `index.html`'s
  `CONFIG` block if needed.
