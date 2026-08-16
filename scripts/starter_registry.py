from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_PATHS = (
    "AGENTS.md",
    "README.md",
    "Makefile",
    "START_HERE.md",
    "data",
    "scripts",
    "src",
    "tests/golden_set.jsonl",
    "workspace/architecture.md",
    "workspace/prd.md",
    "workspace/progress.md",
    "workspace/validation_log.md",
    "_handoff/handoff.md",
    "_handoff/migration_checklist.md",
)


class RegistryError(ValueError):
    pass


def load_registry(root: Path) -> tuple[str, list[dict[str, str]]]:
    registry_path = root / "starter-kits" / "registry.json"
    try:
        data = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RegistryError(f"cannot read starter registry: {exc}") from exc

    if not isinstance(data, dict) or data.get("version") != 1:
        raise RegistryError("starter registry must be an object with version 1")
    primary = data.get("primary")
    kits = data.get("kits")
    if not isinstance(primary, str) or not isinstance(kits, list) or not kits:
        raise RegistryError("starter registry needs primary and a non-empty kits list")

    normalized: list[dict[str, str]] = []
    ids: set[str] = set()
    for kit in kits:
        if not isinstance(kit, dict) or not isinstance(kit.get("id"), str) or not isinstance(kit.get("path"), str):
            raise RegistryError("every starter registry entry needs string id and path")
        kit_id = kit["id"]
        relative_path = Path(kit["path"])
        if kit_id in ids or relative_path.is_absolute() or ".." in relative_path.parts:
            raise RegistryError(f"invalid starter registry entry: {kit_id}")
        ids.add(kit_id)
        normalized.append({"id": kit_id, "path": relative_path.as_posix()})

    if primary not in ids:
        raise RegistryError("starter registry primary must name a registered kit")
    return primary, normalized


def validate_registry(root: Path) -> tuple[str, list[dict[str, str]]]:
    primary, kits = load_registry(root)
    errors: list[str] = []
    for kit in kits:
        kit_root = root / kit["path"]
        if not kit_root.is_dir():
            errors.append(f"{kit['id']}: missing starter directory {kit['path']}")
            continue
        for required in REQUIRED_PATHS:
            if not (kit_root / required).exists():
                errors.append(f"{kit['id']}: missing {required}")
    if errors:
        raise RegistryError("\n".join(errors))
    return primary, kits


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and query the starter-kit registry.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--validate", action="store_true")
    action.add_argument("--paths", action="store_true")
    action.add_argument("--primary-path", action="store_true")
    args = parser.parse_args()

    try:
        primary, kits = validate_registry(args.root.resolve())
    except RegistryError as exc:
        print(f"starter registry: fail\n{exc}", file=sys.stderr)
        return 1

    if args.paths:
        print("\n".join(kit["path"] for kit in kits))
    elif args.primary_path:
        print(next(kit["path"] for kit in kits if kit["id"] == primary))
    else:
        print(f"starter registry: pass ({len(kits)} kit(s), primary={primary})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
