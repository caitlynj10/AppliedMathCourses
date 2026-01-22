# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:50:20 2024

@author: caitlyn jones
"""

import numpy as np
import matplotlib.pyplot as plt
import sklearn.cluster as sk

fancy = np.load("fancy.npy")

k_values = [1,2,3,4,5,6,7,8,9,10]
fancy_obj_val = []

for k in k_values:
    fc = sk.KMeans(n_clusters = k).fit(fancy)
    fancy_obj_val.append(fc.inertia_)
    
    
plt.figure()
plt.plot(k_values, fancy_obj_val, marker = "o")
plt.title("K-Means Objective Values")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Objective Value")
plt.xticks(k_values)
plt.show()

'''
blobs = np.load("blobs.npy")
circles = np.load("circles.npy")

  circle_cluster = sk.KMeans(n_clusters = 2).fit(circles)

blob_center = blob_cluster.cluster_centers_
circle_center = circle_cluster.cluster_centers_

fig, subplt = plt.subplots(1,2)

subplt[0].scatter(blobs[:, 0], blobs[:, 1], c = blob_cluster.labels_, s = 20, marker = "x")
subplt[0].scatter(blob_center[:, 0], blob_center[:, 1], c = "red", s = 100, marker = "x", label = "Centroids")
subplt[0].set_title("Blobs Dataset")
subplt[0].legend()

subplt[1].scatter(circles[:, 0], circles[:, 1], c = circle_cluster.labels_, s = 20, marker = "x")
subplt[1].scatter(circle_center[:, 0], circle_center[:, 1], c = "red", s = 100, marker = "x", label = "Centroids")
subplt[1].set_title("Circles Dataset")
subplt[1].legend()

plt.tight_layout()
plt.show()
'''
