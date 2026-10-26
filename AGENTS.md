# Working agreements

## Skills: load deliberately, never routinely

The catalog already carries every skill's summary. Read those summaries and decide
from them. Load a skill body only when the task genuinely matches, **at most two per
task** (one primary, one support). Never load a skill to see what is inside it, and
never load a second skill that restates the first.

Routing defaults (first match wins):

- New UI, landing page, marketing site → `design-taste-frontend`.
  Cinematic, high-concept, or motion-led brief → `build-awwwards-quality-sites` **instead**.
- Critique or polish existing UI → `impeccable`; component-level feel and spacing → `emil-design-eng`.
- Palettes, fonts, chart types, style research → `ui-ux-pro-max`.
- shadcn components, registries, presets → `shadcn`.
- Motion: React/CSS animation, springs, gestures → `motion`; vanilla timelines/SVG/scroll → `anime`;
  rendered video → `remotion-best-practices`; ad/film-grade motion → `vizavi-motion`.
- Security review of code → `semgrep` or `codeql`; interpreting results → `sarif-parsing`;
  web/API/JWT/XSS testing → the matching `testing-*` skill; live traffic and ports → `yakit-yak`.
- Writing code → `vercel-react-best-practices` for React/Next performance; `tdd` for test-first;
  `diagnosing-bugs` for failures; `code-review` before merge.
- Research against primary sources → `research`.

One aesthetic system per project. Once a skill is loaded, follow it rather than
sampling its siblings.

## Catalog hygiene

Before adding a skill, check whether an existing one already does the job. Prefer one
skill per job, unique names (installs overwrite by directory name), and valid
frontmatter. Remove dead or duplicated skills — every entry costs tokens on every turn.

## One skill folder

Every skill lives in `~/.dsh/skills` and that is the only root DSH scans. When
`npx skills add` installs somewhere else, run `~/.dsh/bin/sync-skills` to mirror
the new directories in. A skill that is not in that folder does not exist here.

The main skill is `skill-router`: load it when a task could match several skills,
and follow its tables instead of loading candidates to compare them.
