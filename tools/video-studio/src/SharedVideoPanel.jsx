import React from 'react';
import {
  AbsoluteFill, Audio, staticFile,
  useCurrentFrame, useVideoConfig, interpolate, Easing,
} from 'remotion';
import { Icon } from './Icon.jsx';

// ═══════════════════════════════════════════════════════════════════════
// SharedVideoPanel — ONE shared component set (Background/Panel-with-
// footer-brand-band/Captions/SlideImage/CTA) that every product's video
// composition renders through, configured entirely by a per-product
// `theme` object instead of hard-coding colors/copy/geometry per video.
//
// Consolidates VideoA_Panel.jsx, VideoB2_Panel.jsx and VideoC_Panel.jsx
// (previously three near-identical copies of this same structure), per
// content/video/DESIGN-SYSTEM.md §7: "these should be ONE shared component
// set that takes a per-product theme object as config."
//
// The footer-embedded brand band (icon + product name + tagline, living
// INSIDE the content Panel) is the canonical layout per DESIGN-SYSTEM.md §6
// ("a quiet footer band inside the content frame, not a large floating
// header") — VideoB2/VideoC already used this; VideoA's older floating
// top BrandBar was the pre-correction pattern and is not reproduced here.
//
// Usage (see Root.jsx):
//   <Composition component={SharedVideoPanel}
//     defaultProps={{ theme: myProductTheme, timings, captionWords }} />
//
// `theme` shape:
// {
//   productName, tagline,
//   colors: { bg, bgDeep, surface, surfaceRaised, surfaceLine, ink,
//             inkMuted, steel, steelSoft, accent, accentSoft, purple, good,
//             capabilityAccents: [blue, teal, purple, green], display, mono },
//   brandIcon,                       // lucide icon node for the footer mark
//   fontFaceUrl,                     // e.g. staticFile('fonts/Inter.woff2'), or null to skip
//   canvas: { width, height },
//   panel: { x, y, w, h, footerH },
//   captions: { enabled, barH } | null,
//   audio: { enabled, src } | null,
//   slidesDir: 'slides' | 'slides-v2' | 'slides-v3' | ...,
//   kenBurns: { [sceneKey]: { from, to, x, y } },
//   cta: { icon, iconSize, title, url, sub, url } | null,
//   customScenes: { [sceneKey]: (p, dur, theme) => JSX } | null,
// }
// ═══════════════════════════════════════════════════════════════════════

const ease = Easing.out(Easing.cubic);

export const ramp = (start, dur = 0.8) => (t) => interpolate(t, [start, start + dur], [0, 1], { easing: ease, extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });

// ── Background: dark graphite ground with a slow-drifting circuit-board
// node/line pattern. Theme-driven colors; geometry/seed identical across
// products (this part never actually varied between the 3 old files).
export const Background = ({ t, colors }) => {
  const nodes = React.useMemo(() => {
    const pts = [];
    let seed = 7;
    const rand = () => { seed = (seed * 16807) % 2147483647; return seed / 2147483647; };
    for (let i = 0; i < 14; i++) pts.push({ x: rand() * 100, y: rand() * 100, ph: rand() * 10 });
    return pts;
  }, []);
  return (
    <AbsoluteFill style={{ background: `radial-gradient(ellipse 90% 70% at 50% 0%, ${colors.surfaceRaised} 0%, ${colors.bg} 55%, ${colors.bgDeep} 100%)` }}>
      <svg width="100%" height="100%" style={{ position: 'absolute', inset: 0 }}>
        {nodes.map((n, i) => nodes.slice(i + 1, i + 3).map((m, j) => (
          <line key={`${i}-${j}`} x1={`${n.x}%`} y1={`${n.y}%`} x2={`${m.x}%`} y2={`${m.y}%`}
            stroke={colors.steelSoft} strokeWidth={1} opacity={0.22 + 0.08 * Math.sin(t * 0.3 + n.ph)} />
        )))}
        {nodes.map((n, i) => (
          <circle key={i} cx={`${n.x}%`} cy={`${n.y}%`} r={2 + Math.sin(t * 0.5 + n.ph) * 0.8}
            fill={colors.steel} opacity={0.35 + 0.15 * Math.sin(t * 0.4 + n.ph)} />
        ))}
      </svg>
    </AbsoluteFill>
  );
};

// ── Optional @font-face injection (vendored Inter, per product). Pass
// `theme.fontFaceUrl = null` for compositions that don't need it.
export const FontFace = ({ url }) => url ? (
  <style>{`
    @font-face {
      font-family: 'Inter';
      src: url('${url}') format('woff2');
      font-weight: 100 900;
      font-display: block;
    }
  `}</style>
) : null;

// ── Panel: the content frame, with the brand/tagline footer band embedded
// inside it (the canonical layout per DESIGN-SYSTEM.md §6).
export const Panel = ({ theme, children, noFooter = false }) => {
  const { x, y, w, h, footerH } = theme.panel;
  const { colors } = theme;
  return (
    <div style={{
      position: 'absolute', left: x, top: y, width: w, height: h,
      background: colors.surface, border: `1.5px solid ${colors.surfaceLine}`, borderRadius: 20,
      boxShadow: `inset 0 1px 0 ${colors.surfaceRaised}, 0 24px 60px -24px #00000070`,
      overflow: 'hidden', display: 'flex', flexDirection: 'column',
    }}>
      <div style={{ position: 'relative', flex: 1, minHeight: 0 }}>
        {children}
      </div>
      {!noFooter && (
        <div style={{
          flexShrink: 0, height: footerH, borderTop: `1px solid ${colors.surfaceLine}`,
          display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          padding: '0 30px', background: colors.bgDeep,
        }}>
          <span style={{
            display: 'flex', alignItems: 'center', gap: 11, fontFamily: colors.mono,
            fontSize: 17, fontWeight: 600, letterSpacing: '.12em', textTransform: 'uppercase', color: colors.ink,
          }}>
            <Icon icon={theme.brandIcon} size={20} color={colors.accent} strokeWidth={2.1} />
            {theme.productName}
          </span>
          <span style={{ fontFamily: colors.mono, fontSize: 16, letterSpacing: '.12em', textTransform: 'uppercase', color: colors.steel }}>
            {theme.tagline}
          </span>
        </div>
      )}
    </div>
  );
};

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

// ── Captions: full-width solid bar sitting just above the footer band
// (the broadcast/subtitle-bar convention — see VideoB2_Panel.jsx's
// original rationale for why a floating pill was rejected: it let slide
// content peek out from behind short captions near the panel's bottom edge).
export const Captions = ({ t, theme, phrases }) => {
  if (!phrases || !theme.captions?.enabled) return null;
  const active = phrases.find((p) => t >= p.start - 0.05 && t < p.end + 0.35);
  if (!active) return null;
  const { x, y, w, h, footerH } = theme.panel;
  const barH = theme.captions.barH ?? 70;
  const bandY = y + h - footerH - barH;
  const o = ramp(active.start, 0.12)(t) * (t > active.end ? Math.max(0, 1 - (t - active.end) / 0.25) : 1);
  return (
    <div style={{
      position: 'absolute', left: x + 1.5, width: w - 3, top: bandY,
      height: barH, display: 'flex', alignItems: 'center', justifyContent: 'center',
      background: theme.colors.bgDeep, opacity: o,
    }}>
      <span style={{ fontFamily: theme.colors.display, fontSize: 24, fontWeight: 600, color: theme.colors.ink, padding: '0 20px' }}>
        {active.text}
      </span>
    </div>
  );
};

// ── Slide scenes reuse a product's actual exported deck images, with a
// slow Ken Burns drift so a static slide still reads as motion picture.
export const SlideImage = ({ theme, p, src, dur = 20 }) => {
  const kb = theme.kenBurns?.[src] || { from: 1, to: 1.05, x: 0, y: 0 };
  const scale = interpolate(p, [0, Math.max(dur, 1)], [kb.from, kb.to], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp' });
  const o = ramp(0, 0.6)(p);
  return (
    <Panel theme={theme}>
      <div style={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', overflow: 'hidden' }}>
        <img
          src={staticFile(`${theme.slidesDir}/${src}.png`)}
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

// ── CTA: closing "try the product" panel. `theme.cta = null` skips it
// entirely (VideoC's composition has no CTA scene at all).
export const CTA = ({ theme, p }) => {
  const cta = theme.cta;
  const { colors } = theme;
  return (
    <Panel theme={theme}>
      <div style={{ position: 'absolute', inset: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
        <Icon icon={cta.icon} size={cta.iconSize ?? 40} color={colors.accent} strokeWidth={1.6} style={{ opacity: ramp(0, 0.6)(p) }} />
        <div style={{ fontFamily: colors.display, fontWeight: 800, fontSize: cta.titleSize ?? 34, color: colors.ink, marginTop: 22, opacity: ramp(0.4, 0.6)(p) }}>{cta.title}</div>
        <div style={{ fontFamily: colors.mono, fontSize: cta.urlSize ?? 17, color: colors.steel, marginTop: 19, opacity: ramp(1.0, 0.6)(p) }}>
          {cta.url}
        </div>
        <div style={{ fontFamily: colors.display, fontSize: cta.subSize ?? 18, color: colors.inkMuted, marginTop: 19, opacity: ramp(1.5, 0.6)(p) }}>
          {cta.sub}
        </div>
      </div>
    </Panel>
  );
};

// ═══════════════════════════════════════════════════════════════════════
// Top-level composition component.
// ═══════════════════════════════════════════════════════════════════════
export const SharedVideoPanel = ({ theme, timings, captionWords }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;

  const phrases = React.useMemo(() => captionWords ? buildPhrases(captionWords) : null, [captionWords]);

  const scene = (() => {
    for (const s of timings.scenes) if (t >= s.start && t < s.end) return s;
    return timings.scenes[timings.scenes.length - 1];
  })();
  const sp = t - scene.start;
  const dur = scene.end - scene.start;

  const custom = theme.customScenes?.[scene.key];

  return (
    <AbsoluteFill style={{ fontFamily: theme.colors.display }}>
      <FontFace url={theme.fontFaceUrl} />
      {theme.audio?.enabled && <Audio src={staticFile(theme.audio.src)} />}
      <Background t={t} colors={theme.colors} />

      {scene.key === 'cta' && theme.cta
        ? <CTA theme={theme} p={sp} />
        : custom
          ? custom(sp, dur, theme)
          : <SlideImage theme={theme} p={sp} src={scene.key} dur={dur} />}

      <Captions t={t} theme={theme} phrases={phrases} />
    </AbsoluteFill>
  );
};
