#!/usr/bin/env python3
"""Install the optional local observer; never start services or approve hooks."""
import argparse
import json
import os
from pathlib import Path
import secrets
import shlex
import shutil
import sys

EVENTS = ('SessionStart', 'SubagentStart', 'PreToolUse', 'PostToolUse',
          'PermissionRequest', 'UserPromptSubmit', 'SubagentStop', 'Stop', 'Interrupt', 'SessionEnd')


def reject_symlinks(path, recursive=False):
    # Refuse redirection before reading credentials, backing up hooks or copying.
    for part in (path, *path.parents):
        if part.is_symlink():
            raise ValueError('Refusing symlink installation destination: ' + str(part))
    if recursive and path.is_dir():
        for child in path.rglob('*'):
            if child.is_symlink():
                raise ValueError('Refusing symlink in installation destination: ' + str(child))


def install(home, scopes, install_hooks=False, update=False):
    home = home.absolute()
    reject_symlinks(home)
    home = home.resolve()
    scopes = [str(Path(s).resolve(strict=True)) for s in scopes]
    if not scopes or any(not Path(s).is_dir() for s in scopes):
        raise ValueError('Provide at least one existing project directory with --scope')
    source = Path(__file__).resolve().parent
    app = home / '.local/share/pixel-agents'
    bridge = home / '.local/share/pixel-agents-codex'
    config = home / '.config/pixel-agents-codex'
    for target in (app, bridge, config):
        reject_symlinks(target, recursive=True)
    reject_symlinks(home / '.codex/hooks.json')
    if not update and any(p.exists() for p in (app, bridge, config)):
        raise ValueError('Pixel Agents already exists; review it, then use --update to retain state/token and merge source')
    hooks_path = home / '.codex/hooks.json'
    hooks = json.loads(hooks_path.read_text()) if install_hooks and hooks_path.exists() else {}
    if not isinstance(hooks, dict) or not isinstance(hooks.get('hooks', {}), dict):
        raise ValueError('Existing hooks.json must contain an object named hooks')
    for entries in hooks.get('hooks', {}).values():
        if not isinstance(entries, list) or any(not isinstance(e, dict) or not isinstance(e.get('hooks', []), list) or any(not isinstance(h, dict) for h in e.get('hooks', [])) for e in entries):
            raise ValueError('Existing event hooks must contain arrays of hook objects')
    # Validate before any copy. No state, external assets or credentials are imported.
    shutil.copytree(source / 'source', app, dirs_exist_ok=update)
    shutil.copytree(source / 'bridge', bridge, dirs_exist_ok=update,
                    ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    config.mkdir(parents=True, exist_ok=True, mode=0o700)
    token = config / 'token'
    if not token.exists():
        with token.open('x') as output:
            os.chmod(token, 0o600)
            output.write(secrets.token_urlsafe(32) + '\n')
    settings = {'scopes': scopes, 'token_file': str(token)}
    (config / 'config.json').write_text(json.dumps(settings, indent=2) + '\n')
    os.chmod(config / 'config.json', 0o600)
    if install_hooks:
        command = shlex.join([sys.executable, str(bridge / 'forward.py')])
        groups = hooks.setdefault('hooks', {})
        for event in EVENTS:
            entries = groups.setdefault(event, [])
            if not isinstance(entries, list):
                raise ValueError('Existing event hooks must be arrays')
            if not any(any(h.get('command') == command for h in entry.get('hooks', [])) for entry in entries):
                entries.append({'hooks': [{'type': 'command', 'command': command, 'timeout': 2}]})
        hooks_path.parent.mkdir(parents=True, exist_ok=True)
        if hooks_path.exists():
            backup = hooks_path.with_name('hooks.json.pixel-backup-' + secrets.token_hex(4))
            shutil.copy2(hooks_path, backup)
        hooks_path.write_text(json.dumps(hooks, indent=2) + '\n')
        print('Hooks merged. Review and trust them through native Codex /hooks; restart chat if needed.')
    print('Installed source and bridge. No dependency installation, service startup or trust changes performed.')
    print('Build: cd ' + shlex.quote(str(app)) + ' && bash build-observer.sh')
    print('Start: ' + shlex.join([sys.executable, str(bridge / 'start.py')]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home', type=Path, default=Path.home(), help='target home (for staging/testing)')
    parser.add_argument('--scope', type=Path, action='append', required=True, help='existing project root; repeat as needed')
    parser.add_argument('--install-hooks', action='store_true', help='merge forwarding hooks; native trust still required')
    parser.add_argument('--update', action='store_true', help='merge source into existing install, retaining token and state')
    args = parser.parse_args()
    try:
        install(args.home, args.scope, args.install_hooks, args.update)
    except (ValueError, OSError, json.JSONDecodeError) as error:
        parser.exit(1, str(error) + '\n')

if __name__ == '__main__':
    main()
