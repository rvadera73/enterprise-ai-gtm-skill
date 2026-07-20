import React from 'react';
import rough from 'roughjs/bin/rough';

const gen = rough.generator();

/**
 * Hand-drawn primitives.
 *
 * IMPORTANT: every shape must pass a stable `seed`. rough.js randomises its wobble
 * on each call, so without a fixed seed the geometry would be regenerated
 * differently on every rendered frame and the video would strobe.
 *
 * `p` (0..1) draws the stroke on progressively, as if someone is drawing it.
 */

const useStroke = (make, deps) => React.useMemo(make, deps);

const Paths = ({ paths, p, len, opacity = 1 }) => (
  <>
    {paths.map((path, i) => (
      <path
        key={i}
        d={path.d}
        stroke={path.stroke === 'none' ? undefined : path.stroke}
        strokeWidth={path.strokeWidth}
        fill={path.fill && path.fill !== 'none' ? path.fill : 'none'}
        strokeLinecap="round"
        strokeLinejoin="round"
        opacity={opacity}
        strokeDasharray={len}
        strokeDashoffset={len * (1 - p)}
      />
    ))}
  </>
);

export const SkRect = ({ x, y, w, h, seed, p = 1, stroke = '#2A3540', strokeWidth = 2.2, fill, fillStyle = 'hachure', roughness = 1.25, opacity = 1 }) => {
  const paths = useStroke(
    () => gen.toPaths(gen.rectangle(x, y, w, h, {
      seed, stroke, strokeWidth, roughness, bowing: 1.1,
      fill, fillStyle, fillWeight: 1.6, hachureGap: 7, hachureAngle: -41,
    })),
    [x, y, w, h, seed, stroke, strokeWidth, fill, fillStyle, roughness],
  );
  return <Paths paths={paths} p={p} len={(w + h) * 2.9} opacity={opacity} />;
};

export const SkEllipse = ({ cx, cy, w, h, seed, p = 1, stroke = '#2A3540', strokeWidth = 2.4, fill, fillStyle = 'hachure', roughness = 1.1, opacity = 1 }) => {
  const paths = useStroke(
    () => gen.toPaths(gen.ellipse(cx, cy, w, h, {
      seed, stroke, strokeWidth, roughness, bowing: 1,
      fill, fillStyle, fillWeight: 1.6, hachureGap: 7,
    })),
    [cx, cy, w, h, seed, stroke, strokeWidth, fill, fillStyle, roughness],
  );
  return <Paths paths={paths} p={p} len={(w + h) * 2.4} opacity={opacity} />;
};

export const SkLine = ({ x1, y1, x2, y2, seed, p = 1, stroke = '#2A3540', strokeWidth = 2, roughness = 1.3, opacity = 1 }) => {
  const paths = useStroke(
    () => gen.toPaths(gen.line(x1, y1, x2, y2, { seed, stroke, strokeWidth, roughness, bowing: 1.6 })),
    [x1, y1, x2, y2, seed, stroke, strokeWidth, roughness],
  );
  const len = Math.hypot(x2 - x1, y2 - y1) * 1.8;
  return <Paths paths={paths} p={p} len={len} opacity={opacity} />;
};

/** Marker underline — a whiteboard emphasis gesture, not a rectangle. */
export const SkUnderline = ({ x, y, w, seed, p = 1, stroke = '#C2721A', strokeWidth = 7, opacity = 0.55 }) => {
  const paths = useStroke(
    () => gen.toPaths(gen.line(x, y, x + w, y, { seed, stroke, strokeWidth, roughness: 2.1, bowing: 3.4 })),
    [x, y, w, seed, stroke, strokeWidth],
  );
  return <Paths paths={paths} p={p} len={w * 1.9} opacity={opacity} />;
};

/**
 * Lucide icon rendered hand-drawn.
 *
 * Lucide ships icons as IconNode: [[tag, attrs], ...] on a 24x24 grid. Each
 * primitive maps onto a rough.js generator, so we keep Lucide's real geometry but
 * in the same sketched language as everything else — a crisp vector icon would
 * read as pasted-in against the drawn boxes.
 */
export const SkIcon = ({ icon, x, y, size = 24, seed = 1, p = 1, stroke = '#28323C', strokeWidth = 1.6 }) => {
  const paths = React.useMemo(() => {
    const o = { seed, stroke, strokeWidth, roughness: 0.9, bowing: 1.2 };
    const out = [];
    (icon || []).forEach(([tag, a], i) => {
      const s = { ...o, seed: seed + i * 3 };
      let drawable = null;
      if (tag === 'path') drawable = gen.path(a.d, s);
      else if (tag === 'circle') drawable = gen.circle(+a.cx, +a.cy, +a.r * 2, s);
      else if (tag === 'line') drawable = gen.line(+a.x1, +a.y1, +a.x2, +a.y2, s);
      else if (tag === 'rect') drawable = gen.rectangle(+a.x, +a.y, +a.width, +a.height, s);
      else if (tag === 'ellipse') drawable = gen.ellipse(+a.cx, +a.cy, +a.rx * 2, +a.ry * 2, s);
      else if (tag === 'polyline' || tag === 'polygon') {
        const pts = a.points.trim().split(/[\s,]+/).map(Number);
        const arr = [];
        for (let k = 0; k < pts.length; k += 2) arr.push([pts[k], pts[k + 1]]);
        drawable = tag === 'polygon' ? gen.polygon(arr, s) : gen.linearPath(arr, s);
      }
      if (drawable) out.push(...gen.toPaths(drawable));
    });
    return out;
  }, [icon, seed, stroke, strokeWidth]);

  const k = size / 24;
  return (
    <g transform={`translate(${x} ${y}) scale(${k})`}>
      <Paths paths={paths} p={p} len={120} />
    </g>
  );
};

/**
 * Stick figure — the thing that makes a whiteboard read as a person thinking
 * rather than a diagram tool. Used to show the team behind each application.
 */
export const SkFigure = ({ x, y, h = 40, seed = 1, p = 1, stroke = '#28323C', strokeWidth = 2 }) => {
  const paths = React.useMemo(() => {
    const o = { seed, stroke, strokeWidth, roughness: 1.5, bowing: 1.6 };
    const head = h * 0.26;
    const cx = x, top = y;
    const neck = top + head;
    const hip = top + h * 0.62;
    const out = [];
    out.push(...gen.toPaths(gen.circle(cx, top + head / 2, head, { ...o, seed })));
    out.push(...gen.toPaths(gen.line(cx, neck, cx, hip, { ...o, seed: seed + 1 })));
    out.push(...gen.toPaths(gen.line(cx - h * 0.24, neck + h * 0.16, cx + h * 0.24, neck + h * 0.16, { ...o, seed: seed + 2 })));
    out.push(...gen.toPaths(gen.line(cx, hip, cx - h * 0.2, y + h, { ...o, seed: seed + 3 })));
    out.push(...gen.toPaths(gen.line(cx, hip, cx + h * 0.2, y + h, { ...o, seed: seed + 4 })));
    return out;
  }, [x, y, h, seed, stroke, strokeWidth]);
  return <Paths paths={paths} p={p} len={h * 2.2} />;
};

/** Hand-drawn brace/circle-around for "look here" moments. */
export const SkCircleAround = ({ cx, cy, w, h, seed, p = 1, stroke = '#C2721A', strokeWidth = 3 }) => {
  const paths = useStroke(
    () => gen.toPaths(gen.ellipse(cx, cy, w, h, { seed, stroke, strokeWidth, roughness: 2.4, bowing: 2 })),
    [cx, cy, w, h, seed, stroke, strokeWidth],
  );
  return <Paths paths={paths} p={p} len={(w + h) * 2.4} />;
};
