import numpy as np
import matplotlib.pyplot as plt
import random

# read in daily maximum temperatures.
temps = open("BostonTemps.txt",'r').read().split()
dates = open("BostonDates.txt",'r').read().split()

N = len(temps)

n = np.random.randint(N)
print("Date: ", dates[n], " Max Temp (deg F): ", temps[n] )
#input("Press any key for a new draw") #Python 3
#raw_input("Press any key for a new draw") #Python 2
