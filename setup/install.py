#!/usr/bin/env python3
"""Install the portable Codex snapshot without overwriting existing files."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MARKER = '@@SETUP_HOME@@'


def relocate(data, home):
    try:
        return data.decode('utf-8').replace(MARKER, str(home)).encode('utf-8')
    except UnicodeDecodeError:
        return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home', type=Path, default=Path.home(), help='Destination user home (also used for path relocation)')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--verify', action='store_true', help='Check installed files without changing anything')
    args = parser.parse_args()
    home = args.home.expanduser().absolute()
    target = home / '.codex'
    manifest = json.loads((ROOT / 'setup/manifest.json').read_text())
    planned = []
    errors = []
    for name, expected in manifest['files'].items():
        rel = Path(name)
        if rel.is_absolute() or '..' in rel.parts or rel.parts[0] != 'codex':
            raise ValueError('Unsafe manifest path')
        source = ROOT / rel
        data = source.read_bytes()
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError(f'Snapshot hash mismatch: {name}')
        destination = target.joinpath(*rel.parts[1:])
        data = relocate(data, home)
        planned.append((destination, data, source.stat().st_mode & 0o777))
    policy = relocate((ROOT / 'setup/AGENTS.template.md').read_bytes(), home)
    planned.append((target / 'AGENTS.md', policy, 0o644))
    for path, data, _ in planned:
        # Refuse symlinked destinations and parents, even for dry run.
        if any(p.is_symlink() for p in [path, *path.parents]):
            errors.append(f'Symlink destination refused: {path}')
        elif path.exists() and (not path.is_file() or path.read_bytes() != data):
            errors.append(f'Existing file differs, preserved: {path}')
        elif args.verify and not path.exists():
            errors.append(f'Missing: {path}')
    if errors:
        print('\n'.join(errors[:20]), file=sys.stderr)
        print(f'{len(errors)} conflicts/missing files; nothing written.', file=sys.stderr)
        return 1
    missing = [(p,d,m) for p,d,m in planned if not p.exists()]
    if not args.dry_run and not args.verify:
        for path, data, mode in missing:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open('xb') as output:
                output.write(data)
            path.chmod(mode)
    print(json.dumps({'skills':manifest['skills'], 'agency_profiles':manifest['agency_profiles'],
                      'files':len(planned), 'new_files':len(missing),
                      'mode':'verify' if args.verify else 'dry-run' if args.dry_run else 'install'}))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
