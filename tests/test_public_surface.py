from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_public_surface.sh"
LINK_SCRIPT = ROOT / "scripts" / "check_public_links.sh"


class PublicSurfaceTests(unittest.TestCase):
    def test_public_surface_rejects_nested_docs_and_archive(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "nested" / "docs").mkdir(parents=True)
            result = subprocess.run(["bash", str(SCRIPT), str(root)], text=True, capture_output=True)
        self.assertEqual(1, result.returncode)
        self.assertIn("forbidden", result.stderr)

    def test_current_tree_has_no_forbidden_public_directories(self):
        result = subprocess.run(["bash", str(SCRIPT), str(ROOT)], text=True, capture_output=True)
        self.assertEqual(0, result.returncode, result.stderr)

    def test_public_link_guard_ignores_worktree_git_pointer(self):
        result = subprocess.run(["bash", str(LINK_SCRIPT)], cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(0, result.returncode, result.stderr)
