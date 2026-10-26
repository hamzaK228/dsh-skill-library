# DSH Skill Library

A single-folder library of **91 agent skills** for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness),
plus the routing policy that keeps them cheap to use.

The point of this repo is not just to collect skills — it is to make them **selectable
without burning context**. Read [How to use this library](#how-to-use-this-library) first.

## Layout

```
.
├── AGENTS.md              # always-on routing policy (copy to ~/.dsh/AGENTS.md)
├── CATALOG.md             # generated index: one row per skill
├── skills/                # 91 skill directories, each with SKILL.md
│   ├── skill-router/      # the "main" skill: resolves overlaps, caps loading
│   ├── ...
├── tools/
│   ├── build-catalog.mjs  # regenerates CATALOG.md from frontmatter
│   └── sync-skills        # imports new skills from other agent folders
└── NOTICE.md              # provenance and licensing
```

A skill is a directory containing `SKILL.md` with YAML frontmatter:

```yaml
---
name: my-skill
description: What it does and when to use it. This is the only part loaded every turn.
---
```

## Install

Clone anywhere, then point DSH at `skills/`:

```bash
git clone git@github.com:hamzaK228/dsh-skill-library.git ~/skill-library
ln -s ~/skill-library/skills ~/.dsh/skills
```

Or copy instead of symlinking, if you prefer a frozen snapshot:

```bash
rsync -a --delete ~/skill-library/skills/ ~/.dsh/skills/
```

If you keep your own `~/.dsh/skills`, add this repo as an extra root instead, via the
profile patch (`~/.dsh/profiles/web/cordis.patch.yml`):

```yaml
- id: skill-filesystem
  name: '@deepseek-ai/dsh-skill-filesystem'
  disabled: false
  config:
    customSkillDirs:
      - /home/you/skill-library/skills
```

Also copy `AGENTS.md` to `~/.dsh/AGENTS.md` — that is what makes the routing work.

## How to use this library

Every installed skill contributes its **name and description to every request**,
whether or not it is used. Loading a skill body adds its whole `SKILL.md` for that
turn. So cost has two parts:

| Cost | Source | Control |
|---|---|---|
| Fixed | 91 descriptions ≈ **4.2k tokens per turn** | keep the catalog lean |
| Variable | skill bodies, 1–5k tokens each | load at most two per task |

Rules, enforced through `AGENTS.md` and the `skill-router` skill:

1. **Decide from the catalog, not by loading.** The description is the summary; a
   skill that matches will say so.
2. **At most two per task** — one primary, one support that covers a different axis
   (e.g. `semgrep` for detection + `sarif-parsing` for triage).
3. **No browsing.** Never load a skill "to see what's inside".
4. **One aesthetic system per project.** `design-taste-frontend` and
   `build-awwwards-quality-sites` are alternatives, not a stack.
5. **If a skill is loaded, follow it** — don't sample its siblings.

### First match wins

| Task | Load |
|---|---|
| New UI, landing page | `design-taste-frontend` |
| Cinematic / motion-led site | `build-awwwards-quality-sites` (not the above) |
| Critique or polish existing UI | `impeccable` |
| Component feel, spacing, states | `emil-design-eng` |
| Palettes, fonts, charts, style research | `ui-ux-pro-max` |
| shadcn components | `shadcn` |
| Design tokens / brand system | `design-system` |
| React/CSS motion, springs, gestures | `motion` |
| Vanilla timelines, SVG, scroll | `anime` |
| Rendered video | `remotion-best-practices` → one `remotion-*` |
| Ad/film-grade motion | `vizavi-motion` |
| Security scan of code | `semgrep` or `codeql` (+ `sarif-parsing`) |
| Live traffic, ports, MITM history | `yakit-yak` |
| Test-first feature | `tdd` |
| Hard bug / regression | `diagnosing-bugs` |
| Pre-merge review | `code-review` or `ponytail-review` |
| Over-engineering, "simplest fix" | `ponytail` |
| Codebase architecture questions | `graphify` |

`skill-router` holds the full matrix, including the "do not also load" column.

## Adding a skill

1. Create `skills/<name>/SKILL.md` with `name` and `description` in frontmatter.
2. Check the name is unique — directory names collide silently.
3. Confirm it doesn't duplicate an existing job; if it does, improve the existing one.
4. Regenerate the index: `node tools/build-catalog.mjs`.
5. Commit.

If a skill was installed elsewhere (`npx skills add …` writes to `~/.claude/skills`),
mirror it in with `tools/sync-skills`, which never overwrites and skips anything in
`~/.dsh/syncignore`.

## Pruning

A healthy size here is roughly 60–80 skills. Remove a skill when:

- two skills share a job — keep the better one;
- it targets a stack you don't use;
- it is platform-locked and cannot function here;
- its frontmatter is invalid, so it costs nothing but never loads.

Measure before and after:

```bash
node -e 'const fs=require("fs"),p=require("path");let t=0,n=0;for(const d of fs.readdirSync("skills")){const f=p.join("skills",d,"SKILL.md");if(!fs.existsSync(f))continue;const m=fs.readFileSync(f,"utf8").match(/^---\n([\s\S]*?)\n---/);const de=(m&&m[1].match(/^description:\s*(.*)$/m)||[])[1]||"";t+=de.length;n++}console.log(n+" skills, ~"+Math.round(t/4)+" tokens/turn")'
```


## Project presets

Skills are global, but each project needs a different subset. `tools/newproj`
writes a project-local `AGENTS.md` that names the must-have skills for that kind
of work; DSH loads it automatically when the project is opened, and its
instructions are more specific than the global policy.

```bash
tools/newproj webapp  ~/code/my-saas
tools/newproj landing ~/code/campaign
tools/newproj motion  ~/code/launch-film
tools/newproj api     ~/code/service
tools/newproj audit   ~/code/legacy-app
tools/newproj redesign ~/code/dashboard
```

| Preset | Must-have skills |
|---|---|
| `webapp` | senior-fullstack, vercel-react-best-practices, tdd, shadcn, motion, design-taste-frontend |
| `landing` | design-taste-frontend *(or build-awwwards-quality-sites)*, impeccable, motion |
| `motion` | vizavi-motion, remotion-best-practices, motion, anime |
| `api` | senior-fullstack, tdd, semgrep, codeql, sarif-parsing |
| `audit` | ponytail-audit, semgrep, codeql, sarif-parsing, testing-api-security-with-owasp-top-10, yakit-yak |
| `redesign` | impeccable, design-md, design-taste-frontend, break-ui |

Commit the generated `AGENTS.md`: it documents the project's skill contract for
every agent and every teammate, and it is what makes selection automatic instead
of a per-session decision.

## Model choice

Default stays `deepseek-flash` at low reasoning effort — cheapest per turn and
strong enough for routing, edits, and most frontend work. Switch to
`deepseek-v4-pro` for architecture decisions, security audits, cross-layer
refactors, and debugging that survives two failed attempts; raise reasoning effort
at the same time.

## License and provenance

Skills come from many upstream authors under their own licenses — see
[NOTICE.md](NOTICE.md). Each skill keeps its upstream terms; this repo adds only the
routing policy, catalog tooling, and consolidation.
