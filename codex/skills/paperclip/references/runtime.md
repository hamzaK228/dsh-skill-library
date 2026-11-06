# Setup and connection

The upstream ships native Claude/OpenAI plugin packages in `integrations/assistant-plugins/{claude,openai}/paperclip/`. They expose three workflows and a remote MCP connection. Their checked-in localhost URL is a development endpoint, not a connected public service. This adapter installs the workflows as references without activating an unconfigured connector.

Resolve a user-selected existing Paperclip instance first. Native MCP requires an authenticated instance, real person/company membership, administrator-enabled experimental `enablePublicMcp`, and human OAuth consent. Read [public-mcp.md](public-mcp.md) and [native plugin instructions](native-plugins.md) for the exact server requirements. Do not alter account access or enable experimental server features just as an installation check. Never use agent API keys or copied browser cookies to substitute for user OAuth.

If the user requests a local application, use Node >=24.11 and pnpm 9.15.4. Choose a directory explicitly; preserve any existing checkout and database. The native runner additionally requires Rust or an actual compatible `PAPERCLIP_RUNNER_BINARY`.

```bash
git clone https://github.com/paperclipai/paperclip.git /path/to/paperclip
git -C /path/to/paperclip checkout --detach f8cb4957dcd9f46c67f12e0feac0ba7cd1528a42
cd /path/to/paperclip
pnpm install --frozen-lockfile
pnpm dev
```

Installation runs package lifecycle scripts. Review them before executing. Startup creates persistent application configuration and embedded PostgreSQL state; do it only for a requested local run. Check the current loopback bind configuration before starting. The default local UI/API is port 3100. Avoid `npx paperclipai@latest onboard --yes` as an automatic smoke check: it configures and starts application state.

A skill-file/hash check only proves installation. A live connection must verify the authenticated person and company with real available tools. Delegation, autonomous execution, provider costs and completion of agent work need their own requested scenario and budget.
