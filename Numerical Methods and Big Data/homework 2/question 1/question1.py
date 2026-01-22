# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:33:46 2024

@author: caitlyn jones
"""

import matplotlib.pyplot as plt
import numpy as np


'''
The coefficients of p(x) = x^4 - 16x^3 + 96x^2 - 256x + 256.
'''
poly_coeff = [1,-16,96,-256,256] 

'''
The function p(x) = (x-4)^4
'''
def p_of_x(x):
    return (x-4)**4


'''
The x-values that will be used to evaluate p(x).
The x-values are 4.00001, 4.00002, ...., 4.00101,
i.e. the values from 4.00001-4.00101, 
increasing by .00001 each time.
'''
x_values = np.linspace(4.00001, 4.00101, 101) 

'''
Next, we need to evaluate p(x) at each x 
and save the values so that we can graph them.
'''

p_eval = np.polyval(poly_coeff, x_values)

p_of_x_eval = p_of_x(x_values)

'''
Lastly, we need to plot these numbers.
'''

plt.plot(x_values, p_eval, label =  "p(x) = x^4 - 16x^3 + 96x^2 - 256x + 256", color = "blue")
plt.plot(x_values, p_of_x_eval, label =  "p(x) = (x-4)^4", color = "red")
plt.xlabel("x")
plt.ylabel("p(x)")
plt.title("Plotting p(x) with x values closest to 4")
plt.legend()
plt.grid(True)
plt.show()


