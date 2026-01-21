# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:36:43 2024

@author: caitlyn jones
"""

import numpy as np



def entropy(N):
   return np.log2(N)


first_entropy = entropy(2)
second_entropy = entropy(5)
third_entropy = entropy(10)

entropy_sum = first_entropy + second_entropy + third_entropy 

total_entropy = entropy(150)

#print("The entropy of the first digit is", first_entropy)
#print("The entropy of the second digit is", second_entropy)
#print("The entropy of the third digit is", third_entropy)
#print("The sum of all three entropies is" , entropy_sum)

print("")
print("The total entropy is" , total_entropy)


