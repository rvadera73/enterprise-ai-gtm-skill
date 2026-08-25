import React from 'react';
import { Composition } from 'remotion';
import { VideoA } from './VideoA.jsx';
import { VideoB } from './VideoB.jsx';
import { UnmaskIQBeat0 } from './UnmaskIQBeat0.jsx';
import timingsA from './timings-VideoA.json';
import timingsB from './timings-VideoB.json';

const FPS = 30;
const frames = (t) => Math.ceil((t.total + 0.9) * FPS);

// UnmaskIQ Beat 0 cold open -- 25fps/1600x1000 to match the Playwright
// screen-capture beats it's concatenated with (unmaskiq_output/
// narration_timing.json: beat 0 spans 0.00-16.895s).
const BEAT0_FPS = 25;
const BEAT0_DURATION_SEC = 16.895;

export const RemotionRoot = () => (
  <>
    <Composition id="VideoA" component={VideoA} durationInFrames={frames(timingsA)}
      fps={FPS} width={1080} height={1080} />
    <Composition id="VideoB" component={VideoB} durationInFrames={frames(timingsB)}
      fps={FPS} width={1080} height={1080} />
    <Composition id="UnmaskIQBeat0" component={UnmaskIQBeat0}
      durationInFrames={Math.ceil(BEAT0_DURATION_SEC * BEAT0_FPS)}
      fps={BEAT0_FPS} width={1600} height={1000} />
  </>
);
