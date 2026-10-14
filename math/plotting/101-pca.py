#!/usr/bin/env python3
"""Advanced task 101: 3D PCA plot of the Iris dataset (from pca.npz).

Reduces the 4 features of each flower to 3 principal components using SVD
and draws them in a 3D scatter plot, colored by species label.
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Load the feature matrix and species labels
lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

# Center the data: PCA requires zero-mean features
data_means = np.mean(data, axis=0)
norm_data = data - data_means
# SVD: rows of Vh are the principal axes, sorted by variance
_, _, Vh = np.linalg.svd(norm_data)
# Project onto the first 3 principal axes
pca_data = np.matmul(norm_data, Vh[:3].T)

# 3D scatter, one color per species
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
    pca_data[:, 0],
    pca_data[:, 1],
    pca_data[:, 2],
    c=labels,
    cmap='plasma'
)

ax.set_title('PCA of Iris Dataset')
ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')

plt.show()
