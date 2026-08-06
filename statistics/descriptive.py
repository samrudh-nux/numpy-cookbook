"""


Descriptive statistics helpers built on NumPy.
"""

import numpy as np


def summary_stats(a):
    # Mean, Median, Std, Variance
    mean = np.mean(a)
    median = np.median(a)
    std = np.std(a)
    var = np.var(a)

    print(f"Mean: {mean}, Median: {median}, Std: {std}, Var: {var}")
    return mean, median, std, var


if __name__ == "__main__":
    a = np.array([2, 4, 4, 4, 5, 5, 7, 9])

    summary_stats(a)
