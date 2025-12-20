from __future__ import annotations

"""Metrics examples for classification and regression.

Run:
  python sections/03-data-science-fundamentals/code/metrics_examples.py

Prints:
- confusion matrix
- accuracy, precision, recall, F1
- ROC-AUC and PR-AUC (Average Precision)
- regression metrics: MAE, RMSE, R² vs baselines

This is intentionally terminal-friendly (prints results).
"""

import numpy as np
from sklearn.datasets import make_classification, make_regression
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    confusion_matrix,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    precision_score,
    r2_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def classification_metrics_demo() -> None:
    print("=" * 70)
    print("CLASSIFICATION METRICS")
    print("=" * 70)

    X, y = make_classification(
        n_samples=5000,
        n_features=15,
        n_informative=6,
        n_redundant=3,
        weights=[0.9, 0.1],
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    pipe = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=400)),
        ]
    )
    pipe.fit(X_train, y_train)

    y_prob = pipe.predict_proba(X_test)[:, 1]
    y_pred = (y_prob >= 0.5).astype(int)

    cm = confusion_matrix(y_test, y_pred)
    print("Confusion matrix [ [TN FP] [FN TP] ]:")
    print(cm)

    print("\nThreshold = 0.50")
    print(f"Accuracy : {accuracy_score(y_test, y_pred):.3f}")
    print(f"Precision: {precision_score(y_test, y_pred, zero_division=0):.3f}")
    print(f"Recall   : {recall_score(y_test, y_pred, zero_division=0):.3f}")
    print(f"F1       : {f1_score(y_test, y_pred, zero_division=0):.3f}")

    print("\nRanking metrics (threshold-independent)")
    print(f"ROC-AUC  : {roc_auc_score(y_test, y_prob):.3f}")
    print(f"PR-AUC(AP): {average_precision_score(y_test, y_prob):.3f}")

    # Show how threshold affects precision/recall
    for thr in [0.2, 0.5, 0.8]:
        yp = (y_prob >= thr).astype(int)
        p = precision_score(y_test, yp, zero_division=0)
        r = recall_score(y_test, yp, zero_division=0)
        print(f"\nThreshold={thr:.2f}  precision={p:.3f}  recall={r:.3f}")


def regression_metrics_demo() -> None:
    print("\n" + "=" * 70)
    print("REGRESSION METRICS")
    print("=" * 70)

    X, y = make_regression(
        n_samples=3000,
        n_features=8,
        n_informative=6,
        noise=25.0,
        random_state=7,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=7
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)

    print("Model: LinearRegression")
    print(f"MAE : {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²  : {r2:.3f}")

    # Baselines
    mean_baseline = np.full_like(y_test, fill_value=float(y_train.mean()), dtype=float)
    median_baseline = np.full_like(y_test, fill_value=float(np.median(y_train)), dtype=float)

    def report_baseline(name: str, yb: np.ndarray) -> None:
        print(f"\nBaseline: {name}")
        print(f"MAE : {mean_absolute_error(y_test, yb):.2f}")
        print(f"RMSE: {mean_squared_error(y_test, yb, squared=False):.2f}")
        print(f"R²  : {r2_score(y_test, yb):.3f}")

    report_baseline("predict mean", mean_baseline)
    report_baseline("predict median", median_baseline)


def main() -> int:
    classification_metrics_demo()
    regression_metrics_demo()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
