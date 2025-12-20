from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


@dataclass(frozen=True)
class UserRecord:
    """A minimal typed view of the JSON schema used in this lesson."""

    user_id: str
    country: str
    score: float


def read_json_records(path: Path) -> list[dict[str, Any]]:
    """Read a JSON file expected to contain a list of objects."""

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {path}: {e}") from e

    if not isinstance(raw, list):
        raise ValueError(f"Expected a JSON list in {path}, got {type(raw).__name__}")

    for idx, item in enumerate(raw):
        if not isinstance(item, dict):
            raise ValueError(
                f"Expected each item to be an object (dict). Item {idx} is {type(item).__name__}."
            )

    return raw  # type: ignore[return-value]


def parse_user_records(raw: Iterable[dict[str, Any]]) -> list[UserRecord]:
    """Convert raw dicts into `UserRecord` with validation.

    Raises:
        ValueError: on missing keys or wrong types.
    """

    records: list[UserRecord] = []
    for idx, item in enumerate(raw):
        try:
            user_id = str(item["id"]).strip()
            country = str(item["country"]).strip().upper()
            score = float(item["score"])
        except KeyError as e:
            raise ValueError(f"Missing key {e} in item {idx}: {item}") from e
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid types in item {idx}: {item}. Error: {e}") from e

        if not user_id:
            raise ValueError(f"Empty id in item {idx}: {item}")
        if not country:
            raise ValueError(f"Empty country in item {idx}: {item}")
        if not (0.0 <= score <= 1.0):
            raise ValueError(f"score must be between 0 and 1 in item {idx}: {item}")

        records.append(UserRecord(user_id=user_id, country=country, score=score))

    return records


def write_csv(path: Path, rows: Iterable[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
