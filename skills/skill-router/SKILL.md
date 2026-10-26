---
name: skill-router
description: "Pick the right installed skill for a task with minimal token cost: resolve overlapping design, motion, security and coding skills, cap loading at two, and keep the catalog lean as new skills are added. Use when several skills could apply, when unsure which skill to load, when the user asks which skill to use, or when adding/removing skills."
---

# Skill router

## Cost model

Every installed skill contributes its name and description to **every request**,
whether or not it is used. Loading a body adds the whole SKILL.md for that turn only.

So:

- Choosing well is about *not* loading, more than about loading fast.
- A 100-skill catalog costs roughly 5k tokens per turn; 45 skills cost roughly 2.5k.
- Two loaded skills that say the same thing cost double for half the value.

## Layout

All skills live in one folder: `~/.dsh/skills`. `~/.claude/skills` and
`~/.zcode/skills` are install sources only; run `~/.dsh/bin/sync-skills` after an
install to copy new directories in. Edit or delete a skill only in that one folder.

## Default posture

Engineering work runs at `senior-fullstack` standard even when that skill is not
loaded: whole path first, proof instead of claims, smallest correct change. Load the
body only when the change crosses layers and the step sequence is worth the tokens.

## Selection procedure

1. Match the task against catalog descriptions only. Do not load a skill to inspect it.
2. Choose **one primary** skill. Add **one support** skill only if it covers a distinct
   axis (e.g. `semgrep` for detection + `sarif-parsing` for triage).
3. If no description matches, do the work directly. Skills are not a checklist.
4. If a skill is already loaded this session, follow it; never load a sibling to compare.

## Resolution matrix

Use this when two or more candidates overlap.

### Interface design

| Situation | Load | Do not also load |
|---|---|---|
| New site/landing page, normal ambition | `design-taste-frontend` | `build-awwwards-quality-sites`, `ui-ux-pro-max` |
| Cinematic / award-level / motion-led site | `build-awwwards-quality-sites` | `design-taste-frontend`, `impeccable` |
| Critique, audit, redesign an existing interface | `impeccable` | `design`, `design-system` |
| Small component feel: spacing, states, micro-detail | `emil-design-eng` | `impeccable` |
| Style research, palettes, font pairs, chart choice | `ui-ux-pro-max` | `design`, `brand` |
| shadcn components / registry / presets | `shadcn` | — |
| Design tokens or brand system from scratch | `design-system` | `design` |
| Logo, CIP, banners, social images | `design` (one artifact per load) | `design-system` when it is a deck |

### Motion

| Situation | Load | Notes |
|---|---|---|
| React/Next micro-interactions, gestures, page transitions | `motion` | Motion (ex-Framer Motion) |
| Vanilla timelines, SVG morphing, scroll, stagger, draggable | `anime` | Anime.js v4 |
| Rendered MP4 from React | `remotion-best-practices` first, then the specific `remotion-*` skill | one sub-skill at a time |
| Ad/film/kinetic-typography piece | `vizavi-motion` | html/css/svg first |
| Audit or improve existing animation code | `improve-animations` (audit) / `review-animations` (single diff) | read-only planners |
| Jank, dropped frames | `animation-performance` | — |
| "What is this effect called" | `animation-vocabulary` | — |

### Security

| Situation | Load |
|---|---|
| Static review of a codebase | `semgrep` (fast, free) or `codeql` (deep dataflow); `sarif-parsing` to triage |
| API surface review | `testing-api-security-with-owasp-top-10` |
| Authn/authz logic | `testing-for-broken-access-control`, `testing-jwt-token-security` |
| XSS / output encoding | `testing-for-xss-vulnerabilities` |
| Secrets in git or CI | `implementing-secret-scanning-with-gitleaks` |
| CI/CD hardening | `securing-github-actions-workflows`, `integrating-sast-into-github-actions-pipeline` |
| Live traffic, ports, fingerprints, captured flows | `yakit-yak` (Yak MCP tools) |
| Threat model with ATT&CK | `implementing-threat-modeling-with-mitre-attack` |

### Coding

| Situation | Load |
|---|---|
| Test-first feature or bug fix | `tdd` |
| Hard bug, regression, slow path | `diagnosing-bugs` |
| Pre-merge review | `code-review` |
| React/Next performance | `vercel-react-best-practices` |
| Module boundaries, seams, API shape | `codebase-design` |
| Naming and glossary | `domain-modeling` |
| Cross-layer change: db → server → client | `senior-fullstack` |
| PR description | `pr` |
| Over-engineered solution, simpler change, dead code | `ponytail` (lite/full/ultra); `ponytail-review` for a diff |
| "What does this codebase actually look like" / cross-file map | `graphify` (needs `graphify` CLI) |

## Adding a skill (do this every time)

1. Search the registry/catalog for an existing skill that already covers the job.
2. Install to `~/.claude/skills` (via `npx skills add ... -g -y --agent claude-code --copy`)
   or `~/.dsh/skills`.
3. Check for a **name collision** — same directory name silently overwrites. Rename the
   new one (e.g. `owner-skillname`) if the job differs.
4. Validate frontmatter: `name` and `description` present, no nested YAML mappings.
5. Add the skill to the matching table above, or state why it needs no row.
6. Delete anything this skill supersedes.

## Pruning

A healthy catalog for this setup is roughly 60–80 skills; the current set is 82 (~4.0k tokens/turn). Prune when:

- two skills share a job — keep the better one;
- a skill targets a stack the user does not use;
- a skill is platform-locked and cannot function here (e.g. Claude Code hooks);
- frontmatter is invalid, so it costs nothing but also never loads — remove the directory.

Measure before and after:

```bash
node -e 'const fs=require("fs"),p=require("path");let t=0,n=0;for(const r of [process.env.HOME+"/.claude/skills",process.env.HOME+"/.dsh/skills"]){if(!fs.existsSync(r))continue;for(const d of fs.readdirSync(r)){const f=p.join(r,d,"SKILL.md");if(!fs.existsSync(f))continue;const m=fs.readFileSync(f,"utf8").match(/^---\n([\s\S]*?)\n---/);const de=(m&&m[1].match(/^description:\s*(.*)$/m)||[])[1]||"";t+=de.length;n++}}console.log(n+" skills, ~"+Math.round(t/4)+" tokens/turn")'
```
