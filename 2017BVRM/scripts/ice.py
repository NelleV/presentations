import numpy as np


def ice(counts, max_iter=1000):
    tolerance = 1e-3
    for i in range(max_iter):
        rows = counts.sum(axis=0)
        counts /= rows[np.newaxis]

        cols = counts.sum(axis=1)
        counts.T /= cols[:, np.newaxis]
        err = ((counts - counts.sum(axis=0))**2).sum()
        if err < tolerance:
            break
    return counts
