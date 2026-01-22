# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:25:10 2024

@author: caitlyn jones
"""

import numpy as np
import pandas as pd
from myqrsteps_skeleton import myqrsteps
import matplotlib.pyplot as plt



data = pd.read_csv("sphinxmoth.txt", sep=" ", header = None)

R = np.array(data[1])
b = np.array(np.log10(R))


'''
The following code is transpose the
 data from W into a design matrix A
'''

W = np.array(data[0])
W_log = np.array(np.log10(W))
ones = np.ones((W_log.shape[0], 1))
data_column = W_log.reshape(-1, 1)
A = np.hstack((ones, data_column))


Q_complete,R_complete = myqrsteps(A)

'''
the following lines are computing the 
right side of the least squares equation
'''

Q_T = np.transpose(Q_complete)
Q_T_b = np.matmul(Q_T,b)

'''
first output is the answer
'''
x,_,_,_  = np.linalg.lstsq(R_complete,Q_T_b, rcond=None)

'''
the following lines are initializing
 the values for a and b
'''
log_b, a = x
b = 10**(log_b)

'''
the following line is computing the equation
that depicts the relationship between R and W
via least squares fit (lsf)
'''

R_lsf = b * (W**a)


'''
the following lines are graphing the values
from the original data table and the values 
from computing the relationship R=bW^a
'''

plt.scatter(W,R, label="Original Data", color = "blue")
plt.plot(W, R_lsf, label="Least Square Fit: R = bW^a", color = "red")
plt.xlabel("Weight of Larvae (g)")
plt.ylabel("Oxygen Consumption of Larvae (mL/hr)")
plt.title("Weight of Larvae vs Oxygen Consumption of Larvae")
plt.xscale("log")
plt.yscale("log")
plt.legend()
plt.show()

