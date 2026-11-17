# Repository integrations for Codex and Claude Code

Added 6 November 2026, expanded and refreshed 9 November 2026. These 15 portable instruction integrations support **Codex and Claude Code**. CLI/application runtimes are separate from skill files. Existing DSH source skills remain unchanged.

| Skill | Upstream revision | Runtime | Invocation |
|---|---|---|---|
| `graphify` | Graphify-Labs/graphify `16218bfc80d4ca2799734d045039f7ed1a5fa9fb` | graphifyy 0.9.103 | Existing routing retained |
| `agent-reach` | Panniantong/Agent-Reach `47898829204ad27521d8a1719e3aeca3b8a3e0ca` | Agent-Reach 1.6.1 | Relevant public-content fallback |
| `mirofish` | 666ghj/MiroFish `7657031ac01184afe2cb220f5ee3545573b5e843` | Separate Python/Vue application | Explicit invocation only |
| `paperclip` | paperclipai/paperclip `f8cb4957dcd9f46c67f12e0feac0ba7cd1528a42` | Authenticated application/MCP | Explicit invocation only |
| `voicestudio` | debpalash/voicestudio `78c27c50497c7191286ffb222ee41a56a2d09c1a` | Separate local speech application | Explicit invocation only, retained |
| `open-seo` | every-app/open-seo `46b815be34723e46ceeefe9b2b907bb62b62fd76` | Hosted Open SEO account/MCP | Explicit invocation only, retained |
| `motionclone` | [Official agent guide](https://motionclone.lol/agents), reviewed 2026-11-09; linked repository returned 404 | Windows/Codex reconstruction; either assistant can edit exports | Task-specific discovery |
| `davinci-resolve-mcp` | samuelgursky/davinci-resolve-mcp `450592c3e9142573751abef61eb344eab73c69f6` | Resolve + separate live/offline MCP server | Task-specific discovery |
| `openmontage` | OpenMontageInc/OpenMontage `fecb9a1e3cc23ef84de30b272059457a427f16f8` | Separate pipeline application | Task-specific discovery |
| `youtube-agent` | Jakeschincariol/youtube-agent-skill `a2feb2104981a375ffd4f87ee04f4f5344ac43c6` | 11 bundled editorial workflows; six optional stdlib helpers | Task-specific discovery |
| `instagram-agent` | Jakeschincariol/instagram-agent-skill `d03c56bb598be770c60b201f94237e5d1a4268a6` | 13 bundled editorial workflows; six optional stdlib helpers | Task-specific discovery |
| `open-higgsfield-ai` | Autom8AI/Open-Higgsfield-AI `297151c245e35696e1519d66c40d09011167bb2d` | Separate studio/provider account; actual client differs from README | Task-specific discovery |
| `openwhispr` | OpenWhispr/openwhispr `e74d1b0bc947088944d7cbd5afb159aa0977694d` | Separate desktop dictation app/models | Task-specific discovery |
| `chatwoot` | chatwoot/chatwoot `d262508b6b6f7386d05f1470a7e840141c3e561b` | User-selected support instance/API | Task-specific discovery |
| `cap` | capsoftware/cap `a42f8f44f61c02b50302d755c41a7b739947a3e7` | Separate screen recorder/cloud or self-hosted service | Task-specific discovery |

MiroFish does not supply an upstream skill/plugin/MCP server at this revision. Its local adapter explains how to set up and operate the real application; it cannot simulate without the application and configured providers.

## Install integrations

From this library checkout:

```bash
python3 setup/install-repo-skills.py --dry-run
python3 setup/install-repo-skills.py
python3 setup/install-repo-skills.py --verify

# Or install only selected skills (both assistants by default):
python3 setup/install-repo-skills.py --skill youtube-agent --skill instagram-agent
```

Default target is both assistants. Use `--target codex` or `--target claude` for one, or `--home /path/to/home` for staging. Existing identical files are skipped. Different files cause a preflight refusal before writing. For an intentional update, use `--replace`: every differing file is backed up first under `~/.local/share/repo-skill-backups/<UTC timestamp>/`. Extra existing files are preserved. Hashes in `setup/manifest.json` verify the source files.

This selective installer copies only selected skill folders; it does not change global instructions, model settings, permissions, hooks, services, credentials or Claude Code's executable. Open a new chat/restart the assistant to discover new skills. In Claude Code invoke `/SKILL-NAME`; in Codex invoke `$SKILL-NAME`, using the exact names in the table. Internal `yt-*` and `ig-*` names route through the two root packs, not 24 separately installed slash commands.

The full `setup/install.py` continues to install the complete Codex snapshot, including all 15 integrations. It does not install Claude Code skills; use the selective installer above for those.

## Install runtimes separately

```bash
uv tool install graphifyy==0.9.103
uv tool install 'git+https://github.com/Panniantong/Agent-Reach.git@47898829204ad27521d8a1719e3aeca3b8a3e0ca'
```

The PyPI package named `agent-reach` is unrelated; use the pinned Git source. Existing uv tool installs can require an explicit update; preserve unrelated tools.

Graphify code-only operation is local: `graphify extract /path/to/code --code-only --no-cluster`. Semantic extraction and hosted/database operations have additional dependencies and authorization requirements.

Agent-Reach `version`, `channels`, and `doctor` inspect the installation; `doctor` does not prove live access. Platform tools may require separate setup or user login. The adapter prefers connected tools where available. Bulk `agent-reach setup` is not run automatically because it can install channels, migrate old files and replace skills; channel setup is requested individually.

For MiroFish follow [runtime instructions](../codex/skills/mirofish/references/runtime.md). Python 3.11/3.12 and Node 22.12+ are supported by the pinned dependency constraints. Default checkout: `~/.local/share/mirofish`, overridable with `MIROFISH_HOME`. LLM and Zep API keys must be configured locally before backend startup; simulations can incur provider costs and upload scenario data. No credentials belong in this library.

## Verification on the installation machine (6 November baseline)

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

## Expansion and verification, 9 November 2026

Nine new adapters were added and VoiceStudio/Open SEO were refreshed. The eleven requested integrations were installed into both `~/.codex/skills/` and `~/.claude/skills/`; selective `--verify` returned zero differences. Changed existing files were backed up under `~/.local/share/repo-skill-backups/20261109T112016835314Z` on the installation machine. No global instructions, models, agent configs, hooks or MCP registration changed.

- All nine new root skills passed `quick_validate.py`. The two existing manual-only skills preserve `disable-model-invocation` plus their existing policy metadata; the current generic validator does not accept that legacy frontmatter field. Temporary validation omitting only that field passed; installed files retain it.
- All nine portable/selective installer tests passed, including fresh/idempotent operation, no-write conflict refusal, backed-up replacement, symlink/parent-file rejection, missing source and selected-skill/target isolation.
- All 12 bundled YouTube/Instagram Python helpers were exercised with synthetic local fixtures. Full upstream text trees, sibling imports, source hashes and MIT notices were preserved. Scores are heuristics; research tools, renderers and account connections remain separate.
- An independent read-only review found no actionable adapter/installer issues. A final pinned-tree check corrected the Resolve analysis-guide path before installation.
- No new application runtime, providers, media upload, capture, render, account mutation or publication was exercised. File installation and static checks do not certify those workflows.

Important availability notes: [MotionClone](https://motionclone.lol/agents) documents a Windows/Codex reconstruction app and exported HyperFrames editing; its linked GitHub repository returned 404 during review. Claude can edit an export, but native Claude reconstruction is not documented. Open Higgsfield AI's pinned README describes Muapi while the actual imported client uses KIE; inspect implementation before selecting credentials, models or prices. OpenWhispr, Chatwoot and Cap adapters use real documented CLI/API contracts but require separately configured runtimes/access. OpenMontage keeps its internal pipeline/provider skills project-scoped instead of adding its entire catalog globally.

This update is local to the library checkout; no commit, push or GitHub publication was performed.
