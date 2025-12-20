from __future__ import annotations

"""Train/validation/test splits demo.

Run:
  python sections/03-data-science-fundamentals/code/splits_demo.py

Shows:
- random split
- stratified split (classification)
- time-based split (temporal data)

This file is intentionally print-based so it runs in any terminal.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


def _class_balance(y: np.ndarray) -> dict[int, float]:
    values, counts = np.unique(y, return_counts=True)
    total = counts.sum()
    return {int(v): float(c) / float(total) for v, c in zip(values, counts)}


def demo_random_vs_stratified() -> None:
    print("=" * 70)
    print("RANDOM VS STRATIFIED SPLIT")
    print("=" * 70)

    X, y = make_classification(
        n_samples=2000,
        n_features=10,
        n_informative=5,
        n_redundant=2,
        weights=[0.9, 0.1],
        random_state=42,
    )

    print(f"Label balance overall: {_class_balance(y)}")

    # Random split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print("\nRandom split:")
    print(f"- train size: {len(y_train)}  balance: {_class_balance(y_train)}")
    print(f"- test  size: {len(y_test)}  balance: {_class_balance(y_test)}")

    # Stratified split
    X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print("\nStratified split:")
    print(f"- train size: {len(y_train_s)}  balance: {_class_balance(y_train_s)}")
    print(f"- test  size: {len(y_test_s)}  balance: {_class_balance(y_test_s)}")

    print("\nTakeaway: stratification keeps class balance stable across splits.")


def demo_time_based_split() -> None:
    print("\n" + "=" * 70)
    print("TIME-BASED SPLIT")
    print("=" * 70)

    rng = np.random.default_rng(42)

    n = 300
    df = pd.DataFrame(
        {
            "day": pd.date_range("2025-01-01", periods=n, freq="D"),
            "feature": rng.normal(0, 1, size=n),
        }
    )

    # Simulate label drift over time: positives become more common later.
    probs = np.linspace(0.05, 0.25, n)
    df["label"] = (rng.random(n) < probs).astype(int)

    # Time split: train first 70%, val next 15%, test last 15%
    train_end = int(n * 0.70)
    val_end = int(n * 0.85)

    train = df.iloc[:train_end]
    val = df.iloc[train_end:val_end]
    test = df.iloc[val_end:]

    def bal(s: pd.Series) -> float:
        return float(s.mean())

    print(f"Train range: {train['day'].min().date()} -> {train['day'].max().date()}  pos_rate={bal(train['label']):.3f}")
    print(f"Val   range: {val['day'].min().date()} -> {val['day'].max().date()}  pos_rate={bal(val['label']):.3f}")
    print(f"Test  range: {test['day'].min().date()} -> {test['day'].max().date()}  pos_rate={bal(test['label']):.3f}")

    print("\nTakeaway: time splits reflect real deployment (future != past).")


def main() -> int:
    demo_random_vs_stratified()
    demo_time_based_split()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
