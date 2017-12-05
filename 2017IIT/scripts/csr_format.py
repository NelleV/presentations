from scipy import sparse
import numpy as np

X = np.random.randn(5, 5)
X[X < 0.5] = 0
print(X)

from scipy import sparse

X_sparse = sparse.csr_matrix(X)

