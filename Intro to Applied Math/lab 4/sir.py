# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:19:45 2024

@author: caitlyn jones
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

beta = 1.0/1000 #Infection rate
gamma = 1.0/(24*14) #Recovery rate


'''
The function below defines the differential equations
for the SIR model
'''
def deriv (x,t):
    ifc = beta *x[0]* x[1] #Rate of new infections based in the population of susceptible and infected people
    rec = gamma* x[1] #Rate of recoveries based on the population of infected people
    return np.array ([-ifc, ifc - rec, rec]) #Returns the rate of change for S, I, and R


time = np.linspace (0, 2000, 1000) #Variable to track time, 2000 hours
xinit = np.array ([100 ,1 ,0]) #Initilizing variables for S, I, and R
x = odeint ( deriv , xinit , time ) #Integrates the equations for S, I, R over time

plt.figure () #Creates a new figure 
p0, = plt.plot (time, x[: ,0]) #Defines and plots the values S(t)
p1, = plt.plot (time, x[: ,1]) #Defines and plots the values I(t)
p2, = plt.plot (time, x[: ,2]) #Defines and plots the values R(t)
plt.legend ([ p0 , p1 , p2 ] ,["S(t)","I(t)","R(t)"]) #Labels the graphs S(t), I(t), R(t)
plt.xlabel ("t ( Hours )") #Labels the x-axis in hours
plt.ylabel ("Population") #Labels the y-axis as population count
plt.show () #Displays the plot

'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

beta = (1.0/1000)*(168)
gamma = 1.0/2


def deriv (x,t):
    ifc = beta *x [0]* x [1]
    rec = gamma * x [1]
    return np.array ([-ifc, ifc - rec, rec])

time = np.linspace (0, 2000/168, 1000)
xinit = np.array ([100 ,1 ,0])
x = odeint ( deriv , xinit , time )

plt.figure ()
p0, = plt.plot (time, x[: ,0])
p1, = plt.plot (time, x[: ,1])
p2, = plt.plot (time, x[: ,2])
plt.legend ([ p0 , p1 , p2 ] ,["S(t)","I(t)","R(t)"])
plt.xlabel ("t ( Weeks )")
plt.ylabel ("Population")
plt.show ()
'''