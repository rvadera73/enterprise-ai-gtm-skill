/**
 * Render the one-pager at exactly the Ask-AI sheet's pixel size:
 * 1240x1600 CSS @ deviceScaleFactor 2 = 2480x3200.
 */
import { chromium } from '@playwright/test';

const SRC = process.argv[2];
const OUT = process.argv[3];

const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: 1240, height: 1600 },
  deviceScaleFactor: 2,
});

const problems = [];
page.on('console', m => { if (m.type() === 'error') problems.push(m.text()); });
page.on('requestfailed', r => problems.push(`FAILED ${r.url()}`));

await page.goto('file://' + SRC, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);

// guard: Inter must actually be loaded, not silently falling back
const interLoaded = await page.evaluate(() =>
  document.fonts.check('800 61px InterVar'));
console.log('Inter loaded:', interLoaded);

// guard: content must not overflow the fixed sheet
const overflow = await page.evaluate(() =>
  document.body.scrollHeight - document.body.clientHeight);
console.log('vertical overflow (px):', overflow);

await page.screenshot({ path: OUT + '.png' });
await page.pdf({
  path: OUT + '.pdf', width: '1240px', height: '1600px',
  printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 },
});

if (problems.length) console.log('PAGE PROBLEMS:', problems);
console.log('wrote', OUT + '.png', OUT + '.pdf');
await browser.close();
