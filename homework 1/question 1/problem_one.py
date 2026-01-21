# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 09:07:23 2024

@author: caitlyn jones
"""

import numpy as np
import math
import matplotlib.pyplot as plt


p_values = np.linspace(0.5, 1, 51)
p = np.array(p_values)


def P(N,m):
    numerator = math.factorial(N)
    x = N-m
    parent = math.factorial(x)
    denom = math.factorial(m)
    
    fraction = numerator / (parent*denom)
    
    return fraction * (p**m) * (1-p)**(N-m)

S1 = np.array(P(1,1))
S3 = np.array(P(3,3) + P(3,2))

plt.xlabel("Probability of p")
plt.ylabel("S(p,N)")
plt.title("S(p,1) and S(p,3) vs. p")
plt.legend()
plt.plot(p,S1, label = "S(p,1)", color = "blue")
plt.plot(p,S3, label = "S(p,3)", color = "green")
plt.show()


