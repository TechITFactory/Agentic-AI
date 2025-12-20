from __future__ import annotations

"""NumPy basics script for Section 02.

Run:
  python sections/02-python-for-ai/code/numpy_basics.py

This is intentionally a script (not a notebook) to reinforce production habits.
"""

import numpy as np


def main() -> int:
    print("=" * 70)
    print("NUMPY BASICS (ARRAYS, MASKING, BROADCASTING)")
    print("=" * 70)

    # 1) Arrays, shapes, dtypes
    a = np.array([1, 2, 3], dtype=np.int64)
    b = np.array([0.1, 0.2, 0.3], dtype=np.float64)
    print("\n1) Arrays")
    print("a:", a, "dtype=", a.dtype, "shape=", a.shape)
    print("b:", b, "dtype=", b.dtype, "shape=", b.shape)

    # 2) 2D arrays + reshape
    x = np.arange(12).reshape(3, 4)
    print("\n2) 2D arrays")
    print("x:\n", x)
    print("x.shape:", x.shape)

    # 3) Slicing
    print("\n3) Slicing")
    print("first row:", x[0])
    print("first column:", x[:, 0])
    print("submatrix rows 0..1, cols 1..2:\n", x[0:2, 1:3])

    # 4) Vectorized math
    print("\n4) Vectorized math")
    y = x * 2 + 1
    print("y = x*2 + 1:\n", y)

    # 5) Boolean masks
    print("\n5) Boolean masking")
    mask = x % 2 == 0
    print("mask (even):\n", mask)
    evens = x[mask]
    print("evens:", evens)

    # 6) Aggregations
    print("\n6) Aggregations")
    print("x.sum():", x.sum())
    print("x.mean():", x.mean())
    print("x.mean(axis=0) (per column):", x.mean(axis=0))
    print("x.mean(axis=1) (per row):", x.mean(axis=1))

    # 7) Broadcasting
    print("\n7) Broadcasting")
    col_scale = np.array([1.0, 10.0, 100.0, 1000.0])
    scaled = x * col_scale
    print("col_scale:", col_scale, "shape=", col_scale.shape)
    print("scaled = x * col_scale:\n", scaled)

    # 8) Dot product and matrix multiply
    print("\n8) Dot product / matmul")
    v = np.array([1.0, 2.0, 3.0, 4.0])
    print("v:", v)
    print("x[0] dot v:", x[0].dot(v))

    w = np.arange(8).reshape(4, 2)
    z = x @ w
    print("\nw (4x2):\n", w)
    print("z = x @ w (3x2):\n", z)

    print("\nDone. Next: Pandas essentials.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
