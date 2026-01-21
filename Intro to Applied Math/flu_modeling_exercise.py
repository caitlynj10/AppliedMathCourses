# Agent-based simulation of epidemic
#
# Modeling questions:
# 1) Try running the code. What differences do you notice and/or expect
#      from the differential equation model?
#
# 2) Find the basic reproduction number.
#     Two possible ways: 
#     (1) start with 1 infected individual, find how many new infections can be caused by this person alone 
#      (2) use the formula, you need find out what is beta in this agent-based model
# 3) Run a vaccination program by 
#    finding the threshold N_vac at which there will be no epidemic
#    and initializing 
#
#         flu_status[1:N_vac+1] = 2
#
#    To count new infections modify 
#        number_recovered[day] = sum(flu_status == 2)
#            ->  number_recovered[day] = sum(flu_status[N_vac+1:] == 2)
#
#    Does the flu still spread?
#
# 4) Is there anything you find surprising about the model?
#       Anything you find unsatisfying? Make changes to improve the model and 
#       see what you observe.

import numpy as np
import matplotlib.pyplot as plt
import math
import random
import sys

#population size
N = 1000

#0=healthy; 1=sick; 2=immune (recovered + vaccinated)
flu_status = np.zeros(N)

N_vac = 200
flu_status[1:N_vac+1] = 2

#average number of meetings per person
m = 8

#probability of recovery after a good night's sleep
p = 0.25

#days in simulation
time_window = 90

#someone got sick!
flu_status[0] = 1


#initialize arrays
number_healthy = np.zeros(time_window)
number_sick = np.zeros(time_window) 
number_recovered = np.zeros(time_window)

for day in range(time_window):
  #first thing in the mo rning, we count who's sick
  number_healthy[day] = sum(flu_status == 0)
  number_sick[day] = sum(flu_status == 1)
  number_recovered[day] = sum(flu_status[N_vac+1:] == 2)

  #we'll assume it takes a day to become infectious
  #and you can't recover during the first day.
  flu_status_new = flu_status.copy()

  #day time: meet & transmit virus :/ 
  for i in range(0,N):
      for j in range(0,m):
          individual_1 = i
          individual_2 = int(math.floor(N*random.random()))
          if (flu_status[individual_1] == 1) and (flu_status[individual_2] == 0):
              flu_status_new[individual_2] = 1
          elif(flu_status[individual_1] == 0) and (flu_status[individual_2] == 1):
              flu_status_new[individual_1] = 1
  
  #night time: sleep & recover
  for i in range(N):
      if(flu_status[i] == 1):
          if random.random() < p:
              flu_status_new[i] = 2

  flu_status = flu_status_new.copy()

print("Total infections is",number_recovered[time_window-1])

# Plot the solutions
plt.figure()
p0,=plt.plot(number_healthy,'bo-')
p1,=plt.plot(number_sick,'ro-')
p2,=plt.plot(number_recovered,'go-')
plt.legend([p0,p1,p2],["S(t)","I(t)","R(t)"])
plt.xlabel('Time (days)')
plt.ylabel('Number')
plt.xlim(0,30)
#plt.ylim(0,100)
plt.show()