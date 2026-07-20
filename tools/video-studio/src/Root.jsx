import React from 'react';
import { Composition } from 'remotion';
import { VideoA } from './VideoA.jsx';
import { VideoB } from './VideoB.jsx';
import timingsA from './timings-VideoA.json';
import timingsB from './timings-VideoB.json';

const FPS = 30;
const frames = (t) => Math.ceil((t.total + 0.9) * FPS);

export const RemotionRoot = () => (
  <>
    <Composition id="VideoA" component={VideoA} durationInFrames={frames(timingsA)}
      fps={FPS} width={1080} height={1080} />
    <Composition id="VideoB" component={VideoB} durationInFrames={frames(timingsB)}
      fps={FPS} width={1080} height={1080} />
  </>
);
