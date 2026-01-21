#!/usr/bin/python
from random import random
import numpy as np
import matplotlib.pyplot as plt

# Time steps
tmax = 200

# Max spatial steps
nmax = 2*tmax

# Number of walkers and initial positions
nwalkers = 1000 #for question 1, I had this as 1000
x = [0]*nwalkers

# Bin random walk positions into an empty 2D array (time, bin)
bins = np.zeros((tmax,nmax+1)) # tmax rows x nmax+1 columns
bins[0,int(nmax/2)] = nwalkers  # all walkers initially at x=0
# spatial index int(nmax/2) corresponds to position x=0


# Intialize statistics
meanx = [0]*tmax
widthx = [0]*tmax

# Time iteration
for i in range(1,tmax):
    
    # Walker iteration
    for j in range(nwalkers):
        
        if random()>0.5:
            x[j] += 1
        else:
            x[j] -= 1
        
        # Increment count for location of x[j]
        bins[i,x[j]+int(nmax/2)] += 1 # recenter bins around x=0
            
    # Statistics
    meanx[i] = sum(x)/float(len(x))
    widthx[i] = np.std(x)
    

log_t = np.log(np.arange(1,tmax))
log_sigma = np.log(widthx[1:])
slope,intercept = np.polyfit(log_t, log_sigma,1)
print("")
print("Slope = ", slope)


time = np.arange(1,tmax)
sigma_t = np.array(widthx[1:])

diffusion_constant = (sigma_t**2)/ (2*time)
        
# Sample plots
def walker_hist(i):
    plt.figure(i)
    bw = float(np.shape(bins)[1]-1)/float(np.shape(bins)[1])
    binx = -0.5*(np.shape(bins)[1]-1)+bw*(0.5+np.arange(np.shape(bins)[1]))
    biny = bins[i,:]
    plt.bar(binx,biny,width=bw) #width here is just a plot style option
    plt.xlim([-nmax/20, nmax/20]) #for question 1, I had this as 20 instead of 10
    
walker_hist(0),walker_hist(1),walker_hist(100)

plt.figure()
#plt.loglog(widthx)
plt.plot(meanx)
plt.title("Average of Walkers Over Time")
plt.axhline(0.5, color = "r", label = "0.5")
plt.xlabel("Time")
plt.ylabel("Average Position")
#plt.plot(widthx)
plt.show()
'''
plt.plot(diffusion_constant, label = "D")
plt.axhline(0.5, color = "r", label = "0.5")
plt.legend()
plt.title("Verifying the Diffusion Constant")
plt.xlabel("Time")
plt.ylabel("Diffusion Constant D")
'''

