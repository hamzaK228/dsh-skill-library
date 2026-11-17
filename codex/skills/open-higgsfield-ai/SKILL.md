---
name: open-higgsfield-ai
description: Work with the Open Higgsfield AI image, video, cinema and lip-sync studio, checking its actual provider client, model routing and generation job lifecycle.
---

# Open Higgsfield AI

Use for this specific application, a user's configured instance, or requested setup/development of it. This adapter provides guidance; no native MCP connection or skill pack was found at the reviewed revision.

1. Identify the actual checkout/instance and whether it runs the Next.js standalone UI, Electron/Vite app, or a hosted variant. Read [runtime notes](references/runtime.md). The reviewed fork's README and implementation disagree about the provider; resolve that before requesting credentials or submitting a job.
2. Inspect the active model definitions and the imported provider client. Match the selected UI model to the actual API model/parameters. Do not infer availability, prices, multi-image limits or the output model from marketing lists. Some client branches silently map unrecognized IDs to defaults; disclose and avoid an unintended model substitution.
3. Draft the prompt, selected inputs, duration/aspect ratio and output target before generation. In the UI, reference images change image/video generation mode; lip sync requires both a source image/video and audio. Validate input counts and supported parameters against the active route.
4. Use an existing authorized instance/connection, or inspect and prepare runtime setup when requested. A self-hosted UI still sends prompts/media to a remote generation provider. Keep credentials out of prompts/logs; user entry of a key belongs in the provider/application's intended local UI or secret store.
5. For an authorized generation, retain the returned task ID, poll its actual provider status with a bounded wait, and report failures without resubmitting a paid job blindly. Download only the authorized generated result to the selected output directory and inspect it with a media probe and visual playback.

No account connection, generation spend, source upload or OS security-setting change is implied by skill installation. [Provenance and README drift](SOURCE-NOTICE.md).
