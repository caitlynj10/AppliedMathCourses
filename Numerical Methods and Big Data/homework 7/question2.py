# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:26:08 2024

@author: caitlyn jones
"""

import numpy as np
import sklearn.linear_model
import matplotlib.pyplot as plt

def shrinkage(y, lam):
    if(y < -lam):
        x = y + lam
    if(y > lam):
        x = y - lam
    if(abs(y) < lam):
        x = 0 
    return x
   
y = np.linspace(-10,10,100)
lam = 2
x = [shrinkage(i,lam) for i in y]
Nsamples = 128

no_noise = np.append((1+np.arange(5))/5,  np.zeros((1,128-5)))
no_noise = np.random.permutation(no_noise)
noisy = no_noise + 0.05*np.random.normal(size=Nsamples)

lambdas = [0.01, 0.05, 0.1, 0.2]
x_noisy = {lamb:[shrinkage(n,lamb) for n in noisy] for lamb in lambdas }

lasso_solutions = {}
for l in lambdas:
    alpha = l / Nsamples
    lasso = sklearn.linear_model.Lasso(alpha=alpha, fit_intercept=False)
    lasso.fit(np.eye(Nsamples), noisy)  
    lasso_solutions[l] = lasso.coef_ 
    
plt.figure()
plt.plot(x, label = "X")
plt.plot(lasso_solutions[0.01], label = "Lambda = 0.01")
plt.plot(lasso_solutions[0.05], label = "Lambda = 0.05")
plt.plot(lasso_solutions[0.1], label = "Lambda = 0.1")
plt.plot(lasso_solutions[0.2], label = "Lambda = 0.2")
plt.title("Soft-Thresholding Function")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.show()


'''
plt.plot(x_noisy[0.01], label = "Lambda = 0.01")
plt.plot(x_noisy[0.05], label = "Lambda = 0.05")
plt.plot(x_noisy[0.1], label = "Lambda = 0.1")
plt.plot(x_noisy[0.2], label = "Lambda = 0.2")
'''
    