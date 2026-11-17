# Chatwoot application API

Use the actual instance origin. Application API conversation paths are under `/api/v1/accounts/{account_id}/conversations`; IDs are account-scoped. Platform provisioning APIs and public website-inbox APIs have different credentials and purposes; do not substitute one for another.

## Authentication and discovery

User tokens come from Profile Settings. The pinned API documents Bearer authentication from v4.19.0 onward; `api_access_token` remains supported but is marked for future deprecation. For an older instance, inspect its matching docs rather than assuming Bearer support. Agent-bot tokens only work on bot-permitted endpoints, and platform-app tokens are for provisioning, not unrestricted conversation reads. Keep tokens out of generated files, logs, and command arguments.

Read conversations with `GET /api/v1/accounts/{account_id}/conversations`. Supported filters include `status`, `assignee_type`, `inbox_id`, `team_id`, `labels`, and `q`; `page` starts at 1. Default status is `open`, so request an explicit status when completeness matters. Bound the page count and report partial coverage.

Read messages with `GET /api/v1/accounts/{account_id}/conversations/{conversation_id}/messages`. The response has `meta` and a message `payload` array. `after=<message_id>` returns up to 100 messages in ascending order; `before=<message_id>` returns up to 20 in ascending order. These parameters are message IDs, not timestamps. Advance from returned IDs, stop on no progress, and do not claim full history after one page.

## Draft and authorized send

Message creation uses `POST` to that same messages path. Text requests are JSON with required `content`; `message_type` is `outgoing` or `incoming`, and `private` controls private-note visibility. Set `private` explicitly: `true` for an internal note, `false` for a customer reply. Do not synthesize an incoming customer message to send an agent reply.

For attachments use multipart form data and `attachments[]`; let the HTTP library create the boundary. WhatsApp templates must be approved in WhatsApp Business Manager; use the actual channel and template metadata rather than generating a purported approval. Record the created message ID and observed status. Inspect available status/error information before claiming delivery; uncertain POST outcomes require a read-back check before retrying to avoid duplicates.

Self-hosting is a separate deployment task with a server/database/worker runtime, not part of skill installation. Enterprise features are separately licensed. Source paths and exact schema links are in [SOURCE-NOTICE.md](../SOURCE-NOTICE.md).
