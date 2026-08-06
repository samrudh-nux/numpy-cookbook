"""


Basic probability distribution sampling with NumPy.
"""

import numpy as np


def normal_distribution(mean=0, std=1, size=5):
    # Normal (Gaussian) Distribution
    a = np.random.normal(mean, std, size)

    print(a)
    return a


def uniform_distribution(low=0, high=1, size=5):
    # Uniform Distribution
    a = np.random.uniform(low, high, size)

    print(a)
    return a


if __name__ == "__main__":
    print("Normal Distribution")
    normal_distribution()

    print("\nUniform Distribution")
    uniform_distribution()
