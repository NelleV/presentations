import os
import numpy as np
from scipy.spatial import distance
from scipy import ndimage

import matplotlib.pyplot as plt

try:
    os.makedirs("images")
except OSError:
    pass

###############################################################################
# Distance génomique
n = 20
X = np.arange(n)[:, np.newaxis]
genomic_distances = distance.squareform(distance.pdist(X, metric="cityblock"))

fig, ax = plt.subplots()
ax.matshow(genomic_distances, cmap="RdBu")
ax.set_xticks([])
ax.set_yticks([])
fig.savefig("images/plot_genomic_distances.pdf")


###############################################################################
# Signal
random_seed = 42
random_state = np.random.RandomState(seed=random_seed)
mask = random_state.rand(n, n)
mask = ~np.triu((mask > 0.7))
signal = 2 * random_state.randn(n, n)
signal[mask] = 0
signal = np.triu(ndimage.gaussian_filter(signal, 1))
signal = signal + signal.T

fig, ax = plt.subplots()
ax.matshow(signal, cmap="RdBu_r")
ax.set_yticks([])
ax.set_xticks([])
fig.savefig("images/plot_signal.pdf")

###############################################################################
# Bias
bias = ndimage.gaussian_filter(1 + random_state.randn(n) / 2, 1)
fig, ax = plt.subplots()
ax.matshow(bias[:, np.newaxis] * bias[np.newaxis, :], cmap="RdBu_r")
ax.set_yticks([])
ax.set_xticks([])
fig.savefig("images/plot_bias.pdf")

###############################################################################
# Fréquence d'interaction
counts = bias * (1 + signal) * (100 * (genomic_distances)**(-1))
counts[np.isinf(counts)] = 0

counts[np.diag_indices_from(counts)] = counts.max()
counts -= counts.min()

fig, ax = plt.subplots()
ax.matshow(np.log(counts+1), cmap="RdBu_r")
ax.set_yticks([])
ax.set_xticks([])
fig.savefig("images/plot_counts.pdf")
