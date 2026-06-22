import {Composition} from 'remotion';
import {FieldkitIntro} from './FieldkitIntro';

export const Root = () => {
  return (
    <Composition
      id="FieldkitIntro"
      component={FieldkitIntro}
      durationInFrames={360}
      fps={30}
      width={1920}
      height={1080}
    />
  );
};
