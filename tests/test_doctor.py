from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCTOR = ROOT / "scripts" / "doctor.py"


class DoctorTests(unittest.TestCase):
    def test_doctor_reports_a_ready_repo_and_codex_next_action(self) -> None:
        result = subprocess.run(
            ["python3", str(DOCTOR), "--root", str(ROOT)],
            text=True,
            capture_output=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("[PASS] repository contract", result.stdout)
        self.assertIn("Next action: make demo", result.stdout)

    def test_doctor_fails_when_the_repository_marker_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result = subprocess.run(
                ["python3", str(DOCTOR), "--root", str(root)],
                text=True,
                capture_output=True,
            )
        self.assertEqual(1, result.returncode)
        self.assertIn("[FAIL] repository contract", result.stdout)
        self.assertIn("AGENTS.md", result.stdout)


if __name__ == "__main__":
    unittest.main()
