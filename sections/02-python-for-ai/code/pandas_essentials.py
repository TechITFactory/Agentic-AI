from __future__ import annotations

"""Pandas essentials script for Section 02.

Run:
  python sections/02-python-for-ai/code/pandas_essentials.py

This script demonstrates:
- read -> inspect -> filter -> assign -> groupby -> merge
- missing values handling

It uses in-memory sample data so it runs anywhere.
"""

import pandas as pd


def main() -> int:
    print("=" * 70)
    print("PANDAS ESSENTIALS (READ, FILTER, JOIN, GROUPBY)")
    print("=" * 70)

    users = pd.DataFrame(
        [
            {"user_id": 1, "country": "US", "plan": "basic"},
            {"user_id": 2, "country": "US", "plan": "premium"},
            {"user_id": 3, "country": "CA", "plan": "basic"},
            {"user_id": 4, "country": "GB", "plan": "free"},
        ]
    )

    events = pd.DataFrame(
        [
            {"user_id": 1, "sessions": 10, "revenue": 120.0},
            {"user_id": 2, "sessions": 3, "revenue": 450.0},
            {"user_id": 3, "sessions": None, "revenue": 80.0},
            {"user_id": 4, "sessions": 0, "revenue": None},
        ]
    )

    print("\nUsers:")
    print(users)
    print("\nEvents:")
    print(events)

    # 1) Missing values
    print("\n1) Missing values")
    events_clean = events.copy()
    events_clean["sessions"] = events_clean["sessions"].fillna(0).astype(int)
    events_clean["revenue"] = events_clean["revenue"].fillna(0.0)
    print(events_clean)

    # 2) Merge/join
    print("\n2) Merge (left join users -> events)")
    df = users.merge(events_clean, on="user_id", how="left")
    print(df)

    # 3) Filtering
    print("\n3) Filtering")
    us_only = df[df["country"] == "US"]
    print("US only:\n", us_only)

    # 4) Feature columns
    print("\n4) Adding derived columns")
    df["avg_rev_per_session"] = df.apply(
        lambda r: (r["revenue"] / r["sessions"]) if r["sessions"] > 0 else 0.0,
        axis=1,
    )
    df["is_paying"] = df["revenue"] > 0
    print(df)

    # 5) Groupby
    print("\n5) Groupby")
    by_country = df.groupby("country").agg(
        users=("user_id", "count"),
        total_revenue=("revenue", "sum"),
        avg_sessions=("sessions", "mean"),
    )
    print(by_country)

    print("\nDone. Next: JSON/CSV/JSONL handling.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
