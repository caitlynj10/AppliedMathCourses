# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 18:04:42 2024

@author: caitlyn jones
"""

import numpy as np
import matplotlib.pyplot as plt

'''
relatedness = np.linspace(0,1,100)
bc_ratio = relatedness #proportional relationship

plt.figure()
plt.plot(relatedness, bc_ratio, linewidth=4, label = "B/C = r")
plt.xlabel("Genetic Relatedness (r)")
plt.ylabel("Benefit to Cost Ratio (B/C)")
plt.title("Relationship Between Relatedness and Benefit-to-Cost Ratio")

plt.legend()
plt.show()
'''
relatedness = np.linspace(0,1,100)
fighting = -relatedness #proportional relationship

plt.figure()
plt.plot(relatedness, fighting, linewidth=4)
plt.xlabel("Genetic Relatedness (r)")
plt.ylabel("Likelihood of Conflict")
plt.title("Relationship Between Relatedness and Likelihood of Conflict")
plt.show()

