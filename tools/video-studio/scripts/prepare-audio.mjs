/**
 * Generate ONE continuous narration take and extract per-scene cue times from it.
 *
 * Why one take: TTS derives prosody from sentence context. Generating each beat
 * separately and stitching produces the "reading slides aloud" effect — every clip
 * starts cold and ends flat. A single pass keeps natural momentum, and we recover
 * the scene boundaries afterwards from edge-tts's own subtitle output.
 *
 *   node scripts/prepare-audio.mjs content/video-a.json
 */
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import ffmpegPath from 'ffmpeg-static';

const HERE = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const cfg = JSON.parse(readFileSync(path.resolve(HERE, process.argv[2]), 'utf8'));

// Namespace per composition id — a shared narration.mp3/timings.json meant
// generating a second video silently clobbered the first one's assets.
const ID = cfg.id || 'Video';
const PUBLIC = path.join(HERE, 'public');
mkdirSync(PUBLIC, { recursive: true });
const mp3 = path.join(PUBLIC, `narration-${ID}.mp3`);
const vtt = path.join(PUBLIC, `narration-${ID}.vtt`);
const TTS = path.join(HERE, '.venv/bin/edge-tts');

console.log(`▶ narrating as ${cfg.voice} (one continuous take)`);
execFileSync(TTS, [
  '--voice', cfg.voice,
  `--rate=${cfg.rate || '-6%'}`,
  '--text', cfg.narration,
  '--write-media', mp3,
  '--write-subtitles', vtt,
], { stdio: ['ignore', 'pipe', 'pipe'] });

// ── duration ────────────────────────────────────────────────────────────────
function durationOf(file) {
  let err = '';
  try { execFileSync(ffmpegPath, ['-i', file], { stdio: ['ignore', 'pipe', 'pipe'] }); }
  catch (e) { err = String(e.stderr || ''); }
  const m = err.match(/Duration:\s*(\d+):(\d+):(\d+\.\d+)/);
  if (!m) throw new Error('no duration for ' + file);
  return (+m[1]) * 3600 + (+m[2]) * 60 + parseFloat(m[3]);
}
const total = durationOf(mp3);

// ── parse the subtitle file into [{start, text}] ────────────────────────────
// edge-tts emits SRT (numeric index, COMMA decimals: 00:00:04,162), not WebVTT.
// Cues are sentence-level, which is exactly the granularity we want.
const raw = readFileSync(vtt, 'utf8');
const cues = [];
{
  const blocks = raw.replace(/\r/g, '').split(/\n\s*\n/);
  const TS = /(\d\d):(\d\d):(\d\d)[.,](\d+)\s*-->/;
  for (const block of blocks) {
    const lines = block.split('\n').filter(Boolean);
    const tsLine = lines.find((l) => TS.test(l));
    if (!tsLine) continue;
    const m = tsLine.match(TS);
    const start = (+m[1]) * 3600 + (+m[2]) * 60 + (+m[3]) + (+`0.${m[4]}`);
    const text = lines.slice(lines.indexOf(tsLine) + 1).join(' ').replace(/\s+/g, ' ').trim();
    if (text) cues.push({ start, text });
  }
}
if (!cues.length) throw new Error('could not parse subtitle cues');

// running transcript with a char-offset -> cue-start index
let transcript = '';
const offsets = [];
for (const c of cues) {
  offsets.push({ at: transcript.length, start: c.start });
  transcript += (transcript ? ' ' : '') + c.text;
}
const norm = transcript.toLowerCase().replace(/[^a-z0-9 ]/g, '');
// map normalised offsets back onto raw offsets
const rawToNorm = [];
{
  let n = 0;
  for (let i = 0; i < transcript.length; i++) {
    const ch = transcript[i].toLowerCase();
    rawToNorm[i] = n;
    if (/[a-z0-9 ]/.test(ch)) n++;
  }
}
function startForPhrase(phrase) {
  const p = phrase.toLowerCase().replace(/[^a-z0-9 ]/g, '');
  const idx = norm.indexOf(p);
  if (idx === -1) return null;
  // find the raw offset whose normalised position is idx
  let rawIdx = rawToNorm.findIndex((v) => v >= idx);
  if (rawIdx === -1) rawIdx = 0;
  let best = offsets[0];
  for (const o of offsets) { if (o.at <= rawIdx) best = o; else break; }
  return best.start;
}

const scenes = cfg.scenes.map((s, i) => {
  const start = i === 0 ? 0 : startForPhrase(s.marker);
  if (start === null) throw new Error(`marker not found in narration: "${s.marker}"`);
  return { key: s.key, start };
});
scenes.forEach((s, i) => { s.end = i < scenes.length - 1 ? scenes[i + 1].start : total; });

const out = { id: ID, audio: `narration-${ID}.mp3`, total, fps: 30, scenes };
writeFileSync(path.join(HERE, 'src', `timings-${ID}.json`), JSON.stringify(out, null, 2));
if (ID === 'VideoA') writeFileSync(path.join(HERE, 'src', 'timings.json'), JSON.stringify(out, null, 2));

console.log(`  duration ${total.toFixed(1)}s`);
scenes.forEach(s => console.log(`  ${s.key.padEnd(10)} ${s.start.toFixed(2)}s → ${s.end.toFixed(2)}s  (${(s.end - s.start).toFixed(1)}s)`));
console.log(`\n✅ public/narration.mp3 + src/timings.json`);
