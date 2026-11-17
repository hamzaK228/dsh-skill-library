# OpenWhispr runtime

## CLI and backend selection

The upstream CLI is `openwhispr` (`@openwhispr/cli`, Node 20+). Desktop development has separate Node requirements; installing this skill installs neither runtime.

Backend precedence is explicit `--local`/`--remote`, `OPENWHISPR_BACKEND`, CLI configuration, then auto detection. Local access uses the running desktop's loopback bridge. Remote access uses the cloud API and a scoped key. Local is authoritative during or immediately after recording; cloud synchronization may lag. Do not read credential files into chat.

Useful read commands, with IDs obtained from results:

```sh
openwhispr notes list --limit 20 --format json
openwhispr notes search "meeting" --limit 20 --format json
openwhispr notes get <id> --format json
openwhispr folders list --format json
openwhispr transcriptions list --limit 20 --format json
openwhispr transcriptions get <id> --format text
```

Pass the selected backend flag explicitly when source matters. Successful list/search CLI output is a bare array; REST lists have an envelope. `notes create` and `notes update` return JSON without a `--format` option; inspect their help before use. The CLI does not expose SRT/VTT export. Audio deletion is local-only; the cloud API does not store audio.

Exit codes: 1 invalid input or unsupported operation; 2 unreachable backend; 3 authentication/scope failure; 4 missing resource. Fix the cause rather than repeatedly retrying authentication. `doctor` probes both backends and exits successfully when at least one works, so inspect each backend's result.

## REST and MCP

REST base: `https://api.openwhispr.com/api/v1`; authenticate with a securely supplied Bearer key. Read routes include `GET /notes/list`, `GET /notes/{id}`, `GET /folders/list`, `GET /transcriptions/list`, `GET /transcriptions/{id}`. Search uses `POST /notes/search` with `query` and optional `limit`.

Personal keys access private content. Workspace keys access team spaces: discover with `GET /spaces/list`, then provide `space_id` for note/folder list, create, or search. Personal-key requests reject `space_id`. Workspace keys currently cannot use transcription endpoints, even with the workspace transcription scope. Do not infer workspace support from CLI personal workflows.

Lists return `data`, `has_more`, and opaque `next_cursor`; pass the cursor back unchanged and stop at the task's result/page budget. Honor `Retry-After` on 429. Use the resource's current `revision` as `base_revision` for `PATCH /notes/{id}`; with that field, content edits require `field_updates` (`set` or `clear`). On 409 `note_version_conflict`, compare returned current data and rebase; do not blindly resend stale text. The API cannot change a note's space.

Official remote MCP endpoint: `https://mcp.openwhispr.com/mcp`, Streamable HTTP with Bearer authentication. Discover actual connected tool schemas before use. A URL in this file does not create a connection or authorize configuration changes.

Pinned authoritative references are linked in [SOURCE-NOTICE.md](../SOURCE-NOTICE.md). Verify installed command help when its version differs.
