"""
vectorization.py

Compares plain Python loops vs NumPy vectorized operations.
"""

import time
import numpy as np


def loop_sum(n=1_000_000):
    # Python loop sum
    start = time.time()
    total = 0
    for i in range(n):
        total += i
    elapsed = time.time() - start

    print(f"Loop sum: {total} in {elapsed:.5f}s")
    return elapsed


def vectorized_sum(n=1_000_000):
    # NumPy vectorized sum
    start = time.time()
    total = np.sum(np.arange(n))
    elapsed = time.time() - start

    print(f"Vectorized sum: {total} in {elapsed:.5f}s")
    return elapsed


if __name__ == "__main__":
    loop_sum()
    vectorized_sum()
