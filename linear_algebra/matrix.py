"""
matrix.py

15 core NumPy matrix operations, each written as a short, self-contained
function with the same simple style: short code + a comment.
"""

import numpy as np


# 1. Matrix Creation
def matrix_creation():
    # Matrix Creation
    a = np.array([[1, 2],
                  [3, 4]])

    print(a)
    return a


# 2. Matrix Addition
def matrix_addition():
    # Matrix Addition
    a = np.array([[1, 2],
                  [3, 4]])

    b = np.array([[5, 6],
                  [7, 8]])

    c = a + b

    print(c)
    return c


# 3. Matrix Subtraction
def matrix_subtraction():
    # Matrix Subtraction
    a = np.array([[1, 2],
                  [3, 4]])

    b = np.array([[5, 6],
                  [7, 8]])

    c = a - b

    print(c)
    return c


# 4. Matrix Multiplication
def matrix_multiplication():
    # Matrix Multiplication
    a = np.array([[1, 2],
                  [3, 4]])

    b = np.array([[5, 6],
                  [7, 8]])

    c = a @ b

    print(c)
    return c


# 5. Element-wise Multiplication (Hadamard Product)
def elementwise_multiplication():
    # Element-wise Multiplication (Hadamard Product)
    a = np.array([[1, 2],
                  [3, 4]])

    b = np.array([[5, 6],
                  [7, 8]])

    c = a * b

    print(c)
    return c


# 6. Scalar Operations
def scalar_multiplication():
    # Scalar Multiplication
    a = np.array([[1, 2],
                  [3, 4]])

    scalar = 5

    c = a * scalar

    print(c)
    return c


# 7. Matrix Transpose
def matrix_transpose():
    # Matrix Transpose
    a = np.array([[1, 2],
                  [3, 4]])

    c = a.T

    print(c)
    return c


# 8. Matrix Reshape
def matrix_reshape():
    # Matrix Reshape
    a = np.arange(12)

    c = a.reshape(3, 4)

    print(c)
    return c


# 9. Matrix Flatten
def matrix_flatten():
    # Matrix Flatten
    a = np.array([[1, 2],
                  [3, 4]])

    c = a.flatten()

    print(c)
    return c


# 10. Matrix Concatenation
def matrix_concatenation():
    # Matrix Concatenation
    a = np.array([[1, 2],
                  [3, 4]])

    b = np.array([[5, 6],
                  [7, 8]])

    c = np.concatenate((a, b), axis=0)

    print(c)
    return c


# 11. Matrix Splitting
def matrix_splitting():
    # Matrix Splitting
    a = np.arange(16).reshape(4, 4)

    c = np.vsplit(a, 2)

    print(c)
    return c


# 12. Identity Matrix
def identity_matrix():
    # Identity Matrix
    a = np.eye(4)

    print(a)
    return a


# 13. Zero Matrix
def zero_matrix():
    # Zero Matrix
    a = np.zeros((3, 4))

    print(a)
    return a


# 14. Ones Matrix
def ones_matrix():
    # Ones Matrix
    a = np.ones((3, 4))

    print(a)
    return a


# 15. Random Matrix
def random_matrix():
    # Random Matrix
    a = np.random.rand(3, 3)

    print(a)
    return a


if __name__ == "__main__":
    print("\n1. Matrix Creation")
    matrix_creation()

    print("\n2. Matrix Addition")
    matrix_addition()

    print("\n3. Matrix Subtraction")
    matrix_subtraction()

    print("\n4. Matrix Multiplication")
    matrix_multiplication()

    print("\n5. Element-wise Multiplication (Hadamard Product)")
    elementwise_multiplication()

    print("\n6. Scalar Operations")
    scalar_multiplication()

    print("\n7. Matrix Transpose")
    matrix_transpose()

    print("\n8. Matrix Reshape")
    matrix_reshape()

    print("\n9. Matrix Flatten")
    matrix_flatten()

    print("\n10. Matrix Concatenation")
    matrix_concatenation()

    print("\n11. Matrix Splitting")
    matrix_splitting()

    print("\n12. Identity Matrix")
    identity_matrix()

    print("\n13. Zero Matrix")
    zero_matrix()

    print("\n14. Ones Matrix")
    ones_matrix()

    print("\n15. Random Matrix")
    random_matrix()
