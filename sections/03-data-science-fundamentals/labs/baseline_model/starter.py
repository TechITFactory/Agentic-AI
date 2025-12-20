from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Baseline churn model (starter).")
    parser.add_argument(
        "--data",
        type=Path,
        default=Path(__file__).parent / "data" / "churn_synth.csv",
        help="Path to churn CSV",
    )
    parser.add_argument("--test-size", type=float, default=0.25, help="Test set fraction")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    return parser.parse_args()


def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(
            f"Missing dataset: {path}. You can regenerate it via: "
            f"python data/generate_churn_synth.py --out {path}"
        )
    return pd.read_csv(path)


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    # TODO: Identify categorical vs numeric columns.
    # Hint: for this dataset you can start with dtype-based detection.
    raise NotImplementedError("TODO: build ColumnTransformer with OneHotEncoder + StandardScaler")


def build_model(preprocessor: ColumnTransformer) -> Pipeline:
    # TODO: Build a Pipeline(preprocessor -> LogisticRegression).
    raise NotImplementedError("TODO: build model pipeline")


def evaluate(y_true, y_pred, label: str) -> None:
    print("\n" + "=" * 70)
    print(label)
    print("=" * 70)
    print("Confusion matrix (rows=true, cols=pred):")
    print(confusion_matrix(y_true, y_pred))
    print("\nKey metrics:")
    print("  precision:", f"{precision_score(y_true, y_pred, zero_division=0):.3f}")
    print("  recall:   ", f"{recall_score(y_true, y_pred, zero_division=0):.3f}")
    print("  f1:       ", f"{f1_score(y_true, y_pred, zero_division=0):.3f}")
    print("\nClassification report:")
    print(classification_report(y_true, y_pred, zero_division=0))


def main() -> int:
    args = parse_args()
    df = load_data(args.data)

    if "churn" not in df.columns:
        raise ValueError("Expected a 'churn' column as the label")

    y = df["churn"].astype(int)
    X = df.drop(columns=["churn"])

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=args.test_size,
        random_state=args.seed,
        stratify=y,
    )

    # Naive baseline: always predict majority class.
    dummy = DummyClassifier(strategy="most_frequent")
    dummy.fit(X_train, y_train)
    dummy_pred = dummy.predict(X_test)
    evaluate(y_test, dummy_pred, label="Naive baseline: DummyClassifier(most_frequent)")

    # TODO: Build preprocessor + model pipeline, then evaluate on the same test set.
    # preprocessor = build_preprocessor(X_train)
    # model = build_model(preprocessor)
    # model.fit(X_train, y_train)
    # model_pred = model.predict(X_test)
    # evaluate(y_test, model_pred, label="Baseline model: LogisticRegression + preprocessing")

    print("\nNEXT STEP")
    print("- Implement build_preprocessor() and build_model()")
    print("- Uncomment the baseline model block in main()")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
