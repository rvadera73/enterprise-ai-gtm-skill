import React from 'react';
import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, Easing } from 'remotion';

// UnmaskIQ Beat 0 cold open -- storyboard-traceforge-demo.md v5, Beat 0
// (docs/gtm/03-video/storyboard-traceforge-demo.md):
//   "open on the sanctions hit itself -- a red flag on an entity node --
//   then pull back to reveal it's one hop behind a clean-looking manifest
//   name."
// Cue timestamps below are the real per-line values from
// unmaskiq_output/narration_timing.json's beat "0" lines (not guessed):
//   0.00-5.80  Emma:  "That name right there -- flagged..."
//   6.25-12.94 Rahul: "And one hop back, that same party's hiding..."
//   13.39-14.97 Emma: "So how did anyone even find it?"
//   15.42-16.45 Rahul: "That's what this is."
// Colors match the live UnmaskIQ product exactly (not invented): navy
// #0B1F33 (header/sidebar), CLEAR green #166534/#DCFCE7, FLAGGED red
// #D83933/#FEE2E2 -- the same palette the Table 3-5 badge (fixed this
// session) actually uses, so the cold open's "flag" visually matches what
// Beat 2 later pays off.

const NAVY = '#0B1F33';
const RED = '#D83933';
const RED_LIGHT = '#FEE2E2';
const GREEN = '#166534';
const GREEN_LIGHT = '#DCFCE7';
const SLATE = '#94A3B8';

const clamp = (t, from, to, out0, out1, easing = Easing.out(Easing.cubic)) =>
  interpolate(t, [from, to], [out0, out1], { extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing });

// A quiet wall of synthetic manifest IDs scrolling behind the reveal --
// "one of thousands of shipping manifests that cross every day," per
// Rahul's line. Deterministic (no Math.random -- scripts run in a context
// where it's unavailable/must stay reproducible across renders).
const MANIFEST_IDS = Array.from({ length: 48 }, (_, i) => {
  const n = (i * 7919 + 3313) % 999999;
  return `SHP-${String(n).padStart(6, '0')}`;
});

const ManifestWall = ({ opacity, highlightIndex, frame }) => (
  <AbsoluteFill style={{ opacity }}>
    <div
      style={{
        position: 'absolute', inset: 0, display: 'grid',
        gridTemplateColumns: 'repeat(8, 1fr)', gap: 18, padding: 60,
        transform: `translateY(${-((frame * 0.4) % 90)}px)`,
      }}
    >
      {MANIFEST_IDS.map((id, i) => {
        const isFlagged = i === highlightIndex;
        return (
          <div
            key={id}
            style={{
              fontFamily: 'monospace', fontSize: 15,
              color: isFlagged ? RED : SLATE,
              fontWeight: isFlagged ? 700 : 400,
              opacity: isFlagged ? 1 : 0.35,
              transition: 'none',
            }}
          >
            {id}
          </div>
        );
      })}
    </div>
  </AbsoluteFill>
);

export const UnmaskIQBeat0 = () => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const t = frame / fps;

  // Beat progression, real cue timestamps.
  const wallOpacity = clamp(t, 0, 0.6, 0, 1) * (1 - clamp(t, 12.9, 13.6, 0, 1));
  const flagPillIn = clamp(t, 1.2, 2.2, 0, 1);
  const flagPillHold = t >= 1.2;

  // "pull back" -- the flag reveal scales down and a second node (the
  // clean shipper) + connecting line fade in one hop back, timed to
  // Rahul's "one hop back" line (6.25-12.94s).
  const pullBack = clamp(t, 6.25, 8.5, 0, 1, Easing.inOut(Easing.cubic));
  const graphScale = 1 - pullBack * 0.28;
  const shipperIn = clamp(t, 7.2, 8.8, 0, 1);
  const lineIn = clamp(t, 6.8, 8.2, 0, 1);

  // Closing text, timed to Emma's + Rahul's final two lines.
  const q3In = clamp(t, 13.39, 14.0, 0, 1) * (1 - clamp(t, 15.3, 15.9, 0, 1));
  const closeIn = clamp(t, 15.42, 16.1, 0, 1);
  const wordmarkIn = clamp(t, 15.7, 16.4, 0, 1);

  // The graph (flag/shipper nodes + connecting line) must clear the frame
  // before the wordmark lands there, or the two overlap unreadably --
  // found on frame-check at t=14s/16s (wordmark text drawn directly over
  // "Manifest declared shipper" / "One hop back from the flag").
  const graphFadeOut = 1 - clamp(t, 14.6, 15.35, 0, 1);

  const cx = width / 2;
  const flaggedCy = height / 2 - 40 + pullBack * -70;
  const shipperCy = flaggedCy + 190;
  const shipperCx = cx + 30;
  const flaggedCx = cx - 30;

  return (
    <AbsoluteFill style={{ backgroundColor: NAVY, overflow: 'hidden' }}>
      <ManifestWall opacity={wallOpacity} highlightIndex={11} frame={frame} />

      {/* Connecting line, one hop back -- drawn before the nodes so it sits underneath */}
      <svg width={width} height={height} style={{ position: 'absolute', inset: 0 }}>
        <line
          x1={flaggedCx} y1={flaggedCy} x2={shipperCx} y2={shipperCy}
          stroke={SLATE} strokeWidth={2} strokeDasharray="6 6"
          opacity={lineIn * 0.7 * graphFadeOut}
        />
      </svg>

      {/* The flag: sanctions hit, front and center at open */}
      <div
        style={{
          position: 'absolute', left: flaggedCx, top: flaggedCy,
          transform: `translate(-50%, -50%) scale(${flagPillIn * graphScale})`,
          opacity: (flagPillHold ? 1 : flagPillIn) * graphFadeOut,
          display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 10,
        }}
      >
        <div
          style={{
            background: RED_LIGHT, color: RED, border: `2px solid ${RED}`,
            borderRadius: 8, padding: '10px 22px', fontFamily: 'system-ui, sans-serif',
            fontWeight: 800, fontSize: 26, letterSpacing: 1,
          }}
        >
          FLAGGED
        </div>
        <div style={{ color: 'white', fontFamily: 'system-ui, sans-serif', fontSize: 20, fontWeight: 600, opacity: 0.9 }}>
          Government Sanctions List
        </div>
      </div>

      {/* One hop back: the clean shipper name it's hiding behind */}
      <div
        style={{
          position: 'absolute', left: shipperCx, top: shipperCy,
          transform: `translate(-50%, -50%) scale(${shipperIn})`,
          opacity: shipperIn * graphFadeOut,
          display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 10,
        }}
      >
        <div
          style={{
            background: GREEN_LIGHT, color: GREEN, border: `2px solid ${GREEN}`,
            borderRadius: 8, padding: '8px 20px', fontFamily: 'system-ui, sans-serif',
            fontWeight: 700, fontSize: 18,
          }}
        >
          Manifest declared shipper
        </div>
        <div style={{ color: SLATE, fontFamily: 'system-ui, sans-serif', fontSize: 15 }}>
          One hop back from the flag
        </div>
      </div>

      {/* Emma's second line */}
      <div
        style={{
          position: 'absolute', left: cx, bottom: 130, transform: 'translateX(-50%)',
          opacity: q3In, color: 'white', fontFamily: 'system-ui, sans-serif',
          fontSize: 32, fontWeight: 600, textAlign: 'center',
        }}
      >
        So how did anyone even find it?
      </div>

      {/* Close: UnmaskIQ wordmark */}
      <div
        style={{
          position: 'absolute', left: cx, top: height / 2, transform: 'translate(-50%, -50%)',
          opacity: closeIn, textAlign: 'center',
        }}
      >
        <div
          style={{
            color: 'white', fontFamily: 'system-ui, sans-serif', fontSize: 56,
            fontWeight: 800, letterSpacing: 1, opacity: wordmarkIn,
            transform: `scale(${0.9 + wordmarkIn * 0.1})`,
          }}
        >
          UNMASKIQ
        </div>
        <div
          style={{
            color: SLATE, fontFamily: 'system-ui, sans-serif', fontSize: 20,
            marginTop: 8, opacity: wordmarkIn,
          }}
        >
          Illegal Transshipment
        </div>
      </div>
    </AbsoluteFill>
  );
};
