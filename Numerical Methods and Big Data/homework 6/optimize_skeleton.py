import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import scipy.optimize

##############################
# Optimization by Newton's method 
##############################

def f(x,y):
  return x**4/16-2*x*y+y**4

##############################
#Your code for the gradient and Hessian goes here
def Df(x,y):
    return np.array([x**3/4 - 2*y, -2*x + 4*(y**3)])
def DDf(x,y):
    return np.array([[3*(x**2)/4, -2.],
                    [-2., 12*(y**2)]])
##############################

#vector arguments
def F(x):
  return f(x[0],x[1])
def DF(x):
  return Df(x[0],x[1])
def DDF(x):
  return DDf(x[0],x[1])

# Initial condition
##############################
pt = np.array([1,1])
##############################

tol = 1e-7

    
#gradient descent
step = 999
x = pt
rec = x[:,np.newaxis]
while (np.linalg.norm(step)>tol):
    def myfun(t):
        #restrict function to steepest descent direction
        return F(x-t*DF(x))

    #do a line search
    tmin = scipy.optimize.fmin(func=myfun,x0=0)
    
    ##############################
    # Your code for the gradient descent step goes here 
    step = -tmin * DF(x)
    ##############################
        
    x=x+step
    rec=np.hstack((rec,x[:,np.newaxis]))

print("Gradient, start at ",pt[0],pt[1])
print("steps",len(rec[0,:].flatten())-1)
print(rec.shape)
print(rec)
hndG = plt.plot(rec[0,:],rec[1,:],'g-',label='Gradient')
  
 
#Newton's method
step=999
x = pt
rec = x[:,np.newaxis]
while (np.linalg.norm(step)>tol):
    ##############################
    # Your code for the Newton's method step goes here 
    step = -np.linalg.inv(DDF(x)) @ DF(x)
    ##############################
        
    print("step size is",np.linalg.norm(step))
    x=x+step
    rec=np.hstack((rec,x[:,np.newaxis]))

print("Newton, start at ",pt[0],pt[1])
print("steps",len(rec[0,:].flatten())-1)
hndN = plt.plot(rec[0,:],rec[1,:],'r-',label='Newton')

hndS = plt.plot(pt[0],pt[1],'ko',label='Start Pt')
hndM = plt.plot(2,1,'bd',label='Global Min')
plt.legend([hndG[0], hndN[0], hndS[0], hndM[0]],['Gradient','Newton','Start Pt','Global Min'])

myxlim = np.array([-4, 4])
myylim = np.array([-2, 2])
X=np.kron(np.linspace(myxlim[0],myxlim[1],400),np.ones((400,1)))
Y=np.kron(np.linspace(myylim[0],myylim[1],400)[:,np.newaxis],np.ones((1,400)))
print(X.shape)
print(Y.shape)
V = -3+np.logspace(1e-16,1,20)
plt.contour(X,Y,f(X,Y),V)
#axis([myxlim myylim])

plt.axis([myxlim[0],myxlim[1],myylim[0],myylim[1]])
plt.show()    
