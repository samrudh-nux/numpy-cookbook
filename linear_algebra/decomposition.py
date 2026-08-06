"""
decomposition.py

LU and QR matrix decompositions using NumPy/SciPy.
"""

import numpy as np


def lu_decomposition(a):
    # LU Decomposition (via Gaussian elimination, no pivoting library needed)
    from scipy.linalg import lu

    p, l, u = lu(a)

    print("P:\n", p)
    print("L:\n", l)
    print("U:\n", u)
    return p, l, u


def qr_decomposition(a):
    # QR Decomposition
    q, r = np.linalg.qr(a)

    print("Q:\n", q)
    print("R:\n", r)
    return q, r


if __name__ == "__main__":
    a = np.array([[4, 3],
                  [6, 3]], dtype=float)

    print("\nLU Decomposition")
    lu_decomposition(a)

    print("\nQR Decomposition")
    qr_decomposition(a)
