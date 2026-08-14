// SUPERSEDED: kept as reference only — new work should use SharedVideoPanel.jsx
// (see Root.jsx's `videoCPanelTheme`), the consolidated component this and
// VideoA_Panel.jsx/VideoB2_Panel.jsx were merged into.
import React from 'react';
import {
  AbsoluteFill, staticFile,
  useCurrentFrame, useVideoConfig, interpolate, Easing,
} from 'remotion';
import { RF } from './theme-riskforge.js';
import { Icon } from './Icon.jsx';
import timings from './timings-VideoC-Panel.json';

import Anvil from 'lucide/dist/esm/icons/anvil.mjs';

const ease = Easing.out(Easing.cubic);
const CANVAS_W = 1920;
const CANVAS_H = 1080;
const PANEL_X = 88;
const PANEL_Y = 28;
const PANEL_W = 1744;
const PANEL_H = 1030;
const FOOTER_H = 64;

const ramp = (start, dur = 0.8) => (t) => interpolate(t, [start, start + dur], [0, 1], { easing: ease, extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

// Same Inter font vendored for Video B2 — reused as-is, no re-copy needed
// since staticFile() resolves from this project's shared public/ dir.
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

const Panel = ({ children, noFooter = false }) => (
  <div style={{
    position: 'absolute', left: PANEL_X, top: PANEL_Y, width: PANEL_W, height: PANEL_H,
    background: RF.surface, border: `1.5px solid ${RF.surfaceLine}`, borderRadius: 20,
    boxShadow: `inset 0 1px 0 ${RF.surfaceRaised}, 0 24px 60px -24px #00000070`,
    overflow: 'hidden', display: 'flex', flexDirection: 'column',
  }}>
    <div style={{ position: 'relative', flex: 1, minHeight: 0 }}>
      {children}
    </div>
    {!noFooter && (
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
    )}
  </div>
);

// Slide beats reuse the corrected NotebookLM-sourced deck images (issue found
// and hand-patched 2026-08-14 -- see storyboard-video3-full-tour.md's Open
// Items #5 for what was fixed in each). Ken-Burns pan/zoom per slide, same
// technique as Video B2.
const SLIDE_KEN_BURNS = {
  final_02: { from: 1.0, to: 1.05, x: 0, y: 0 },   // beat 0: disagreement reveal
  final_03: { from: 1.02, to: 1.07, x: -1, y: 0 }, // beat 1: architecture pipeline
  final_04: { from: 1.0, to: 1.06, x: 1, y: -1 },  // beat 8: zoom-out lifecycle
  final_05: { from: 1.02, to: 1.06, x: 0, y: 0 },  // beat 9a: MLOps card
  final_06: { from: 1.02, to: 1.06, x: 0, y: 0 },  // beat 9b: DecisionOps card
  final_01: { from: 1.0, to: 1.04, x: 0, y: 0 },   // beat 9c: title/tagline close
};

const SlideImage = ({ p, src, dur = 10 }) => {
  const kb = SLIDE_KEN_BURNS[src] || { from: 1, to: 1.05, x: 0, y: 0 };
  const scale = interpolate(p, [0, Math.max(dur, 1)], [kb.from, kb.to], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const o = ramp(0, 0.5)(p);
  return (
    <Panel>
      <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden' }}>
        <img
          src={staticFile(`slides-v3/${src}.png`)}
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

// Beat 3's precision-proof reveal — never generated as a NotebookLM slide
// (only 4 visual moments were requested there: disagreement, architecture,
// zoom-out, MLOps/DecisionOps close). Built directly here since it's simple
// numeric/text staging, not a diagram. Matches the storyboard's exact
// escalation sequence and "let it sit ~2s" pacing note.
const PrecisionReveal = ({ p }) => {
  const stage = (start, dur = 0.5) => ramp(start, dur)(p);
  return (
    <Panel noFooter>
      <div style={{
        position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column',
        alignItems: 'center', justifyContent: 'center', gap: 18,
      }}>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 28, opacity: stage(0) }}>
          <span style={{ fontFamily: RF.mono, fontSize: 64, fontWeight: 700, color: RF.inkMuted, textDecoration: p > 0.9 ? 'line-through' : 'none', opacity: interpolate(p, [0.9, 1.3], [1, 0.45], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' }) }}>
            2.8%
          </span>
          <span style={{ fontFamily: RF.mono, fontSize: 40, color: RF.steel, opacity: stage(0.9) }}>→</span>
          <span style={{ fontFamily: RF.mono, fontSize: 84, fontWeight: 800, color: RF.forge, opacity: stage(0.9) }}>
            15.2%
          </span>
        </div>
        <div style={{ fontFamily: RF.display, fontSize: 22, letterSpacing: '.08em', textTransform: 'uppercase', color: RF.inkMuted, opacity: stage(1.6) }}>
          Measured Precision
        </div>
        <div style={{ fontFamily: RF.mono, fontSize: 30, fontWeight: 700, color: RF.purple, marginTop: 8, opacity: stage(2.6) }}>
          +5.4× MEASURED PRECISION
        </div>
        <div style={{ display: 'flex', gap: 40, marginTop: 28 }}>
          <div style={{
            fontFamily: RF.display, fontSize: 26, fontWeight: 700, color: RF.ink,
            border: `1.5px solid ${RF.surfaceLine}`, borderRadius: 12, padding: '14px 26px',
            opacity: stage(5.0),
          }}>
            NO MODEL CHANGE
          </div>
          <div style={{
            fontFamily: RF.display, fontSize: 26, fontWeight: 700, color: RF.bgDeep,
            background: RF.steel, borderRadius: 12, padding: '14px 26px',
            opacity: stage(7.0),
          }}>
            RULES BECAME TUNABLE
          </div>
        </div>
      </div>
    </Panel>
  );
};

export const VideoCPanel = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;

  const scene = (() => {
    for (const s of timings.scenes) if (t >= s.start && t < s.end) return s;
    return timings.scenes[timings.scenes.length - 1];
  })();
  const sp = t - scene.start;
  const dur = scene.end - scene.start;

  return (
    <AbsoluteFill style={{ fontFamily: RF.display }}>
      <FontFace />
      <Background t={t} />
      {scene.key === 'precision-reveal'
        ? <PrecisionReveal p={sp} />
        : <SlideImage p={sp} src={scene.key} dur={dur} />}
    </AbsoluteFill>
  );
};
