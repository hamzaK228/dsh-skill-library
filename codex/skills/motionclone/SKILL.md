---
name: motionclone
description: Reconstruct reference motion with MotionClone or edit its exported HyperFrames projects, including typography, scene geometry, timing, and comparison exports.
---

# MotionClone

Use for a reference video that should become editable motion graphics, or an existing MotionClone export. This adapter supplies workflow guidance for Codex and Claude Code; it does not install the Windows application.

1. Identify whether the input is a reference video, a local application project, or an exported HyperFrames ZIP. Read [runtime notes](references/runtime.md) for platform and availability constraints before offering reconstruction.
2. For reconstruction, use a user-configured app/studio and authorized reference. Check availability before uploading anything. Selected frames are analyzed remotely through the user's Codex/ChatGPT access. The documented local app uses Codex; Claude Code can edit the exported code, but a native Claude reconstruction integration is not documented.
3. For exported projects, extract into a separate workspace, inspect its README and package scripts, and check existing dependencies. Generated scenes use `project.json` and `npm run sync`; authored scenes use `scene-*.js` and `tokens.css`. Edit the requested text, colors, geometry, or timing in the actual source format. Do not edit generated output that the sync step will replace.
4. Use the export's preview/render scripts after inspecting their definitions. Dependency installation requires the runtime setup scope; merely loading this skill does not install anything. Inspect representative frames and playback, then verify the exported file with ffprobe.
5. Report which artifact was produced: editable project, rebuilt video, or comparison MP4. Note approximate reconstruction, missing assets, or text/font mismatches. Original reference media is excluded from editable ZIPs; request a usable source when needed.

Provenance and availability: [SOURCE-NOTICE.md](SOURCE-NOTICE.md).
