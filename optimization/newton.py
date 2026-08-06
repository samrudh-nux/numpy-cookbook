"""
newton.py

Newton's method for root finding.
"""

import numpy as np


def newtons_method(f, f_prime, x0=1.0, steps=20):
    # Newton's Method: x_(n+1) = x_n - f(x_n)/f'(x_n)
    x = x0

    for i in range(steps):
        x = x - f(x) / f_prime(x)

    print(f"Root found near x = {x}")
    return x


if __name__ == "__main__":
    # Example: find root of f(x) = x^2 - 2 (sqrt of 2)
    f = lambda x: x**2 - 2
    f_prime = lambda x: 2 * x

    newtons_method(f, f_prime, x0=1.0)
