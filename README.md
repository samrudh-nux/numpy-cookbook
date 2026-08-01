# NumPyLab

A hands-on NumPy playground covering linear algebra, statistics, optimization,
image processing, and machine learning — built from scratch on top of NumPy.

## Structure

```
NumPyLab/
│
├── numpylab/
│   ├── linear_algebra/     # matrix ops, decomposition, eigenvalues
│   ├── statistics/         # descriptive stats, probability
│   ├── optimization/       # gradient descent, newton's method
│   ├── image_processing/   # filters, transforms
│   ├── machine_learning/   # k-means, PCA, neural network
│   └── benchmarks/         # vectorization vs loops, timing utils
│
├── notebooks/              # exploratory Jupyter notebooks
├── tests/                  # unit tests
└── docs/                   # documentation
```

## Installation

```bash
git clone https://github.com/<your-username>/NumPyLab.git
cd NumPyLab
pip install -r requirements.txt
```

## Usage

```python
from numpylab.linear_algebra import matrix

matrix.matrix_creation()
```

Each module in `numpylab/` can also be run directly as a script:

```bash
python numpylab/linear_algebra/matrix.py
```

## Modules

| Module | Description |
|---|---|
| `linear_algebra/matrix.py` | 15 core matrix operations (creation, addition, multiplication, reshape, etc.) |
| `linear_algebra/decomposition.py` | LU and QR decomposition |
| `linear_algebra/eigen.py` | Eigenvalues and eigenvectors |
| `statistics/descriptive.py` | Mean, median, variance, std, etc. |
| `statistics/probability.py` | Basic probability distributions |
| `optimization/gradient_descent.py` | Gradient descent from scratch |
| `optimization/newton.py` | Newton's method for root finding |
| `image_processing/filters.py` | Blur, sharpen, edge detection filters |
| `image_processing/transforms.py` | Rotation, flipping, scaling |
| `machine_learning/kmeans.py` | K-means clustering |
| `machine_learning/pca.py` | Principal Component Analysis |
| `machine_learning/neural_network.py` | Minimal feed-forward neural network |
| `benchmarks/vectorization.py` | NumPy vectorization vs Python loops |
| `benchmarks/timings.py` | Timing utility helpers |

## License

MIT License — see [LICENSE](LICENSE).
