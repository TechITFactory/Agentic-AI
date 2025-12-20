from __future__ import annotations

import argparse
import logging
from pathlib import Path

from python_crash_course.filtering import filter_records, to_csv_rows
from python_crash_course.io_utils import parse_user_records, read_json_records, write_csv

logger = logging.getLogger(__name__)


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Read JSON user records, filter them, and write CSV output.",
    )
    p.add_argument("--in", dest="input_path", required=True, help="Path to input JSON")
    p.add_argument("--out", dest="output_path", required=True, help="Path to output CSV")
    p.add_argument(
        "--min-score",
        dest="min_score",
        type=float,
        default=0.7,
        help="Minimum score threshold (0..1). Default: 0.7",
    )
    p.add_argument(
        "--country",
        dest="country",
        default=None,
        help="Optional country filter (e.g., US).",
    )
    p.add_argument(
        "--log-level",
        dest="log_level",
        default="INFO",
        help="Logging level (DEBUG, INFO, WARNING, ERROR). Default: INFO",
    )
    return p


def main() -> int:
    args = _build_parser().parse_args()

    logging.basicConfig(level=getattr(logging, str(args.log_level).upper(), logging.INFO))

    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    logger.info("Reading input JSON: %s", input_path)
    raw = read_json_records(input_path)
    records = parse_user_records(raw)

    logger.info("Loaded %d records", len(records))

    filtered = filter_records(records, min_score=float(args.min_score), country=args.country)
    logger.info("Filtered down to %d records", len(filtered))

    rows = to_csv_rows(filtered)
    write_csv(output_path, rows, fieldnames=["id", "country", "score"])

    logger.info("Wrote CSV: %s", output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
