import re #regular expression module
import numpy as np
import matplotlib.pyplot as plt 


def wordcount(filename):
    # Open and read entire file to a string
    f = open(filename,'r')
    s = f.read()
    f.close()
    
    # Split string into list of words
    words = re.split("[\W\s\!+\.+,+\?+\"]",s)
    #print(words)
    # Don't count the empty strings
    empties = words.count('')
    print("There are", empties, "empty strings")
    
    # Build dictionary of word:wordcount
    dicto = {}
    for word in words:
        if word in dicto.keys(): 
            """
            if the current word is already a key in dicto,
            then its frequency needs to be increased by 1
            """
            dicto[word] += 1 
        else:
            """
            If the word is not yet a key in the dictionary,
            a new key-value pair (key, freq) is added to the dicto,
            where the word is the key and the initial freq is set to 1
            """
            dicto[word] = 1
            
    dicto.pop('') # remove empty string from dictionary
    print(dicto)
    # Returning the dictionary and 
    # an array of frequencies of each word as a percentage of the total non-empty words
    return dicto, (np.array(sorted(dicto.values())[::-1])/
                   float(len(words)-empties)*100)#, words, empties

"""
Notes:
    dicto.keys() stores words
    dicto.values() stores the number of times the wordsappear in the text
    
    sorted(dicto.values())
    This sorts the values in ascending order, lowest freq to highest freq
    
    sorted(dicto.values())[::-1]:
    This uses slicing ([::-1]) to reverse the sorted list of values, 
    placing them in descending order (highest to lowest frequencies).
    
    4, np.array(sorted(dicto.values())[::-1]):
    This converts the reversed list of values into a NumPy array, allowing for array operations.
    
    len(words):
    len(words) gives the total number of words in the list (words).

    len(words)-empties:
    Here, empties seems to be a variable that represents the count of empty words or something similar. Subtracting this count from the total number of words gives the count of non-empty words.

    7, float(len(words)-empties)*100:
    This converts the count of non-empty words into a float and multiplies it by 100.

    Division and Percentage Calculation:
    The NumPy array obtained in step 4 is divided element-wise by the result of step 7. This effectively calculates the frequency of each word as a percentage of the total non-empty words.


"""

    
    
    
    
    
    
    
    
    
"""
what is (np.array(sorted(dicto.values())[::-1])/
               float(len(words)-empties)*100)?

It's helpful to break commands down:
    - what is dicto.values()
    - what is sorted(dicto.values()
    - what is sorted(dicto.values())[::-1]
    - what is np.array(sorted(dicto.values())[::-1])
    - what is (np.array(sorted(dicto.values())[::-1])/
                   float(len(words)-empties))
    - what is (np.array(sorted(dicto.values())[::-1])/
                   float(len(words)-empties)*100)
        

if freq0 = (np.array(sorted(dicto.values())[::-1])/
               float(len(words)-empties)*100)
what does plt.loglog(freq0, 'g.') do?


"""
results0, freq0 = wordcount("gettysburg.txt")


results1 , freq1 = wordcount("hsm2.txt")




p0 = plt.loglog(freq0, 'g.', label = "Gettysburg Frequency")


p1 = plt.loglog(freq1, "b.", label = "High School Musical 2 Excerpt Frequency")
plt.title("Word Frequencies from Various Text Passages")
plt.xlabel("Rank of Words")
plt.ylabel("Frequency")
plt.legend()


def entropy(frequency):
    f = frequency
    coeff = f * np.log2(f)
    summation = -np.sum(coeff)/100    
    return summation

print("")
print("Entropy of Gettysburg Address: ", entropy(freq0))
print("Entropy of High School Musical 2 Excerpt: ", entropy(freq1))
