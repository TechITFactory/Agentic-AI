"""Environment verification script for the Agentic-AI course.

Goal: give students a single, reliable command that validates:
- Python version
- venv activation (best-effort)
- pip availability
- importability of core course dependencies

This script is intentionally dependency-free (stdlib only).
"""

from __future__ import annotations

import os
import platform
import shutil
import subprocess
import sys
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def _run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def _python_version_ok(min_major: int = 3, min_minor: int = 10) -> CheckResult:
    v = sys.version_info
    ok = (v.major, v.minor) >= (min_major, min_minor)
    return CheckResult(
        name="Python version",
        ok=ok,
        detail=f"{v.major}.{v.minor}.{v.micro} (min {min_major}.{min_minor})",
    )


def _pip_ok() -> CheckResult:
    pip_path = shutil.which("pip")
    if not pip_path:
        return CheckResult("pip on PATH", False, "pip not found on PATH")

    proc = _run([pip_path, "--version"])
    if proc.returncode != 0:
        return CheckResult("pip runnable", False, (proc.stderr or proc.stdout).strip() or "pip failed")
    return CheckResult("pip runnable", True, proc.stdout.strip())


def _venv_hint() -> CheckResult:
    # Not all shells export VIRTUAL_ENV, but it is a good quick indicator.
    venv = os.environ.get("VIRTUAL_ENV")
    if venv:
        return CheckResult("venv active", True, venv)
    return CheckResult(
        "venv active",
        False,
        "VIRTUAL_ENV not set (you may not be in the course venv). Continue if this is intentional.",
    )


def _imports_ok(modules: Iterable[str]) -> list[CheckResult]:
    results: list[CheckResult] = []
    for module in modules:
        try:
            __import__(module)
            results.append(CheckResult(f"import {module}", True, "ok"))
        except Exception as e:  # noqa: BLE001 - we want a clear student-facing failure
            results.append(CheckResult(f"import {module}", False, f"{type(e).__name__}: {e}"))
    return results


def _print(results: list[CheckResult]) -> int:
    width = max(len(r.name) for r in results) if results else 0

    failures = [r for r in results if not r.ok]
    for r in results:
        status = "OK" if r.ok else "FAIL"
        print(f"[{status}] {r.name.ljust(width)}  {r.detail}")

    if failures:
        print("\nNext steps:")
        if any(r.name == "Python version" for r in failures):
            print("- Install Python 3.10+ and ensure it is the selected interpreter in VS Code.")
        if any(r.name.startswith("import ") for r in failures):
            print("- Run: pip install -r requirements.txt")
        if any(r.name == "venv active" for r in failures):
            print("- Activate venv (PowerShell): .\\venv\\Scripts\\activate")
        return 1

    print("\nAll checks passed. You're ready for Section 02.")
    return 0


def main() -> int:
    print("Agentic-AI environment verification")
    print(f"- Python: {sys.executable}")
    print(f"- OS: {platform.system()} {platform.release()} ({platform.platform()})")

    checks: list[CheckResult] = []
    checks.append(_python_version_ok())
    checks.append(_venv_hint())
    checks.append(_pip_ok())

    # Keep this list small and representative; do not fail students on optional tools.
    core_modules = [
        "numpy",
        "pandas",
        "sklearn",
        "fastapi",
        "pydantic",
        "pytest",
    ]
    checks.extend(_imports_ok(core_modules))

    return _print(checks)


if __name__ == "__main__":
    raise SystemExit(main())
