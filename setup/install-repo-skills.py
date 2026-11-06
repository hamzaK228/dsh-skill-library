#!/usr/bin/env python3
"""Install the six repository integrations for Codex and/or Claude Code."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('graphify', 'agent-reach', 'mirofish', 'paperclip', 'voicestudio', 'open-seo')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--home', type=Path, default=Path.home())
    p.add_argument('--target', choices=('codex', 'claude', 'both'), default='both')
    p.add_argument('--dry-run', action='store_true')
    p.add_argument('--verify', action='store_true')
    p.add_argument('--replace', action='store_true', help='Back up each differing file before replacing it')
    args = p.parse_args()
    home = args.home.expanduser().absolute()
    targets = ('codex', 'claude') if args.target == 'both' else (args.target,)
    manifest = json.loads((ROOT / 'setup/manifest.json').read_text())['files']
    planned, errors = [], []
    for target in targets:
        for name in SKILLS:
            source_root = ROOT / 'codex/skills' / name
            prefix = f'codex/skills/{name}/'
            expected_paths = sorted(key for key in manifest if key.startswith(prefix))
            if prefix + 'SKILL.md' not in expected_paths:
                raise ValueError(f'Missing skill in manifest: {name}')
            for key in expected_paths:
                rel = Path(key)
                if rel.is_absolute() or '..' in rel.parts:
                    raise ValueError(f'Unsafe source path: {key}')
                src = ROOT / rel
                if any(x.is_symlink() for x in (src, *src.parents)):
                    raise ValueError(f'Source symlink refused: {src}')
                data = src.read_bytes()
                if hashlib.sha256(data).hexdigest() != manifest[src.relative_to(ROOT).as_posix()]:
                    raise ValueError(f'Source hash mismatch: {src}')
                dest = home / f'.{target}/skills' / name / src.relative_to(source_root)
                if any(x.is_symlink() for x in (dest, *dest.parents)):
                    errors.append(f'Symlink refused: {dest}')
                    continue
                if any(x.exists() and not x.is_dir() for x in dest.parents):
                    errors.append(f'Parent is not a directory: {dest}')
                    continue
                if dest.exists() and not dest.is_file():
                    errors.append(f'Not a file: {dest}')
                    continue
                different = dest.exists() and dest.read_bytes() != data
                if args.verify and (different or not dest.exists()):
                    errors.append(f'Missing or different: {dest}')
                elif different and not args.replace:
                    errors.append(f'Conflict preserved: {dest}; use --replace for a backed-up update')
                elif different or not dest.exists():
                    planned.append((dest, data, different))
    if errors:
        raise ValueError('\n'.join(errors[:15]) + '\nNothing written.')
    backup = home / '.local/share/repo-skill-backups' / datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    if any(x[2] for x in planned):
        for parent in (backup, *backup.parents):
            if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
                raise ValueError(f'Unsafe backup directory: {parent}; nothing written.')
    if not args.verify and not args.dry_run:
        # Back up all existing files before writing any skill file.
        for dest, _, different in planned:
            if different:
                saved = backup / dest.relative_to(home)
                saved.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(dest, saved)
        for dest, data, _ in planned:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
    print(json.dumps({'targets': targets, 'skills': list(SKILLS), 'changed_files': len(planned),
                      'mode': 'verify' if args.verify else 'dry-run' if args.dry_run else 'install',
                      'backup': str(backup) if any(x[2] for x in planned) and not args.dry_run and not args.verify else None}))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError) as e:
        raise SystemExit(str(e))
