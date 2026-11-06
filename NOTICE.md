# Provenance and licensing

This repository consolidates skills authored by many different people. **Each skill
remains under its upstream license.** Nothing here relicenses third-party work; the
original copyright and terms travel with each `SKILL.md`.

## Sources

| Origin | Notes |
|---|---|
| [skills.sh](https://skills.sh) registry | Installed with `npx skills add`, including `anthropics/skills`, `vercel-labs/agent-skills`, `mattpocock/skills`, `emilkowalski/skill`, `nextlevelbuilder/ui-ux-pro-max-skill`, `pbakaus/impeccable`, `remotion-dev/skills`, `shadcn-ui/ui`, `heygen-com/hyperframes`, `trailofbits/skills`, `github/spec-kit` |
| [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | Curated subset of a much larger collection |
| [MengTo/Skills](https://github.com/MengTo/Skills) | `build-awwwards-quality-sites`, MIT |
| [dietrichgebert/ponytail](https://github.com/dietrichgebert/ponytail) | `ponytail*` family |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | `graphify` skill; CLI installed separately |
| Local / authored here | `skill-router`, `yakit-yak`, `vizavi-motion` (user-supplied) |

## Caveats

- Several skills are **thin wrappers around external tooling** (`semgrep`, `codeql`,
  `graphify`, `yakit`). The skill text is included; the binaries are not.
- Some skills reference platform features of other agents (Claude Code hooks, slash
  commands). Those parts do not execute under DeepSeek Harness.
- License coverage has not been exhaustively audited. Several upstreams are MIT,
  but not all terms were verified individually. Preserved notices and source links
  do not grant rights missing from an upstream; check the relevant terms before
  further redistribution or commercial use. Proprietary plugin bodies are excluded.

## Attribution

If you republish or redistribute, preserve each skill's original `SKILL.md` header and
link back to its upstream repository. Corrections and removals: open an issue.

## Portable Codex snapshot (2026-11-05)

`codex/skills/` preserves the user's local adaptations and supporting resources;
`setup/manifest.json` hashes this distribution after replacing the original home
with a relocation marker. Historical upstream hashes and commits remain provenance
for the original artifacts; they are not hashes of relocated installs. Existing
manual-only invocation restrictions are preserved. Local `SOURCE-NOTICE.md` and
license files remain authoritative; absence of a license is not a new grant.

Agency profiles and references derive from `msitarzewski/agency-agents`; MIT notice
is retained at `codex/skills/agency-team/references/LICENSE`, with pinned sources
and role provenance beside it. Pixel Agents source and local modifications are
packaged separately with upstream MIT notice and `pixel-agents/PROVENANCE.md`.

Plugin caches, proprietary/system skill bodies, credentials and remote service
implementations are not redistributed. `setup/plugins.json` records only public
package metadata and installation requirements. Each recipient installs plugins
through their own Codex distribution and connects their own accounts.

## Repository integrations (2026-11-06)

The six portable assistant integrations are documented in `docs/REPO-INTEGRATIONS.md`. Their `SOURCE-NOTICE.md` files pin the actual upstream revisions and distinguish local adapters from copied workflow references. Original licenses and attribution remain with copied material; runtime applications, credentials, model weights and connected accounts are not included in this repository. VoiceStudio and MiroFish retain their upstream AGPL notices; no relicensing is implied.
