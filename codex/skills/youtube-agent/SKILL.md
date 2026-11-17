---
name: youtube-agent
description: Draft YouTube scripts, titles and thumbnail briefs, Shorts, descriptions, chapters and comment replies, or analyze channel plans, transcript edits and audience retention. Use for YouTube creator work; outputs are drafts and analysis.
---

# YouTube creator workflows

Choose the relevant workflow below and read only its linked instructions. These bundled upstream workflows provide editorial methods and optional local tools; this adapter governs host paths, execution and action boundaries.

| Request | Read |
| --- | --- |
| Script or opening hooks | [yt-script](references/skills/yt-script/SKILL.md) |
| Titles, thumbnail copy, packaging or CTR | [yt-package](references/skills/yt-package/SKILL.md) |
| Transcript edit decisions | [yt-edit](references/skills/yt-edit/SKILL.md) |
| Comment reply drafts | [yt-comment](references/skills/yt-comment/SKILL.md) |
| Content calendar | [yt-plan](references/skills/yt-plan/SKILL.md) |
| Public niche research and outlier ranking | [yt-viral](references/skills/yt-viral/SKILL.md) |
| Audience retention export | [yt-retention](references/skills/yt-retention/SKILL.md) |
| Shorts from existing footage/transcript | [yt-shorts](references/skills/yt-shorts/SKILL.md) |
| Description, tags and search queries | [yt-seo](references/skills/yt-seo/SKILL.md) |
| Timestamped chapters | [yt-chapters](references/skills/yt-chapters/SKILL.md) |
| Channel audit | [yt-audit](references/skills/yt-audit/SKILL.md) |

Resolve native slash commands as routing labels in this table, not installed host commands. Resolve sibling references relative to the selected upstream folder; keep the complete tree together.

## Portable state and inputs

Use supplied voice samples and analytics first. When persistent state is needed, use a project workspace selected with the user (reuse an already agreed location); map upstream `~/.claude/youtube/voice.md` to `voice.md` there. Do not silently read or write another host's home directory. Start from the [voice template](references/templates/voice.md) if useful, and disclose inferred voice choices. Do not require three videos when existing samples suffice. Keep private analytics and transcripts out of the installed skill tree.

## Optional tools

Bundled Python helpers use the standard library. Before executing a helper for an authorized task, inspect its source and its inputs; use `python3` with the path resolved from this skill directory, never assume the shell starts inside a native folder. Upstream commands are examples, not an instruction to execute every tool. Do not install dependencies or run collection tools automatically. If Python or an input is unavailable, provide a clearly labeled editorial assessment without claiming a computed score.

- `references/skills/yt-script/hookscore.py`: hook text file or `--hook "..."`.
- `references/skills/yt-package/title.py`: `--title "..." --thumb "..."` or title file.
- `references/skills/yt-edit/deadair.py`: timestamped SRT, VTT or Whisper JSON; `--floor 0.35 --json`. Produces proposed cuts, does not edit media.
- `references/skills/yt-chapters/chapters.py`: transcript file, optional `--target 8`; retitle generated topic words yourself. Needs sibling `yt-edit/deadair.py`.
- `references/skills/yt-retention/retention.py`: CSV with at least eight numeric position/retention rows, optional `--duration 600 --transcript transcript.srt --json`. It infers percent when maximum position is <=100.5, which can misread seconds for short videos; establish axis units before trusting output. Transcript matching needs sibling `yt-edit`.
- `references/skills/yt-viral/swipe.py`: JSON array (or object with `videos`) of `{channel,title,views,url,duration}`, optional `--min 2.0 --json`; fewer than four videos/channel are skipped. Needs sibling hook formulas.

Public listings, pasted data or a user's export are valid research inputs. Optional `yt-dlp` and transcription tools are separate prerequisites, not bundled or installed here. Never use credentials or a logged-in session for automated collection.

## Evidence and handoff

Keep facts, estimated runtimes and heuristic scores distinct. Hook scores do not predict success; title formula classification describes words, not causes. Retention thresholds are editorial heuristics, not universal diagnoses. Verify current platform limits against official sources when they matter. Never invent metrics, outcomes, sources or transcript timestamps.

Return reviewable copy or analysis. Draft approval does not authorize uploading, posting replies, changing metadata, pinning, hearting or modifying the channel. This pack has no publishing integration. Honor the user's requested scope and existing authorization instead of treating the upstream closing question as a new mandatory approval ritual.

See [SOURCE-NOTICE.md](SOURCE-NOTICE.md) for pinned provenance and [LICENSE](LICENSE) for upstream terms.
