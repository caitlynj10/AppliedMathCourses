# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:39:05 2024

@author: caitlyn jones
"""

from skimage import data,io
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt


def denoise_image(image):
    a=io.imread(image, as_gray=True).astype("float64")
    a*=1/255.0


    (y,x) = a.shape
    b = np.copy(a)


    for j in range(1,y-1):
        for i in range(1, x-1):
            l = [a[j-1,i-1],a[j-1,i],a[j-1,i+1], 
                 a[j,i-1],a[j,i], a[j,i+1],
                 a[j+1,i-1],a[j+1,i], a[j+1,i+1]]
            b[j,i] = np.median(l)
            
    return b
        
denoised = denoise_image("audrey_lnoise.png")   
        
#io.imsave=("denoise.png",b)

plt.figure(figsize=(10, 5))

'''
plt.subplot(1, 2, 1)
plt.imshow(a, cmap='gray')
plt.title("Original Image")
plt.axis("off")
'''
plt.subplot(1, 2, 2)
plt.imshow(denoised, cmap='gray')
plt.title("Denoised Image")
plt.axis("off")

plt.show()