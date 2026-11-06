# Runtime

Package: `graphifyy` (executable `graphify`), not the unrelated `graphify` package.

```bash
uv tool install graphifyy==0.9.103
graphify --help
graphify extract /path/to/code --code-only --no-cluster
```

The code-only smoke test uses local AST parsing and writes graphify-out under the chosen path. Use a temporary fixture for verification. Do not run `graphify install` as routine setup: it can also alter instructions/hooks. Copy this skill with the selective library installer instead. Semantic extraction, hosted services, model calls and database uploads require the current task's authorization and credentials.
