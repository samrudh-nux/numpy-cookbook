"""
filters.py

Basic image filters implemented with NumPy convolution.
"""

import numpy as np


def convolve2d(image, kernel):
    # Simple 2D convolution (valid mode, no padding)
    kh, kw = kernel.shape
    ih, iw = image.shape
    oh, ow = ih - kh + 1, iw - kw + 1

    output = np.zeros((oh, ow))
    for i in range(oh):
        for j in range(ow):
            output[i, j] = np.sum(image[i:i+kh, j:j+kw] * kernel)

    return output


def blur_filter(image):
    # Simple 3x3 average blur kernel
    kernel = np.ones((3, 3)) / 9

    result = convolve2d(image, kernel)

    print(result)
    return result


def edge_detection(image):
    # Simple Sobel-like edge detection kernel (horizontal)
    kernel = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    result = convolve2d(image, kernel)

    print(result)
    return result


if __name__ == "__main__":
    image = np.random.randint(0, 255, (6, 6)).astype(float)

    print("Blur Filter")
    blur_filter(image)

    print("\nEdge Detection")
    edge_detection(image)
