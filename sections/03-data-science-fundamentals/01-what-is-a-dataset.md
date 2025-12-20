# What Is a Dataset? (Rows, Columns, Features, Labels)

In ML, your model can only learn what your dataset *contains*. If you misunderstand the dataset, you will:

- train a model that looks great but fails in production
- accidentally leak target information
- pick the wrong metric

This chapter gives you a production-first mental model for datasets.

---

## Outcomes

You will be able to:

- Distinguish **features** vs **labels** (targets)
- Explain **rows** (samples) vs **columns** (fields)
- Identify common dataset traps: IDs, leakage columns, duplicates, missing values
- Inspect a dataset quickly (shape, types, missingness, label distribution)

**Estimated time**: 60–90 minutes

**Prerequisites**: Section 02 (Pandas basics)

---

## 1) What a dataset is (in practical terms)

A dataset is a structured representation of reality.

Most ML tasks start with a table:

- each **row** is one example
- each **column** is information about that example

In supervised learning, one column (or a computed value) is the **label** you want to predict.

---

## 2) The four core words (you must be fluent)

### Row / sample / example

One unit the model learns from:

- one customer
- one transaction
- one document chunk

### Column / field

One attribute of the sample:

- `tenure_months`
- `monthly_charges`
- `country`

### Features

Inputs to the model (what it learns from).

Features can be:

- numeric (`age`, `revenue`)
- categorical (`plan_type`)
- text (support ticket)
- timestamps (signup time)

### Label / target

The thing you predict:

- churn: 0/1
- fraud: 0/1
- price: a number

---

## 3) Tiny example (churn)

| customer_id | age | tenure_months | contract_type | churn |
|---:|---:|---:|---|---:|
| 123 | 42 | 18 | month-to-month | 1 |
| 124 | 30 | 6 | one-year | 0 |

- **Features**: `age`, `tenure_months`, `contract_type`
- **Label**: `churn`
- `customer_id` is *usually* **not a feature** (it’s an identifier)

---

## 4) The “ID column trap”

It’s common to have identifiers:

- user_id
- account_id
- session_id

Should IDs be used as features?

- Usually **no** (they encode nothing stable or meaningful)
- Sometimes yes if the ID has semantic meaning (rare, and risky)

If you include IDs, models can:

- memorize user behavior in training
- fail to generalize to new users

---

## 5) Dataset health checks (what you do on day 1)

When you receive a dataset, do this immediately:

1) shape: `df.shape`
2) preview: `df.head()`
3) dtypes: `df.dtypes`
4) missingness: `df.isnull().sum()`
5) label distribution (classification): `df[label].value_counts(normalize=True)`
6) duplicates: `df.duplicated().sum()`

Example:

```python
import pandas as pd

df = pd.read_csv(
	"sections/03-data-science-fundamentals/labs/baseline_model/data/churn_synth.csv"
)

print(df.shape)
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
print(df["churned"].value_counts(normalize=True))
```

---

## 6) The most dangerous dataset mistake: target leakage

Leakage means your features include information that would not be available at prediction time.

Examples:

- `cancellation_date` used to predict churn
- `refund_amount` used to predict fraud
- computing normalization using the full dataset (train + test)

Leakage is covered deeply in `04-data-leakage.md`, but you should start spotting it now.

---

## Exercises

1) For the churn example table above, list 3 possible leakage columns that *might* exist in a real dataset.
2) What’s the difference between a feature that is “highly predictive” and a feature that is “leaky”?
3) If you find duplicates, what questions do you ask before removing them?

---

## Checkpoint

You’re done if you can explain (in your own words):

- rows vs columns
- features vs label
- why post-event fields create leakage

---

## Next lesson

Continue to `02-train-val-test-splits.md`.
