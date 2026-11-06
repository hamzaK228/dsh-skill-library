# Repository integrations for Codex and Claude Code

Added 6 November 2026. These are portable instruction skills for **Codex and Claude Code**. CLI/application runtimes are separate from skill files. Existing DSH source skills remain unchanged.

| Skill | Upstream revision | Runtime | Invocation |
|---|---|---|---|
| `graphify` | Graphify-Labs/graphify `16218bfc80d4ca2799734d045039f7ed1a5fa9fb` | graphifyy 0.9.103 | Existing routing retained |
| `agent-reach` | Panniantong/Agent-Reach `47898829204ad27521d8a1719e3aeca3b8a3e0ca` | Agent-Reach 1.6.1 | Relevant public-content fallback |
| `mirofish` | 666ghj/MiroFish `7657031ac01184afe2cb220f5ee3545573b5e843` | Separate Python/Vue application | Explicit invocation only |
| `paperclip` | paperclipai/paperclip `f8cb4957dcd9f46c67f12e0feac0ba7cd1528a42` | Authenticated application/MCP | Explicit invocation only |
| `voicestudio` | debpalash/voicestudio `c88bf7006e65266eb1692bec977e2e88c3062486` | Separate local speech application | Explicit invocation only |
| `open-seo` | every-app/open-seo `0749caf15796888dd9034cd52e8d344e2b44e09f` | Hosted Open SEO account/MCP | Explicit invocation only |

MiroFish does not supply an upstream skill/plugin/MCP server at this revision. Its local adapter explains how to set up and operate the real application; it cannot simulate without the application and configured providers.

## Install these six skills

From this library checkout:

```bash
python3 setup/install-repo-skills.py --dry-run
python3 setup/install-repo-skills.py
python3 setup/install-repo-skills.py --verify
```

Default target is both assistants. Use `--target codex` or `--target claude` for one, or `--home /path/to/home` for staging. Existing identical files are skipped. Different files cause a preflight refusal before writing. For an intentional update, use `--replace`: every differing file is backed up first under `~/.local/share/repo-skill-backups/<UTC timestamp>/`. Extra existing files are preserved. Hashes in `setup/manifest.json` verify the source files.

This selective installer copies only the six skill folders; it does not change global instructions, model settings, permissions, hooks, services, credentials or Claude Code's executable. Open a new chat/restart the assistant to load new skills. In Claude Code invoke `/graphify`, `/agent-reach`, `/mirofish`, `/paperclip`, `/voicestudio`, `/open-seo`; in Codex invoke `$graphify`, `$agent-reach`, `$mirofish`, `$paperclip`, `$voicestudio`, `$open-seo`.

The full `setup/install.py` continues to install the complete Codex snapshot, including these six skills. It does not install Claude Code skills; use the selective installer above for those.

## Install runtimes separately

```bash
uv tool install graphifyy==0.9.103
uv tool install 'git+https://github.com/Panniantong/Agent-Reach.git@47898829204ad27521d8a1719e3aeca3b8a3e0ca'
```

The PyPI package named `agent-reach` is unrelated; use the pinned Git source. Existing uv tool installs can require an explicit update; preserve unrelated tools.

Graphify code-only operation is local: `graphify extract /path/to/code --code-only --no-cluster`. Semantic extraction and hosted/database operations have additional dependencies and authorization requirements.

Agent-Reach `version`, `channels`, and `doctor` inspect the installation; `doctor` does not prove live access. Platform tools may require separate setup or user login. The adapter prefers connected tools where available. Bulk `agent-reach setup` is not run automatically because it can install channels, migrate old files and replace skills; channel setup is requested individually.

For MiroFish follow [runtime instructions](../codex/skills/mirofish/references/runtime.md). Python 3.11/3.12 and Node 22.12+ are supported by the pinned dependency constraints. Default checkout: `~/.local/share/mirofish`, overridable with `MIROFISH_HOME`. LLM and Zep API keys must be configured locally before backend startup; simulations can incur provider costs and upload scenario data. No credentials belong in this library.

## Verification on the installation machine

- Selective skill installation and byte comparison passed for all six skills in both assistant directories.
- Installer tests cover fresh/idempotent installs, conflict refusal with no writes, backed-up replacement, symlink refusal, and absent source files. The original portable installer tests also pass.
- Graphify 0.9.103 created a code-only fixture graph containing 3 nodes and 3 edges without model calls.
- Agent-Reach 1.6.1 read the public Graphify GitHub repository successfully (`ok: true`, one result). Other platforms are not certified by this check.
- MiroFish source checkout and frontend dependency installation/production build passed. The optional frozen backend dependency download was stopped before completion because the skill installation does not require a fully configured application. Its cache is preserved; backend runtime readiness is not claimed. No provider calls or simulations are part of installation verification.

Upstream runtime dependencies are not security-certified. The pinned MiroFish root npm lockfile reports two critical root audit entries in the concurrently/shell-quote dependency chain ([GHSA-pqg4-j6r4-53mv](https://github.com/advisories/GHSA-pqg4-j6r4-53mv)); The frontend separately reports 12 high and 1 moderate audit entries; no automatic dependency changes were made. The documented startup uses separate processes rather than the root concurrently command.

License/provenance notices accompany each skill. Graphify retains Apache-2.0, MIT and NOTICE texts; Agent-Reach retains MIT; MiroFish includes its AGPL-3.0 notice and license, with application source available at the pinned upstream revision.

## Additional application and service requirements

- **Paperclip:** adapter includes the three official assistant workflows. A usable connection requires an authenticated instance, administrator-enabled experimental public MCP and human OAuth consent. Native plugin files point at a localhost development endpoint. Installing the workflow adapter does not start teams or agents. No Paperclip runtime, database or MCP account connection was started by this installation.
- **VoiceStudio:** native skill adapted for both assistants. Separate application installation and a loaded voice engine are required for generation. Its local MCP endpoint is `http://127.0.0.1:3900/mcp/`. No speech models were downloaded and no voice was cloned/generated during skill installation.
- **Open SEO:** scoped adapter retains native workflow references. Upstream's full Claude plugin is under `plugins/openseo`; its connector is `https://app.openseo.so/mcp`. OAuth/account configuration and DataForSEO credentials/credits are separate. No hosted connector was registered, no site was changed and no paid SEO operation was run.

These adapters are the installed skills, not evidence that their external application/service is configured. Their manual-only policies prevent automatic application operations from skill discovery.

To resume the optional MiroFish backend dependency setup on the installation machine:

```bash
uv sync --frozen --project ~/.local/share/mirofish/backend --python 3.12
```

The pinned backend includes large Torch/CUDA dependencies even before provider configuration. Skill installation is complete independently of this optional runtime setup.
