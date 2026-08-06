"""
kmeans.py

K-Means clustering implemented from scratch with NumPy.
"""

import numpy as np


def kmeans(x, k=2, iterations=10):
    # K-Means Clustering
    rng = np.random.default_rng(42)
    centroids = x[rng.choice(len(x), k, replace=False)]

    for _ in range(iterations):
        distances = np.linalg.norm(x[:, None] - centroids[None, :], axis=2)
        labels = np.argmin(distances, axis=1)

        for i in range(k):
            if np.any(labels == i):
                centroids[i] = x[labels == i].mean(axis=0)

    print("Centroids:\n", centroids)
    print("Labels:\n", labels)
    return centroids, labels


if __name__ == "__main__":
    x = np.array([[1, 2], [1, 4], [1, 0],
                  [10, 2], [10, 4], [10, 0]], dtype=float)

    kmeans(x, k=2)
