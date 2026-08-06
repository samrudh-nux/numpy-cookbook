"""
pca.py

Principal Component Analysis (PCA) from scratch using NumPy.
"""

import numpy as np


def pca(x, n_components=1):
    # Center the data
    x_centered = x - np.mean(x, axis=0)

    # Covariance matrix
    cov = np.cov(x_centered, rowvar=False)

    # Eigenvalues / eigenvectors, sorted descending
    values, vectors = np.linalg.eigh(cov)
    order = np.argsort(values)[::-1]
    vectors = vectors[:, order]

    # Project onto top n components
    components = vectors[:, :n_components]
    transformed = x_centered @ components

    print("Transformed data:\n", transformed)
    return transformed


if __name__ == "__main__":
    x = np.array([[2.5, 2.4],
                  [0.5, 0.7],
                  [2.2, 2.9],
                  [1.9, 2.2],
                  [3.1, 3.0]])

    pca(x, n_components=1)
