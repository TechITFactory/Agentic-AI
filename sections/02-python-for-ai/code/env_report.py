from __future__ import annotations

"""Environment report script for Section 02.

This complements the course-wide `scripts/verify_env.py` by printing details that help
students debug environment issues.

Run:
  python sections/02-python-for-ai/code/env_report.py
"""

import os
import platform
import sys


def main() -> int:
    print("=" * 70)
    print("PYTHON ENV REPORT")
    print("=" * 70)
    print(f"sys.executable: {sys.executable}")
    print(f"python: {sys.version.split()[0]}")
    print(f"platform: {platform.platform()}")
    print(f"VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV')}")
    print(f"cwd: {os.getcwd()}")

    print("\nTop of sys.path:")
    for p in sys.path[:8]:
        print("-", p)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
