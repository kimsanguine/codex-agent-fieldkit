from __future__ import annotations

import os
import subprocess
from pathlib import Path

from starter_registry import validate_registry


ROOT = Path(__file__).resolve().parents[1]


def build_checks(root: Path = ROOT) -> list[tuple[str, list[str]]]:
    _, kits = validate_registry(root)
    checks = [("starter registry", ["python3", "scripts/starter_registry.py", "--validate"])]
    checks.extend((f"starter {kit['id']} validation", ["make", "-C", kit["path"], "validate"]) for kit in kits)
    checks.extend(
        [
            ("repo unit tests", ["python3", "-m", "unittest", "discover", "-s", "tests"]),
            ("secret scan", ["bash", "scripts/check_no_secrets.sh"]),
            ("private-term scan", ["bash", "scripts/check_no_private_terms.sh"]),
            ("pii scan", ["bash", "scripts/check_no_pii.sh"]),
            ("public-link scan", ["bash", "scripts/check_public_links.sh"]),
            ("documentation link scan", ["python3", "scripts/check_docs_links.py"]),
            ("generated-artifact scan", ["bash", "scripts/check_no_generated_artifacts.sh"]),
            ("gitleaks wrapper", ["bash", "scripts/check_gitleaks.sh"]),
            ("public-surface scan", ["bash", "scripts/check_public_surface.sh"]),
        ]
    )
    return checks


def run_command(command: list[str], root: Path = ROOT) -> tuple[int, str]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        command,
        cwd=root,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return result.returncode, result.stdout.strip().replace(str(root), ".")


def status_for(label: str, code: int, output: str) -> str:
    if code != 0:
        return "Failed"
    if label == "gitleaks wrapper" and "skipped" in output.lower():
        return os.environ.get("FIELDKIT_GITLEAKS_STATUS", "Skipped")
    return "Passed"


def overall_status(statuses: list[str]) -> str:
    if "Failed" in statuses:
        return "Failed"
    if "Skipped" in statuses:
        return "Incomplete"
    return "Passed"
