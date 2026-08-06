"""

Eigenvalues and eigenvectors.
"""

import numpy as np


def eigen_decomposition(a):
    # Eigenvalues and Eigenvectors
    values, vectors = np.linalg.eig(a)

    print("Eigenvalues:\n", values)
    print("Eigenvectors:\n", vectors)
    return values, vectors


if __name__ == "__main__":
    a = np.array([[2, 0],
                  [0, 3]])

    eigen_decomposition(a)
