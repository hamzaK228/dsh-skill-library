"""Reproducible installer checks; never use the user's actual home."""
import importlib.util
import json
from pathlib import Path
import stat
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('installer', Path(__file__).with_name('install.py'))
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def test_preserve_hooks_token_and_idempotent_update(self):
        with tempfile.TemporaryDirectory() as directory:
            home = Path(directory)
            scope = home / 'projects'
            scope.mkdir()
            hooks = home / '.codex/hooks.json'
            hooks.parent.mkdir()
            existing = {'hooks': {'Stop': [{'hooks': [{'type': 'command', 'command': 'existing'}]}]}, 'custom': True}
            hooks.write_text(json.dumps(existing))
            installer.install(home, [scope], True)
            token = home / '.config/pixel-agents-codex/token'
            first = token.read_text()
            self.assertEqual(stat.S_IMODE(token.stat().st_mode), 0o600)
            installer.install(home, [scope], True, True)
            saved = json.loads(hooks.read_text())
            self.assertTrue(saved['custom'])
            self.assertEqual(saved['hooks']['Stop'][0], existing['hooks']['Stop'][0])
            self.assertEqual(len(saved['hooks']['Stop']), 2)
            self.assertEqual(token.read_text(), first)
            self.assertTrue(list(hooks.parent.glob('hooks.json.pixel-backup-*')))

    def test_symlink_destinations_fail_before_mutation(self):
        for suffix in ('.local/share/pixel-agents', '.local/share/pixel-agents-codex',
                       '.config/pixel-agents-codex/token', '.codex/hooks.json'):
            with self.subTest(suffix=suffix), tempfile.TemporaryDirectory() as directory:
                home = Path(directory) / 'home'
                home.mkdir()
                scope = home / 'projects'
                scope.mkdir()
                external = Path(directory) / 'untouched'
                external.write_text('private')
                destination = home / suffix
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.symlink_to(external)
                with self.assertRaisesRegex(ValueError, 'symlink'):
                    installer.install(home, [scope], True, True)
                self.assertEqual(external.read_text(), 'private')
                self.assertFalse((home / '.local/share/pixel-agents/package.json').exists())


if __name__ == '__main__':
    unittest.main()
