# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:42:25 2024

@author: caitlyn jones
"""

import random
import matplotlib.pyplot as plt


def truncate(x):
    new_int = int(x * 1000) #moves the decimal 3 places to the right and drops the other numbers because this is an int
    
    return float(new_int/1000) #moves the decimal place 3 to the left, leaving the first three decimal places from the original number

print(truncate(735.32567))


def round_to_three(x):
    return round(x,3)

print(round_to_three(735.32567))

daily_stock_changes = [1000] #list of the 2800 stock changes a day
tt_month_stock_changes = [1000] #list of the daily stock changes over 22 months

baseline_sum = 0.0 #sum of the 1400 stocks

def initial_stock_value():
    global baseline_sum   
    stocks = [random.randint(0,200) for _ in range(1400)]
    baseline_sum = float(sum(stocks))
    
    scale = 1000/baseline_sum #scaling number used to rescale the stocks to 1000
    
    price_scaled = [price * scale for price in stocks]
    #print(baseline_sum)
    
    return sum(price_scaled);


initial_index = initial_stock_value() #initial index = 1000

old_index = initial_index

def calculate_change():
    global old_index
    stock_change = random.uniform(-2.00,2.00) #stock change of [-200,200] cents which is equivalent to [-2.00,2.00] dollars
    new_index = old_index + (stock_change) * (1000/baseline_sum) #equation given in assigment
    old_index = new_index #update the old index for the next stock change

    rounded = round_to_three(old_index) #truncate the old index
    old_index = rounded #update with the truncated old index
    
    return rounded



'''
The following method imitates the 2800 a day stock changes
'''
def daily_evolution():
    for i in range (2799):
        daily_stock_changes.append(calculate_change())
        
    return; 
    
daily_evolution()


tt_months = 2800 * 30 * 22

'''
The following method imitates the stock changes over 22 months
'''
def tt_month_evolution():
    for i in range(tt_months-1):
        tt_month_stock_changes.append(calculate_change())
        
    return;   
    
tt_month_evolution()

plt.figure(figsize=(30,30))
plt.scatter(range(0,2800), daily_stock_changes,label = "1 Day Evolution", marker = "o", color = "blue")
#plt.scatter(range(0,tt_months), tt_month_stock_changes,label = "22 Month Evolution", marker = "o", color = "red")
plt.xlabel("Time")
plt.ylabel("Stock Value")
plt.title("Stock Evolution")
plt.legend()
plt.grid(True)
plt.show()
