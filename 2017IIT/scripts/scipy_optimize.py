
import numpy as np
from scipy import optimize

def f(x):
    return -np.exp(-(x - 0.7)**2)
    
result = optimize.minimize_scalar(f)
result.success # check if solver was successful

