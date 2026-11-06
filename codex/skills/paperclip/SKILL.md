---
name: paperclip
description: Explicitly requested Paperclip AI team setup, delegation, team review and result follow-up using an authenticated Paperclip connection or local application.
disable-model-invocation: true
---

# Paperclip

This portable adapter packages the official Paperclip assistant workflows as references. It does not create a company, run agents, start a database, grant access or connect an MCP server by loading.

1. Discover whether actual Paperclip tools are available and authenticated. If absent, report **Paperclip connection unavailable** and read [runtime.md](references/runtime.md) for requested setup. Never invent tools or treat installation as a working connection.
2. Choose the requested official workflow: [delegate work](references/delegate-work.md), [review my team](references/review-my-team.md), or [follow up results](references/follow-up-results.md). Use only tools actually exposed to this assistant.
3. Read-only review can inspect existing tasks. Creating tasks, starting agents, changing budgets/access or sending team messages requires matching user authorization; installation alone authorizes none of those actions. Delegation can consume separately configured model/provider budgets.
4. Preserve task IDs and idempotency IDs across retries. Report returned submitted/running/blocked/completed states precisely. Never claim submitted work is completed.

See SOURCE-NOTICE.md for fixed upstream provenance and LICENSE. Keep tokens, cookies and account credentials out of this skill.
