# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 17:18:25 2024

@author: caitlyn jones
"""
from random import choice

'''
This function first creates an array based on 
the numbers that were chosen in the last round.
Then, it makes an array based on numbers that
were NOT chosen. If this array has values, then
the function returns a random one from here, if
not, the function returns 0.
'''
def play(n,hist,lw,lc,y):
    
   chosen_numbers = lc
   
   new_numbers = [num for num in range(100) if num not in chosen_numbers] 
   
   if len(new_numbers) > 0:
       return choice(new_numbers)
   else:
       return 0
   
   
