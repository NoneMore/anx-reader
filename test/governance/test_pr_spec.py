"""Synthetic Git-history tests for the strict PR-Spec validator."""

import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

VALIDATOR = Path(__file__).resolve().parents[2] / "scripts/governance/check_pr_spec.py"
spec = importlib.util.spec_from_file_location("check_pr_spec", VALIDATOR)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

ACTIVE = "# Example\n\n## Intent\nImprove reliability.\n\n## Scope\nOnly one subsystem.\n\n## Acceptance Criteria\n- Tests pass.\n"
ARCHIVED = ACTIVE + "\n## Outcome\nImplemented and archived.\n\n## Verification\nRan test suite successfully.\n\n## Unresolved\nNone.\n"


class LifecycleTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.old = os.getcwd()
        os.chdir(self.tmp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "ci@example.invalid")
        self.git("config", "user.name", "Governance Test")
        self.write("README.md", "base\n")
        self.commit("base")
        self.base = self.sha()

    def tearDown(self):
        os.chdir(self.old)
        self.tmp.cleanup()

    def git(self, *args):
        return subprocess.check_output(["git", *args], stderr=subprocess.STDOUT, text=True).strip()

    def sha(self):
        return self.git("rev-parse", "HEAD")

    def write(self, path, content):
        file = Path(path)
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content, encoding="utf-8")

    def remove(self, path):
        Path(path).unlink()

    def commit(self, message):
        self.git("add", "-A")
        self.git("commit", "-qm", message)

    def activate(self, name="fix-one", content=ACTIVE):
        self.write(f"specs/active/{name}/spec.md", content)
        self.commit("spec first")

    def implement(self):
        self.write("lib/feature.dart", "void main() {}\n")
        self.commit("implementation")

    def archive(self, name="fix-one", content=ARCHIVED):
        self.remove(f"specs/active/{name}/spec.md")
        self.write(f"specs/archive/{name}/spec.md", content)
        self.commit("archive")

    def check(self):
        # Synthetic merge is head since base is an ancestor and no parallel commits.
        return checker.validate(self.base, self.sha(), self.sha())

    def expect_failure(self, code):
        with self.assertRaisesRegex(checker.ValidationError, code):
            self.check()

    def test_valid_lifecycle(self):
        self.activate()
        self.implement()
        self.archive()
        self.assertEqual(self.check(), ["fix-one"])

    def test_valid_planned_activation(self):
        self.write("specs/planned/fix-one/spec.md", ACTIVE)
        self.commit("planned")
        self.base = self.sha()
        self.remove("specs/planned/fix-one/spec.md")
        self.activate()
        self.archive()
        self.assertEqual(self.check(), ["fix-one"])

    def test_no_spec(self):
        self.implement()
        self.expect_failure("G01")

    def test_code_before_spec(self):
        self.implement()
        self.activate()
        self.archive()
        self.expect_failure("G04")

    def test_activation_and_code_same_commit(self):
        self.write("specs/active/fix-one/spec.md", ACTIVE)
        self.write("lib/feature.dart", "source")
        self.commit("bad")
        self.archive()
        self.expect_failure("G04")

    def test_spec_empty(self):
        self.activate(content=" ")
        self.expect_failure("G03")

    def test_archive_missing(self):
        self.activate()
        self.expect_failure("G05")

    def test_archive_outcome_missing(self):
        self.activate()
        self.archive(content=ACTIVE)
        self.expect_failure("G03/G07")

    def test_archive_name_reuse(self):
        self.write("specs/archive/fix-one/spec.md", ARCHIVED)
        self.commit("historical")
        self.base = self.sha()
        self.activate()
        self.archive()
        self.expect_failure("G02")

    def test_existing_archive_immutable(self):
        self.write("specs/archive/old-fix/spec.md", ARCHIVED)
        self.commit("historical")
        self.base = self.sha()
        self.activate()
        self.write("specs/archive/old-fix/spec.md", ARCHIVED + "extra")
        self.commit("modify old archive")
        self.archive()
        self.expect_failure("G08")

    def test_unrelated_active_leftover(self):
        self.activate()
        self.write("specs/active/stray/readme.md", "stray")
        self.commit("stray")
        self.archive()
        self.expect_failure("G06")

    def test_second_change_after_implementation(self):
        self.activate("fix-one")
        self.implement()
        self.activate("fix-two")
        self.archive("fix-one")
        self.archive("fix-two")
        self.expect_failure("G04")

    def test_two_changes_before_implementation(self):
        self.activate("fix-one")
        self.activate("fix-two")
        self.implement()
        self.archive("fix-one")
        self.archive("fix-two")
        self.assertEqual(self.check(), ["fix-one", "fix-two"])


if __name__ == "__main__":
    unittest.main()
