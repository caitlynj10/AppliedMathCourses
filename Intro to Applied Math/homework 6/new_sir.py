# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:20:13 2024

@author: caitlyn jones
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def replicator_dynamics(p, q, A):
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    
    payoff1 = p*a + q*b
    payoff2 = p*c + q*d
    
    average_payoff = p*payoff1 + q*payoff2
    
    dPdT = p*(payoff1-average_payoff)
    dQdT = q*(payoff2-average_payoff)
    
    return np.array([dPdT, dQdT])

A_chicken = np.array([[-1, 1],
                     [0, 1/2]])

chicken_game = replicator_dynamics(1,0,A_chicken)
print(chicken_game)