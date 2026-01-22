# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:31:19 2024

@author: caitlyn jones
"""
import numpy as np

'''
A = np.array([[1,20],[1,30],[1,10]])
print(A)
y = np.array([35, 70, 30])
print(y)

c = np.linalg.lstsq(A,y)
print(c)

y_100 = 5 + 2*100
print(y_100)


A = np.array([[1,20,400],[1,30, 900],[1,10,100]])
print(A)
y = np.array([35, 70, 30])
print(y)

c = np.linalg.lstsq(A,y)
print(c)

y_100 = 55 + -4*100 + 0.15*(100**2)
print(y_100)

'''

r1_exact,r2_exact = np.roots([1, -1e5, 1])
np.set_printoptions(precision = 10)
print(r1_exact, ", " , r2_exact)


def quadratic_plus(a,b,c):
    rad = np.sqrt((b**2) - 4*a*c)
    numer = -b + rad
    return numer/(2*a)


def quadratic_minus(a,b,c):
    rad = np.sqrt((b**2) - 4*a*c)
    numer = -b - rad
    return numer/(2*a)


r1_computed = quadratic_plus(1, -10**5, 1)
#r2_computed = quadratic_minus(1, -10**5, 1)
print(r1_computed)

r2_computed = 1/(1*r1_computed)
print(r2_computed)

def relative_error(approximate,true):
    absolute = approximate - true
    return absolute/true


print(relative_error(r1_computed, r1_exact))
print(relative_error(r2_computed, r2_exact))