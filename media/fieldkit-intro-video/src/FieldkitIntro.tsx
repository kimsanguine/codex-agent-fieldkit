import React from 'react';
import {
  AbsoluteFill,
  Easing,
  interpolate,
  Sequence,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';

const palette = {
  paper: '#fbfaf4',
  ink: '#111111',
  muted: '#77736b',
  blue: '#315f9f',
  green: '#2f6f5e',
  orange: '#d46a32',
  violet: '#7553a8',
};

const fade = (frame: number, start: number, duration: number) =>
  interpolate(frame, [start, start + duration], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

const slide = (frame: number, start: number, from: number) =>
  interpolate(frame, [start, start + 22], [from, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

const DotGrid = () => (
  <svg width="1920" height="1080" style={{position: 'absolute', inset: 0}}>
    <defs>
      <pattern id="dot" width="24" height="24" patternUnits="userSpaceOnUse">
        <circle cx="2" cy="2" r="1.1" fill={palette.ink} opacity="0.06" />
      </pattern>
    </defs>
    <rect width="1920" height="1080" fill={palette.paper} />
    <rect width="1920" height="1080" fill="url(#dot)" />
    <rect x="34" y="34" width="1852" height="1012" fill="none" stroke={palette.ink} strokeOpacity="0.42" strokeWidth="2" />
    <line x1="120" y1="34" x2="120" y2="1046" stroke={palette.ink} strokeOpacity="0.12" />
    <line x1="34" y1="936" x2="1886" y2="936" stroke={palette.ink} strokeOpacity="0.12" />
  </svg>
);

const Label = ({children, x, y, color = palette.muted}: {children: React.ReactNode; x: number; y: number; color?: string}) => (
  <div
    style={{
      position: 'absolute',
      left: x,
      top: y,
      fontFamily: 'Menlo, Consolas, monospace',
      fontSize: 24,
      letterSpacing: 4,
      color,
      textTransform: 'uppercase',
    }}
  >
    {children}
  </div>
);

const Layer = ({label, index, color}: {label: string; index: number; color: string}) => {
  const frame = useCurrentFrame();
  const enter = fade(frame, 78 + index * 12, 18);
  const y = index * 92;
  return (
    <g opacity={enter} transform={`translate(${slide(frame, 78 + index * 12, 90)} ${y})`}>
      <polygon points="75,0 710,0 642,76 0,76" fill={palette.paper} stroke={palette.ink} strokeWidth="2" />
      <polygon points="650,15 690,15 622,91 584,91" fill={color} opacity="0.28" stroke={color} strokeWidth="2" />
      <rect x="150" y="14" width="48" height="48" fill={color} opacity="0.18" stroke={color} strokeWidth="2" />
      <text x="236" y="49" fill={palette.ink} fontFamily="Menlo, Consolas, monospace" fontSize="27" letterSpacing="2">
        {label}
      </text>
    </g>
  );
};

const Workflow = () => {
  const frame = useCurrentFrame();
  const progress = spring({
    frame: frame - 70,
    fps: 30,
    config: {damping: 18, stiffness: 80},
  });
  const x = interpolate(progress, [0, 1], [110, 0]);
  const opacity = fade(frame, 60, 22);
  return (
    <svg width="910" height="620" style={{position: 'absolute', right: 112, top: 182, opacity, transform: `translateX(${x}px)`}}>
      <text x="26" y="28" fill={palette.muted} fontFamily="Menlo, Consolas, monospace" fontSize="22" letterSpacing="4">
        DELIVERY LOOP
      </text>
      <g transform="translate(122 68)">
        <Layer label="FOLDER" index={0} color={palette.blue} />
        <Layer label="MEMORY" index={1} color={palette.green} />
        <Layer label="DATA" index={2} color={palette.orange} />
        <Layer label="EVAL" index={3} color={palette.violet} />
        <Layer label="SAFETY" index={4} color={palette.blue} />
        <Layer label="HANDOFF" index={5} color={palette.green} />
      </g>
      <path d="M14 210 C74 210 106 148 152 148" fill="none" stroke={palette.blue} strokeWidth="3" strokeLinecap="square" />
      <path d="M14 390 C110 390 100 572 270 572" fill="none" stroke={palette.green} strokeWidth="3" strokeLinecap="square" />
      <circle cx="14" cy="210" r="8" fill={palette.paper} stroke={palette.blue} strokeWidth="3" />
      <circle cx="14" cy="390" r="8" fill={palette.paper} stroke={palette.green} strokeWidth="3" />
      <text x="0" y="184" fill={palette.muted} fontFamily="Menlo, Consolas, monospace" fontSize="20">IDEA</text>
      <text x="0" y="365" fill={palette.muted} fontFamily="Menlo, Consolas, monospace" fontSize="20">OPERATOR</text>
    </svg>
  );
};

const OutputCard = ({children, color, top, start}: {children: React.ReactNode; color: string; top: number; start: number}) => {
  const frame = useCurrentFrame();
  return (
    <div
      style={{
        position: 'absolute',
        right: 88,
        top,
        width: 180,
        height: 64,
        border: `2px solid ${color}`,
        borderRadius: 8,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: 'Menlo, Consolas, monospace',
        fontSize: 25,
        color,
        background: palette.paper,
        opacity: fade(frame, start, 14),
        transform: `translateX(${slide(frame, start, 46)}px)`,
      }}
    >
      {children}
    </div>
  );
};

export const FieldkitIntro = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const title = fade(frame, 8, 24);
  const sub = fade(frame, 34, 24);
  const underline = interpolate(frame, [48, 82], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
  const finalOpacity = fade(frame, 250, 24);

  return (
    <AbsoluteFill style={{backgroundColor: palette.paper, color: palette.ink}}>
      <DotGrid />
      <Label x={142} y={88} color={palette.orange}>FIG_CAF_VIDEO / PUBLIC-SAFE DELIVERY KIT</Label>
      <Label x={142} y={970}>SYNTHETIC FAQ / GOLDEN SET / SAFETY SCAN / HANDOFF</Label>

      <Sequence from={0}>
        <div
          style={{
            position: 'absolute',
            left: 142,
            top: 250,
            fontFamily: 'Georgia, serif',
            fontWeight: 700,
            fontSize: 118,
            lineHeight: 1.02,
            opacity: title,
            transform: `translateY(${slide(frame, 8, 36)}px)`,
          }}
        >
          Codex Agent
          <br />
          Fieldkit
        </div>
        <div
          style={{
            position: 'absolute',
            left: 142,
            top: 520,
            width: 680,
            height: 7,
            background: `linear-gradient(90deg, ${palette.orange} ${underline * 100}%, rgba(17,17,17,0.18) ${underline * 100}%)`,
          }}
        />
        <div
          style={{
            position: 'absolute',
            left: 142,
            top: 570,
            fontFamily: 'Inter, system-ui, sans-serif',
            fontWeight: 750,
            fontSize: 45,
            opacity: sub,
          }}
        >
          From prompt docs to verified agent handoff
        </div>
      </Sequence>

      <Workflow />
      <OutputCard color={palette.blue} top={280} start={150}>DEMO</OutputCard>
      <OutputCard color={palette.green} top={375} start={166}>TESTS</OutputCard>
      <OutputCard color={palette.orange} top={470} start={182}>REPORT</OutputCard>
      <OutputCard color={palette.violet} top={565} start={198}>HANDOFF</OutputCard>

      <div
        style={{
          position: 'absolute',
          left: 142,
          bottom: 90,
          fontFamily: 'Inter, system-ui, sans-serif',
          fontSize: 34,
          color: palette.muted,
          opacity: finalOpacity,
        }}
      >
        No API key for the starter. Synthetic data only. Not production certification.
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          bottom: 30,
          width: '100%',
          height: 8,
          background: `repeating-linear-gradient(90deg, ${palette.ink} 0 28px, transparent 28px 40px, ${palette.green} 40px 58px, transparent 58px 70px, ${palette.blue} 70px 84px, transparent 84px 94px, ${palette.orange} 94px 104px, transparent 104px 118px)`,
          opacity: interpolate(frame, [0, fps], [0, 1], {extrapolateRight: 'clamp'}),
        }}
      />
    </AbsoluteFill>
  );
};
