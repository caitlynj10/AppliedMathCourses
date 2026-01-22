# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:29:56 2024

@author: caitlyn jones
"""

import numpy as np
import matplotlib.pyplot as plt

name_matrix = np.loadtxt("cjones_name.txt")
_, svd, _ = np.linalg.svd(name_matrix, full_matrices=False)
name_rank = np.linalg.matrix_rank(name_matrix)


'''
the following lines are plotting the svd values
on a regular scale
'''

plt.plot(svd, "o-", label="Singular Values")
plt.title("Singular Values (regular scale)")
plt.xlabel("Index")
plt.ylabel("Singular Value")
plt.show


'''
the following lines are plotting the svd values
on a log scale
'''

plt.plot(svd, "o-", label="Singular Values")
plt.title("Singular Values (log scale)")
plt.xlabel("Index")
plt.ylabel("Singular Value")
plt.xscale("log")
plt.yscale("log")
plt.show()


'''
the following lines will construct
low rank approximations for name_matrix
'''
U,S,V = np.linalg.svd(name_matrix, full_matrices=False)

#rank1
S_one = np.diag(S[:1])
U_one = U[:, :1]
V_one = V[:1, :]
rank_one = U_one @ S_one @ V_one

#rank2
S_two = np.diag(S[:2])
U_two = U[:, :2]
V_two = V[:2, :]
rank_two = U_two @ S_two @ V_two

#rank3
S_three = np.diag(S[:3])
U_three = U[:, :3]
V_three = V[:3, :]
rank_three = U_three @ S_three @ V_three

#rank4
S_four = np.diag(S[:4])
U_four = U[:, :4]
V_four = V[:4, :]
rank_four = U_four @ S_four @ V_four


'''
the following lines will construct the
images for the low-rank approximations
'''

plt.imshow(rank_one, cmap = "grey")
plt.title("Rank-1 Approximation")

plt.imshow(rank_two, cmap = "grey")
plt.title("Rank-2 Approximation")

plt.imshow(rank_three, cmap = "grey")
plt.title("Rank-3 Approximation")

plt.imshow(rank_four, cmap = "grey")
plt.title("Rank-4 Approximation")






