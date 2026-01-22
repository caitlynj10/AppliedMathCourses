# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:44:52 2024

@author: caitlyn jones
"""

import numpy as np
import matplotlib.pyplot as plt


#matrix = np.loadtxt('tfai_name.txt')
#plt.spy(matrix)


rows = 16
cols = 8 * 7

matrix = np.zeros((rows, cols), dtype=int)
matrix[2:14, 2] = 1 
matrix[2, 2:7] = 1  
matrix[13, 2:7] = 1 
matrix[2:14, 10] = 1
matrix[2:14, 14] = 1
matrix[2, 10:15] = 1
matrix[8, 10:15] = 1
matrix[2:14, 18] = 1
matrix[2, 26:31] = 1
matrix[2:14, 28] = 1
matrix[2:14, 34] = 1
matrix[13, 34:39] = 1
matrix[2:8, 42] = 1
matrix[2:8, 46] = 1
matrix[8:14, 44] = 1
matrix[2:14, 48] = 1
matrix[2:14, 55] = 1
for i in range(7):
    matrix[3 + i, 49 + i] = 1
    



plt.spy(matrix, markersize=5)
plt.show()
matrix = np.savetxt('cjones_name.txt', matrix, fmt = "%d")
    
    

