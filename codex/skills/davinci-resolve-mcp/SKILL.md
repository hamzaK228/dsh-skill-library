---
name: davinci-resolve-mcp
description: Operate DaVinci Resolve through its MCP servers for editing, grading, Fusion, Fairlight, media organization and delivery, or inspect offline Resolve project files.
---

# DaVinci Resolve MCP

This adapter guides a separately installed Resolve MCP connection. For setup or missing connection, read [runtime notes](references/runtime.md). Discover the actual connected tools and schemas; the live Python and offline Node servers have different capabilities.

1. Read the active project/timeline and exact Resolve build before modifying anything. With the compound server, use `resolve_control` version/support/API-truth actions exposed by its schema. A version gate without evidence means unknown; probe rather than promise.
2. Choose the relevant [domain reference](references/domains.md). Prefer the compact compound server for ordinary work. Live Python operates a running Resolve; advanced Node operates project files and does not drive the application.
3. Inspect the target and prepare a recoverable project/timeline/grade copy before edits with meaningful loss risk. Keep source footage untouched unless the task specifically calls for source-media changes. Offline database writes require the target project closed and the application's lifecycle requirements checked.
4. Before grades/LUT/CDL/DRX changes, inspect Resolve-rendered frames and preserve a recoverable grade version. Use the server's validation and confirmation gates for edits, imports, render settings and overwrite operations; inspect refusals instead of bypassing them.
5. Read back the changed state. Compound returns can include `_operation.status`, verification, changes, warnings and execution ID. `partial`, `blocked`, `failed`, `unverified` or contradiction must remain visible in the report; a missing changes block does not prove no changes occurred.
6. For delivery, inspect available codecs/settings, choose a distinct output path, monitor the queued job, probe the completed file and inspect representative frames/audio. A queued job is not a completed render.

Do not run setup, register MCP servers, install plugins or launch paid analysis merely because the skill is selected. Existing task authorization determines which operations to perform. [Provenance](SOURCE-NOTICE.md).
