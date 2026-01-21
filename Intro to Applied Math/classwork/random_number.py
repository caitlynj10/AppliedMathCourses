# Draw a random number from 1 to N, where N is provided as an
# argument to the function.

import numpy as np

N = 10

n = np.random.randint(N)+1
print("Random number between 1 and 10:",n)
