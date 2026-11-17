# Runtime

Reviewed upstream commit `450592c3e9142573751abef61eb344eab73c69f6`, 2026-11-09.

- Repository: https://github.com/samuelgursky/davinci-resolve-mcp
- Setup guide: https://github.com/samuelgursky/davinci-resolve-mcp/blob/450592c3e9142573751abef61eb344eab73c69f6/docs/install.md
- Live compound entrypoint: `<checkout>/src/server.py` under the server's Python environment, Python 3.10+. Prefer its managed environment; Python 3.10–3.12 has broader compatibility with older Resolve builds.
- Granular mode: `src/server.py --full`; avoid switching merely to expose hundreds of tools.
- Optional offline entrypoint: `node <checkout>/bin/davinci-resolve-advanced-mcp.mjs`. Discover `capabilities` for optional dependencies. Offline project reads/writes still need actual input files and relevant write authorization.

For Studio, Resolve must be running with external scripting configured locally. Upstream describes a free-edition in-app bridge through 21.0.x; its README says free 21.1 stopped exposing Python scripts in the menu. Do not assume the bridge works on every free build. Verify exact build and current docs before setup. Do not change scripting from Local to Network without a user-requested remote connection.

Upstream's `npx davinci-resolve-mcp setup` or `python install.py` installs dependencies and can register multiple assistant configurations. Neither is a read-only diagnostic. Inspect its options and existing configs, back up affected settings, and limit registration to the requested client. This skill installation runs neither installer.

The source checkout's `scripts/doctor.py --json` is documented as a read-only environment diagnostic. Inspect the local script before execution; it is not bundled here. Extra transcription/embedding features may need optional packages/model downloads. Check before analysis, and preserve scope for media-derived artifacts.
