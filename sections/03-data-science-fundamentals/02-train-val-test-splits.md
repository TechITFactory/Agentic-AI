# Train vs Validation vs Test Splits (and why models lie)

If you evaluate a model incorrectly, you will deploy something that looks great in a notebook and fails in production.

Splits are the simplest defense.

---

## Outcomes

You will be able to:

- Explain the role of train vs validation vs test
- Create reproducible splits (fixed random seed)
- Choose split strategies: random, stratified, time-based, grouped
- Understand when cross-validation helps (and when it doesn’t)

**Estimated time**: 60–90 minutes

---

## 1) Why we split at all

Your model learns patterns from training data.

If you evaluate on the same data you trained on, you measure **memorization**, not generalization.

We want performance on **new, unseen data**.

---

## 2) The three splits

### Training set

Used to fit model parameters.

### Validation set

Used during development to:

- choose hyperparameters
- compare model variants
- pick thresholds

### Test set

Used once at the end as a “final exam.”

Rule: do not repeatedly tune based on test performance.

---

## 3) Typical split ratios

Common starting points:

- 70/15/15
- 80/10/10

If you have very little data:

- use cross-validation
- keep a small test set if possible

---

## 4) Random split (baseline)

This is good when:

- samples are independent
- there is no time component

In scikit-learn:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.2, random_state=42
)
```

---

## 5) Stratified split (classification, imbalanced labels)

If 5% of your samples are positive (fraud/churn), a naive split can accidentally produce:

- train: 2% positives
- test: 8% positives

Then your metrics become noisy and misleading.

Use stratification:

```python
X_train, X_test, y_train, y_test = train_test_split(
	X, y,
	test_size=0.2,
	random_state=42,
	stratify=y,
)
```

---

## 6) Time-based split (most production systems)

Use time splits when:

- you predict the future using the past
- data distribution changes over time

Example:

- train: Jan–Sep
- validation: Oct
- test: Nov

This better matches reality.

---

## 7) Grouped split (avoid user leakage)

If your dataset has multiple rows per user (events), random splitting can put the same user in train and test.

This leaks identity patterns.

Fix: split by `user_id` groups.

---

## Run the split demo script

This repo includes a runnable reference:

```bash
python sections/03-data-science-fundamentals/code/splits_demo.py
```

It prints:

- split sizes
- class balance
- how stratification changes results
- a simple time-based split example

---

## Exercises

1) Why is validation different from test?
2) In churn prediction, what makes time-based splits more realistic?
3) If your dataset has multiple rows per customer, what split strategy should you use?

---

## Checkpoint

You’re done if you can justify:

- when to use stratification
- when to use time-based splits

---

## Next lesson

Continue to `03-overfitting-underfitting.md`.
