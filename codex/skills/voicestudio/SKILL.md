---
name: voicestudio
description: Explicit-only VoiceStudio speech generation, transcription, cloning, dubbing, and local API or MCP setup. Requires the separate VoiceStudio application and installed models.
disable-model-invocation: true
---

# VoiceStudio

A portable Codex/Claude Code adapter for the upstream application and its native skill; this folder contains instructions, not a speech engine.

- Resolve an existing source checkout from `VOICESTUDIO_HOME`, otherwise `~/.local/share/voicestudio`. An installed desktop application or user-configured backend is also supported. Honor the user's backend URL; default `http://127.0.0.1:3900`.
- For audio work, read [the native workflow](references/upstream-skill.md). Its setup/startup suggestions apply only when the user requested runtime setup or startup. Loading this skill never starts a service or installs a model.
- Check `GET /health`, then discover the actual contract at `GET /openapi.json` and voices at `GET /v1/audio/voices`. Use the existing HTTP MCP connection at `/mcp/` if configured; otherwise REST works without editing global MCP settings. Treat 401/403 as missing authorization.
- Before generation, confirm the engine/model is installed. First generation can automatically download about 2.3 GB; do not use generation as a credential-free installation check. Obtain the user's model choice/download authorization and check available disk/RAM first. Clone only authorized reference voices.
- Keep audio on disk rather than returning base64 to the model. For MCP, `OMNIVOICE_MCP_OUTPUT_MODE=files` and an explicitly selected `OMNIVOICE_MCP_BASE_PATH` are backend settings; the directory must be shared with the client. Preserve existing settings and profiles.
- Verify generated media with a decoder/probe and report output path, duration, actual engine, and limitations. A successful health request does not prove speech generation or microphone access.

For requested installation or diagnosis, read [runtime notes](references/runtime.md). Provider connections, model downloads, microphone recording, and external uploads follow the user's authorized task. Provenance and license: [SOURCE-NOTICE.md](SOURCE-NOTICE.md).
