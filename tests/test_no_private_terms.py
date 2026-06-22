import os
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIVATE_TERMS = [
    "삼성생명",
    "Samsung Life",
    "BIZROUTER",
    "kimsanguine@gmail.com",
    "2606_삼성_바이브코딩",
]
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".venv"}
SKIP_FILES = {"test_no_private_terms.py", "check_no_private_terms.sh"}


class PublicBoundaryTest(unittest.TestCase):
    def test_no_private_terms_in_text_files(self) -> None:
        hits: list[str] = []
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            if path.name in SKIP_FILES:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for term in PRIVATE_TERMS:
                if term in text:
                    hits.append(f"{path.relative_to(ROOT)} contains {term}")
        self.assertEqual([], hits)


if __name__ == "__main__":
    unittest.main()
