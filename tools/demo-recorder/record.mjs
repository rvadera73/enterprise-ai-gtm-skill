/**
 * enterprise-gtm — demo recorder
 *
 * Renders a narrated product video to MP4 with no paid services and no sudo:
 *   edge-tts   -> one narration clip per beat (alternating male/female voices)
 *   ffmpeg     -> pad each clip so audio length == slide hold length
 *   Playwright -> drive the page, advancing on those exact durations, record webm
 *   ffmpeg     -> mux audio + video -> 1:1 MP4
 *
 * Because slide holds are derived FROM the audio durations, narration and visuals
 * stay in lockstep automatically — no manual syncing.
 *
 * Usage:
 *   node record.mjs --config config/<name>.json
 */
import { chromium } from '@playwright/test';
import ffmpegPath from 'ffmpeg-static';
import { execFileSync } from 'node:child_process';
import { readFileSync, mkdirSync, rmSync, existsSync, writeFileSync, readdirSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const argv = process.argv.slice(2);
const cfgPath = argv[argv.indexOf('--config') + 1];
if (!cfgPath || argv.indexOf('--config') === -1) {
  console.error('usage: node record.mjs --config config/<name>.json');
  process.exit(1);
}
const cfg = JSON.parse(readFileSync(path.resolve(HERE, cfgPath), 'utf8'));

const OUT = path.resolve(HERE, cfg.outDir || 'out');
const CLIPS = path.join(OUT, 'clips');
const RAW = path.join(OUT, 'raw');
rmSync(OUT, { recursive: true, force: true });
mkdirSync(CLIPS, { recursive: true });
mkdirSync(RAW, { recursive: true });

const ff = (args) => execFileSync(ffmpegPath, args, { stdio: ['ignore', 'pipe', 'pipe'] });
const TTS = path.join(HERE, '.venv/bin/edge-tts');
if (!existsSync(TTS)) {
  console.error('edge-tts missing — run: npm run setup');
  process.exit(1);
}

/** ffmpeg prints duration to stderr; parse it rather than shipping ffprobe. */
function durationOf(file) {
  let err = '';
  try { execFileSync(ffmpegPath, ['-i', file], { stdio: ['ignore', 'pipe', 'pipe'] }); }
  catch (e) { err = String(e.stderr || ''); }
  const m = err.match(/Duration:\s*(\d+):(\d+):(\d+\.\d+)/);
  if (!m) throw new Error('could not read duration of ' + file);
  return (+m[1]) * 3600 + (+m[2]) * 60 + parseFloat(m[3]);
}

// ── 1. narrate each beat, alternating voices ────────────────────────────────
const pad = cfg.padSeconds ?? 0.6;
const beats = [];
console.log(`\n▶ narrating ${cfg.beats.length} beats (${cfg.voices.join(' / ')})`);

cfg.beats.forEach((beat, i) => {
  const voice = beat.voice || cfg.voices[i % cfg.voices.length];
  const rawMp3 = path.join(CLIPS, `${String(i + 1).padStart(2, '0')}-raw.mp3`);
  const outMp3 = path.join(CLIPS, `${String(i + 1).padStart(2, '0')}.mp3`);

  // NOTE: `--rate=-8%` must use the equals form — argparse reads a bare "-8%"
  // as a flag and errors with "expected one argument".
  execFileSync(TTS, [
    '--voice', voice,
    `--rate=${cfg.rate || '-8%'}`,
    '--text', beat.text,
    '--write-media', rawMp3,
  ], { stdio: ['ignore', 'pipe', 'pipe'] });

  const spoken = durationOf(rawMp3);
  const hold = +(spoken + pad).toFixed(3);
  // pad with trailing silence so the audio clip length == the slide hold exactly
  ff(['-y', '-i', rawMp3, '-af', `apad=pad_dur=${pad}`, '-t', String(hold),
      '-ar', '24000', '-ac', '1', '-c:a', 'libmp3lame', '-q:a', '4', outMp3]);

  beats.push({ i, voice, spoken, hold, file: outMp3, text: beat.text });
  console.log(`  ${String(i + 1).padStart(2, '0')}  ${voice.padEnd(20)} ${spoken.toFixed(2)}s -> hold ${hold.toFixed(2)}s`);
});

const total = beats.reduce((s, b) => s + b.hold, 0);
console.log(`  total: ${total.toFixed(1)}s`);

// ── 2. drive the page and record ────────────────────────────────────────────
console.log(`\n▶ recording ${cfg.url}`);
const W = cfg.width || 1080, H = cfg.height || 1080;

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: W, height: H },
  deviceScaleFactor: cfg.deviceScaleFactor || 1,
  recordVideo: { dir: RAW, size: { width: W, height: H } },
  reducedMotion: 'no-preference',
});
const page = await context.newPage();
await page.goto(cfg.url, { waitUntil: 'load' });
if (cfg.injectCss) await page.addStyleTag({ content: cfg.injectCss });
await page.waitForTimeout(cfg.leadInMs ?? 700);

for (const b of beats) {
  await page.waitForTimeout(Math.round(b.hold * 1000));
  if (b.i < beats.length - 1) await page.keyboard.press(cfg.advanceKey || 'Space');
}
await page.waitForTimeout(cfg.tailMs ?? 900);

await context.close();
await browser.close();

const webm = readdirSync(RAW).filter(f => f.endsWith('.webm')).map(f => path.join(RAW, f))[0];
if (!webm) { console.error('no video produced'); process.exit(1); }
console.log(`  captured ${(durationOf(webm)).toFixed(1)}s of video`);

// ── 3. concat narration ─────────────────────────────────────────────────────
const listFile = path.join(CLIPS, 'list.txt');
writeFileSync(listFile, beats.map(b => `file '${b.file.replace(/'/g, "'\\''")}'`).join('\n'));
const narration = path.join(OUT, 'narration.mp3');
ff(['-y', '-f', 'concat', '-safe', '0', '-i', listFile, '-c', 'copy', narration]);

// ── 4. mux -> mp4 ───────────────────────────────────────────────────────────
const final = path.join(OUT, cfg.output || 'video.mp4');
ff(['-y',
  '-i', webm,
  '-i', narration,
  '-map', '0:v:0', '-map', '1:a:0',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '20', '-pix_fmt', 'yuv420p',
  '-vf', `scale=${W}:${H}:force_original_aspect_ratio=decrease,pad=${W}:${H}:(ow-iw)/2:(oh-ih)/2,fps=30`,
  '-c:a', 'aac', '-b:a', '160k', '-shortest',
  '-movflags', '+faststart',
  final,
]);

// ── 5. contact-sheet so the result can be eyeballed without playback ────────
const sheet = path.join(OUT, 'frames.jpg');
try {
  ff(['-y', '-i', final, '-vf', `fps=1/${Math.max(2, Math.round(total / 9))},scale=340:-1,tile=3x3`,
      '-frames:v', '1', '-q:v', '3', sheet]);
} catch { /* contact sheet is a convenience, never fatal */ }

console.log(`\n✅ ${final}`);
console.log(`   ${durationOf(final).toFixed(1)}s · ${W}x${H}`);
if (existsSync(sheet)) console.log(`   contact sheet: ${sheet}`);
