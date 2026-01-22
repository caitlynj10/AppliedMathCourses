# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 12:14:08 2024

@author: caitlyn jones
"""
import numpy as np

i = 43
A_i = np.array([[2**(-i), 0],[0,1]])
x_exact = np.array([[1.], [1.]])

print(A_i)
print(x_exact)

print("")

A_cond_num = np.linalg.cond(A_i)
print("Condition number of A_43: ",A_cond_num)
print("")

b = np.matmul(A_i, x_exact)
print(b)
print("")

x_computed = np.linalg.solve(A_i,b)
print(x_computed)

print("")

def relative_error(x,y):
       
    rel_err = np.abs(x - y)/(np.abs(x))
    
    return rel_err


print(relative_error(x_exact, x_computed))

print("")
print("Problem 2: ")
print("")

theta = np.pi/5
R_theta = np.array(([[np.cos(theta), np.sin(theta)],[np.sin(theta)*-1, np.cos(theta)]]))
R_inv = np.linalg.inv(R_theta)
M_i = np.matmul(R_inv,A_i,R_theta)

print(M_i)
print(x_exact)

print("")

b = np.matmul(M_i, x_exact)
print(b)
print("")

x_computed = np.linalg.solve(M_i,b)
print(x_computed)

print("")

print(relative_error(x_exact, x_computed))

print("")
M_cond_num = np.linalg.cond(M_i)
print("Condition number of M_43: ",M_cond_num)
print("")

error_bound_A = (A_cond_num) * (10**(-16))
error_bound_M = (M_cond_num) * (10**(-16))

print(error_bound_A)
print("")
print(error_bound_M)



