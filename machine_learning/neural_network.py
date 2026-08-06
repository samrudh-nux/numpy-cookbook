"""
neural_network.py

A minimal feed-forward neural network (single hidden layer) built with
NumPy only, trained with basic backpropagation.
"""

import numpy as np


def sigmoid(x):
    # Sigmoid activation
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    # Derivative of sigmoid
    return x * (1 - x)


def train_neural_network(x, y, hidden_size=4, epochs=1000, lr=0.1):
    rng = np.random.default_rng(0)
    input_size = x.shape[1]
    output_size = y.shape[1]

    w1 = rng.standard_normal((input_size, hidden_size))
    w2 = rng.standard_normal((hidden_size, output_size))

    for epoch in range(epochs):
        # Forward pass
        hidden = sigmoid(x @ w1)
        output = sigmoid(hidden @ w2)

        # Backpropagation
        error = y - output
        d_output = error * sigmoid_derivative(output)
        d_hidden = (d_output @ w2.T) * sigmoid_derivative(hidden)

        w2 += hidden.T @ d_output * lr
        w1 += x.T @ d_hidden * lr

    print("Final output:\n", output)
    return w1, w2


if __name__ == "__main__":
    # XOR dataset
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    y = np.array([[0], [1], [1], [0]], dtype=float)

    train_neural_network(x, y)
