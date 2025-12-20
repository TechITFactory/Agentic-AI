from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class GeneratorConfig:
    rows: int
    seed: int


def _sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def generate_dataframe(cfg: GeneratorConfig) -> pd.DataFrame:
    rng = np.random.default_rng(cfg.seed)

    contract_type = rng.choice(["month-to-month", "one-year", "two-year"], size=cfg.rows, p=[0.55, 0.25, 0.20])
    internet_service = rng.choice(["dsl", "fiber", "none"], size=cfg.rows, p=[0.35, 0.5, 0.15])
    payment_method = rng.choice(
        ["bank-transfer", "credit-card", "electronic-check", "mailed-check"],
        size=cfg.rows,
        p=[0.2, 0.25, 0.35, 0.2],
    )

    tenure_months = rng.integers(1, 73, size=cfg.rows)
    monthly_charges = rng.normal(loc=75, scale=20, size=cfg.rows).clip(18, 125)
    support_tickets = rng.poisson(lam=0.6, size=cfg.rows).clip(0, 6)

    # Add a few interactions to make the task non-trivial.
    contract_risk = np.select(
        [contract_type == "month-to-month", contract_type == "one-year", contract_type == "two-year"],
        [0.9, 0.2, -0.2],
        default=0.0,
    )
    fiber_risk = np.where(internet_service == "fiber", 0.5, 0.0)
    echeck_risk = np.where(payment_method == "electronic-check", 0.35, 0.0)

    # Build a logit with reasonable signal + noise.
    logit = (
        -1.2
        + contract_risk
        + fiber_risk
        + echeck_risk
        + 0.02 * (monthly_charges - 70)
        - 0.03 * (tenure_months - 24)
        + 0.25 * support_tickets
        + rng.normal(0, 0.35, size=cfg.rows)
    )

    churn_prob = _sigmoid(logit)
    churn = (rng.random(cfg.rows) < churn_prob).astype(int)

    total_charges = (monthly_charges * tenure_months + rng.normal(0, 25, size=cfg.rows)).clip(0)

    df = pd.DataFrame(
        {
            "customer_id": np.arange(1, cfg.rows + 1),
            "tenure_months": tenure_months,
            "monthly_charges": monthly_charges.round(2),
            "total_charges": total_charges.round(2),
            "contract_type": contract_type,
            "internet_service": internet_service,
            "payment_method": payment_method,
            "support_tickets": support_tickets,
            "churn": churn,
        }
    )

    return df


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a synthetic churn dataset.")
    parser.add_argument("--out", type=Path, default=Path("churn_synth.csv"), help="Output CSV path")
    parser.add_argument("--rows", type=int, default=500, help="Number of rows")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    args = parser.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)

    df = generate_dataframe(GeneratorConfig(rows=args.rows, seed=args.seed))
    df.to_csv(args.out, index=False)

    print(f"Wrote {len(df):,} rows to {args.out}")
    print("Columns:", ", ".join(df.columns))
    print("Churn rate:", f"{df['churn'].mean():.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
