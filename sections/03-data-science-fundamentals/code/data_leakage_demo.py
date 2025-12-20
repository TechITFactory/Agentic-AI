from __future__ import annotations

"""Data leakage demo.

Run:
  python sections/03-data-science-fundamentals/code/data_leakage_demo.py

Demonstrates two common leakage patterns:
1) Target leakage via a post-event feature
2) Preprocessing leakage (fit on full data) and the correct pipeline approach

The goal is to build intuition: suspiciously high scores are a smell.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def _report(name: str, y_true: np.ndarray, y_prob: np.ndarray) -> None:
    roc = roc_auc_score(y_true, y_prob)
    ap = average_precision_score(y_true, y_prob)
    print(f"{name}: ROC-AUC={roc:.3f}  PR-AUC(AP)={ap:.3f}")


def demo_target_leakage() -> None:
    print("=" * 70)
    print("TARGET LEAKAGE (POST-EVENT FEATURE)")
    print("=" * 70)

    X, y = make_classification(
        n_samples=4000,
        n_features=12,
        n_informative=6,
        n_redundant=2,
        weights=[0.85, 0.15],
        random_state=42,
    )

    # Create a leaky feature that is basically the target plus tiny noise.
    rng = np.random.default_rng(42)
    leaky = y.astype(float) + rng.normal(0, 0.05, size=y.shape[0])
    X_leaky = np.column_stack([X, leaky])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    X_train_l, X_test_l, _, _ = train_test_split(
        X_leaky, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    p = model.predict_proba(X_test)[:, 1]
    _report("No leakage", y_test, p)

    model_leaky = LogisticRegression(max_iter=200)
    model_leaky.fit(X_train_l, y_train)
    p_leaky = model_leaky.predict_proba(X_test_l)[:, 1]
    _report("With leaky feature", y_test, p_leaky)

    print("\nInterpretation:")
    print("- The leaky feature makes the model look unrealistically strong.")
    print("- In production, that feature would not exist at prediction time.")


def demo_preprocessing_leakage() -> None:
    print("\n" + "=" * 70)
    print("PREPROCESSING LEAKAGE (SCALING FIT)")
    print("=" * 70)

    X, y = make_classification(
        n_samples=3000,
        n_features=20,
        n_informative=6,
        n_redundant=4,
        weights=[0.9, 0.1],
        random_state=7,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=7, stratify=y
    )

    # WRONG: fit scaler on full data (train + test)
    scaler_wrong = StandardScaler()
    X_all_scaled = scaler_wrong.fit_transform(np.vstack([X_train, X_test]))
    X_train_wrong = X_all_scaled[: len(X_train)]
    X_test_wrong = X_all_scaled[len(X_train) :]

    m_wrong = LogisticRegression(max_iter=300)
    m_wrong.fit(X_train_wrong, y_train)
    p_wrong = m_wrong.predict_proba(X_test_wrong)[:, 1]
    _report("Wrong (scaler fit on full data)", y_test, p_wrong)

    # RIGHT: use a pipeline so fit happens only on training data
    pipe = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=300)),
        ]
    )
    pipe.fit(X_train, y_train)
    p_right = pipe.predict_proba(X_test)[:, 1]
    _report("Right (pipeline fit on train only)", y_test, p_right)

    print("\nTakeaway:")
    print("- The safe default is: put preprocessing + model in a Pipeline.")


def main() -> int:
    demo_target_leakage()
    demo_preprocessing_leakage()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
