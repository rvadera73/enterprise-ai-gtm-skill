import React from 'react';
import {
  AbsoluteFill, Audio, staticFile, useCurrentFrame, useVideoConfig,
  interpolate, Easing,
} from 'remotion';
import { T, APPS, FOUNDATIONS, CAPS } from './theme.js';
import { SkRect, SkEllipse, SkLine, SkUnderline, SkCircleAround, SkIcon, SkFigure } from './Sketch.jsx';
import { Search, ChartColumn, Share2, Workflow, ShieldCheck, Lock, FileCheck, Box } from 'lucide';
import timings from './timings.json';

const CAP_ICONS = [Search, ChartColumn, Share2, Workflow, ShieldCheck, Lock, FileCheck, Box];
const FOUND_ICONS = [Search, ChartColumn, Workflow, Lock, ShieldCheck];

/** label fades in as its box finishes drawing, instead of popping at a threshold */
const inkIn = (p) => Math.max(0, Math.min(1, (p - 0.5) / 0.42));

const S = Object.fromEntries(timings.scenes.map((s) => [s.key, s]));
const ease = Easing.out(Easing.cubic);
const W = 1080;

/** short label -> up to two centred lines inside a sketched box */
const BoxLabel = ({ x, y, w, h, text, size = 20, fill = T.ink, weight = 500 }) => {
  const words = text.split(' ');
  let lines = [text];
  if (text.length > 14 && words.length > 1) {
    const mid = Math.ceil(words.length / 2);
    lines = [words.slice(0, mid).join(' '), words.slice(mid).join(' ')];
  }
  const cy = y + h / 2;
  const start = cy - ((lines.length - 1) * size * 0.62) / 2;
  return (
    <text x={x + w / 2} textAnchor="middle" fontFamily={T.display}
      fontSize={size} fontWeight={weight} fill={fill}>
      {lines.map((l, i) => (
        <tspan key={i} x={x + w / 2} y={start + i * size * 1.24} dominantBaseline="middle">{l}</tspan>
      ))}
    </text>
  );
};

export const VideoA = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;

  const ramp = (from, dur = 0.8, e = ease) =>
    interpolate(t, [from, from + dur], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: e });
  const fade = (s, lead = 0.5, tail = 0.5) =>
    interpolate(t, [s.start, s.start + lead], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease }) *
    (1 - interpolate(t, [s.end - tail, s.end], [0, 1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease }));

  // ── layout ────────────────────────────────────────────────────────────────
  const aW = 190, aH = 92, aGap = 12;
  const aTotal = APPS.length * aW + (APPS.length - 1) * aGap;
  const aX = (W - aTotal) / 2;
  const appX = (i) => aX + i * (aW + aGap);
  // The apps row opens centred (nothing below it yet) and lifts to make room as the
  // foundations are drawn in — otherwise beat 1 is all dead space under the boxes.
  const appY = interpolate(
    t, [S.sameneeds.start - 1.0, S.sameneeds.start + 0.6], [470, 356],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.inOut(Easing.cubic) },
  );

  const fW = 190, fH = 92;
  const fY = 700;

  // apps persist through beats 1-4
  const appsAlive = t < S.caps.start - 0.3;
  const appIn = APPS.map((_, i) => ramp(1.1 + i * 0.5, 0.55));

  // beat 2 — foundations
  const fIn = FOUNDATIONS.map((_, i) => ramp(S.sameneeds.start + 2.6 + i * 0.75, 0.5));
  const arrowIn = ramp(S.sameneeds.start + 1.6, 0.6);
  const foundationsAlive = t >= S.sameneeds.start && t < S.rebuild.start + 0.6;

  // beat 3 — duplication (before)
  const dupIn = APPS.map((_, i) => ramp(S.rebuild.start + 1.2 + i * 0.32, 0.45));
  const dupOut = interpolate(t, [S.askai.start + 1.4, S.askai.start + 2.6], [0, 1],
    { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: ease });
  const dupAlive = t >= S.rebuild.start && dupOut < 0.99;
  const circleIn = ramp(S.rebuild.start + 4.6, 0.9);

  // beat 4 — the shared service (after)
  const sharedIn = ramp(S.askai.start + 2.4, 1.2);
  const railIn = APPS.map((_, i) => ramp(S.askai.start + 3.4 + i * 0.22, 0.5));
  const sharedAlive = t >= S.askai.start + 1.8 && t < S.caps.start - 0.3;
  const shY = 700, shH = 118;

  // beat 5 — capability hub
  const hubAlive = t >= S.caps.start - 0.2 && t < S.standard.start + 0.4;
  const hubFade = fade({ start: S.caps.start - 0.2, end: S.standard.start + 0.4 }, 0.5, 0.4);
  const hubIn = ramp(S.caps.start + 0.5, 0.8);
  const capIn = CAPS.map((_, i) => ramp(S.caps.start + 1.6 + i * 0.42, 0.45));
  // radius grew with the boxes (they now carry an icon above the label)
  const hubCx = W / 2, hubCy = 648, hubR = 254;

  // beat 6 — statement
  const stAlive = t >= S.standard.start && t < S.question.start;
  const stFade = fade(S.standard, 0.5, 0.4);
  const stUnder = ramp(S.standard.start + 2.4, 0.8);

  // beat 7/8 — close
  const qAlive = t >= S.question.start - 0.2;
  const qIn = ramp(S.question.start + 0.3, 0.7);
  const qCircle = ramp(S.question.start + 3.0, 1.3);
  const ctaIn = ramp(S.cta.start + 0.2, 0.7);

  const headline = (() => {
    if (t < S.sameneeds.start) return { o: fade(S.pattern, 0.5, 0.4), a: 'More applications.', b: 'The same AI needs.' };
    if (t < S.rebuild.start) return { o: fade(S.sameneeds, 0.5, 0.4), a: 'They all need', b: 'the same foundations.' };
    if (t < S.askai.start) return { o: fade(S.rebuild, 0.5, 0.4), a: 'Rebuilt in every', b: 'application.' };
    if (t < S.caps.start) return { o: fade(S.askai, 0.5, 0.4), a: 'Or built once —', b: 'Ask-AI MCP Service.' };
    if (t < S.standard.start) return { o: hubFade, a: 'Inside Ask-AI MCP Service.', b: '' };
    return { o: 0, a: '', b: '' };
  })();

  return (
    <AbsoluteFill style={{ backgroundColor: T.paper, fontFamily: T.display }}>
      <Audio src={staticFile('narration.mp3')} />

      {/* paper tooth */}
      <AbsoluteFill style={{
        backgroundImage: `radial-gradient(circle at 30% 20%, rgba(0,0,0,.022) 0 1px, transparent 1px),
                          radial-gradient(circle at 70% 65%, rgba(0,0,0,.018) 0 1px, transparent 1px)`,
        backgroundSize: '13px 13px, 17px 17px',
      }} />

      {/* header */}
      <div style={{
        position: 'absolute', top: 54, left: 64, right: 64, display: 'flex',
        justifyContent: 'space-between', alignItems: 'baseline',
        fontFamily: T.mono, fontSize: 16, letterSpacing: '.18em',
        textTransform: 'uppercase', color: T.inkSoft,
      }}>
        <span><span style={{ color: T.teal }}>◆</span>&nbsp;&nbsp;Ask-AI MCP Service</span>
        <span>Shared AI capabilities</span>
      </div>

      {/* headline */}
      {headline.o > 0.01 && (
        <div style={{
          position: 'absolute', left: 64, right: 64, top: 140, opacity: headline.o,
          fontSize: 62, fontWeight: 700, letterSpacing: '-.028em', lineHeight: 1.08, color: T.ink,
        }}>
          {headline.a}{headline.b && <br />}{headline.b}
        </div>
      )}

      <svg width={W} height={W} style={{ position: 'absolute', inset: 0 }}>

        {/* ── applications row ─────────────────────────────── */}
        {appsAlive && APPS.map((a, i) => appIn[i] > 0.01 && (
          <g key={a} opacity={Math.min(1, appIn[i] * 1.2)}>
            {/* the team behind each application — stick figures are what make a
                whiteboard feel like a person explaining rather than a diagram */}
            <SkFigure x={appX(i) + aW / 2} y={appY - 56} h={42} seed={700 + i * 5}
              p={appIn[i]} stroke={T.inkSoft} strokeWidth={2} />
            <SkRect x={appX(i)} y={appY} w={aW} h={aH} seed={11 + i} p={appIn[i]} stroke={T.ink} strokeWidth={2.2} />
            <g opacity={inkIn(appIn[i])}>
              <BoxLabel x={appX(i)} y={appY} w={aW} h={aH} text={a} size={19} />
            </g>
          </g>
        ))}

        {/* ── beat 2 · foundations ─────────────────────────── */}
        {foundationsAlive && (
          <g opacity={fade({ start: S.sameneeds.start, end: S.rebuild.start + 0.6 }, 0.5, 0.5)}>
            {arrowIn > 0.01 && (
              <>
                <SkLine x1={W / 2} y1={appY + aH + 26} x2={W / 2} y2={fY - 46} seed={91} p={arrowIn} stroke={T.inkSoft} strokeWidth={2} />
                <SkLine x1={W / 2 - 13} y1={fY - 68} x2={W / 2} y2={fY - 44} seed={92} p={arrowIn} stroke={T.inkSoft} strokeWidth={2} />
                <SkLine x1={W / 2 + 13} y1={fY - 68} x2={W / 2} y2={fY - 44} seed={93} p={arrowIn} stroke={T.inkSoft} strokeWidth={2} />
              </>
            )}
            {FOUNDATIONS.map((f, i) => fIn[i] > 0.01 && (
              <g key={f} opacity={Math.min(1, fIn[i] * 1.2)}>
                <SkRect x={appX(i)} y={fY} w={fW} h={fH} seed={31 + i} p={fIn[i]} stroke={T.teal} strokeWidth={2.4} />
                <g opacity={inkIn(fIn[i])}>
                  <SkIcon icon={FOUND_ICONS[i]} x={appX(i) + fW / 2 - 14} y={fY + 18} size={28}
                    seed={640 + i * 4} stroke={T.teal} strokeWidth={1.7} />
                  <text x={appX(i) + fW / 2} y={fY + 74} textAnchor="middle" fontFamily={T.display}
                    fontSize={18} fontWeight={500} fill={T.ink}>{f}</text>
                </g>
              </g>
            ))}
          </g>
        )}

        {/* ── beat 3 · duplication under every app ─────────── */}
        {dupAlive && (
          <g opacity={1 - dupOut}>
            {APPS.map((_, i) => dupIn[i] > 0.01 && (
              <g key={i}>
                {[0, 1, 2, 3, 4].map((j) => (
                  <SkRect key={j} x={appX(i) + 12} y={appY + aH + 34 + j * 34} w={aW - 24} h={24}
                    seed={200 + i * 7 + j} p={dupIn[i]} stroke={T.amber} strokeWidth={1.9} />
                ))}
              </g>
            ))}
            {circleIn > 0.01 && (
              <>
                <SkCircleAround cx={W / 2} cy={appY + aH + 122} w={aTotal + 46} h={228} seed={77} p={circleIn} stroke={T.amber} strokeWidth={3.2} />
                <text x={W / 2} y={appY + aH + 268} textAnchor="middle" fontFamily={T.mono}
                  fontSize={23} fill={T.amber} opacity={circleIn} letterSpacing="1.6">
                  the same foundations × 5
                </text>
              </>
            )}
          </g>
        )}

        {/* ── beat 4 · one shared service ──────────────────── */}
        {sharedAlive && (
          <g opacity={fade({ start: S.askai.start + 1.8, end: S.caps.start - 0.3 }, 0.5, 0.4)}>
            {APPS.map((_, i) => railIn[i] > 0.01 && (
              <SkLine key={i} x1={appX(i) + aW / 2} y1={appY + aH + 8} x2={appX(i) + aW / 2} y2={shY - 8}
                seed={300 + i} p={railIn[i]} stroke={T.teal} strokeWidth={2} />
            ))}
            {sharedIn > 0.01 && (
              <>
                <SkRect x={aX} y={shY} w={aTotal} h={shH} seed={55} p={sharedIn}
                  stroke={T.teal} strokeWidth={3} fill={T.tealSoft} fillStyle="hachure" />
                {sharedIn > 0.6 && (
                  <>
                    <text x={W / 2} y={shY + 46} textAnchor="middle" fontFamily={T.display}
                      fontSize={30} fontWeight={700} fill={T.ink}>Ask-AI MCP Service</text>
                    <text x={W / 2} y={shY + 84} textAnchor="middle" fontFamily={T.display}
                      fontSize={20} fill={T.inkSoft}>
                      Retrieval · Analytics · Orchestration · Access · Governance
                    </text>
                  </>
                )}
              </>
            )}
            {sharedIn > 0.85 && (
              <text x={W / 2} y={shY + shH + 52} textAnchor="middle" fontFamily={T.display}
                fontSize={21} fill={T.inkSoft} opacity={ramp(S.askai.start + 5.2, 0.6)}>
                Each application keeps its own logic, workflows and data.
              </text>
            )}
          </g>
        )}

        {/* ── beat 5 · capability hub ──────────────────────── */}
        {hubAlive && (
          <g opacity={hubFade}>
            {CAPS.map((c, i) => {
              const ang = (i / CAPS.length) * Math.PI * 2 - Math.PI / 2;
              const p = capIn[i];
              if (p < 0.01) return null;
              const nx = hubCx + Math.cos(ang) * hubR, ny = hubCy + Math.sin(ang) * hubR;
              const bw = 172, bh = 88;
              return (
                <g key={c}>
                  <SkLine x1={hubCx + Math.cos(ang) * 90} y1={hubCy + Math.sin(ang) * 90}
                    x2={nx - Math.cos(ang) * 10} y2={ny - Math.sin(ang) * 10}
                    seed={400 + i} p={p} stroke={T.inkFaint} strokeWidth={1.8} />
                  <SkRect x={nx - bw / 2} y={ny - bh / 2} w={bw} h={bh} seed={420 + i} p={p}
                    stroke={T.ink} strokeWidth={2} />
                  <g opacity={inkIn(p)}>
                    <SkIcon icon={CAP_ICONS[i]} x={nx - 14} y={ny - bh / 2 + 14} size={28}
                      seed={460 + i * 4} stroke={T.teal} strokeWidth={1.7} />
                    <text x={nx} y={ny + bh / 2 - 18} textAnchor="middle" fontFamily={T.display}
                      fontSize={17} fontWeight={500} fill={T.ink}>{c}</text>
                  </g>
                </g>
              );
            })}
            {hubIn > 0.01 && (
              <>
                <SkEllipse cx={hubCx} cy={hubCy} w={172} h={172} seed={500} p={hubIn}
                  stroke={T.teal} strokeWidth={3.2} fill={T.tealSoft} fillStyle="solid" />
                {hubIn > 0.6 && (
                  <text x={hubCx} textAnchor="middle" fontFamily={T.display} fontSize={23} fontWeight={700} fill={T.ink}>
                    <tspan x={hubCx} y={hubCy - 8}>Ask-AI</tspan>
                    <tspan x={hubCx} y={hubCy + 20}>MCP</tspan>
                  </text>
                )}
              </>
            )}
          </g>
        )}

        {/* ── beat 6 · the statement ───────────────────────── */}
        {stAlive && stUnder > 0.01 && (
          <g opacity={stFade}>
            <SkUnderline x={148} y={540} w={784} seed={606} p={stUnder} stroke={T.highlight} strokeWidth={26} opacity={0.75} />
          </g>
        )}

        {/* ── beat 7 · the question ────────────────────────── */}
        {qAlive && qCircle > 0.01 && (
          <SkCircleAround cx={W / 2} cy={556} w={880} h={186} seed={909} p={qCircle} stroke={T.amber} strokeWidth={3.6} />
        )}

        {/* ── beat 8 · CTA ─────────────────────────────────── */}
        {t >= S.cta.start && ctaIn > 0.01 && (
          <SkRect x={214} y={786} w={652} h={116} seed={808} p={ctaIn} stroke={T.teal} strokeWidth={2.8} />
        )}
      </svg>

      {/* ── HTML text for the wrapped copy ────────────────── */}
      {stAlive && (
        <div style={{
          position: 'absolute', left: 120, right: 120, top: 404, opacity: stFade,
          fontSize: 46, fontWeight: 700, letterSpacing: '-.02em', lineHeight: 1.24, color: T.ink,
        }}>
          Not standardising every application —<br />standardising the AI capabilities they all need.
        </div>
      )}

      {qAlive && (
        <div style={{ position: 'absolute', left: 90, right: 90, top: 350, opacity: qIn, textAlign: 'center' }}>
          <div style={{ fontSize: 48, fontWeight: 600, color: T.inkSoft, letterSpacing: '-.02em' }}>
            Maybe it isn’t which model.
          </div>
          <div style={{ fontSize: 66, fontWeight: 750, color: T.ink, letterSpacing: '-.03em', marginTop: 26, lineHeight: 1.12 }}>
            Where does AI belong<br />in your architecture?
          </div>
        </div>
      )}

      {t >= S.cta.start && (
        <div style={{
          position: 'absolute', left: 214, width: 652, top: 786, height: 116, opacity: ctaIn,
          display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', gap: 6,
        }}>
          <div style={{ fontSize: 27, fontWeight: 650, color: T.ink }}>Try the Ask-AI MCP Service demo</div>
          <div style={{ fontFamily: T.mono, fontSize: 18, color: T.teal, letterSpacing: '.05em' }}>link in the post</div>
        </div>
      )}

      {/* progress */}
      <div style={{ position: 'absolute', left: 64, right: 64, bottom: 52, height: 3 }}>
        <div style={{ height: '100%', width: `${(t / timings.total) * 100}%`, background: T.teal, opacity: 0.75 }} />
      </div>
    </AbsoluteFill>
  );
};
