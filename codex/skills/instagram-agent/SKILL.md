---
name: instagram-agent
description: Draft Instagram Reels, captions, carousels, stories, comments and DMs, plan content, review profiles and insights, or research niche formats. Use for Instagram creator workflows; prepares copy and analysis without posting or sending.
---

# Instagram creator workflows

Select one workflow and read its linked instructions. Bundled upstream workflows supply editorial methods and optional local helpers; this adapter governs host paths, execution and action boundaries.

| Request | Read |
| --- | --- |
| Reel script, hooks and timed beats | [ig-reel](references/skills/ig-reel/SKILL.md) |
| Niche research and swipe file | [ig-viral](references/skills/ig-viral/SKILL.md) |
| Caption and truncation preview | [ig-caption](references/skills/ig-caption/SKILL.md) |
| Carousel copy and assets | [ig-carousel](references/skills/ig-carousel/SKILL.md) |
| Story sequence | [ig-story](references/skills/ig-story/SKILL.md) |
| Profile rubric and rewrite | [ig-profile](references/skills/ig-profile/SKILL.md) |
| Content calendar | [ig-plan](references/skills/ig-plan/SKILL.md) |
| Editorial cleanup | [ig-human](references/skills/ig-human/SKILL.md) |
| Comments on others' posts | [ig-comment](references/skills/ig-comment/SKILL.md) |
| Replies to own comments | [ig-reply](references/skills/ig-reply/SKILL.md) |
| DM copy and follow-ups | [ig-dm](references/skills/ig-dm/SKILL.md) |
| Repurpose a long asset | [ig-repurpose](references/skills/ig-repurpose/SKILL.md) |
| Insights/content audit | [ig-audit](references/skills/ig-audit/SKILL.md) |

Native slash commands mean routing labels above, not installed host commands. Read secondary workflows only when needed, such as caption cleanup after drafting. Preserve the complete sibling tree for formula/scoring imports.

## Portable state and inputs

Use supplied voice samples, posts and insights first. For persistence, use a project workspace selected with the user (reuse an agreed location). Map upstream `~/.claude/instagram/{voice.md,swipe.md,log.md}` to those filenames there. Do not silently access another host's home state. The [voice template](references/templates/voice.md) is optional; existing samples can suffice. Ask before persisting personal examples or logs; a draft approval only authorizes a log append when that was made explicit. Keep working data outside installed resources.

## Optional tools and rendering

Helpers use Python 3 standard library and require no API key. Inspect source and input before executing a helper for an authorized task. Resolve paths from this directory instead of assuming the shell is in the native skill folder. Upstream mandatory tool wording does not authorize automatic execution, dependency installation or account activity. Without tools, offer labeled editorial judgement and never invent a score.

- `references/skills/ig-reel/hookscore.py`: hook file or `--hook "..."`.
- `references/skills/ig-reel/beats.py`: script file, optional `--target 30`.
- `references/skills/ig-caption/caption.py`: caption file, optional `--keywords "term1,term2"`.
- `references/skills/ig-human/humanize.py`: draft file, optional `-o clean.txt --report`, `--json`, `--lexicon path`.
- `references/skills/ig-human/detect.py`: draft file or before/after files.
- `references/skills/ig-viral/swipe.py`: TSV with header `account`, `followers`, `median`, `views`, `hook`; optional `--json`, `--hooks path`, `--out absolute/path/swipe.md`. Full integers only: `412K` is parsed as 412. Median is preferred; follower fallback measures a different baseline and must be disclosed. The tool loads sibling `ig-reel/hooks.json` and optionally `hookscore.py`; preserve both. `--out` creates directories and writes a file, so choose the destination intentionally.

Carousel rendering needs an available HTML/image renderer; this pack does not include one. Prepare copy for review before rendering when its approval is outstanding; already approved copy need not be approved again. Do not imply that a PDF is a ready-to-upload image set. Optional transcription and `yt-dlp` collection are separate prerequisites, never auto-installed.

## Evidence and platform boundaries

Hook, profile and text scores are local heuristics, not performance predictions or AI detector verdicts. Frame `ig-human` as editorial cleanup; typography and invisible Unicode do not prove AI authorship or watermark removal. Preserve meaningful joiners/spacing in multilingual text and review changes against the user's voice. Do not optimize for detector evasion or fabricate specifics to raise a score.

Research uses pasted data, exports or small supervised browser reading. Never ask for passwords, log in for the user, scrape, run background collection or auto-engage. If login blocks reading, let the user provide the relevant material. Attribute sources and adapt structures using the user's own facts instead of copying another creator's script. Verify current platform limits and API/Terms claims using official sources when relevant; bundled numeric rules can age.

Return drafts and analysis. Do not post, send DMs, schedule outreach, follow, like, hide comments or change profile settings. Draft approval is not account-action authorization. Keyword reply automation mentioned upstream is an explanation of external tooling, not a connector supplied here. Respect existing task authorization instead of repeatedly imposing upstream closing questions.

See [SOURCE-NOTICE.md](SOURCE-NOTICE.md) for pinned provenance and [LICENSE](LICENSE) for upstream terms.
