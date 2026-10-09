/**
 * Render the one-pager HTML to PNG + PDF.
 * A LinkedIn post needs an IMAGE — HTML is not a deliverable.
 */
import { chromium } from '@playwright/test';
import path from 'node:path';

const SRC = process.argv[2];
const OUT = process.argv[3];

const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: 900, height: 1400 },
  deviceScaleFactor: 2,          // retina — stays crisp when LinkedIn re-compresses
});
await page.goto('file://' + SRC, { waitUntil: 'networkidle' });

// strip the grey page surround so the sheet itself is the image
await page.addStyleTag({ content: 'body{background:#fff !important;padding:0 !important} .sheet{box-shadow:none !important;max-width:none !important}' });
await page.waitForTimeout(400);

const sheet = page.locator('.sheet');
await sheet.screenshot({ path: OUT + '.png' });
await page.pdf({ path: OUT + '.pdf', format: 'A4', printBackground: true, margin: { top: '0', bottom: '0', left: '0', right: '0' } });

const box = await sheet.boundingBox();
console.log(`png: ${OUT}.png  (${Math.round(box.width)}x${Math.round(box.height)} css px @2x)`);
console.log(`pdf: ${OUT}.pdf`);
await browser.close();
