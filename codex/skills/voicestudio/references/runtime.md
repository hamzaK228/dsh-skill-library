# Runtime and connection notes

Pinned application: `78c27c50497c7191286ffb222ee41a56a2d09c1a` from https://github.com/debpalash/VoiceStudio.

Linux x64 supports CPU and NVIDIA CUDA; the current Linux guide also documents optional AMD ROCm support. Source setup uses Python >=3.11, Bun 1.4.2, Node.js >=22.12.0, Rust/Cargo and native development libraries, Electron, PyTorch/torchaudio/torchvision, transformers, WhisperX, and other sizable dependencies. Run the checkout's `node electron/scripts/node-version.mjs` check before requested source setup. Python/model downloads are separate from this skill. Exact installed size depends on accelerator/engines; no measured total is asserted. CPU setup avoids CUDA wheels, but still requires substantial storage. Default model alone is about 2.3 GB. Individual model terms differ from the app's AGPL license.

Prefer an existing application. If source installation is requested, inspect the selected checkout's `package.json`, `pyproject.toml`, `scripts/setup-api.mjs`, and `electron/README.md` before execution. `bun run dev` has a `predev` hook that installs dependencies and launches Electron/backend. `OMNIVOICE_TORCH_VARIANT=cpu bun run setup:api` explicitly selects CPU wheels on supported Linux. Never execute the README's remote curl-to-shell installer without inspecting a pinned copy.

A metadata-only verification can check package names/versions and native skill availability without executing application code. A service smoke test can check health/OpenAPI on an already requested local runtime without generating speech or downloading weights. End-to-end generation remains unverified until an installed model produces decodable audio.

MCP path arguments require an explicitly configured `OMNIVOICE_MCP_BASE_PATH`; relative paths resolve against it and resolved inputs must remain inside it. Current backends accept both `/mcp` and `/mcp/`; keep the trailing slash for older-version compatibility.

Native MCP is mounted on the backend at `http://127.0.0.1:3900/mcp/`. Inspect `docs/mcp.md` in the selected checkout before connecting. The desktop Integrations screen exports client configurations. Keep any existing connection and authentication. Registering MCP is a separate configuration change; do it only when requested and useful with an available runtime.

Pinned guides:
- https://github.com/debpalash/VoiceStudio/blob/78c27c50497c7191286ffb222ee41a56a2d09c1a/electron/README.md
- https://github.com/debpalash/VoiceStudio/blob/78c27c50497c7191286ffb222ee41a56a2d09c1a/docs/mcp.md
- https://github.com/debpalash/VoiceStudio/blob/78c27c50497c7191286ffb222ee41a56a2d09c1a/docs/install/linux.md
