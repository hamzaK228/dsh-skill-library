# Runtime and export workflow

Reviewed 2026-11-09: [agent guide](https://motionclone.lol/agents), [setup guide](https://motionclone.lol/get-started).

The local app is documented for Windows with Python 3.11+, Node 22+, Git, Chrome, FFmpeg/ffprobe and the official Codex CLI. Its launcher is `start.ps1`; the documented UI port is 4319. This Linux machine has not been validated as a reconstruction host.

The official site links `https://github.com/blixvip/MotionClone`, but the GitHub connector returned 404 during this review. No source checkout, installer, or native skill could be verified. Do not present a clone/install command as tested. Recheck the official source before runtime setup, or work from a user-provided export. The hosted studio requires sign-in and a separate ChatGPT connection; no public rendering API is documented.

Within an existing export, inspect `package.json` before running commands. Typical scripts are `npm run sync` for project.json scenes, `npm run preview`, and `npm run render`. Ensure required assets exist and keep output separate from source media. Verify output duration, dimensions, audio, visible text and the requested aspect ratio. A comparison render is distinct from the rebuilt-only video.

AI access and usage limits are separate from the app download. Frame analysis contacts ChatGPT, and a public-video download contacts its source service. User-approved uploads and account connections are necessary for those operations; installation of this adapter supplies neither.
