import "./index.css";
import {Composition} from "remotion";
import {CodexFrameworkDiagramVideo} from "./Composition";

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="CodexFrameworkDiagramVideo"
      component={CodexFrameworkDiagramVideo}
      durationInFrames={1080}
      fps={30}
      width={1080}
      height={1920}
    />
  );
};
