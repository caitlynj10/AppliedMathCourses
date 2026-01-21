# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:11:16 2024

@author: caitlyn jones
"""

import numpy as np
import matplotlib.pyplot as plt
from test_image import makesquare




'''
ax_square = makesquare(ax,(20,20),160,1.0)
ax_square = makesquare(ax,(40,40),120,0.0)
ax_square = makesquare(ax,(60,60),80,1.0)
ax_square = makesquare(ax,(80,80),40,0.0)
'''





def makesquare_large(image, x, y):
    for i in range (1,10):
        if (i%2 == 1):
            image = makesquare(image,(x+10, x+10),y-20, 1.0)
        else: 
            image = makesquare(image, (x+10, x+10), y-20, 0.0)
            
        x += 10
        y -= 20
    
    return image
    

ax = np.zeros((200,200))
ax_square = makesquare_large(ax,0,200)        

plt.imshow(ax_square, cmap = plt.cm.gray , vmin = 0.0 , vmax = 1.0)
plt.show ()
  



