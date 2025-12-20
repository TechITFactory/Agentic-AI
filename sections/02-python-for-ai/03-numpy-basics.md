# NumPy Basics (Arrays, Masking, Broadcasting)

NumPy is the foundation for almost everything numeric in ML:

- arrays (vectors/matrices)
- vectorized math (fast operations without Python loops)
- indexing/masking (filtering)
- broadcasting (one of the most important mental models)

This chapter teaches NumPy the way you’ll use it in modeling, feature engineering, and evaluation.

---

## Outcomes

You will be able to:

- Create arrays, understand `shape` and `dtype`
- Slice arrays and filter using boolean masks
- Perform vectorized operations and common reductions
- Explain (and use) broadcasting correctly
- Use dot products / matrix multiplication for basic linear algebra

**Estimated time**: 60–90 minutes

---

## What is NumPy, really?

NumPy arrays are fixed-type, contiguous blocks of memory.

That’s why they’re fast:

- operations happen in compiled code
- you avoid Python-level loops

The tradeoff:

- you must care about shapes and dtypes

---

## 1) Arrays, shapes, dtypes

```python
import numpy as np

a = np.array([1, 2, 3], dtype=np.int64)
print(a.shape, a.dtype)
```

Key properties:

- `shape`: dimensions, e.g. `(rows, cols)`
- `dtype`: underlying type (float64, int64, etc.)

Why `dtype` matters in ML:

- floats are needed for many models
- memory usage matters for large datasets

---

## 2) Reshaping and 2D mental model

```python
x = np.arange(12).reshape(3, 4)
print(x)
```

Think of this as 3 rows, 4 columns.

---

## 3) Slicing

```python
first_row = x[0]
first_col = x[:, 0]
sub = x[0:2, 1:3]
```

The most common patterns:

- `x[i]` row selection
- `x[:, j]` column selection
- `x[r0:r1, c0:c1]` submatrix

---

## 4) Vectorized math (no loops)

Bad (slow, error-prone):

```python
out = []
for v in x.flatten():
	out.append(v * 2 + 1)
```

Good:

```python
y = x * 2 + 1
```

---

## 5) Boolean masking

Masking is how you filter data efficiently.

```python
mask = x % 2 == 0
evens = x[mask]
```

This is used in:

- removing invalid rows
- selecting a class
- filtering outliers

---

## 6) Reductions (sum/mean/std)

```python
x.sum()
x.mean(axis=0)  # per column
x.mean(axis=1)  # per row
```

The `axis` parameter is critical:

- `axis=0` collapses rows (keeps columns)
- `axis=1` collapses columns (keeps rows)

---

## 7) Broadcasting (most important concept)

Broadcasting is how NumPy applies operations across shapes.

Example: scaling each column by a different value.

```python
col_scale = np.array([1.0, 10.0, 100.0, 1000.0])
scaled = x * col_scale
```

What happened?

- `x` is shape `(3, 4)`
- `col_scale` is shape `(4,)`

NumPy treats `(4,)` as compatible with the last dimension of `(3, 4)` and “stretches” it across rows.

---

## 8) Dot products / matrix multiply

```python
v = np.array([1.0, 2.0, 3.0, 4.0])
score = x[0].dot(v)
```

Matrix multiply uses `@`:

```python
w = np.arange(8).reshape(4, 2)
z = x @ w
```

---

## Run the full worked example

This repo includes a complete runnable script:

```bash
python sections/02-python-for-ai/code/numpy_basics.py
```

---

## Exercises (do these without Google first)

1) Create a random array `A` of shape `(5, 3)` and compute column means.
2) Filter rows where the first column is greater than 0.5.
3) Standardize each column (subtract mean, divide by std). What shape are the means/stds?

---

## Checkpoint

You’re done if you can explain:

- why vectorization is faster than loops
- what `axis=0` vs `axis=1` means
- why `x * col_scale` works (broadcasting)

---

## Next lesson

Continue to `04-pandas-essentials.md`.
