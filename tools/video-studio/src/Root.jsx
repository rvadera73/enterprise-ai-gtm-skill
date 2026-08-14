import React from 'react';
import { Composition, staticFile, interpolate } from 'remotion';
import { VideoA } from './VideoA.jsx';
import { VideoB } from './VideoB.jsx';
import { SharedVideoPanel, Panel, ramp } from './SharedVideoPanel.jsx';
import { RF } from './theme-riskforge.js';
import timingsA from './timings-VideoA.json';
import timingsB from './timings-VideoB.json';
import timingsAPanel from './timings-VideoA-Panel.json';
import timingsB2Panel from './timings-VideoB2-Panel.json';
import timingsCPanel from './timings-VideoC-Panel.json';
import captionsAPanel from './captions-VideoA-Panel.json';
import captionsB2Panel from './captions-VideoB2-Panel.json';

import Anvil from 'lucide/dist/esm/icons/anvil.mjs';
import Sparkles from 'lucide/dist/esm/icons/sparkles.mjs';

const FPS = 30;
const frames = (t) => Math.ceil((t.total + 0.9) * FPS);

// Strike-through fade for the precision-reveal scene's old "2.8%" figure
// (a different [start,end] pair than `ramp`'s single-start ramp, hence not
// reusing `ramp` here — matches the original VideoC_Panel.jsx behavior).
const fadeOldFigure = (p) => interpolate(p, [0.9, 1.3], [1, 0.45], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

// ── Shared RiskModelForgeIQ palette, wired into the SharedVideoPanel theme
// shape (content/video/DESIGN-SYSTEM.md §1 capability accent family:
// blue/teal/purple/green). All three RiskModelForgeIQ videos use the same
// product colors today; a future different product would only need a new
// `colors`/`productName`/`tagline` block here, not a new component file.
const RF_COLORS = {
  bg: RF.bg, bgDeep: RF.bgDeep, surface: RF.surface, surfaceRaised: RF.surfaceRaised,
  surfaceLine: RF.surfaceLine, ink: RF.ink, inkMuted: RF.inkMuted, inkFaint: RF.inkFaint,
  accent: RF.forge, accentDeep: RF.forgeDeep, accentSoft: RF.forgeSoft,
  steel: RF.steel, steelSoft: RF.steelSoft, steelDeep: RF.steelDeep,
  purple: RF.purple, good: RF.good,
  capabilityAccents: [RF.forge, RF.steel, RF.purple, RF.good],
  display: RF.display, mono: RF.mono,
};

// ── Video A (Panel edition) theme — 1080x1080 square canvas.
const videoAPanelTheme = {
  productName: 'RiskModelForgeIQ',
  tagline: 'Your Decision Intelligence Layer',
  colors: RF_COLORS,
  brandIcon: Anvil,
  fontFaceUrl: null, // VideoA never vendored the Inter woff2; keeps prior font-stack fallback
  canvas: { width: 1080, height: 1080 },
  panel: { x: 40, y: 168, w: 1080 - 80, h: 726, footerH: 64 },
  captions: { enabled: true, barH: 70 },
  audio: { enabled: true, src: timingsAPanel.audio },
  slidesDir: 'slides',
  kenBurns: {
    intro: { from: 1.0, to: 1.05, x: 0, y: 0 },
    evidence: { from: 1.02, to: 1.08, x: -1, y: 0 },
    layer: { from: 1.0, to: 1.06, x: 1, y: -1 },
    defensible: { from: 1.02, to: 1.07, x: 0, y: 1 },
    shadow: { from: 1.0, to: 1.05, x: -1, y: 1 },
    close: { from: 1.02, to: 1.08, x: 0, y: 0 },
  },
  cta: {
    icon: Sparkles, iconSize: 38, titleSize: 30, urlSize: 16, subSize: 17,
    title: 'Try RiskModelForgeIQ',
    url: 'riskmodelforgeiq-demo-xdkyxlbwxa-uc.a.run.app',
    sub: 'Link in the post',
  },
  customScenes: null,
};

// ── Video B2 (Panel edition) theme — 1920x1080, deck-native 16:9 fit.
const videoB2PanelTheme = {
  productName: 'RiskModelForgeIQ',
  tagline: 'Your Decision Intelligence Layer',
  colors: RF_COLORS,
  brandIcon: Anvil,
  fontFaceUrl: staticFile('fonts/Inter.woff2'),
  canvas: { width: 1920, height: 1080 },
  panel: { x: 88, y: 28, w: 1744, h: 1030, footerH: 64 },
  captions: { enabled: true, barH: 70 },
  audio: { enabled: true, src: timingsB2Panel.audio },
  slidesDir: 'slides-v2',
  kenBurns: {
    page_01: { from: 1.0, to: 1.05, x: 0, y: 0 },
    page_02: { from: 1.02, to: 1.07, x: -1, y: 0 },
    page_03: { from: 1.0, to: 1.06, x: 1, y: -1 },
    page_04: { from: 1.02, to: 1.07, x: 0, y: 1 },
    page_05: { from: 1.0, to: 1.05, x: -1, y: 1 },
    page_06: { from: 1.02, to: 1.08, x: 1, y: 0 },
    page_07: { from: 1.0, to: 1.06, x: 0, y: -1 },
    page_08: { from: 1.02, to: 1.07, x: -1, y: 0 },
  },
  cta: {
    icon: Sparkles, iconSize: 44, titleSize: 40, urlSize: 19, subSize: 20,
    title: 'Try RiskModelForgeIQ',
    url: 'riskmodelforgeiq-demo-xdkyxlbwxa-uc.a.run.app',
    sub: 'See the governance engine in action',
  },
  customScenes: null,
};

// ── Video C (Panel edition) theme — 1920x1080, graphic beats only (no
// audio baked in; narration is muxed separately at the ffmpeg stitch step,
// no CTA scene). Beat 3's precision-reveal insert is bespoke numeric/text
// staging (never a NotebookLM slide), ported here as a `customScenes` entry
// exactly as it behaved in the old VideoC_Panel.jsx.
const precisionRevealScene = (p, _dur, theme) => {
  const { colors } = theme;
  const stage = (start, dur = 0.5) => ramp(start, dur)(p);
  return (
    <Panel theme={theme} noFooter>
      <div style={{
        position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column',
        alignItems: 'center', justifyContent: 'center', gap: 18,
      }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 28, opacity: stage(0) }}>
          <span style={{ fontFamily: colors.mono, fontSize: 64, fontWeight: 700, color: colors.inkMuted, textDecoration: p > 0.9 ? 'line-through' : 'none', opacity: fadeOldFigure(p) }}>
            2.8%
          </span>
          <span style={{ fontFamily: colors.mono, fontSize: 40, color: colors.steel, opacity: stage(0.9) }}>→</span>
          <span style={{ fontFamily: colors.mono, fontSize: 84, fontWeight: 800, color: colors.accent, opacity: stage(0.9) }}>
            15.2%
          </span>
        </div>
        <div style={{ fontFamily: colors.display, fontSize: 22, letterSpacing: '.08em', textTransform: 'uppercase', color: colors.inkMuted, opacity: stage(1.6) }}>
          Measured Precision
        </div>
        <div style={{ fontFamily: colors.mono, fontSize: 30, fontWeight: 700, color: colors.purple, marginTop: 8, opacity: stage(2.6) }}>
          +5.4× MEASURED PRECISION
        </div>
        <div style={{ display: 'flex', gap: 40, marginTop: 28 }}>
          <div style={{
            fontFamily: colors.display, fontSize: 26, fontWeight: 700, color: colors.ink,
            border: `1.5px solid ${colors.surfaceLine}`, borderRadius: 12, padding: '14px 26px',
            opacity: stage(5.0),
          }}>
            NO MODEL CHANGE
          </div>
          <div style={{
            fontFamily: colors.display, fontSize: 26, fontWeight: 700, color: colors.bgDeep,
            background: colors.steel, borderRadius: 12, padding: '14px 26px',
            opacity: stage(7.0),
          }}>
            RULES BECAME TUNABLE
          </div>
        </div>
      </div>
    </Panel>
  );
};
const videoCPanelTheme = {
  productName: 'RiskModelForgeIQ',
  tagline: 'Your Decision Intelligence Layer',
  colors: RF_COLORS,
  brandIcon: Anvil,
  fontFaceUrl: staticFile('fonts/Inter.woff2'),
  canvas: { width: 1920, height: 1080 },
  panel: { x: 88, y: 28, w: 1744, h: 1030, footerH: 64 },
  captions: { enabled: false },
  audio: { enabled: false },
  slidesDir: 'slides-v3',
  kenBurns: {
    final_02: { from: 1.0, to: 1.05, x: 0, y: 0 },   // beat 0: disagreement reveal
    final_03: { from: 1.02, to: 1.07, x: -1, y: 0 }, // beat 1: architecture pipeline
    final_04: { from: 1.0, to: 1.06, x: 1, y: -1 },  // beat 8: zoom-out lifecycle
    final_05: { from: 1.02, to: 1.06, x: 0, y: 0 },  // beat 9a: MLOps card
    final_06: { from: 1.02, to: 1.06, x: 0, y: 0 },  // beat 9b: DecisionOps card
    final_01: { from: 1.0, to: 1.04, x: 0, y: 0 },   // beat 9c: title/tagline close
  },
  cta: null,
  customScenes: { 'precision-reveal': precisionRevealScene },
};

export const RemotionRoot = () => (
  <>
    <Composition id="VideoA" component={VideoA} durationInFrames={frames(timingsA)}
      fps={FPS} width={1080} height={1080} />
    <Composition id="VideoB" component={VideoB} durationInFrames={frames(timingsB)}
      fps={FPS} width={1080} height={1080} />
    {/* All three "*Panel" compositions below now render through the single
        SharedVideoPanel.jsx component (content/video/DESIGN-SYSTEM.md §7),
        configured entirely via defaultProps.theme instead of a bespoke file
        per video. VideoA_Panel.jsx / VideoB2_Panel.jsx / VideoC_Panel.jsx
        are kept in place as superseded references, not deleted. */}
    <Composition id="RiskForgeVideoAPanel" component={SharedVideoPanel} durationInFrames={frames(timingsAPanel)}
      fps={FPS} width={1080} height={1080}
      defaultProps={{ theme: videoAPanelTheme, timings: timingsAPanel, captionWords: captionsAPanel }} />
    {/* 1920x1080 (16:9), not 1080x1080 -- deck slides are natively ~1.79:1;
        forcing them into a square canvas was the root cause of the "too much
        blank space above/below the slide" defect. See VideoB2_Panel.jsx. */}
    <Composition id="RiskForgeVideoB2Panel" component={SharedVideoPanel} durationInFrames={frames(timingsB2Panel)}
      fps={FPS} width={1920} height={1080}
      defaultProps={{ theme: videoB2PanelTheme, timings: timingsB2Panel, captionWords: captionsB2Panel }} />
    {/* Video 3's 4 graphic beats (0, 1, 8, 9) + the Beat 3 precision-reveal
        insert, rendered as one contiguous internal timeline (no audio baked
        in -- narration is muxed separately at the ffmpeg stitch step). Scene
        boundaries in timings-VideoC-Panel.json are used to extract each
        segment's sub-range during that stitch, not played back as one piece. */}
    <Composition id="RiskForgeVideoCPanel" component={SharedVideoPanel} durationInFrames={frames(timingsCPanel)}
      fps={FPS} width={1920} height={1080}
      defaultProps={{ theme: videoCPanelTheme, timings: timingsCPanel, captionWords: null }} />
  </>
);
