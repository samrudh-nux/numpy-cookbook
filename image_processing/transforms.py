"""
transforms.py

Basic image transforms using NumPy array operations.
"""

import numpy as np


def flip_horizontal(image):
    # Horizontal Flip
    c = np.fliplr(image)

    print(c)
    return c


def flip_vertical(image):
    # Vertical Flip
    c = np.flipud(image)

    print(c)
    return c


def rotate_90(image):
    # Rotate 90 degrees
    c = np.rot90(image)

    print(c)
    return c


if __name__ == "__main__":
    image = np.arange(9).reshape(3, 3)

    print("Horizontal Flip")
    flip_horizontal(image)

    print("\nVertical Flip")
    flip_vertical(image)

    print("\nRotate 90")
    rotate_90(image)
