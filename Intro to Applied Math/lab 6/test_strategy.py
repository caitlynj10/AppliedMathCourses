'''
def play(n,hist,lw,lc,y):

    # Just always return 10
    return 10

def play(n,hist,lw,lc,y):
    
    #Return an offset number of the last winning number
    return (lw + 5) % 100

def play(n,hist,lw,lc,y):

    #Returns numbers that are less frequently chosen
    return min(range(len(hist)), key=lambda x: hist[x])
'''


