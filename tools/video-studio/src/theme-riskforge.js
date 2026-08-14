/**
 * RiskModelForgeIQ visual system — CORRECTED 2026-07-31 to the real, verified
 * portfolio palette, replacing the previously ad hoc "forge/molten-copper"
 * identity (invented for this video pipeline, never checked against the real
 * one-pager or DESIGN-SYSTEM.md).
 *
 * These are the exact values already sampled and verified in RiskModelForgeIQ's
 * own real one-pager (`cbp-risk-engine` docs/gtm/02-one-pager/), which itself
 * was confirmed to match Ask-AI's actual rendered one-pager PDF — dark slate
 * ground, Inter, blue/teal/purple/green accents. See
 * `enterprise-ai-gtm-skill/content/video/DESIGN-SYSTEM.md` §1 for the
 * portfolio-wide source of truth this now derives from.
 *
 * Property names kept stable (bg/forge/steel/etc.) so existing usage sites
 * (VideoA_Panel.jsx, VideoB2_Panel.jsx) don't need a rename to pick up the
 * corrected values — only the hex values changed, not the API.
 */
export const RF = {
  bg: '#0F172A',
  bgDeep: '#0B1220',
  surface: '#0E1A30',
  surfaceRaised: '#111A2E',
  surfaceLine: '#1E2C48',
  ink: '#D1D5DB',
  inkMuted: '#8A94A6',
  inkFaint: '#93A4BF',

  forge: '#60A5FA',
  forgeDeep: '#3B82F6',
  forgeSoft: '#60A5FA33',

  steel: '#2DD4BF',
  steelSoft: '#2DD4BF33',
  steelDeep: '#0F766E',

  purple: '#A78BFA',
  good: '#34D399',

  display: '"Inter", ui-sans-serif, system-ui, "Segoe UI", "Helvetica Neue", Arial, sans-serif',
  mono: 'ui-monospace, "SF Mono", "Cascadia Mono", "Segoe UI Mono", Consolas, monospace',
};
