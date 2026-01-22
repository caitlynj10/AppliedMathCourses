import matplotlib.pyplot as plt
from collatz_skeleton import collatz

n = 5
collatz_list, collatz_len = collatz(n)
plt.plot(collatz_list)
plt.title("n = " + str(n))
plt.show()




