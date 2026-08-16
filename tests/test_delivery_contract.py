from __future__ import annotations

import json
import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "scripts" / "starter_registry.py"
LINKS = ROOT / "scripts" / "check_docs_links.py"
REPORT = ROOT / "scripts" / "write_validation_report.py"


class StarterRegistryContractTests(unittest.TestCase):
    def test_current_registry_validates_and_lists_the_primary_starter(self) -> None:
        result = subprocess.run(
            ["python3", str(REGISTRY), "--root", str(ROOT), "--validate"],
            text=True,
            capture_output=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)

        paths = subprocess.run(
            ["python3", str(REGISTRY), "--root", str(ROOT), "--paths"],
            text=True,
            capture_output=True,
        )
        self.assertEqual(0, paths.returncode, paths.stderr)
        self.assertEqual("starter-kits/faq-agent-lite\n", paths.stdout)

    def test_registry_rejects_a_starter_missing_handoff_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            kit = root / "starter-kits" / "demo-kit"
            shutil.copytree(ROOT / "starter-kits" / "faq-agent-lite", kit)
            (kit / "_handoff" / "handoff.md").unlink()
            (root / "starter-kits").mkdir(exist_ok=True)
            (root / "starter-kits" / "registry.json").write_text(
                json.dumps({"version": 1, "primary": "demo-kit", "kits": [{"id": "demo-kit", "path": "starter-kits/demo-kit"}]}),
                encoding="utf-8",
            )
            result = subprocess.run(
                ["python3", str(REGISTRY), "--root", str(root), "--validate"],
                text=True,
                capture_output=True,
            )
        self.assertNotEqual(0, result.returncode)
        self.assertIn("_handoff/handoff.md", result.stderr)


class DocumentationAndReportContractTests(unittest.TestCase):
    def test_current_markdown_links_resolve(self) -> None:
        result = subprocess.run(
            ["python3", str(LINKS), "--root", str(ROOT)],
            text=True,
            capture_output=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)

    def test_link_checker_rejects_a_missing_relative_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("[missing](guides/validation_log.md)\n", encoding="utf-8")
            result = subprocess.run(
                ["python3", str(LINKS), "--root", str(root)],
                text=True,
                capture_output=True,
            )
        self.assertNotEqual(0, result.returncode)
        self.assertIn("README.md", result.stderr)
        self.assertIn("guides/validation_log.md", result.stderr)

    def test_validation_report_contract_is_full_and_marks_local_gitleaks_skipped(self) -> None:
        sys.path.insert(0, str(REPORT.parent))
        spec = importlib.util.spec_from_file_location("validation_report", REPORT)
        self.assertIsNotNone(spec)
        self.assertIsNotNone(spec.loader)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)

        with patch.dict("os.environ", {}, clear=True):
            labels = [label for label, _ in module.build_checks(ROOT)]
            self.assertIn("starter registry", labels)
            self.assertIn("documentation link scan", labels)
            self.assertIn("public-surface scan", labels)
            self.assertIn("gitleaks wrapper", labels)
            self.assertEqual("Skipped", module.status_for("gitleaks wrapper", 0, "gitleaks scan: skipped"))
            self.assertEqual("Incomplete", module.overall_status(["Passed", "Skipped"]))


if __name__ == "__main__":
    unittest.main()
