"""
============================================
Segmenting camera into region using mean shift
============================================

"""

# Author: Nelle Varoquaux <nelle.varoquaux@gmail.com> 
# License: BSD

import numpy as np
import scipy as sp

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster.mean_shift_ import MeanShift, estimate_bandwidth
from sklearn.externals.joblib import Memory

from skimage.data import camera

mem = Memory(cachedir='.')

def calculate_cluster(camera, camera_mat, quantile):
    bandwidth = estimate_bandwidth(camera_mat, quantile=quantile, n_samples=500)
    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(camera_mat)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    camera_clustered = camera.copy()
    camera_clustered_value = camera.copy()
    camera_mat_clustered = camera_mat.copy()
    camera_mat_clustered_value = camera_mat.copy()

    for point, pointb, value in zip(camera_mat_clustered, camera_mat_clustered_value, labels):
        point[2] = value
        pointb[2] = cluster_centers[value, 2]
        camera_clustered[point[0], point[1]] = value
        camera_clustered_value[point[0], point[1]] = cluster_centers[value, 2]

    image = {"image": camera_clustered_value,
             "quantile": quantile,
             "clusters": n_clusters_}
    return image



camera = camera()
# My computer is crap - I don't have enough ram to compute the clustering on
# the whole camera image. Let's downsample the image by a factor of 4
#camera = camera[::2, ::2] + camera[1::2, ::2] + camera[::2, 1::2] + camera[1::2, 1::2]
#camera = camera[::2, ::2] + camera[1::2, ::2] + camera[::2, 1::2] + camera[1::2, 1::2]

# camera as an image is useless. Let's create a 512*3 matrix (x, y, value)
camera_mat = []
for x, i in enumerate(camera):
    for y, j in enumerate(i):
        camera_mat.append([x, y, j])

camera_mat = np.array(camera_mat)

quantile_range = np.linspace(0.004, 0.02, 11)
images = []
images.append({"image": camera.copy(), "quantile": 0, "clusters": 0})

for i, quantile in enumerate(quantile_range):
    print "%d calculating for quantile %f" % (i, quantile)
    image = mem.cache(calculate_cluster)(camera, camera_mat, quantile)
    images.append(image)

fig = plt.figure()

for i, image in enumerate(images):
    ax = fig.add_subplot(4, 3, i)
    ax.set_axis_off()
    ax.set_title('clusters: %d - quantile %f' % (image['clusters'],
                                                 image['quantile']))
    ax.matshow(image['image'])


#fig = plt.figure(1)
#ax = fig.add_subplot(111, projection='3d')
#
#ax.plot(camera_mat[:, 0], camera_mat[:, 1], camera_mat[:, 2], 'w',
#markerfacecolor='#111111', marker='.')
#
#plt.show()
#
# Let's display some of the results






