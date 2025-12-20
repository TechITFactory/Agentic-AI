from __future__ import annotations

from dataclasses import asdict
from typing import Iterable

from python_crash_course.io_utils import UserRecord


def filter_records(
    records: Iterable[UserRecord],
    *,
    min_score: float,
    country: str | None = None,
) -> list[UserRecord]:
    if not (0.0 <= min_score <= 1.0):
        raise ValueError("min_score must be between 0 and 1")

    country_norm = country.strip().upper() if country else None

    out: list[UserRecord] = []
    for r in records:
        if r.score < min_score:
            continue
        if country_norm and r.country != country_norm:
            continue
        out.append(r)

    return out


def to_csv_rows(records: Iterable[UserRecord]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for r in records:
        d = asdict(r)
        rows.append({"id": d["user_id"], "country": d["country"], "score": d["score"]})
    return rows
