# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:58:44 2024

@author: caitlyn jones
"""
 
import numpy as np
import sklearn.linear_model
import matplotlib.pyplot as plt


x = np.append((1+np.arange(5))/5,  np.zeros((1,128-5)))
x = np.random.permutation(x)

y = x + 0.05*np.random.normal(size=(1,128))

lambdas = [0.01, 0.05, 0.1, 0.2]
x_analytical = [(1/(1+lam))*y for lam in lambdas]



ridge_solutions = [sklearn.linear_model.Ridge(alpha = lam,fit_intercept=False) for lam in lambdas]
x_ridge = [(r.fit(y.T, y.T).predict(y.T).flatten()) for r in ridge_solutions]
   
plt.figure()
plt.plot(x, label = "Original Signal")
plt.plot(y[0], label = "Noisy Signal")
'''
plt.plot(x_analytical[0][0], label = "Lambda = 0.01")
plt.plot(x_analytical[1][0], label = "Lambda = 0.05")
plt.plot(x_analytical[2][0], label = "Lambda = 0.1")
plt.plot(x_analytical[3][0], label = "Lambda = 0.2")
'''
plt.plot(x_ridge[0], label = "Lambda = 0.01")
plt.plot(x_ridge[1], label = "Lambda = 0.05")
plt.plot(x_ridge[2], label = "Lambda = 0.1")
plt.plot(x_ridge[3], label = "Lambda = 0.2")
plt.title("Sparse Signals")
plt.xlabel("Signal Index")
plt.ylabel("Signal Value")
plt.legend()
plt.show()








