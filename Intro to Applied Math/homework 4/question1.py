# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:05:37 2024

@author: caitlyn jones
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

alpha = 1.5
beta = 0.5
gamma = 0.4
delta = 0.8


def deriv(x,t):
    R, F = x
    dRdt = alpha*R - beta*R*F
    dFdt = -gamma*F + delta*R*F
    return np.array([dRdt, dFdt]) 


time = np.linspace(0, 50, 100) 
xinit = np.array([0,5]) 
#xinit = np.array([10,5])
#xinit = np.array([10,0])
x = odeint(deriv, xinit, time ) 

plt.figure() 
p0, = plt.plot(time, x[:, 0]) 
p1, = plt.plot(time, x[:, 1]) 
plt.legend([p0, p1] ,["Rabbits: R(t)", "Foxes: F(t)"]) 
plt.xlabel("Time") 
plt.ylabel("Population") 
plt.show() 