# Cap runtime and workflows

These commands describe the pinned CLI contract; inspect `cap guide --json` and installed help before use. Use `--json` for structured stdout; stderr is diagnostic. Exit 1 indicates runtime failure; exit 2 indicates invalid usage.

## Library reads

```sh
cap auth status --json
cap caps list --json
cap caps get <id-or-url> --json
cap caps context <id-or-url> --json
cap caps wait <id-or-url> --for transcript --json
```

`auth status` verifies the credential with the server. `get` provides lightweight metadata/capabilities; `context` gathers richer transcript, chapter, comment, and processing context. Wait only observes processing already underway. Downloading media is a separate operation: use it only when the requested workflow needs an authorized local copy. For large transcripts, `cap caps transcript <id-or-url> --format text --output transcript.txt --json` writes to a chosen task output path.

When `PASSWORD_REQUIRED` is returned, let the user run `cap caps unlock <id-or-url>` in a secure terminal. Do not put the password into chat, command arguments, or MCP parameters. Respect scope failures rather than changing login privileges. Provider authentication/checkout URLs are user handoffs; do not mistake an opened URL for completed authorization.

## Local capture and export

Readiness checks: `cap doctor --json` and `cap targets --json`. For an authorized recording of unknown duration, the documented lifecycle is:

```sh
cap record start --screen <id> --detach --json
cap record stop --id <recordingId> --json
cap project validate <path.cap> --json
cap export <path.cap> --output out.mp4 --json
```

Obtain screen and recording IDs from actual results. `recordingMetaExists` must be true after stopping before reporting the recording complete. The desktop/OS must support capture and grant required permissions; a guide command alone proves neither. Upload is a separate `cap upload <file> --json` action and changes data exposure.

Instant Mode uploads during recording; Studio Mode records locally and opens editing. Choose based on the user's output/privacy requirements before capture. A local export is not an uploaded share link. For durable server operations, follow the returned operation with `cap jobs wait <operationId> --json`; acceptance is not completion. Read state again after mutations, and pass CLI confirmation flags only when the action is authorized.

## Runtime boundaries

`cap mcp serve` is the CLI's local stdio MCP server; stdout must remain protocol-only. It does not become available simply by installing this skill. Do not run `cap agents install` or edit Codex/Claude configuration without authorization. Secure-input and local-file actions may require CLI even when MCP is connected.

Cap's native desktop application, web/API services, media service, database, and storage are separate runtimes. The pinned repository uses Rust/GPUI for desktop and Next.js/Drizzle/MySQL for web. Self-hosting and connecting S3 storage are independent tasks. Current source locations are `apps/desktop-gpui`, `apps/web`, `apps/cli`, `apps/media-server`, and `crates/*`; consult actual checkout versions rather than assuming the older desktop architecture.
