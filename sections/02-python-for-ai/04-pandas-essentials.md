# Pandas Essentials (Read, Filter, Join, Groupby)

Pandas is the standard tool for turning “raw tables” into “model-ready features”.

In production, Pandas is often used for:

- dataset loading and validation
- cleaning missing values
- joining multiple sources
- aggregating events to user-level features

This chapter teaches the operations you’ll use constantly.

---

## Outcomes

You will be able to:

- Understand `DataFrame` vs `Series`
- Read and inspect datasets quickly
- Filter and create columns without loops
- Merge/join tables
- Groupby/aggregate to build features
- Handle missing values without breaking dtypes

**Estimated time**: 90–120 minutes

---

## Mental model: `DataFrame` and `Series`

- `Series`: one column (vector)
- `DataFrame`: table of columns

```python
import pandas as pd

df = pd.DataFrame({"x": [1, 2], "y": [10, 20]})
col = df["x"]            # Series
sub = df[["x", "y"]]     # DataFrame
```

---

## 1) Read + inspect (fast)

Common inspection commands:

- `df.head()`
- `df.shape`
- `df.dtypes`
- `df.isnull().sum()`
- `df.describe()`

Rule of thumb: do inspection *before* you start cleaning.

---

## 2) Selecting and filtering

### Selecting columns

```python
df[["user_id", "revenue"]]
```

### Filtering rows

```python
df[df["revenue"] > 0]
df[(df["country"] == "US") & (df["plan"] != "free")]
```

Avoid loops for filtering.

---

## 3) Creating columns

Vectorized math:

```python
df["rev_per_session"] = df["revenue"] / df["sessions"].replace(0, 1)
```

Boolean flags:

```python
df["is_paying"] = df["revenue"] > 0
```

---

## 4) Missing values (the real work)

Two common strategies:

- fill (`fillna`) when missing means “0 / none / unknown”
- drop (`dropna`) when missing makes the row unusable

Example:

```python
df["sessions"] = df["sessions"].fillna(0).astype(int)
df["revenue"] = df["revenue"].fillna(0.0)
```

Be careful with `astype(int)` when missing values exist: fill first, then cast.

---

## 5) Merge/join (how you build features)

You’ll often have:

- user table (one row per user)
- events table (many rows per user)

You merge after aggregating events:

```python
features = events.groupby("user_id").agg(total_revenue=("revenue", "sum"))
df = users.merge(features, on="user_id", how="left")
```

---

## 6) Groupby/aggregate (core ML feature engineering)

Example patterns:

- counts
- sums
- means
- last-seen timestamps

```python
by_country = df.groupby("country").agg(
	users=("user_id", "count"),
	total_revenue=("revenue", "sum"),
)
```

---

## Run the worked examples

Two runnable scripts are available:

```bash
python sections/02-python-for-ai/code/pandas_essentials.py
python sections/02-python-for-ai/code/pandas_examples.py
```

`pandas_essentials.py` is the clean “production-style” reference.
`pandas_examples.py` is a longer demo file.

---

## Exercises

1) Create a `high_value` flag for users with revenue > 200.
2) Compute average revenue per plan.
3) Join a user table to aggregated event features.

---

## Checkpoint

You’re done if you can:

- join two tables and compute grouped metrics without loops
- explain why `fillna` before `astype(int)` matters

---

## Next lesson

Continue to `05-json-csv-data.md`.
