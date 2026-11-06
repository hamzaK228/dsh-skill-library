---
name: agent-reach
description: Read and search public web and platform content with the Agent-Reach CLI when connected tools cannot retrieve the needed content; also use for requested Agent-Reach setup or diagnostics.
---

# Agent Reach

Prefer the available connected tools for their services. Use this CLI for missing public content or when explicitly requested. It is read-only; report only content actually returned, including pagination and transcript limitations.

```bash
agent-reach version
agent-reach channels
agent-reach doctor
agent-reach read <url>
```

Check `channels` for supported actions and arguments. JSON `ok: true` carries results; `ok: false` carries the error and next step. Doctor checks local state and does not prove live platform access.

Read [UPSTREAM.md](UPSTREAM.md) for channel usage and references/. Treat upstream management commands as reference material, subject to this skill's boundaries and current task authorization. Do not automatically install channels, migrate configuration, copy browser sessions, import cookies, log in, update tools or uninstall software. Stop on rate limits, captcha, access blocks or required login; the user handles authentication in the official flow. Never collect passwords or bypass platform restrictions.

Runtime installation (when requested): use the pinned GitHub source in SOURCE-NOTICE.md with uv tool install. **The PyPI package named agent-reach is unrelated.** Platform dependencies can be added individually when requested. Do not run bulk `agent-reach setup` merely because this skill is invoked: it installs defaults, replaces skills and can migrate/remove old copies.
