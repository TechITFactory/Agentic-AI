from __future__ import annotations

"""Convert JSONL logs to a flat CSV.

Run:
  python sections/02-python-for-ai/code/jsonl_to_csv.py --in sections/02-python-for-ai/code/sample_logs.jsonl --out /tmp/logs.csv

Why JSONL?
- Many systems emit one JSON object per line.
- It allows streaming processing (not loading whole file).

This script demonstrates:
- robust line-by-line parsing
- best-effort flattening of nested `meta` keys
- schema drift handling (missing/extra fields)
"""

import argparse
import csv
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class LogRow:
    ts: str
    user_id: str
    event: str
    meta: dict[str, Any]


def _flatten(prefix: str, obj: Any, out: dict[str, object]) -> None:
    """Flatten nested dictionaries using a simple dotted-key scheme."""

    if isinstance(obj, dict):
        for k, v in obj.items():
            key = f"{prefix}.{k}" if prefix else str(k)
            _flatten(key, v, out)
        return

    # For arrays/other types, store as JSON string to avoid losing info.
    if isinstance(obj, list):
        out[prefix] = json.dumps(obj, ensure_ascii=False)
        return

    out[prefix] = obj


def read_jsonl(path: Path) -> list[LogRow]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    rows: list[LogRow] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON on line {line_no}: {e}") from e

            if not isinstance(obj, dict):
                raise ValueError(f"Expected JSON object per line; got {type(obj).__name__} on line {line_no}")

            ts = str(obj.get("ts", ""))
            user_id = str(obj.get("user_id", ""))
            event = str(obj.get("event", ""))
            meta_raw = obj.get("meta", {})
            meta = meta_raw if isinstance(meta_raw, dict) else {"meta": meta_raw}

            if not ts or not user_id or not event:
                raise ValueError(f"Missing required fields on line {line_no}: {obj}")

            rows.append(LogRow(ts=ts, user_id=user_id, event=event, meta=meta))

    return rows


def to_flat_dicts(rows: list[LogRow]) -> list[dict[str, object]]:
    flat_rows: list[dict[str, object]] = []

    for r in rows:
        out: dict[str, object] = {"ts": r.ts, "user_id": r.user_id, "event": r.event}
        _flatten("meta", r.meta, out)
        flat_rows.append(out)

    return flat_rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    # Union of keys = handles schema drift by expanding columns.
    all_keys: set[str] = set()
    for r in rows:
        all_keys.update(r.keys())

    fieldnames = ["ts", "user_id", "event"] + sorted(k for k in all_keys if k not in {"ts", "user_id", "event"})

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Convert JSONL logs to a flattened CSV.")
    p.add_argument("--in", dest="input_path", required=True, help="Path to input JSONL")
    p.add_argument("--out", dest="output_path", required=True, help="Path to output CSV")
    p.add_argument("--log-level", dest="log_level", default="INFO")
    return p


def main() -> int:
    args = _build_parser().parse_args()
    logging.basicConfig(level=getattr(logging, str(args.log_level).upper(), logging.INFO))

    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    logger.info("Reading JSONL: %s", input_path)
    rows = read_jsonl(input_path)
    logger.info("Loaded %d events", len(rows))

    flat = to_flat_dicts(rows)
    write_csv(output_path, flat)

    logger.info("Wrote CSV: %s", output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
