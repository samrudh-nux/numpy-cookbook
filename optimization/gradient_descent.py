"""

Simple gradient descent implementation to minimize f(x) = x^2.
"""

import numpy as np


def gradient_descent(lr=0.1, steps=20, start=10.0):
    # Gradient Descent on f(x) = x^2, gradient = 2x
    x = start

    for i in range(steps):
        grad = 2 * x
        x = x - lr * grad

    print(f"Minimum found near x = {x}")
    return x


if __name__ == "__main__":
    gradient_descent()
