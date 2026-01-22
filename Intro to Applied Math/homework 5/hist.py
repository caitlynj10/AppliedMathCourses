#!/usr/bin/python
import matplotlib.pyplot as plt
from random import random
import numpy as np

# Create a test data set of 10000 entries where each is the sum
# of two uniformly distributed random variables.
test_data=[random()+random() for i in range(20000)]

# Basic histogram command
plt.hist(test_data,bins=30)

# A log scale can also be used
#plt.hist(test_data,bins=30,log=True);

# Set labels and show the plot
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
