# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:39:39 2024

@author: caitlyn jones
"""

import numpy as np


A = np.array([[-2,0], [0,3]])

svds = np.linalg.svd(A)

print(svds)