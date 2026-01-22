import numpy as np
import matplotlib.pyplot as plt

# Open the file in the "read" mode
f=open("SP_500.csv","r")

# Read in header line
h=f.readline().split(",")
# Initialize 7 empty lists
s=[]

for i in range(7):
    s.append([])

# Loop over the remaining lines    
for l in f:
    
    # Create a list by separating the line at commas
    d=l.split(",")
    
    # Store the 7 columns in the line to each relevant list
    for i in range(7):
        s[i].append(d[i])
        
# Close the file
f.close()

number_years = 50
N = 300*number_years #approximately 300 market days per year

#convert stock data into floats
column_index = 1 #put column index to plot here
stock_data = [float(x) for x in s[column_index][-N:] ] 


time = np.arange(N) 
S_t = 20*np.exp(3e-4*time)

'''
plt.figure() 
plt.plot(time,stock_data, label = "Data") 
plt.semilogy(time, S_t, label = "Fit Data")
plt.xlabel('t (days)')
plt.ylabel('Opening Price')
plt.title("Stock Market")
plt.legend()
plt.show()
'''
'''
opening_prices = np.array(s[1], dtype=float)
differences = np.diff(opening_prices)
plt.hist(differences, bins = 30, log = True)
plt.xlim(-100,100)
plt.ylim(0,1000)
plt.title("Histogram of Daily Differences")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
'''
'''
opening_prices = np.array(s[1], dtype=float)
growth_rates = np.diff(opening_prices)/opening_prices[:-1]
plt.hist(growth_rates, bins = 30, log = True)
plt.xlim(-.2,.2)
plt.ylim(0,8000)
plt.title("Histogram of Growth Rates")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
mean_growth_rate = np.mean(growth_rates)
print("The mean is", mean_growth_rate)
'''

opening_prices = np.array(s[1], dtype=float)
growth_rates5 = [(opening_prices[i+5]-opening_prices[i])/opening_prices[i] for i in range(len(opening_prices) - 5)]
plt.hist(growth_rates5, bins = 30)
plt.title("Histogram of Growth Rates")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

opening_prices = np.array(s[1], dtype=float)
growth_rates20 = [(opening_prices[i+20]-opening_prices[i])/opening_prices[i] for i in range(len(opening_prices) - 20)]
plt.hist(growth_rates20, bins = 30)
plt.title("Histogram of Growth Rates")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
print("")

print("Standard deviation for step size 5:", np.std(growth_rates5))
print("Standard deviation for step size 20:", np.std(growth_rates20))


k_vals = np.arange(1, 101)
sigma_t = []
for k in range(1,101):
    growth_rates_k = [(opening_prices[i+k]-opening_prices[i])/opening_prices[i] for i in range(len(opening_prices) - k)]
    sigma_t.append(np.std(growth_rates_k))
    

plt.plot(k_vals, sigma_t)
plt.xlabel("Step Size K")
plt.ylabel("Standard Deviation (Width)")
plt.title("Width as a Function of K")
plt.show()
print("")

sigma2 = np.array(sigma_t)**2
diffusion_constant = (sigma2)/ (2*k_vals)
print("D =",np.mean(diffusion_constant))