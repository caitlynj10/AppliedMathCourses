# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:48:05 2024

@author: caitlyn jones
"""

import numpy as np
import scipy as sc

H_4 = sc.linalg.hilbert(4)
H_10 = sc.linalg.hilbert(10)
H_20 = sc.linalg.hilbert(20)

U,S,V = np.linalg.svd(H_20)


x_true_4 = np.ones(4)
x_true_10 = np.ones(10)
x_true_20 = np.ones(20)

b_4 = H_4 @ x_true_4
b_10 = H_10 @ x_true_10
b_20 = H_20 @ x_true_20

x_computed_4 = np.linalg.solve(H_4,b_4)
x_computed_10 = np.linalg.solve(H_10,b_10)
x_computed_20 = np.linalg.solve(H_20,b_20)

'''
def relative_error(computed,true):
    numer = np.linalg.norm(computed-true)
    denom = np.linalg.norm(true)
    return numer/denom
    
print(relative_error(x_computed_4, x_true_4))
print(relative_error(x_computed_10, x_true_10))
print(relative_error(x_computed_20, x_true_20))
'''

cond_H4 = np.linalg.cond(H_4)
cond_H10 = np.linalg.cond(H_10)
cond_H20 = np.linalg.cond(H_20)

E_mach = 10**(-16)

def relative_error(cond_number, e_mach):
    return cond_number*e_mach

print(relative_error(cond_H4, E_mach))
print(relative_error(cond_H10, E_mach))
print(relative_error(cond_H20, E_mach))


def relative_backward_error(b, Ax_computed):
    numer = np.linalg.norm(b-Ax_computed, ord=2)
    denom = np.linalg.norm(b, ord=2)
    return numer/denom


print(relative_backward_error(b_4, H_4 @x_computed_4))
print(relative_backward_error(b_10, H_10 @x_computed_10))
print(relative_backward_error(b_20, H_20 @x_computed_20))


