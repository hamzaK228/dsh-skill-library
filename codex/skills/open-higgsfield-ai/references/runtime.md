# Runtime and implementation drift

Reviewed https://github.com/Autom8AI/Open-Higgsfield-AI at `297151c245e35696e1519d66c40d09011167bb2d`, 2026-11-09.

The README describes Muapi and older framework versions, but the current standalone shell stores a KIE key and its studio components import `packages/studio/src/kie.js`. The named `muapi.js` file in the README was absent at this revision. Do not connect a Muapi credential to a KIE route or promise the README's model catalog works as stated.

Inspected implementation:

- `components/StandaloneShell.js`: chooses image/video/lipsync/cinema components and uses the browser-local `kie_key` slot. Do not inspect or copy the value during diagnostics.
- `packages/studio/src/kie.js`: base URL `https://api.kie.ai`, Bearer authorization. General jobs submit `POST /api/v1/jobs/createTask` with model/input and poll `GET /api/v1/jobs/recordInfo?taskId=...`. Veo uses `/api/v1/veo/generate` and `/api/v1/veo/record-info`. File uploads use `/api/v1/file-stream-upload`.
- Model mapping uses substring branches and fallback models; UI labels are insufficient evidence of the model actually submitted. Inspect `imageSlug`, `editSlug` and `videoSlug` before relying on a model selection.
- `package.json` uses Next 15/React 19, npm workspaces and both Next and Vite/Electron scripts. Follow its lockfile/engines and supported Node release during requested setup; do not rely on the README's Next 14/React 18 section.

Documented local scripts: `npm run dev` (Next), `npm run build`, `npm run start`; desktop build scripts run Vite and electron-builder. Dependencies are separate and have not been installed by this adapter. Inspect scripts/configs before execution. Never blindly run recursive quarantine removal, disable Gatekeeper/SmartScreen, or install an unsigned binary because a README recommends it.

The README claims free use and local data, but the implementation sends inputs to remote providers. Current account credits, model pricing and data handling require verification for the user's actual instance. This inspection made no network generation, upload or credential check.
