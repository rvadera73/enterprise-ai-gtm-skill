// SUPERSEDED: kept as reference only — new work should use SharedVideoPanel.jsx
// (see Root.jsx's `videoAPanelTheme`), the consolidated component this and
// VideoB2_Panel.jsx/VideoC_Panel.jsx were merged into.
import React from 'react';
import {
  AbsoluteFill, Audio, staticFile,
  useCurrentFrame, useVideoConfig, interpolate, Easing,
} from 'remotion';
import { RF } from './theme-riskforge.js';
import { Icon } from './Icon.jsx';
import timings from './timings-VideoA-Panel.json';
import captionWords from './captions-VideoA-Panel.json';

import Anvil from 'lucide/dist/esm/icons/anvil.mjs';
import Sparkles from 'lucide/dist/esm/icons/sparkles.mjs';

const ease = Easing.out(Easing.cubic);
const W = 1080;

const ramp = (start, dur = 0.8) => (t) => interpolate(t, [start, start + dur], [0, 1], { easing: ease, extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

// ── Background: dark graphite ground with a slow-drifting circuit-board
// node/line pattern.
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

const BrandBar = () => (
  <div style={{
    position: 'absolute', top: 46, left: 64, right: 64, display: 'flex',
    justifyContent: 'space-between', alignItems: 'center',
    fontFamily: RF.mono, fontSize: 15, letterSpacing: '.16em',
    textTransform: 'uppercase', color: RF.inkMuted,
  }}>
    <span style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
      <Icon icon={Anvil} size={20} color={RF.forge} strokeWidth={2} />
      RiskModelForgeIQ
    </span>
    <span>Your Decision Intelligence Layer</span>
  </div>
);

const Panel = ({ x = 40, y = 168, w = W - 80, h = 726, children }) => (
  <div style={{
    position: 'absolute', left: x, top: y, width: w, height: h,
    background: RF.surface, border: `1.5px solid ${RF.surfaceLine}`, borderRadius: 18,
    boxShadow: `inset 0 1px 0 ${RF.surfaceRaised}, 0 20px 50px -20px #00000066`,
    overflow: 'hidden',
  }}>
    {children}
  </div>
);

// ── Rolling captions.
const CAPTION_BAND_Y = 918;
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

const Captions = ({ t }) => {
  const active = PHRASES.find((p) => t >= p.start - 0.05 && t < p.end + 0.35);
  if (!active) return null;
  const o = ramp(active.start, 0.12)(t) * (t > active.end ? Math.max(0, 1 - (t - active.end) / 0.25) : 1);
  return (
    <div style={{ position: 'absolute', left: 64, right: 64, top: CAPTION_BAND_Y, textAlign: 'center', opacity: o }}>
      <span style={{
        fontFamily: RF.display, fontSize: 20, fontWeight: 600, color: RF.ink,
        background: `${RF.bgDeep}CC`, padding: '5px 16px', borderRadius: 8,
        boxDecorationBreak: 'clone', WebkitBoxDecorationBreak: 'clone',
      }}>
        {active.text}
      </span>
    </div>
  );
};

// ═══════════════════════════════════════════════════════════════════════
// Scenes
// ═══════════════════════════════════════════════════════════════════════

// ── Slide scenes reuse the ACTUAL NotebookLM deck images (watermark
// stripped, one factual overclaim on the shadow slide also removed — see
// public/slides/*.png provenance). Each scene gets a slow Ken Burns
// drift so a static slide still reads as motion picture, not a screenshot.
const SLIDE_KEN_BURNS = {
  intro: { from: 1.0, to: 1.05, x: 0, y: 0 },
  evidence: { from: 1.02, to: 1.08, x: -1, y: 0 },
  layer: { from: 1.0, to: 1.06, x: 1, y: -1 },
  defensible: { from: 1.02, to: 1.07, x: 0, y: 1 },
  shadow: { from: 1.0, to: 1.05, x: -1, y: 1 },
  close: { from: 1.02, to: 1.08, x: 0, y: 0 },
};

const SlideImage = ({ p, src, dur = 20 }) => {
  const kb = SLIDE_KEN_BURNS[src] || { from: 1, to: 1.05, x: 0, y: 0 };
  const scale = interpolate(p, [0, Math.max(dur, 1)], [kb.from, kb.to], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const o = ramp(0, 0.6)(p);
  return (
    <Panel>
      <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden' }}>
        <img
          src={staticFile(`slides/${src}.png`)}
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
      <Icon icon={Sparkles} size={38} color={RF.forge} strokeWidth={1.6} style={{ opacity: ramp(0, 0.6)(p) }} />
      <div style={{ fontFamily: RF.display, fontWeight: 800, fontSize: 30, color: RF.ink, marginTop: 20, opacity: ramp(0.4, 0.6)(p) }}>Try RiskModelForgeIQ</div>
      <div style={{ fontFamily: RF.mono, fontSize: 16, color: RF.steel, marginTop: 18, opacity: ramp(1.0, 0.6)(p) }}>
        riskmodelforgeiq-demo-xdkyxlbwxa-uc.a.run.app
      </div>
      <div style={{ fontFamily: RF.display, fontSize: 17, color: RF.inkMuted, marginTop: 18, opacity: ramp(1.5, 0.6)(p) }}>
        Link in the post
      </div>
    </div>
  </Panel>
);

export const VideoAPanel = () => {
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
      <Audio src={staticFile(timings.audio)} />
      <Background t={t} />
      <BrandBar />

      {scene.key !== 'cta' && ['intro', 'evidence', 'layer', 'defensible', 'shadow', 'close'].includes(scene.key) &&
        <SlideImage p={sp} src={scene.key} dur={scene.end - scene.start} />}
      {scene.key === 'cta' && <CTA p={sp} />}

      <Captions t={t} />
    </AbsoluteFill>
  );
};
