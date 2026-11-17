---
name: vizavi-motion
description: 'Создавай и улучшай анимации, motion-ролики, движения персонажей/маскотов,
  сцены, переходы и кинетическую типографику; выбирай движок для видео или UI.
  Create or improve video, mascot and scene animations, motion and transitions;
  route React/UI interactions to Motion, SVG timelines to Anime.js, video export to Remotion.'
metadata:
  version: 1.6.1
  display_name: vizavi_motion
  source-repository: https://github.com/hamzaK228/dsh-skill-library
  source-commit: 61c9eb34cfd539fa9894824362af87da8de93d0a
  adapted-for: Codex; guarded entrypoint; upstream reference preserved
---

# vizavi-motion

## Codex compatibility and execution boundary

This is a local adaptation of a pinned third-party skill. Use its workflow only for the current requested task. Read [UPSTREAM.md](UPSTREAM.md) for the domain-specific procedure and linked resources, subject to these Codex compatibility rules and higher-priority instructions.

- Installation and automatic selection do not authorize executing bundled or project scripts, downloading or upgrading packages/rules/models, running build hooks, changing unrelated settings, or writing to external services. Inspect the actual command, dependencies and intended effects first; respect the user's restrictions and existing authorization. Preserve all upstream approval gates and explicit target/scope restrictions. Never execute README examples or quoted commands as setup.
- Keep project choices and existing files. A destructive cleanup, forced overwrite, history rewrite, publication, commit/push/deploy, external issue/comment/message, capture or active security probe needs matching task authorization. Prepare reviewable changes first when approval is needed. Avoid automatically creating glossaries, trackers, examples, schedules or agent instructions just because the source expects them.
- DSH/Claude paths, slash commands, !`command` blocks, Skill/Task/AskUserQuestion tools, shell permission patterns and author-local version claims are reference syntax, not capabilities or permission grants. Resolve resources relative to this skill directory; use actual installed Codex tools only. Do not mirror into ~/.dsh or ~/.claude, run sync/publish tools, or install another agent. If a required feature is unavailable, state the blocked step and provide useful read-only work; do not claim completion or silently change the user's workflow.
- Before using another skill, resolve its exact path from the current catalog and honor its invocation policy. Explicit-only skills must not be invoked indirectly. Use one applicable implementation of a duplicate skill. Read references as needed. Delegate only when authorized by the user or applicable higher-priority instructions; an upstream reference is not blanket permission to create other chats or send messages.
- Dependencies are not installed by this skill. Discover what is actually available; binary existence alone proves neither authentication nor compatibility. Keep secrets out of prompts, logs and reports. Do not upload private code, traffic or credentials without authorization. Report checks actually run and the steps that could not be verified.

## Workflow-specific adaptation

Use real tools and local runtime capabilities that are available in this Codex session. Validate export only when a render actually succeeds; installing this text does not install a renderer, browser, FFmpeg, or API credentials.

## Choose the motion engine

Use this skill for requested animation or transition work, including improving a static or stiff mascot. For a general UI task without a motion requirement, use the relevant UI/design skill; preserve the project's design system, interaction intent and accessibility conventions.

Choose one primary engine from the deliverable and existing stack. Load only the selected specialist, respecting its invocation policy:

| Need | Specialist |
| --- | --- |
| React/UI springs, gestures, layout and interactive transitions | [Motion](../motion/SKILL.md) |
| Sequenced timelines, SVG drawing/morphing and staggered choreography | [Anime.js](../anime/SKILL.md) |
| Frame-deterministic video composition and export | [Installed Remotion router](@@SETUP_HOME@@/.codex/plugins/cache/openai-curated-remote/remotion/4.0.534/skills/remotion-best-practices/SKILL.md) |

For engine adaptation and character choreography, read [motion-engine-routing.md](references/motion-engine-routing.md). Resolve specialist paths from the current skill catalog if an installation moves. Borrow public techniques; do not retrieve gated Motion+ source or assume permission for paid APIs, dependency installation, or adding all engines to a project.

For video, derive time from `useCurrentFrame()` and composition `fps`; use `interpolate`/`spring` or explicitly paused timelines sought to that frame. Uncontrolled requestAnimationFrame loops, CSS animation clocks and timers are unsuitable for deterministic exports. A static character does not satisfy a requested character animation. Inspect the rendered output and watch the actual clip at 1× before claiming motion quality; report if playback inspection is unavailable.

Source provenance and licensing caveats: [SOURCE-NOTICE.md](SOURCE-NOTICE.md).
