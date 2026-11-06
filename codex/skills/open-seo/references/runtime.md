# Native plugin, connection, and runtime

Pinned repository: https://github.com/every-app/open-seo/tree/0749caf15796888dd9034cd52e8d344e2b44e09f.

The root `.claude-plugin/marketplace.json` advertises marketplace `openseo`, with plugin `openseo` sourced from `./plugins/openseo`. Its `.claude-plugin/plugin.json` declares version 1.0.25, MIT, twelve workflow skills. Its `.mcp.json` declares HTTP server `openseo` at `https://app.openseo.so/mcp`. The hosted connection requires user OAuth/account authorization; installation alone is not a connected account or free SEO data. This adapter intentionally does not register a hosted server or add twelve separate catalog entries. If the user requests the official plugin instead, inspect the pinned manifests and current client's supported plugin commands before installing; avoid duplicate workflow registrations.

A self-hosted instance exposes `/mcp` on its own URL. Source development requires Node.js 20+ and pnpm 10.30.1 (from `packageManager`), install with a frozen lockfile, then run the local D1 migration and dev scripts per `docs/LOCAL_DEVELOPMENT.md`. Source setup includes native/bundled tool dependencies and may download substantial packages; exact size was not measured. Do not run scripts containing `deploy`, remote database migration, or provider usage as setup checks.

Current recommended Docker self-hosting uses `deploy/standalone/compose.yaml`, with a prebuilt `ghcr.io/every-app/open-seo-standalone` image, at least 4 GiB Docker memory, persistent state, and a unique storage secret. The first visitor creates the admin account. Inspect the compose port bindings and keep services on loopback for local use. The root `compose.yaml` is an older single-container setup with `local_noauth`; do not mistake it for the current authenticated standalone instructions.

SEO data requires a DataForSEO account/key. Optional OpenRouter and Maps/Google integrations have separate credentials and potential charges. No credentials, accounts, billable calls, images, or public deployment are installed by this skill.

Pinned setup instructions:
- https://github.com/every-app/open-seo/blob/0749caf15796888dd9034cd52e8d344e2b44e09f/docs/LOCAL_DEVELOPMENT.md
- https://github.com/every-app/open-seo/blob/0749caf15796888dd9034cd52e8d344e2b44e09f/docs/SELF_HOSTING_DOCKER.md

Verify skill metadata without running the app. A requested existing connection can be checked with tool discovery and permitted project listing. This does not establish provider-backed research readiness.
