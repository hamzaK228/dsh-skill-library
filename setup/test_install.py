import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name('install.py')


class InstallTests(unittest.TestCase):
    def run_install(self, home, *args):
        return subprocess.run([sys.executable, str(SCRIPT), '--home', str(home), *args], capture_output=True, text=True)

    def test_fresh_relocated_idempotent(self):
        with tempfile.TemporaryDirectory(prefix='setup home ') as d:
            home = Path(d)
            self.assertEqual(self.run_install(home, '--dry-run').returncode, 0)
            self.assertFalse((home / '.codex').exists())
            result = self.run_install(home)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(self.run_install(home, '--verify').returncode, 0)
            self.assertIn('"new_files": 0', self.run_install(home).stdout)
            self.assertNotIn('@@SETUP_HOME@@', (home / '.codex/AGENTS.md').read_text())
            agency = home / '.codex/skills/agency-team/scripts/install_profiles.py'
            checked = subprocess.run([sys.executable, str(agency), '--verify', '--target-dir',
                                      str(home / '.codex/agents')], capture_output=True, text=True)
            self.assertEqual(checked.returncode, 0, checked.stderr)
            profiles = list((home / '.codex/agents').glob('*.toml'))
            self.assertEqual(len(profiles), 283)

    def test_conflict_writes_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            home = Path(d)
            dest = home / '.codex'
            dest.mkdir()
            (dest / 'AGENTS.md').write_text('My instructions')
            self.assertNotEqual(self.run_install(home).returncode, 0)
            self.assertEqual(list(dest.iterdir()), [dest / 'AGENTS.md'])
            self.assertEqual((dest / 'AGENTS.md').read_text(), 'My instructions')

    def test_symlink_refused(self):
        with tempfile.TemporaryDirectory() as d:
            home = Path(d)
            other = home / 'other'
            other.mkdir()
            (home / '.codex').symlink_to(other, target_is_directory=True)
            self.assertNotEqual(self.run_install(home).returncode, 0)
            self.assertEqual(list(other.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
