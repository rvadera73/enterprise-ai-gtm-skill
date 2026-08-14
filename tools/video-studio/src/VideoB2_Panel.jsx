// SUPERSEDED: kept as reference only — new work should use SharedVideoPanel.jsx
// (see Root.jsx's `videoB2PanelTheme`), the consolidated component this and
// VideoA_Panel.jsx/VideoC_Panel.jsx were merged into.
import React from 'react';
import {
  AbsoluteFill, Audio, staticFile,
  useCurrentFrame, useVideoConfig, interpolate, Easing,
} from 'remotion';
import { RF } from './theme-riskforge.js';
import { Icon } from './Icon.jsx';
import timings from './timings-VideoB2-Panel.json';
import captionWords from './captions-VideoB2-Panel.json';

import Anvil from 'lucide/dist/esm/icons/anvil.mjs';
import Sparkles from 'lucide/dist/esm/icons/sparkles.mjs';

const ease = Easing.out(Easing.cubic);

// ── 1920x1080 (16:9), not 1080x1080 — REBUILT 2026-07-31. The deck slides are
// natively 2867x1600 (~1.79:1, essentially 16:9). Forcing that into a square
// canvas is what caused the "too much blank space above/below the slide"
// complaint: object-fit:contain inside a taller-than-wide box letterboxes
// hard. Real research (see storyboard doc) confirms 16:9 is the recommended
// format specifically for slide/presentation-led content, preserving layout
// and readability -- this is the root-cause fix, not a bigger-font band-aid.
const CANVAS_W = 1920;
const CANVAS_H = 1080;

// Panel sized so its content area's aspect ratio (1744 / (1030-64) = 1.806)
// nearly exactly matches the real slide aspect (2867/1600 = 1.792) -- fitting
// by height leaves only ~6px of pillarbox, effectively invisible, instead of
// the ~100px+ letterbox bars the square canvas produced.
const PANEL_X = 88;
const PANEL_Y = 28;
const PANEL_W = 1744;
const PANEL_H = 1030;
const FOOTER_H = 64;

const ramp = (start, dur = 0.8) => (t) => interpolate(t, [start, start + dur], [0, 1], { easing: ease, extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

// Real Inter font (vendored from the actual RiskModelForgeIQ one-pager's own
// assets), not just named in the font stack without loading it.
const FontFace = () => (
  <style>{`
    @font-face {
      font-family: 'Inter';
      src: url('${staticFile('fonts/Inter.woff2')}') format('woff2');
      font-weight: 100 900;
      font-display: block;
    }
  `}</style>
);

const Background = ({ t }) => {
  const nodes = React.useMemo(() => {
    const pts = [];
    let seed = 7;
    const rand = () => { seed = (seed * 16807) % 2147483647; return seed / 2147483647; };
    for (let i = 0; i < 14; i++) pts.push({ x: rand() * 100, y: rand() * 100, ph: rand() * 10 });
    return pts;
  }, []);
  return (
    <AbsoluteFill style={{ background: `radial-gradient(ellipse 90% 70% at 50% 0%, ${RF.surfaceRaised} 0%, ${RF.bg} 55%, ${RF.bgDeep} 100%)` }}>
      <svg width="100%" height="100%" style={{ position: 'absolute', inset: 0 }}>
        {nodes.map((n, i) => nodes.slice(i + 1, i + 3).map((m, j) => (
          <line key={`${i}-${j}`} x1={`${n.x}%`} y1={`${n.y}%`} x2={`${m.x}%`} y2={`${m.y}%`}
            stroke={RF.steelSoft} strokeWidth={1} opacity={0.22 + 0.08 * Math.sin(t * 0.3 + n.ph)} />
        )))}
        {nodes.map((n, i) => (
          <circle key={i} cx={`${n.x}%`} cy={`${n.y}%`} r={2 + Math.sin(t * 0.5 + n.ph) * 0.8}
            fill={RF.steel} opacity={0.35 + 0.15 * Math.sin(t * 0.4 + n.ph)} />
        ))}
      </svg>
    </AbsoluteFill>
  );
};

// ── Panel embeds its own footer band (brand + tagline) — every scene gets it
// for free. Footer is now sized for real legibility (20px icon, 17px text,
// was 14/13 — genuinely too small per feedback), not just "slightly bigger."
const Panel = ({ x = PANEL_X, y = PANEL_Y, w = PANEL_W, h = PANEL_H, children }) => (
  <div style={{
    position: 'absolute', left: x, top: y, width: w, height: h,
    background: RF.surface, border: `1.5px solid ${RF.surfaceLine}`, borderRadius: 20,
    boxShadow: `inset 0 1px 0 ${RF.surfaceRaised}, 0 24px 60px -24px #00000070`,
    overflow: 'hidden', display: 'flex', flexDirection: 'column',
  }}>
    <div style={{ position: 'relative', flex: 1, minHeight: 0 }}>
      {children}
    </div>
    <div style={{
      flexShrink: 0, height: FOOTER_H, borderTop: `1px solid ${RF.surfaceLine}`,
      display: 'flex', alignItems: 'center', justifyContent: 'space-between',
      padding: '0 30px', background: RF.bgDeep,
    }}>
      <span style={{
        display: 'flex', alignItems: 'center', gap: 11, fontFamily: RF.mono,
        fontSize: 17, fontWeight: 600, letterSpacing: '.12em', textTransform: 'uppercase', color: RF.ink,
      }}>
        <Icon icon={Anvil} size={20} color={RF.forge} strokeWidth={2.1} />
        RiskModelForgeIQ
      </span>
      <span style={{ fontFamily: RF.mono, fontSize: 16, letterSpacing: '.12em', textTransform: 'uppercase', color: RF.steel }}>
        Your Decision Intelligence Layer
      </span>
    </div>
  </div>
);

const buildPhrases = (words) => {
  const phrases = [];
  let cur = [];
  for (const w of words) {
    cur.push(w);
    if (cur.length >= 5 || /[.?!]$/.test(w.w)) {
      phrases.push({ text: cur.map((x) => x.w).join(' '), start: cur[0].start, end: cur[cur.length - 1].end });
      cur = [];
    }
  }
  if (cur.length) phrases.push({ text: cur.map((x) => x.w).join(' '), start: cur[0].start, end: cur[cur.length - 1].end });
  return phrases;
};
const PHRASES = buildPhrases(captionWords);

// Captions sit right above the footer as a FULL-WIDTH, SOLID bar — not a
// floating pill sized to the text. A pill let real slide content (e.g. the
// "Mechanism 1" telemetry box, which runs close to the panel's bottom edge)
// peek out from behind it, reading as a glitch/cut-off sentence rather than
// an intentional overlay. A solid full-width bar always fully occludes
// whatever's behind it at that strip — the standard broadcast/subtitle-bar
// convention — so it reads as deliberate regardless of the slide underneath.
const CAPTION_BAR_H = 70;
const CAPTION_BAND_Y = PANEL_Y + PANEL_H - FOOTER_H - CAPTION_BAR_H;

const Captions = ({ t }) => {
  const active = PHRASES.find((p) => t >= p.start - 0.05 && t < p.end + 0.35);
  if (!active) return null;
  const o = ramp(active.start, 0.12)(t) * (t > active.end ? Math.max(0, 1 - (t - active.end) / 0.25) : 1);
  return (
    <div style={{
      position: 'absolute', left: PANEL_X + 1.5, width: PANEL_W - 3, top: CAPTION_BAND_Y,
      height: CAPTION_BAR_H, display: 'flex', alignItems: 'center', justifyContent: 'center',
      background: RF.bgDeep, opacity: o,
    }}>
      <span style={{ fontFamily: RF.display, fontSize: 24, fontWeight: 600, color: RF.ink, padding: '0 20px' }}>
        {active.text}
      </span>
    </div>
  );
};

// ── Slide scenes reuse the actual NotebookLM deck images for Video 2
// (watermark stripped, the one garbled-text slide title patched — see
// public/slides-v2/*.png provenance in storyboard-video2-policy-lifecycle.md).
const SLIDE_KEN_BURNS = {
  page_01: { from: 1.0, to: 1.05, x: 0, y: 0 },
  page_02: { from: 1.02, to: 1.07, x: -1, y: 0 },
  page_03: { from: 1.0, to: 1.06, x: 1, y: -1 },
  page_04: { from: 1.02, to: 1.07, x: 0, y: 1 },
  page_05: { from: 1.0, to: 1.05, x: -1, y: 1 },
  page_06: { from: 1.02, to: 1.08, x: 1, y: 0 },
  page_07: { from: 1.0, to: 1.06, x: 0, y: -1 },
  page_08: { from: 1.02, to: 1.07, x: -1, y: 0 },
};

const SlideImage = ({ p, src, dur = 20 }) => {
  const kb = SLIDE_KEN_BURNS[src] || { from: 1, to: 1.05, x: 0, y: 0 };
  const scale = interpolate(p, [0, Math.max(dur, 1)], [kb.from, kb.to], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const o = ramp(0, 0.6)(p);
  return (
    <Panel>
      <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden' }}>
        <img
          src={staticFile(`slides-v2/${src}.png`)}
          style={{
            width: '100%', height: '100%', objectFit: 'contain',
            transform: `scale(${scale}) translate(${kb.x}%, ${kb.y}%)`,
            opacity: o,
          }}
        />
      </div>
    </Panel>
  );
};

const CTA = ({ p }) => (
  <Panel>
    <div style={{ position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
      <Icon icon={Sparkles} size={44} color={RF.forge} strokeWidth={1.6} style={{ opacity: ramp(0, 0.6)(p) }} />
      <div style={{ fontFamily: RF.display, fontWeight: 800, fontSize: 40, color: RF.ink, marginTop: 24, opacity: ramp(0.4, 0.6)(p) }}>Try RiskModelForgeIQ</div>
      <div style={{ fontFamily: RF.mono, fontSize: 19, color: RF.steel, marginTop: 20, opacity: ramp(1.0, 0.6)(p) }}>
        riskmodelforgeiq-demo-xdkyxlbwxa-uc.a.run.app
      </div>
      <div style={{ fontFamily: RF.display, fontSize: 20, color: RF.inkMuted, marginTop: 20, opacity: ramp(1.5, 0.6)(p) }}>
        See the governance engine in action
      </div>
    </div>
  </Panel>
);

export const VideoB2Panel = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;

  const scene = (() => {
    for (const s of timings.scenes) if (t >= s.start && t < s.end) return s;
    return timings.scenes[timings.scenes.length - 1];
  })();
  const sp = t - scene.start;

  return (
    <AbsoluteFill style={{ fontFamily: RF.display }}>
      <FontFace />
      <Audio src={staticFile(timings.audio)} />
      <Background t={t} />

      {scene.key !== 'cta' && <SlideImage p={sp} src={scene.key} dur={scene.end - scene.start} />}
      {scene.key === 'cta' && <CTA p={sp} />}

      <Captions t={t} />
    </AbsoluteFill>
  );
};
