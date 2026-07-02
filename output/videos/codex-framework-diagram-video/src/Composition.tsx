import type {CSSProperties, ReactNode} from "react";
import {
  AbsoluteFill,
  Easing,
  Img,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

const scenes = [
  {start: 0, end: 120},
  {start: 120, end: 270},
  {start: 270, end: 450},
  {start: 450, end: 630},
  {start: 630, end: 810},
  {start: 810, end: 960},
  {start: 960, end: 1080},
] as const;

const colors = {
  ink: "#121826",
  muted: "#526173",
  paper: "#f8fafc",
  panel: "rgba(255,255,255,0.86)",
  line: "rgba(25, 33, 46, 0.12)",
  blue: "#2563eb",
  cyan: "#06b6d4",
  violet: "#7c3aed",
  orange: "#f97316",
  green: "#16a34a",
};

const clamp = {
  extrapolateLeft: "clamp" as const,
  extrapolateRight: "clamp" as const,
};

const easeOut = Easing.bezier(0.16, 1, 0.3, 1);
const easeInOut = Easing.bezier(0.45, 0, 0.55, 1);

const fit = (value: number, start: number, end: number) =>
  interpolate(value, [start, end], [0, 1], {
    ...clamp,
    easing: easeOut,
  });

const sceneOpacity = (frame: number, start: number, end: number) =>
  interpolate(frame, [start, start + 18, end - 18, end], [0, 1, 1, 0], clamp);

const liftIn = (frame: number, delay = 0, distance = 44) => {
  const progress = fit(frame, delay, delay + 28);
  return {
    opacity: progress,
    transform: `translateY(${(1 - progress) * distance}px)`,
  };
};

const softCard: CSSProperties = {
  background: colors.panel,
  border: `1px solid ${colors.line}`,
  borderRadius: 34,
  boxShadow: "0 28px 90px rgba(15, 23, 42, 0.13)",
  backdropFilter: "blur(18px)",
};

const Base = ({children}: {children: ReactNode}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const pulse = interpolate(
    frame,
    [0, fps * 18, fps * 36],
    [0, 1, 0],
    {...clamp, easing: easeInOut},
  );

  return (
    <AbsoluteFill
      style={{
        background:
          "radial-gradient(circle at 16% 8%, rgba(37,99,235,0.20), transparent 28%), radial-gradient(circle at 86% 18%, rgba(6,182,212,0.18), transparent 30%), linear-gradient(180deg, #f8fafc 0%, #eef6ff 58%, #f8fafc 100%)",
        color: colors.ink,
        fontFamily:
          'Inter, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif',
        overflow: "hidden",
      }}
    >
      <div
        style={{
          position: "absolute",
          inset: 0,
          opacity: 0.26,
          backgroundImage:
            "linear-gradient(rgba(37, 99, 235, 0.14) 1px, transparent 1px), linear-gradient(90deg, rgba(37, 99, 235, 0.14) 1px, transparent 1px)",
          backgroundSize: "72px 72px",
          transform: `translateY(${-pulse * 36}px)`,
        }}
      />
      <div
        style={{
          position: "absolute",
          width: 620,
          height: 620,
          borderRadius: 999,
          left: -190,
          top: 230,
          background:
            "linear-gradient(135deg, rgba(37,99,235,0.13), rgba(6,182,212,0.08))",
          filter: "blur(6px)",
        }}
      />
      <div
        style={{
          position: "absolute",
          width: 520,
          height: 520,
          borderRadius: 999,
          right: -210,
          bottom: 190,
          background:
            "linear-gradient(135deg, rgba(124,58,237,0.10), rgba(249,115,22,0.10))",
          filter: "blur(8px)",
        }}
      />
      {children}
      <div
        style={{
          position: "absolute",
          left: 72,
          right: 72,
          bottom: 54,
          height: 8,
          borderRadius: 999,
          background: "rgba(15,23,42,0.08)",
          overflow: "hidden",
        }}
      >
        <div
          style={{
            width: `${(frame / (fps * 36)) * 100}%`,
            height: "100%",
            borderRadius: 999,
            background: "linear-gradient(90deg, #2563eb, #06b6d4)",
          }}
        />
      </div>
    </AbsoluteFill>
  );
};

const SceneShell = ({
  index,
  children,
}: {
  index: number;
  children: (localFrame: number) => ReactNode;
}) => {
  const frame = useCurrentFrame();
  const scene = scenes[index];
  const opacity = sceneOpacity(frame, scene.start, scene.end);

  return (
    <AbsoluteFill
      style={{
        opacity,
        pointerEvents: "none",
      }}
    >
      {children(frame - scene.start)}
    </AbsoluteFill>
  );
};

const Label = ({children, color = colors.blue}: {children: ReactNode; color?: string}) => (
  <div
    style={{
      display: "inline-flex",
      alignItems: "center",
      gap: 12,
      padding: "12px 22px",
      borderRadius: 999,
      background: `${color}18`,
      border: `1px solid ${color}35`,
      color,
      fontSize: 26,
      fontWeight: 750,
      letterSpacing: 1,
    }}
  >
    <span
      style={{
        width: 12,
        height: 12,
        borderRadius: 99,
        background: color,
        boxShadow: `0 0 24px ${color}`,
      }}
    />
    {children}
  </div>
);

const BigTitle = ({children}: {children: ReactNode}) => (
  <div
    style={{
      fontSize: 86,
      lineHeight: 1.08,
      letterSpacing: -4,
      fontWeight: 900,
      maxWidth: 910,
    }}
  >
    {children}
  </div>
);

const Subtitle = ({children}: {children: ReactNode}) => (
  <div
    style={{
      marginTop: 26,
      fontSize: 34,
      lineHeight: 1.55,
      color: colors.muted,
      maxWidth: 860,
      fontWeight: 520,
    }}
  >
    {children}
  </div>
);

const Screenshot = ({
  src,
  style,
  caption,
}: {
  src: string;
  style?: CSSProperties;
  caption?: string;
}) => (
  <div style={{...softCard, padding: 14, overflow: "hidden", ...style}}>
    <Img
      src={staticFile(src)}
      style={{
        width: "100%",
        height: "100%",
        objectFit: "cover",
        borderRadius: 22,
        display: "block",
      }}
    />
    {caption ? (
      <div
        style={{
          position: "absolute",
          left: 28,
          bottom: 28,
          padding: "10px 18px",
          borderRadius: 999,
          color: "white",
          fontSize: 22,
          fontWeight: 760,
          background: "rgba(15,23,42,0.72)",
        }}
      >
        {caption}
      </div>
    ) : null}
  </div>
);

const MiniCard = ({
  title,
  text,
  color,
  style,
}: {
  title: string;
  text: string;
  color: string;
  style?: CSSProperties;
}) => (
  <div
    style={{
      ...softCard,
      padding: "30px 30px 28px",
      width: 420,
      minHeight: 210,
      ...style,
    }}
  >
    <div
      style={{
        width: 46,
        height: 46,
        borderRadius: 16,
        background: `${color}20`,
        color,
        fontWeight: 900,
        fontSize: 28,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        marginBottom: 20,
      }}
    >
      ✓
    </div>
    <div style={{fontSize: 34, fontWeight: 850, marginBottom: 10}}>{title}</div>
    <div style={{fontSize: 25, color: colors.muted, lineHeight: 1.45}}>{text}</div>
  </div>
);

const Node = ({
  x,
  y,
  title,
  detail,
  color,
  progress,
}: {
  x: number;
  y: number;
  title: string;
  detail: string;
  color: string;
  progress: number;
}) => (
  <div
    style={{
      position: "absolute",
      left: x,
      top: y,
      width: 250,
      padding: "24px 22px",
      borderRadius: 28,
      background: "rgba(255,255,255,0.92)",
      border: `2px solid ${color}30`,
      boxShadow: "0 22px 60px rgba(15,23,42,0.12)",
      opacity: progress,
      transform: `scale(${0.86 + progress * 0.14})`,
    }}
  >
    <div
      style={{
        width: 38,
        height: 38,
        borderRadius: 14,
        background: color,
        marginBottom: 16,
      }}
    />
    <div style={{fontSize: 31, fontWeight: 880, marginBottom: 6}}>{title}</div>
    <div style={{fontSize: 22, color: colors.muted, lineHeight: 1.38}}>{detail}</div>
  </div>
);

const FlowLine = ({progress}: {progress: number}) => (
  <svg
    width="900"
    height="520"
    viewBox="0 0 900 520"
    style={{position: "absolute", left: 90, top: 630, opacity: 0.9}}
  >
    <path
      d="M190 120 C350 60 500 70 650 130"
      fill="none"
      stroke="#2563eb"
      strokeWidth="8"
      strokeLinecap="round"
      strokeDasharray="680"
      strokeDashoffset={680 * (1 - progress)}
    />
    <path
      d="M660 180 C600 300 430 340 260 325"
      fill="none"
      stroke="#06b6d4"
      strokeWidth="8"
      strokeLinecap="round"
      strokeDasharray="620"
      strokeDashoffset={620 * (1 - progress)}
    />
    <path
      d="M265 360 C395 465 575 455 720 350"
      fill="none"
      stroke="#7c3aed"
      strokeWidth="8"
      strokeLinecap="round"
      strokeDasharray="580"
      strokeDashoffset={580 * (1 - progress)}
    />
  </svg>
);

const Typewriter = ({text, frame, start = 0}: {text: string; frame: number; start?: number}) => {
  const count = Math.floor(interpolate(frame, [start, start + 84], [0, text.length], clamp));
  return <>{text.slice(0, count)}</>;
};

const TitleScene = ({frame}: {frame: number}) => (
  <div style={{position: "absolute", left: 72, top: 180, right: 72}}>
    <div style={liftIn(frame, 0)}>
      <Label>文章转视频 · Codex 工作流</Label>
    </div>
    <div style={{...liftIn(frame, 12), marginTop: 74}}>
      <BigTitle>
        如何用 Codex
        <br />画框架图？
      </BigTitle>
    </div>
    <div style={liftIn(frame, 26)}>
      <Subtitle>把资料、链接和目标交给 Codex，先生成可编辑初稿，再由人调整重点和表达。</Subtitle>
    </div>
    <Screenshot
      src="article-images/01-codex-sidebar.png"
      caption="一句需求 → 结构初稿"
      style={{
        position: "absolute",
        left: 40,
        top: 770,
        width: 870,
        height: 440,
        transform: `translateY(${(1 - fit(frame, 38, 76)) * 70}px) rotate(-2deg)`,
        opacity: fit(frame, 38, 76),
      }}
    />
  </div>
);

const PainSolutionScene = ({frame}: {frame: number}) => {
  const arrow = fit(frame, 54, 90);
  return (
    <div style={{position: "absolute", left: 72, top: 156, right: 72}}>
      <div style={liftIn(frame, 0)}>
        <Label color={colors.orange}>为什么值得做？</Label>
      </div>
      <div style={{...liftIn(frame, 12), marginTop: 48}}>
        <BigTitle>少拖拽，多表达。</BigTitle>
      </div>
      <div style={{display: "flex", gap: 34, marginTop: 100}}>
        <div style={{...liftIn(frame, 28)}}>
          <MiniCard
            title="以前"
            text="反复拖拽、对齐、改文案，结构还容易越画越乱。"
            color={colors.orange}
          />
        </div>
        <div style={{...liftIn(frame, 50)}}>
          <MiniCard
            title="现在"
            text="先让 Codex 提炼结构，直接生成一版可编辑框架图。"
            color={colors.blue}
          />
        </div>
      </div>
      <svg
        width="330"
        height="120"
        viewBox="0 0 330 120"
        style={{position: "absolute", left: 368, top: 555, opacity: arrow}}
      >
        <path
          d="M30 60 H280"
          stroke="#2563eb"
          strokeWidth="10"
          strokeLinecap="round"
          strokeDasharray="260"
          strokeDashoffset={260 * (1 - arrow)}
        />
        <path d="M250 30 L290 60 L250 90" fill="none" stroke="#2563eb" strokeWidth="10" strokeLinecap="round" />
      </svg>
      <div
        style={{
          ...softCard,
          ...liftIn(frame, 78),
          position: "absolute",
          top: 850,
          left: 32,
          right: 32,
          padding: "34px 38px",
          fontSize: 31,
          lineHeight: 1.55,
          color: colors.ink,
        }}
      >
        核心不是“替代审美”，而是快速得到一个<span style={{color: colors.blue, fontWeight: 900}}>能改、能讨论、能沉淀</span>的结构初稿。
      </div>
    </div>
  );
};

const ExcalidrawScene = ({frame}: {frame: number}) => (
  <div style={{position: "absolute", left: 72, top: 128, right: 72}}>
    <div style={liftIn(frame, 0)}>
      <Label>方式一 · Codex + Excalidraw</Label>
    </div>
    <div style={{...liftIn(frame, 10), marginTop: 46}}>
      <BigTitle>个人梳理，先画草图。</BigTitle>
    </div>
    <Screenshot
      src="article-images/02-karpathy-wiki.png"
      caption="资料 → 框架图"
      style={{
        position: "absolute",
        top: 350,
        left: 0,
        width: 936,
        height: 520,
        opacity: fit(frame, 24, 58),
        transform: `translateX(${(1 - fit(frame, 24, 58)) * 70}px)`,
      }}
    />
    <div style={{position: "absolute", top: 930, display: "flex", gap: 22}}>
      <MiniCard title="轻量" text="打开网页就能用，适合快速起稿。" color={colors.cyan} style={{width: 286, minHeight: 188}} />
      <MiniCard title="自由" text="技术草图、文章配图都好改。" color={colors.violet} style={{width: 286, minHeight: 188}} />
      <MiniCard title="可编辑" text="不是死图，元素可以继续移动。" color={colors.green} style={{width: 286, minHeight: 188}} />
    </div>
    <Screenshot
      src="article-images/03-editable-excalidraw.png"
      style={{
        position: "absolute",
        top: 1260,
        left: 100,
        width: 740,
        height: 425,
        opacity: fit(frame, 95, 138),
        transform: `scale(${0.92 + fit(frame, 95, 138) * 0.08})`,
      }}
    />
  </div>
);

const ProcessScene = ({frame}: {frame: number}) => {
  const progress = fit(frame, 38, 116);
  return (
    <div style={{position: "absolute", inset: 0}}>
      <div style={{position: "absolute", left: 72, top: 132, right: 72}}>
        <div style={liftIn(frame, 0)}>
          <Label color={colors.violet}>更稳的操作顺序</Label>
        </div>
        <div style={{...liftIn(frame, 10), marginTop: 46}}>
          <BigTitle>先提炼，再画图。</BigTitle>
        </div>
      </div>
      <FlowLine progress={progress} />
      <Node x={80} y={700} title="资料" detail="文章、链接、说明" color={colors.blue} progress={fit(frame, 22, 50)} />
      <Node x={660} y={720} title="提炼" detail="抓核心概念" color={colors.cyan} progress={fit(frame, 48, 78)} />
      <Node x={170} y={1030} title="生成" detail="画出层级关系" color={colors.violet} progress={fit(frame, 76, 106)} />
      <Node x={620} y={1300} title="调整" detail="删减、改结构、强化重点" color={colors.green} progress={fit(frame, 100, 130)} />
      <div
        style={{
          ...softCard,
          ...liftIn(frame, 132),
          position: "absolute",
          left: 92,
          right: 92,
          bottom: 190,
          padding: "30px 34px",
          fontSize: 30,
          lineHeight: 1.48,
        }}
      >
        复杂资料不要全塞进图里：<span style={{fontWeight: 900, color: colors.violet}}>优先保证读者一眼看懂。</span>
      </div>
    </div>
  );
};

const FeishuScene = ({frame}: {frame: number}) => (
  <div style={{position: "absolute", left: 72, top: 126, right: 72}}>
    <div style={liftIn(frame, 0)}>
      <Label color={colors.green}>方式二 · Codex + 飞书画板</Label>
    </div>
    <div style={{...liftIn(frame, 12), marginTop: 48}}>
      <BigTitle>团队协作，放进文档。</BigTitle>
    </div>
    <Subtitle>如果最终要进入团队文档、多人补充或持续沉淀，飞书画板更合适。</Subtitle>
    <Screenshot
      src="article-images/04-feishu-board.png"
      caption="团队可查看、编辑、补充"
      style={{
        position: "absolute",
        top: 440,
        left: 54,
        width: 828,
        height: 718,
        opacity: fit(frame, 34, 72),
        transform: `translateY(${(1 - fit(frame, 34, 72)) * 70}px)`,
      }}
    />
    <div style={{position: "absolute", top: 1245, left: 20, right: 20, display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24}}>
      {["精简层级", "调整模块关系", "改左右 / 上下结构", "补充说明文字"].map((item, index) => (
        <div
          key={item}
          style={{
            ...softCard,
            padding: "25px 28px",
            fontSize: 30,
            fontWeight: 820,
            opacity: fit(frame, 82 + index * 12, 108 + index * 12),
            transform: `translateY(${(1 - fit(frame, 82 + index * 12, 108 + index * 12)) * 34}px)`,
          }}
        >
          {item}
        </div>
      ))}
    </div>
  </div>
);

const PromptScene = ({frame}: {frame: number}) => (
  <div style={{position: "absolute", left: 72, top: 150, right: 72}}>
    <div style={liftIn(frame, 0)}>
      <Label color={colors.blue}>提示词模板</Label>
    </div>
    <div style={{...liftIn(frame, 10), marginTop: 50}}>
      <BigTitle>这样说，更稳。</BigTitle>
    </div>
    <div
      style={{
        ...softCard,
        ...liftIn(frame, 30),
        marginTop: 92,
        padding: "46px 44px",
        fontSize: 35,
        lineHeight: 1.62,
        minHeight: 590,
      }}
    >
      <span style={{color: colors.blue, fontWeight: 900}}>“</span>
      <Typewriter
        frame={frame}
        start={44}
        text="请根据以下资料，画一张适合技术文章使用的框架图。要求结构清晰、层级分明、文字简洁，突出核心模块和它们之间的关系。生成后保持可编辑。"
      />
      <span style={{color: colors.blue, fontWeight: 900}}>”</span>
      <div
        style={{
          marginTop: 42,
          paddingTop: 32,
          borderTop: "1px solid rgba(15,23,42,0.12)",
          color: colors.muted,
          fontSize: 29,
          opacity: fit(frame, 118, 146),
        }}
      >
        资料复杂时再加一句：先提炼核心概念，不要把所有细节都塞进去。
      </div>
    </div>
    <Screenshot
      src="article-images/05-customize.png"
      style={{
        position: "absolute",
        left: 92,
        top: 1135,
        width: 750,
        height: 455,
        opacity: fit(frame, 132, 165),
        transform: `rotate(${(1 - fit(frame, 132, 165)) * 3 - 1.5}deg)`,
      }}
    />
  </div>
);

const OutroScene = ({frame}: {frame: number}) => (
  <div style={{position: "absolute", left: 72, top: 168, right: 72}}>
    <div style={liftIn(frame, 0)}>
      <Label color={colors.cyan}>小结</Label>
    </div>
    <div style={{...liftIn(frame, 10), marginTop: 62}}>
      <BigTitle>先让 Codex 画结构，再由人判断重点。</BigTitle>
    </div>
    <div style={{display: "flex", flexDirection: "column", gap: 28, marginTop: 96}}>
      <div style={liftIn(frame, 34)}>
        <MiniCard
          title="个人草图"
          text="用 Excalidraw：轻量、自由、可继续编辑。"
          color={colors.blue}
          style={{width: "100%", minHeight: 190}}
        />
      </div>
      <div style={liftIn(frame, 58)}>
        <MiniCard
          title="团队沉淀"
          text="用飞书画板：进入文档，方便协作修改。"
          color={colors.green}
          style={{width: "100%", minHeight: 190}}
        />
      </div>
    </div>
    <div
      style={{
        position: "absolute",
        top: 1220,
        left: 20,
        right: 20,
        fontSize: 50,
        lineHeight: 1.25,
        fontWeight: 900,
        textAlign: "center",
        color: colors.ink,
        opacity: fit(frame, 82, 112),
      }}
    >
      让复杂内容，先变成一张看得懂的图。
    </div>
  </div>
);

export const CodexFrameworkDiagramVideo = () => {
  return (
    <Base>
      <SceneShell index={0}>{(localFrame) => <TitleScene frame={localFrame} />}</SceneShell>
      <SceneShell index={1}>{(localFrame) => <PainSolutionScene frame={localFrame} />}</SceneShell>
      <SceneShell index={2}>{(localFrame) => <ExcalidrawScene frame={localFrame} />}</SceneShell>
      <SceneShell index={3}>{(localFrame) => <ProcessScene frame={localFrame} />}</SceneShell>
      <SceneShell index={4}>{(localFrame) => <FeishuScene frame={localFrame} />}</SceneShell>
      <SceneShell index={5}>{(localFrame) => <PromptScene frame={localFrame} />}</SceneShell>
      <SceneShell index={6}>{(localFrame) => <OutroScene frame={localFrame} />}</SceneShell>
    </Base>
  );
};
