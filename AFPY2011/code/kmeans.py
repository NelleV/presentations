import numpy as np
from matplotlib import pyplot as plt

from sklearn.cluster.k_means_ import KMeans
from sklearn.datasets.samples_generator import make_blobs

np.random.seed(0)

batch_size = 45
centers = [[1, 1], [-1, -1], [1, -1]]
n_clusters = len(centers)
X, labels_true = make_blobs(n_samples=1000, centers=centers, cluster_std=0.4)

# Draw randoms
indxs = np.arange(1000)
np.random.shuffle(indxs)
centroids = X[indxs[:3]]

k_means = KMeans(k=3, max_iter=1, init=centroids)
k_means.fit(X)
k_means_labels1 = k_means.labels_
k_means_cluster_centers1 = k_means.cluster_centers_

k_means = KMeans(k=3, max_iter=2, init=centroids)
k_means.fit(X)
k_means_labels2 = k_means.labels_
k_means_cluster_centers2 = k_means.cluster_centers_

k_means = KMeans(k=3, max_iter=3, init=centroids)
k_means.fit(X)
k_means_labels3 = k_means.labels_
k_means_cluster_centers3 = k_means.cluster_centers_

k_means = KMeans(k=3, max_iter=4, init=centroids)
k_means.fit(X)
k_means_labels4 = k_means.labels_
k_means_cluster_centers4 = k_means.cluster_centers_

k_means = KMeans(k=3, max_iter=5, init=centroids)
k_means.fit(X)
k_means_labels5 = k_means.labels_
k_means_cluster_centers5 = k_means.cluster_centers_

k_means = KMeans(k=3, max_iter=6, init=centroids)
k_means.fit(X)
k_means_labels6 = k_means.labels_
k_means_cluster_centers6 = k_means.cluster_centers_

colors = ['#4EACC5', '#FF9C34', '#4E9A06']
fig = plt.figure(0)
ax = fig.add_subplot(1, 1, 1)
ax.plot(X[:, 0], X[:, 1], ' ', marker='.',
        markerfacecolor='#bbbbbb',
        markeredgecolor='#111111')

ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
fig.savefig('figure_0.svg')

fig = plt.figure(1)
ax = fig.add_subplot(1, 1, 1)
ax.plot(X[:, 0], X[:, 1], ' ', marker='.',
        markerfacecolor='#bbbbbb',
        markeredgecolor='#111111')
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

for i in range(3):
    ax.plot(centroids[i, 0], centroids[i, 1], colors[i],
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)

fig.savefig('figure_1.svg')


fig = plt.figure(2)
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels1 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(centroids[i, 0], centroids[i, 1], ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)

fig.savefig('figure_2.svg')


fig = plt.figure(3)
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels1 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(k_means_cluster_centers1[i, 0], k_means_cluster_centers1[i, 1],
            ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)

fig.savefig('figure_3.svg')

fig = plt.figure(4)
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels2 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(k_means_cluster_centers1[i, 0], k_means_cluster_centers1[i, 1],
            ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)

fig.savefig('figure_4.svg')

fig = plt.figure(5)
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels2 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(k_means_cluster_centers2[i, 0], k_means_cluster_centers2[i, 1],
            ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)

fig.savefig('figure_5.svg')

fig = plt.figure(6)
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels3 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(k_means_cluster_centers2[i, 0], k_means_cluster_centers2[i, 1],
            ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)

fig.savefig('figure_6.svg')


fig = plt.figure(7)
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels3 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(k_means_cluster_centers3[i, 0], k_means_cluster_centers3[i, 1],
            ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)

fig.savefig('figure_7.svg')

fig = plt.figure(8)
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels4 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(k_means_cluster_centers3[i, 0], k_means_cluster_centers3[i, 1],
            ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)

fig.savefig('figure_8.svg')

fig = plt.figure(10)

ax = fig.add_subplot(2, 2, 1)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels1 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(k_means_cluster_centers1[i, 0], k_means_cluster_centers1[i, 1],
            ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)

ax = fig.add_subplot(2, 2, 2)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels2 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(k_means_cluster_centers2[i, 0], k_means_cluster_centers2[i, 1],
            ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)


ax = fig.add_subplot(2, 2, 3)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels3 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(k_means_cluster_centers3[i, 0], k_means_cluster_centers3[i, 1],
            ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)



ax = fig.add_subplot(2, 2, 4)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

colors = ['#4EACC5', '#FF9C34', '#4E9A06']

for i in range(3):
    my_members = k_means_labels4 == i
    ax.plot(X[my_members, 0], X[my_members, 1], ' ', marker='.',
        markerfacecolor=colors[i],
        markeredgecolor='k')

for i in range(3):
    ax.plot(k_means_cluster_centers4[i, 0], k_means_cluster_centers4[i, 1],
            ' ',
            marker='o',
            markerfacecolor=colors[i],
            markeredgecolor='k', markersize=6)

fig.savefig('figure_10.svg')
