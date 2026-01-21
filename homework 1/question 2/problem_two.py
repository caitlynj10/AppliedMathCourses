# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 11:31:37 2024

@author: caitlyn jones
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


def my_factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
                
    return factorial

print("")

print("my_factorial(10) = ", my_factorial(10))
print("math.factorial(10) = ", math.factorial(10))


def my_binomial(p,N,m):
    
    numerator = my_factorial(N)
    x = N-m
    coefficient = (numerator)/((my_factorial(x))*(my_factorial(m)))
    P_N_m = coefficient * ((p**m)*(1-p)**x)
    
    return P_N_m



p = 1/2
N = 100
m_values = np.arange(0, N+1)


binomial_values = [my_binomial(p,N,m) for m in m_values]


plt.plot(m_values, binomial_values, label= "P(N,m)", color = "blue")
plt.xlabel("m")
plt.ylabel("P(N,m)")
plt.title("Binomial Distribution for N and p")
plt.legend()
plt.show()



plt.plot(m_values, binom.pmf(m_values,N,p), label= "P(N,m)", color = "blue")
plt.xlabel("m")
plt.ylabel("P(N,m)")
plt.title("Binomial Distribution for N and p")
plt.legend()
plt.show()


   

   
   
