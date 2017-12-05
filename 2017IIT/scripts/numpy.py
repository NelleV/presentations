import numpy as np

# Create two random arrays of shape 100, 100
A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

# We can do many operations on those:
AB_sum = A + B
AB_element_wise_product = A * B
AB_dot_product = np.dot(A, B)
A_mean = A.mean()
