import caitlyn_jones
import mean
import histo
import prev
import random_choice


'''
# Play with forty-nine players
n=49
trials=20000

# Counters for who won
rcw=0
tsw=0
now=0

# Data about the runs
hist=[0 for i in range(100)]
lc=[0 for i in range(n)]
lw=0

# Function to ensure choices are in the allowable range
def ra(x):
    if x<0:
        return 0
    elif x>99:
        return 99
    return x

# Simulate a large number of trials 
for i in range(trials):
    cc=[0 for i in range(n)]

    # First n-1 players use the random_choice strategy
    for i in range(n-1):
        cc[i]=ra(random_choice.play(n,hist,lw,lc,i))

    # Last player uses the test_strategy strategy
    cc[n-1]=ra(test_strategy.play(n,hist,lw,lc,n-1))
    
    # Tally the guesses
    c=[0 for i in range(100)]
    for i in cc:
        c[i]+=1
        hist[i]+=1

    # Find the winning number
    lw=0
    while(lw<100):
        if(c[lw]==1):
            break
        lw+=1

    # See who won
    if lw==100:
        now+=1
    elif cc[n-1]==lw:
        tsw+=1
    else:
        rcw+=1

    # Move this round's choices to lc 
    lc=cc
    
# Print the probabilities of winning
f=100.0/trials
print("Wins for random_choice :%6.2f%% (%.2f%% per player)" % (rcw*f,rcw*f/(n-1)))
print("Wins for test_strategy :%6.2f%%" % (tsw*f))
print("No winner              :%6.2f%%" % (now*f))
'''
# Play with forty-nine players
n = 49
trials = 20000

# Counters for who won
player1 = 0 #caitlyn_jones.py
player2 = 0 #mean.py
player3 = 0 #histo.py
player4 = 0 #prev.py
random_players = 0
no_winner = 0

# Data about the runs
hist = [0 for i in range(100)]
lc = [0 for i in range(n)]
lw = 0

# Function to ensure choices are in the allowable range
def ra(x):
    if x < 0:
        return 0
    elif x > 99:
        return 99
    return x

# Simulate a large number of trials 
for i in range(trials):
    cc = [0 for i in range(n)]

    #Player 1 uses my strategy
    cc[0] = ra(caitlyn_jones.play(n, hist, lw, lc, 0))
    
    #Player 2 uses mean.py
    cc[1] = ra(mean.play(n, hist, lw, lc, 1))
    
    #Player 3 uses histo.py
    cc[2] = ra(histo.play(n, hist, lw, lc, 2))
    
    #Player 4 prev.py
    cc[3] = ra(prev.play(n, hist, lw, lc, 3))

    #Last n-4 players use random_choice.py
    for i in range(4,n):
        cc[i] = ra(random_choice.play(n,hist,lw,lc,i))
    
    # Tally the guesses
    c = [0 for i in range(100)]
    for i in cc:
        c[i] += 1
        hist[i] += 1

    # Find the winning number
    lw = 0
    while(lw < 100):
        if(c[lw] == 1):
            break
        lw += 1

    # See who won
    if lw == 100:
        no_winner += 1
    elif cc[0] == lw:
        player1 += 1
    elif cc[1] == lw:
        player2 += 1
    elif cc[2] == lw:
        player3 += 1
    elif cc[3] == lw:
        player4 += 1
    else:
        random_players += 1

    # Move this round's choices to lc 
    lc = cc

print("")    
# Print the probabilities of winning
f = 100.0/trials
print("Wins for caitlyn_jones strategy :%6.2f%%" % (player1 * f))
print("Wins for mean stratgey :%6.2f%%" % (player2 * f))
print("Wins for histo strategy :%6.2f%%" % (player3 * f))
print("Wins for prev strategy :%6.2f%%" % (player4 * f))
print("Wins for random_choice :%6.2f%% (%.2f%% per player)" % (random_players* f, random_players * f/(n-1)))
print("No winner              :%6.2f%%" % (no_winner * f))

