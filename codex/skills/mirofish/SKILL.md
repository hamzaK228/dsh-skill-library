---
name: mirofish
description: Explicit-only local MiroFish setup, operation, and simulation guidance. Use when the user invokes mirofish; requires a separate application runtime and provider credentials.
disable-model-invocation: true
---

# MiroFish

This is a Codex/Claude Code instruction adapter for the MiroFish web application, not an upstream plugin or an embedded simulator.

1. Resolve the runtime checkout from `MIROFISH_HOME` when set, otherwise `~/.local/share/mirofish`. Verify `backend/pyproject.toml`, `backend/run.py`, and `frontend/package.json` exist. If absent, report **MiroFish runtime unavailable**; the skill alone cannot run simulations.
2. For requested installation, startup, or diagnosis, read [runtime.md](references/runtime.md). Inspect the selected checkout and its pinned version before executing it. Install dependencies or fetch source only when that work is requested; do not install or start services merely by loading this skill.
3. Use the application's browser workflow or inspect its actual API routes before making requests. Never invent a `mirofish` CLI or MCP server; this upstream version supplies neither.
4. Before a simulation, establish the user's scenario, seed files, provider authorization, and round/agent budget. Upload only the specified materials to the authorized services. Do not create accounts, spend provider credits, upload documents, or run simulations as an installation smoke check.
5. Treat outputs as scenario simulations, not validated predictions. Report which checks ran and distinguish local application health from successful provider calls and completed simulations.

Keep credentials in local environment configuration, never in skill files or logs. Preserve existing configuration and invocation restrictions. See [source notice](SOURCE-NOTICE.md) for provenance and the upstream license.
