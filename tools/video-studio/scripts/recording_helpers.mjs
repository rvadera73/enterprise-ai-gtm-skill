// Reusable Playwright helpers for GTM demo-video recording scripts.
//
// This is a REFERENCE MODULE to copy into a product's own recording script (e.g.
// cbp-risk-engine/scripts/gtm_record_video3.mjs), not a cross-repo import -- the
// actual recording code lives in each product's repo, same as the rest of this
// skill's "reference implementation" pattern (a storyboard or script to copy from,
// not a shared library another repo pulls in directly).
//
// Why this exists: this session's two most expensive real recording bugs were both
// fixed with a FIXED sleep duration (a flat 2000ms after a domain switch, then two
// rounds of extending a beat's recording window) -- a fixed sleep can only ever
// approximate the real settle time, and both fixes were arrived at by trial and
// error against one specific app under one specific load. A poll-until-ready
// pattern removes the guesswork: it waits exactly as long as the real condition
// takes, with a sane upper bound, and it FAILS LOUDLY on timeout instead of silently
// proceeding with an unsettled page (which is what let the domain-switch race and
// the short-recording-window bugs both slip through unnoticed until playback).

/**
 * Poll a predicate against the page until it returns true, instead of sleeping a
 * fixed duration and hoping. Use this in place of `page.waitForTimeout(N)` for any
 * "wait for the app to settle" step.
 *
 * @param {import('playwright').Page} page
 * @param {(page: import('playwright').Page) => Promise<boolean>} predicateFn
 * @param {{ pollMs?: number, timeoutMs?: number, label?: string }} [opts]
 * @returns {Promise<boolean>} true if the predicate resolved true before timeout
 */
export async function waitUntilSettled(page, predicateFn, opts = {}) {
  const { pollMs = 250, timeoutMs = 8000, label = 'settle condition' } = opts;
  const started = Date.now();
  while (Date.now() - started < timeoutMs) {
    if (await predicateFn(page)) {
      const elapsed = Date.now() - started;
      console.log(`  [waitUntilSettled] "${label}" settled after ${elapsed}ms`);
      return true;
    }
    await page.waitForTimeout(pollMs);
  }
  console.log(
    `  WARNING [waitUntilSettled] "${label}" did NOT settle within ${timeoutMs}ms -- ` +
      `proceeding anyway, but this recording may be unsettled. Do not treat this as a ` +
      `silent pass; re-check the resulting frames (see qa_frame_sample.py).`
  );
  return false;
}

/**
 * Wait for a loading/spinner indicator (matched by visible text) to disappear from
 * the page, instead of a fixed sleep. Generalizes the one-off
 * `page.waitForFunction(() => !document.body.innerText.includes(spinnerText))`
 * pattern used inline in earlier recording scripts into a named, reusable helper.
 *
 * @param {import('playwright').Page} page
 * @param {string} spinnerText - substring to search for in document.body.innerText
 * @param {{ timeoutMs?: number }} [opts]
 * @returns {Promise<boolean>} true if the spinner text disappeared before timeout
 */
export async function waitUntilSpinnerGone(page, spinnerText, opts = {}) {
  const { timeoutMs = 15000 } = opts;
  try {
    await page.waitForFunction(
      (text) => !document.body.innerText.includes(text),
      spinnerText,
      { timeout: timeoutMs }
    );
    return true;
  } catch {
    console.log(
      `  WARNING [waitUntilSpinnerGone] "${spinnerText}" still visible after ${timeoutMs}ms -- ` +
        `proceeding anyway. Check the resulting recording's frames before accepting it.`
    );
    return false;
  }
}

// Example usage, replacing a fixed-sleep domain-switch settle wait:
//
//   import { waitUntilSettled } from './recording_helpers.mjs';
//
//   await select.selectOption({ index: idx });
//   await waitUntilSettled(
//     page,
//     (p) => p.evaluate(() => window.__appReady === true), // or any real DOM/state check
//     { timeoutMs: 5000, label: 'domain switch settle' }
//   );
//
// If the app doesn't expose a clean readiness signal, the next-best real predicate
// is usually "the element I'm about to interact with is visible AND enabled" --
// checking the actual precondition for the next action, not a proxy for it.
