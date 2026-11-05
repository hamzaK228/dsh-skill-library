#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")"
node -e 'const [a,b]=process.versions.node.split(".").map(Number); if(a<22||(a===22&&b<12)) {console.error("Node >=22.12 required (Vite 8)");process.exit(1)}'
# Dependency install is deliberate, never triggered by the root setup installer.
# Ignore lifecycle scripts (including upstream Husky); esbuild distributes platform binaries.
if [[ ! -d node_modules ]]; then npm ci --ignore-scripts; fi
npm run build:webview
mkdir -p dist
node - <<'JS'
const fs = require('node:fs');
require('esbuild').buildSync({entryPoints:['server/src/codexObserverCli.ts'],bundle:true,
  platform:'node',target:'node22',format:'cjs',outfile:'dist/codex-observer.cjs'});
fs.cpSync('webview-ui/public/assets','dist/assets',{recursive:true});
JS
printf '%s\n' 'Observer built. Start manually with python3 ~/.local/share/pixel-agents-codex/start.py'
