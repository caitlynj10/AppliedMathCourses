# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 12:20:12 2024

@author: caitlyn jones
"""
import numpy as np

A = np.array([[1.,2.],[0.,1.],[1.,0.]])

print("")

Q_complete, R_complete = np.linalg.qr(A, mode = "complete")
print("Q complete is \n", Q_complete)
print("R complete is \n", R_complete)

print("")

Q_reduced,R_reduced = np.linalg.qr(A, mode = "reduced")
print("Q reduced is \n", Q_reduced)
print("R reduced is \n", R_reduced)

print("")

Q_complete_transpose = np.transpose(Q_complete)
print("The transpose of Q complete is \n", Q_complete_transpose)
print("Checking orthogonality of Q complete: \n", np.matmul(Q_complete_transpose,Q_complete))

print("")


Q_reduced_transpose = np.transpose(Q_reduced)
print("The transpose of Q reduced is \n", Q_reduced_transpose)
print("Checking orthogonality of Q complete: \n", np.matmul(Q_reduced_transpose,Q_reduced))