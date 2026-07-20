/**
 * Video B — capture the live demo.
 *
 * Records the local demo (access gate inert, so no sign-in) driving the real UI.
 * Playwright records the PAGE VIEWPORT only, so no browser chrome or URL appears.
 *
 * Emits out/demo-raw.webm plus out/demo-cues.json — the wall-clock time of each
 * beat, so the narration and hand-drawn callouts can be aligned to what is
 * actually on screen rather than guessed.
 *
 *   node record-demo.mjs [--url http://localhost:5173/demo]
 */
import { chromium } from '@playwright/test';
import { mkdirSync, rmSync, readdirSync, writeFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const argv = process.argv.slice(2);
const URL = argv.includes('--url') ? argv[argv.indexOf('--url') + 1] : 'http://localhost:5173/demo';
// Taller viewport so the role cards AND the chat are on screen together — otherwise
// every role change needs a scroll, which reads badly on video.
const W = 1280, H = 1400;

const OUT = path.join(HERE, 'out');
const RAW = path.join(OUT, 'raw-demo');
rmSync(RAW, { recursive: true, force: true });
mkdirSync(RAW, { recursive: true });

const cues = [];
let t0;
const mark = (name) => {
  const at = (Date.now() - t0) / 1000;
  cues.push({ name, at: +at.toFixed(2) });
  console.log(`  ${at.toFixed(1).padStart(6)}s  ${name}`);
};

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: W, height: H },
  deviceScaleFactor: 2,
  recordVideo: { dir: RAW, size: { width: W, height: H } },
  reducedMotion: 'no-preference',
});
const page = await context.newPage();

// keep the cursor visible-ish: slow, deliberate movement reads better on video
const settle = (ms) => page.waitForTimeout(ms);

async function pickRole(name) {
  const btn = page.locator('button', { hasText: name }).first();
  await btn.scrollIntoViewIfNeeded();
  await btn.hover();
  await settle(420);
  await btn.click();
  await settle(700);
}

async function askStarter(fragment) {
  const btn = page.locator('button', { hasText: fragment }).first();
  await btn.scrollIntoViewIfNeeded();
  await btn.hover();
  await settle(420);
  await btn.click();
}

/**
 * Wait for a string we know only appears in THIS beat's answer.
 * DOM-shape guessing (counting .prose / [class*=Message]) silently never matched
 * and burned the full timeout on every beat — waiting on real answer content is
 * both robust and self-documenting.
 */
/** Wait for the analytics chart to actually render (vega-embed -> svg/canvas). */
async function waitForChart(timeout = 90000) {
  try {
    await page.locator('.vega-embed, .vega-embed canvas, .vega-embed svg, canvas')
      .first().waitFor({ state: 'visible', timeout });
    await settle(1400);
    console.log('    chart rendered');
    return true;
  } catch {
    console.log('    ! chart never rendered');
    return false;
  }
}

async function waitForText(fragment, timeout = 75000) {
  try {
    await page.getByText(fragment, { exact: false }).first().waitFor({ state: 'visible', timeout });
    await settle(900);
    return true;
  } catch {
    console.log(`    ! never saw "${fragment}"`);
    return false;
  }
}

console.log(`▶ recording ${URL}  (${W}x${H})`);
await page.goto(URL, { waitUntil: 'networkidle' });
await page.evaluate(() => window.scrollTo(0, 0));
await settle(1500);
t0 = Date.now();
mark('open');

await settle(1600);

// 1 · day-to-day operations role
await pickRole('Docket Clerk');
mark('role_ops');
await askStarter('deadlines for case 2024-BLA-05432');
mark('ask_ops');
await waitForText('Upcoming deadlines');
mark('answer_ops');
await settle(2400);

// 2 · deeper review role — SAME case, deliberately
await pickRole('Attorney-Advisor');
mark('role_review');
await askStarter('full record for case 2024-BLA-05432');
mark('ask_review');
await waitForText('Whitfield');          // claimant name only the full record returns
mark('answer_review');
await settle(2800);

// 3 · analyst — plain English -> SQL -> chart
await pickRole('Analyst');
mark('role_analyst');
await askStarter('How many cases are there by office');
mark('ask_analyst');
// NOT a text match here: "Washington DC" also appears in the Attorney-Advisor
// answer above, so waiting on it returned instantly against stale content and the
// chart never got captured. Wait for the rendered chart element itself.
await waitForChart();
mark('answer_analyst');
await settle(5200);
mark('end');

await context.close();
await browser.close();

const webm = readdirSync(RAW).filter((f) => f.endsWith('.webm')).map((f) => path.join(RAW, f))[0];
writeFileSync(path.join(OUT, 'demo-cues.json'), JSON.stringify({ video: webm, width: W, height: H, cues }, null, 2));
console.log(`\n✅ ${webm}`);
console.log(`   cues -> out/demo-cues.json`);
