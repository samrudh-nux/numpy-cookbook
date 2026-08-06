"""
test_matrix.py

Basic unit tests for numpylab.linear_algebra.matrix
"""

import numpy as np
from numpylab.linear_algebra import matrix


def test_matrix_addition():
    result = matrix.matrix_addition()
    expected = np.array([[6, 8], [10, 12]])
    assert np.array_equal(result, expected)


def test_matrix_multiplication():
    result = matrix.matrix_multiplication()
    expected = np.array([[19, 22], [43, 50]])
    assert np.array_equal(result, expected)


def test_identity_matrix():
    result = matrix.identity_matrix()
    assert np.array_equal(result, np.eye(4))
