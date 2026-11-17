# Engine choice and lively motion

Read this reference when choosing an engine or improving scene/character motion. Keep the approved story, assets, output format and project stack; engine choice is not authorization to install packages or expand scope.

## Adapt techniques to the deliverable

- **Motion:** use the selected Motion specialist for React/UI springs, gestures, layout changes and responsive interaction. Preserve reduced-motion behavior and the existing UI hierarchy. Public `animate` techniques are documented at [Motion animate](https://motion.dev/docs/animate); do not copy or fetch gated Motion+ implementations.
- **Anime.js:** use the selected Anime specialist for coordinated timelines, SVG drawing/morphing and stagger. Consult the installed version before using API syntax. The public [timeline documentation](https://animejs.com/documentation/timeline/) supports sequencing techniques; it is a reference, not a script to run.
- **Remotion:** choose it for rendered video. Build the composition around the frame and `fps`, with `interpolate`/`spring` or equivalent pure calculations. Reuse Motion/Anime choreography concepts without requiring both libraries. If an installed timeline engine is necessary, pause automatic playback and seek from the current frame on every render; verify out-of-order and repeated frame renders give the same visual result. Do not let wall-clock time, rAF loops, CSS animations or timers advance the export independently.

Load only the relevant specialist and its needed references. Keep public technique reuse separate from dependencies: an ease, stagger or anticipation pattern does not require adding its source engine. Prefer the existing compatible engine when it meets the task.

## Fast, smooth character and scene motion

Treat these as starting points to tune to scale, tone, frame rate and narration, not fixed numeric requirements:

- Give a major move a brief anticipation, a readable travel arc, an arrival and a restrained settle. A roughly 0.2–0.45 second arrival can suit a quick accent; slower explanation or larger travel may need more time.
- Coordinate body lean and squash/stretch with velocity; let limbs follow through instead of moving the entire character as a rigid sticker.
- Add quick blinks, deliberate gaze, expression and hand/foot gestures when character animation is requested. Preserve the supplied silhouette, colors and identity. Use pauses so the character remains expressive without competing continuously with the message.
- Stagger related items with a clear reading order. Keep motion away from captions, important text, faces and the action being demonstrated; preserve mobile legibility.
- Match transitions to the story and voice. Do not equate extra bounce, perpetual bobbing or a static replacement image with a better animation.

## Check the delivered motion

Inspect representative rendered frames, scene boundaries and the ending for clipping, overlap and legibility. Watch the actual rendered clip at 1× to assess speed, smoothness, settle and whether gestures support the speech. Where applicable check the UI interaction and reduced-motion variant as well. A successful build or a contact sheet alone does not verify animation quality or audio timing. Name any unavailable playback/render checks and pass the remaining check to the next owner.
