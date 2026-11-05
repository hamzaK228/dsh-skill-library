#!/usr/bin/env python3
"""Start the observer in the foreground using this user's approved scopes."""
import json
import os
from pathlib import Path
import shutil

home = Path.home()
config = json.loads((home / '.config/pixel-agents-codex/config.json').read_text())
node = shutil.which('node')
if not node:
    raise SystemExit('Node.js required; install it before starting Pixel Agents')
app = home / '.local/share/pixel-agents'
entry = app / 'dist/codex-observer.cjs'
if not entry.is_file():
    raise SystemExit('Build first: cd ~/.local/share/pixel-agents && bash build-observer.sh')
os.environ['PIXEL_CODEX_TOKEN_FILE'] = config['token_file']
os.environ['PIXEL_CODEX_SCOPES'] = json.dumps(config['scopes'])
os.chdir(app)
os.execv(node, [node, str(entry)])
