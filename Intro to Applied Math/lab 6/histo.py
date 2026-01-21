from random import randint

def play(n,hist,lw,lc,y):

    # Sum total histogram entries
    s=0
    for i in range(100):
        s+=hist[i]

    # If there's nothing in the histogram then guess zero
    if s==0:
        return 0

    # Check for a low value in the histogram. We want probability(i)=hist[i]/s
    # to be less than 1/n. Add a random displacement from -2 to 2.
    for i in range(100):
        if(n*hist[i]<s):
            return i+randint(-2,2)

    # Fall back on 99 if no suitable value was found
    return 99
