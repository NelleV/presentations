"""
==============================================
Baboon in 3D space
==============================================

"""

# Author: Nelle Varoquaux <nelle.varoquaux@gmail.com>
# License: BSD

import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster.k_means_ import KMeans
from sklearn.externals.joblib import Memory

from data import baboon
from cluster import data_reshape

mem = Memory(cachedir='.')

baboon = baboon(small=True).mean(axis=2)
baboon_mat = data_reshape(baboon)

fig = plt.figure(0)
ax = fig.add_subplot(1, 1, 1)

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

ax.plot(baboon_mat[:, 0], baboon_mat[:, 1], baboon_mat[:, 2],
        'w', marker='.')
