#!/usr/bin/python
from random import random

# Starting position
a=0

# Number of steps
steps=20

# Carry out steps
for i in range(steps):

    # Print current position
    print(i,a)

    # Carry out a random step
    if random()<0.5:
        a+=1
    else:
        a-=1

# Print final position
print(steps,a)
