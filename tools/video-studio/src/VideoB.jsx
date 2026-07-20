import React from 'react';
import {
  AbsoluteFill, Audio, Img, OffthreadVideo, Sequence, staticFile,
  useCurrentFrame, useVideoConfig, interpolate, Easing,
} from 'remotion';
import { T } from './theme.js';
import { SkRect, SkUnderline, SkCircleAround, SkFigure, SkLine } from './Sketch.jsx';
import timings from './timings-VideoB.json';

const S = Object.fromEntries(timings.scenes.map((s) => [s.key, s]));
const ease = Easing.out(Easing.cubic);
const W = 1080;

/**
 * Video B — the demo, narrated.
 *
 * The capture is 28.8s but the narration runs 98.8s, and the opening 37.7s
 * (industry figure -> argument -> callback) has no footage at all. So the video is
 * a hybrid: hand-drawn intro in Video A's language, then the real screen capture,
 * then a drawn CTA. Where narration outlasts the footage we hold a still rather
 * than slow the video down — slow-motion UI reads as broken.
 */

// source capture geometry
const SRC_W = 1280, SRC_H = 1400;
const CROP_TOP = 58, CROP_BOTTOM = 950;          // trim page chrome + footer panel
const SCALE = W / SRC_W;                          // 0.84 — keeps UI text legible
const VIEW_H = (CROP_BOTTOM - CROP_TOP) * SCALE;  // ~752
const VIEW_Y = 172;

const Screen = ({ children }) => (
  <div style={{
    position: 'absolute', left: 0, top: VIEW_Y, width: W, height: VIEW_H,
    overflow: 'hidden', background: '#EEF2F6',
  }}>
    <div style={{ position: 'absolute', left: 0, top: -CROP_TOP * SCALE, width: W, height: SRC_H * SCALE }}>
      {children}
    </div>
  </div>
);

const Vid = ({ fromSec }) => (
  <OffthreadVideo src={staticFile('demo-capture.webm')} startFrom={Math.round(fromSec * 30)}
    style={{ width: '100%', height: '100%', objectFit: 'fill' }} muted />
);
const Still = ({ name }) => (
  <Img src={staticFile(`stills/${name}.jpg`)} style={{ width: '100%', height: '100%', objectFit: 'fill' }} />
);

export const VideoB = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const F = (sec) => Math.round(sec * fps);

  const ramp = (from, dur = 0.7, e = ease) =>
    interpolate(t, [from, from + dur], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: e });
  const fade = (s, lead = 0.5, tail = 0.45) =>
    interpolate(t, [s.start, s.start + lead], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease }) *
    (1 - interpolate(t, [s.end - tail, s.end], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease }));

  const demoStart = S.hook.start;            // 37.7
  const demoEnd = S.cta.start;               // 90.9
  const inDemo = t >= demoStart - 0.4 && t < demoEnd + 0.3;
  const inIntro = t < demoStart;

  // caption under the screen during the demo
  const caption = (() => {
    if (t < S.ops.start) return { o: fade(S.hook, 0.4, 0.35), a: 'Same system. Same case.', b: 'Two different people.' };
    if (t < S.review.start) return { o: fade(S.ops, 0.4, 0.35), a: 'Day-to-day operations', b: 'What do I have to act on?' };
    if (t < S.insight.start) return { o: fade(S.review, 0.4, 0.35), a: 'Deeper review — same record', b: 'The full file, for analysis.' };
    if (t < S.analytics.start) return { o: fade(S.insight, 0.35, 0.3), a: 'The job changes the answer.', b: 'Not just what you may see.' };
    if (t < S.shared.start) return { o: fade(S.analytics, 0.4, 0.35), a: 'Asked in plain English', b: 'Ask-AI MCP Service writes the SQL.' };
    return { o: fade(S.shared, 0.4, 0.4), a: 'One shared service.', b: 'Each application keeps its own data.' };
  })();

  return (
    <AbsoluteFill style={{ backgroundColor: T.paper, fontFamily: T.display }}>
      <Audio src={staticFile(timings.audio)} />

      <AbsoluteFill style={{
        backgroundImage: `radial-gradient(circle at 30% 20%, rgba(0,0,0,.022) 0 1px, transparent 1px)`,
        backgroundSize: '13px 13px',
      }} />

      {/* brand rule — product name on screen throughout */}
      <div style={{
        position: 'absolute', top: 50, left: 64, right: 64, display: 'flex',
        justifyContent: 'space-between', alignItems: 'baseline',
        fontFamily: T.mono, fontSize: 16, letterSpacing: '.18em',
        textTransform: 'uppercase', color: T.inkSoft,
      }}>
        <span><span style={{ color: T.teal }}>◆</span>&nbsp;&nbsp;Ask-AI MCP Service</span>
        <span>Live demo</span>
      </div>

      {/* ── INTRO (hand-drawn) ─────────────────────────────────── */}
      {inIntro && (
        <>
          {/* the industry figure */}
          {t < S.callback.start && (
            <div style={{ position: 'absolute', left: 74, right: 74, top: 250, opacity: fade({ start: 0, end: S.callback.start }, 0.6, 0.5) }}>
              {/* Figure web-verified 2026-07. The commonly quoted "30%" is Gartner's
                  2024 FORECAST for end-2025; the actual outcome exceeded 50%. */}
              <div style={{ fontSize: 168, fontWeight: 800, color: T.ink, letterSpacing: '-.05em', lineHeight: 1 }}>
                50%+
              </div>
              <div style={{ fontSize: 40, fontWeight: 650, color: T.ink, marginTop: 18, lineHeight: 1.2 }}>
                of generative AI projects abandoned<br />after proof of concept.
              </div>
              <div style={{ fontFamily: T.mono, fontSize: 19, color: T.inkSoft, marginTop: 20, letterSpacing: '.04em' }}>
                Gartner
              </div>
              {t > S.why.start + 1.4 && (
                <div style={{ fontSize: 30, color: T.inkSoft, marginTop: 40, lineHeight: 1.4, opacity: ramp(S.why.start + 1.4, 0.7) }}>
                  Rarely the model. Usually everything built around it —<br />
                  cost, governance, unclear value.
                </div>
              )}
            </div>
          )}

          {/* callback + setup */}
          {t >= S.callback.start && (
            <div style={{ position: 'absolute', left: 74, right: 74, top: 280, opacity: fade({ start: S.callback.start, end: demoStart }, 0.55, 0.45) }}>
              <div style={{ fontSize: 58, fontWeight: 750, color: T.ink, letterSpacing: '-.03em', lineHeight: 1.1 }}>
                Build those capabilities once.
              </div>
              <div style={{ fontSize: 34, color: T.inkSoft, marginTop: 26, lineHeight: 1.35 }}>
                Let applications connect to them.
              </div>
              <div style={{ fontSize: 34, color: T.ink, marginTop: 34, fontWeight: 650 }}>
                Here it is running.
              </div>
            </div>
          )}

          <svg width={W} height={W} style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
            {t > 2.2 && t < S.callback.start && (
              <SkUnderline x={80} y={432} w={720} seed={31} p={ramp(2.4, 0.9)} stroke={T.amber} strokeWidth={22} opacity={0.5} />
            )}
            {t >= S.callback.start && (
              <>
                <SkFigure x={250} y={640} h={78} seed={11} p={ramp(S.callback.start + 1.2, 0.6)} stroke={T.inkSoft} strokeWidth={2.4} />
                <SkFigure x={540} y={640} h={78} seed={22} p={ramp(S.callback.start + 1.6, 0.6)} stroke={T.inkSoft} strokeWidth={2.4} />
                <SkFigure x={830} y={640} h={78} seed={33} p={ramp(S.callback.start + 2.0, 0.6)} stroke={T.inkSoft} strokeWidth={2.4} />
                <SkRect x={190} y={790} w={700} h={104} seed={44} p={ramp(S.callback.start + 2.6, 0.9)}
                  stroke={T.teal} strokeWidth={3} fill={T.tealSoft} fillStyle="hachure" />
                {ramp(S.callback.start + 3.2, 0.5) > 0.4 && (
                  <text x={540} y={848} textAnchor="middle" fontFamily={T.display} fontSize={30} fontWeight={700} fill={T.ink}>
                    Ask-AI MCP Service
                  </text>
                )}
                {[250, 540, 830].map((x, i) => (
                  <SkLine key={x} x1={x} y1={726} x2={x} y2={784} seed={55 + i}
                    p={ramp(S.callback.start + 2.4 + i * 0.15, 0.5)} stroke={T.teal} strokeWidth={2} />
                ))}
              </>
            )}
          </svg>
        </>
      )}

      {/* ── DEMO (real capture, held on stills where narration runs long) ── */}
      {inDemo && (
        <>
          <Screen>
            <Sequence from={F(demoStart)} durationInFrames={F(2.9)}><Vid fromSec={0} /></Sequence>
            <Sequence from={F(demoStart + 2.9)} durationInFrames={F(S.ops.start - demoStart - 2.9)}><Still name="ops" /></Sequence>

            <Sequence from={F(S.ops.start)} durationInFrames={F(5.2)}><Vid fromSec={2.9} /></Sequence>
            <Sequence from={F(S.ops.start + 5.2)} durationInFrames={F(S.review.start - S.ops.start - 5.2)}><Still name="ops" /></Sequence>

            <Sequence from={F(S.review.start)} durationInFrames={F(5.6)}><Vid fromSec={8.1} /></Sequence>
            <Sequence from={F(S.review.start + 5.6)} durationInFrames={F(S.analytics.start - S.review.start - 5.6)}><Still name="review" /></Sequence>

            <Sequence from={F(S.analytics.start)} durationInFrames={F(11.2)}><Vid fromSec={13.7} /></Sequence>
            <Sequence from={F(S.analytics.start + 11.2)} durationInFrames={F(demoEnd - S.analytics.start - 11.2 + 1)}><Still name="chart" /></Sequence>
          </Screen>

          {/* sketched frame around the screen */}
          <svg width={W} height={W} style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
            <SkRect x={6} y={VIEW_Y - 8} w={W - 12} h={VIEW_H + 16} seed={404}
              p={ramp(demoStart - 0.2, 0.8)} stroke={T.ink} strokeWidth={2.6} />
            {/* marker sweep under the caption's key line */}
            {t >= S.analytics.start + 2.0 && t < S.shared.start && (
              <SkUnderline x={120} y={1004} w={560} seed={77} p={ramp(S.analytics.start + 2.0, 0.8)}
                stroke={T.highlight} strokeWidth={24} opacity={0.7} />
            )}
          </svg>

          {/* caption band */}
          <div style={{ position: 'absolute', left: 64, right: 64, top: 952, opacity: caption.o }}>
            <div style={{ fontFamily: T.mono, fontSize: 17, letterSpacing: '.16em', textTransform: 'uppercase', color: T.teal }}>
              {caption.a}
            </div>
            <div style={{ fontSize: 33, fontWeight: 650, color: T.ink, marginTop: 8, letterSpacing: '-.02em' }}>
              {caption.b}
            </div>
          </div>
        </>
      )}

      {/* ── CTA ────────────────────────────────────────────────── */}
      {t >= demoEnd && (
        <>
          <div style={{ position: 'absolute', left: 80, right: 80, top: 330, textAlign: 'center', opacity: ramp(demoEnd + 0.3, 0.7) }}>
            <div style={{ fontSize: 62, fontWeight: 750, color: T.ink, letterSpacing: '-.03em', lineHeight: 1.12 }}>
              Try it yourself.
            </div>
            <div style={{ fontSize: 31, color: T.inkSoft, marginTop: 26, lineHeight: 1.4 }}>
              The Ask-AI MCP Service demo is linked in the post.<br />
              What would you want it to answer?
            </div>
          </div>
          <svg width={W} height={W} style={{ position: 'absolute', inset: 0, pointerEvents: 'none' }}>
            <SkCircleAround cx={540} cy={372} w={620} h={150} seed={912} p={ramp(demoEnd + 1.6, 1.2)} stroke={T.amber} strokeWidth={3.4} />
            <SkRect x={300} y={640} w={480} h={104} seed={913} p={ramp(demoEnd + 2.6, 0.9)} stroke={T.teal} strokeWidth={3} />
          </svg>
          <div style={{
            position: 'absolute', left: 300, width: 480, top: 640, height: 104,
            display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 5,
            opacity: ramp(demoEnd + 2.8, 0.6),
          }}>
            <div style={{ fontSize: 25, fontWeight: 650, color: T.ink }}>Ask-AI MCP Service</div>
            <div style={{ fontFamily: T.mono, fontSize: 18, color: T.teal, letterSpacing: '.05em' }}>demo · link in post</div>
          </div>
        </>
      )}

      <div style={{ position: 'absolute', left: 64, right: 64, bottom: 40, height: 3 }}>
        <div style={{ height: '100%', width: `${(t / timings.total) * 100}%`, background: T.teal, opacity: 0.75 }} />
      </div>
    </AbsoluteFill>
  );
};
