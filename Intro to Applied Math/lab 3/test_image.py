# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt


a = np.zeros((10,10))
a[:,:] = 0.0

for j in range (2,4):
    for i in range (6,8):
        a[j, i] = 1.0


def makesquare(image, upper_left, size, shade):
    row, col = upper_left
    image[row:row+size, col:col+size] = shade
    
    return image

ax = np.zeros((10,10))
ax_square = makesquare(ax,(2,6),2,1.0)
plt.imshow(ax_square, cmap = plt.cm.gray , vmin = 0.0 , vmax = 1.0)
plt.show ()

#plt.imshow(a, cmap = plt.cm.gray , vmin = 0.0 , vmax = 1.0)


