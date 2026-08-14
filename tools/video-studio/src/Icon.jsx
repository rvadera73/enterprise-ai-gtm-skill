import React from 'react';

/** Crisp (non-sketched) Lucide icon renderer — precision-engineering register,
 * not the hand-drawn rough.js look used elsewhere. Lucide IconNode: array of
 * [tag, attrs] on a 24x24 grid. */
export const Icon = ({ icon, size = 24, color = 'currentColor', strokeWidth = 1.8, style }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color}
    strokeWidth={strokeWidth} strokeLinecap="round" strokeLinejoin="round" style={style}>
    {(icon || []).map(([tag, a], i) => {
      if (tag === 'path') return <path key={i} d={a.d} />;
      if (tag === 'circle') return <circle key={i} cx={a.cx} cy={a.cy} r={a.r} />;
      if (tag === 'line') return <line key={i} x1={a.x1} y1={a.y1} x2={a.x2} y2={a.y2} />;
      if (tag === 'rect') return <rect key={i} x={a.x} y={a.y} width={a.width} height={a.height} rx={a.rx} />;
      if (tag === 'ellipse') return <ellipse key={i} cx={a.cx} cy={a.cy} rx={a.rx} ry={a.ry} />;
      if (tag === 'polyline') return <polyline key={i} points={a.points} />;
      if (tag === 'polygon') return <polygon key={i} points={a.points} />;
      return null;
    })}
  </svg>
);
