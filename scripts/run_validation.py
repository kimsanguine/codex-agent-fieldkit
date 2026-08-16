from __future__ import annotations

from validation_contract import ROOT, build_checks, run_command, status_for


def main() -> int:
    failed = False
    for label, command in build_checks(ROOT):
        code, output = run_command(command, ROOT)
        status = status_for(label, code, output)
        print(f"[{status}] {label}")
        if output:
            print(output)
        failed = failed or status == "Failed"
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
