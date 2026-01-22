from mygausselim_skeleton import mygausselim
import numpy as np


A = np.array([[3.,4.,5.],[1.,0.,1.],[-2.,2.,2.]])
b = np.array([2., 2., -1.])

x_true = np.linalg.solve(A,b)
print("x_true is", x_true)

[L, U, P, x] = mygausselim(A,b) 
print("x is", x)

print("L: \n", L)
print("U: \n", U)
print("P: \n", P)


'''
Must answer the following question:
    Does LU = PA for each value of k?
'''


def testing_e():
    k_values = [5,10]
    
    for k in k_values:
        e = 10**(-k)
        A = np.array([[e,1], [1,1]])
        b = np.array([0,0])
        
        [L, U, P, x] = mygausselim(A, b)
        
        print(f"For e = 10^(-{k}):")
        print(f"A: \n{A}")
        print(f"L: \n{L}")
        print(f"U: \n{U}")
        print(f"P: \n{P}")
        
        
        print(f"LU = \n{L*U}")
        print(f"PA: \n{P*A}")
        
testing_e()

