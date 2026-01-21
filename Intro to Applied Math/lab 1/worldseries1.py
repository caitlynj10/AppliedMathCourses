#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: yangyangwang
"""

import random
import math
import matplotlib.pyplot as plt

values = [0,0,0,0]

# function for simulating a world series
def worldseries(p, N): 
       
    """
    Function for simulating a world series
    p is the probability that the best team wins
    N is the number of games in the world series , usually take N=7
    """
    win = 0 #tracking the number of games the winning team wins
    lose = 0 #tracking the number of games the winning team loses
    while (max(win, lose) < math.floor(N/2)+1): #this line states that while the number of games lost or won is more than half of the games in the series, represented by N
       #in this case, this while loop will be running until a team wins or loses four games, which is more than half of 7 
        if random.random() < p: #if the random number between [0,1] is less than p
            win = win + 1 #then the winning team wins the game
        else :
            lose = lose +1 #otherwise, the winning team loses
    
    save_losses(win,lose) #saves the frequency of the number of games the losing team wins
    return win, lose #this returns the number of games the winning team wins and loses

def run_worldseries_loop_one(): 
    """
    This method holds the loop that will help
    in tally up all 44 games in one place. 
    Once the loop is done running, a 
    statement is printed.
    
    """
    i = 0
    while (i<44):
        worldseries(0.65,7)
        i+= 1
    return values


def run_worldseries_loop_two():
    """
    This method holds the loop that will help
    in tally up all 4400 games in one place. 
    Once the loop is done running, a 
    statement is printed.
    
    """
    i = 0
    while (i<4400):
        worldseries(0.65,7)
        i+= 1
    return values
#we only want to plot the number of games that the losing team wins
#need to make a function that takes the number of losses and plots them in the appropriate column on the graph



def save_losses(x,y): #parameters are x,y. x = wins and y = loss, which are returned by the worldseries(p,N) method
    if(y < 4): #if the losers win less than 4 games (they lose the series), then do the following
        values[y] += 1 #add a tally to the number of the games win by the losing team which corresponds to its position in the list
    else:
        print("The losing team won the series.") #print this statement because you won't need to add a tally if the losing team wins the whole series

    return values 

run_worldseries_loop_one()
run_worldseries_loop_two() 

"""
The followuing six lines are used to create the bar graph
based on the data saved from running to loop of 44 world series'.
"""
categories = ['0','1', '2', '3']
plt.bar(categories, values, color = "skyblue")
plt.title("Number of Games the Losing Team Wins")
plt.xlabel("Number of Games Won")
plt.ylabel("Frequency of Games Won")
plt.grid(True)
plt.show()
    


    


    

