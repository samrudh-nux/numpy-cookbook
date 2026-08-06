"""
timings.py

Small reusable timing utility for benchmarking functions.
"""

import time


def time_function(func, *args, **kwargs):
    # Time any function call
    start = time.time()
    result = func(*args, **kwargs)
    elapsed = time.time() - start

    print(f"{func.__name__} took {elapsed:.5f}s")
    return result, elapsed


if __name__ == "__main__":
    def sample_task(n):
        return sum(range(n))

    time_function(sample_task, 1_000_000)
