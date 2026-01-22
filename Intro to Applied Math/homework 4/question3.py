# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:46:51 2024

@author: caitlyn jones
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

beta = 0.1
beta_2 = 0.05
beta_3 = 0.5
gamma = 20

def deriv(x,t):
    S, I, R, S_h, I_h, R_h = x
    dSdt = -S*(beta*I + beta_2*I_h)
    dIdt = S*(beta*I + beta_2*I_h) - gamma*I
    dRdt = gamma*I
    dShdt = -S_h*(beta_2*I + beta_3*I_h)
    dIhdt = S_h*(beta_2*I + beta_3*I_h) - gamma*I_h
    dRhdt = gamma*I_h
    return np.array([dSdt, dIdt, dRdt, dShdt, dIhdt, dRhdt])
    
    
time = np.linspace(0,1.2,100)
xinit = np.array([90,10,0,100,0,0])
x = odeint(deriv, xinit, time)

plt.figure ()
p0, = plt.plot (time, x[: ,0])
p1, = plt.plot (time, x[: ,1])
p2, = plt.plot (time, x[: ,2])
p3, = plt.plot (time, x[: ,3])
p4, = plt.plot (time, x[: ,4])
p5, = plt.plot (time, x[: ,5])
plt.legend ([ p0 , p1 , p2, p3, p4, p5 ] ,["S(t)","I(t)","R(t)", "S_h(t)", "I_h(t)", "R_h(t)"])
plt.xlabel ("Time")
plt.ylabel ("Population")
plt.show ()

'''
beta = 0.1
gamma = 20



def deriv (x,t):
    ifc = beta *x [0]* x [1]
    rec = gamma * x [1]
    return np.array ([-ifc, ifc - rec, rec])


time = np.linspace (0, 1.2, 100)
xinit = np.array ([90 ,10 ,0])
x = odeint ( deriv , xinit , time )

plt.figure ()
p0, = plt.plot (time, x[: ,0])
p1, = plt.plot (time, x[: ,1])
p2, = plt.plot (time, x[: ,2])
plt.legend ([ p0 , p1 , p2 ] ,["S(t)","I(t)","R(t)"])
plt.xlabel ("Time")
plt.ylabel ("Population")
plt.show ()
'''
