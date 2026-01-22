from myqrsteps_skeleton import myqrsteps
import numpy as np

A = np.array([[1.,2.],[0.,1.],[1.,0.]])


Q_true, R_true = np.linalg.qr(A,mode = 'complete')
print("Q_true is\n", Q_true)
print("R_true is\n", R_true)

Q, R = myqrsteps(A) 
print("Q is\n", Q)
print("R is\n", R)

