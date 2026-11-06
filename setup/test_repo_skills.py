from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name('install-repo-skills.py')

class RepoSkillsTests(unittest.TestCase):
    def run_install(self, home, *args):
        return subprocess.run([sys.executable, str(SCRIPT), '--home', str(home), *args], capture_output=True, text=True)

    def test_both_idempotent(self):
        with tempfile.TemporaryDirectory(prefix='skill home ') as d:
            home=Path(d)
            self.assertEqual(self.run_install(home, '--dry-run').returncode, 0)
            self.assertFalse((home/'.codex').exists())
            r=self.run_install(home)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(self.run_install(home, '--verify').returncode, 0)
            self.assertIn('"changed_files": 0', self.run_install(home).stdout)
            for name in ('graphify', 'agent-reach', 'mirofish', 'paperclip', 'voicestudio', 'open-seo'):
                self.assertEqual((home/'.codex/skills'/name/'SKILL.md').read_bytes(), (home/'.claude/skills'/name/'SKILL.md').read_bytes())

    def test_conflict_preserved_and_replace_backed_up(self):
        with tempfile.TemporaryDirectory() as d:
            home=Path(d); dest=home/'.claude/skills/graphify/SKILL.md'
            dest.parent.mkdir(parents=True); dest.write_text('custom skill')
            self.assertNotEqual(self.run_install(home).returncode, 0)
            self.assertFalse((home/'.codex').exists())
            r=self.run_install(home, '--replace')
            self.assertEqual(r.returncode, 0, r.stderr)
            saved=list((home/'.local/share/repo-skill-backups').glob('*/.claude/skills/graphify/SKILL.md'))
            self.assertEqual(len(saved),1); self.assertEqual(saved[0].read_text(),'custom skill')

    def test_symlink_refused_before_writes(self):
        with tempfile.TemporaryDirectory() as d:
            home=Path(d); other=home/'elsewhere'; other.mkdir()
            (home/'.claude').symlink_to(other, target_is_directory=True)
            self.assertNotEqual(self.run_install(home, '--replace').returncode, 0)
            self.assertFalse((home/'.codex').exists()); self.assertEqual(list(other.iterdir()),[])

    def test_parent_file_refused_before_writes(self):
        with tempfile.TemporaryDirectory() as d:
            home=Path(d); blocked=home/'.claude/skills/graphify/references'
            blocked.parent.mkdir(parents=True); blocked.write_text('preserve')
            self.assertNotEqual(self.run_install(home, '--replace').returncode, 0)
            self.assertFalse((home/'.codex').exists())
            self.assertEqual(blocked.read_text(),'preserve')

    def test_missing_source_refused(self):
        with tempfile.TemporaryDirectory() as d:
            import shutil
            root=Path(d)/'library'; (root/'setup').mkdir(parents=True)
            shutil.copy2(SCRIPT, root/'setup'/SCRIPT.name)
            shutil.copy2(SCRIPT.with_name('manifest.json'), root/'setup/manifest.json')
            home=Path(d)/'home'
            r=subprocess.run([sys.executable,str(root/'setup'/SCRIPT.name),'--home',str(home)],capture_output=True)
            self.assertNotEqual(r.returncode,0); self.assertFalse(home.exists())

if __name__ == '__main__': unittest.main()
