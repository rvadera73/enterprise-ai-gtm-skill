import React from 'react';
import { Composition } from 'remotion';
import { VideoA } from './VideoA.jsx';
import timings from './timings.json';

const FPS = timings.fps || 30;

export const RemotionRoot = () => (
  <>
    <Composition
      id="VideoA"
      component={VideoA}
      durationInFrames={Math.ceil((timings.total + 0.9) * FPS)}
      fps={FPS}
      width={1080}
      height={1080}
    />
  </>
);
