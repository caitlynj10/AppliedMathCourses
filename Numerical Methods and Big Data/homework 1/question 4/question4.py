input_file = "brandeisbabson (1).txt"
with open(input_file, 'r',encoding='utf-16') as file:
    lines = file.readlines()
 
rows = [];

for line in lines: 
    row = line.strip().split()
    rows.append(row)
    

#print(rows)
    
column_five = []
column_six = []

def calculate_diff(x,y): #calculates and returns the absolute value of the difference in score
    
    return abs(x - y)


def winner(x,y):
    winner_int = 0;
    #calculates the winner of the match by finding the difference in scores
    #if the difference in score is negative, that means Babson won, so the method returns -1 
    #if the score = 0, returns 0 (there was a tie)
    #if winner is positive, returns 1 because Brandeis won
    score_diff = x - y
    if (score_diff < 0):
        winner_int = -1
    elif (score_diff > 0):
        winner_int = 1
    else:
        winner_int = 0
    return winner_int
    
for row in rows:
    diff = calculate_diff(int(row[2]), int(row[3]))
    column_five.append(diff)
    

    
for row in rows:
    winners = winner(int((row[2])),int(row[3]))
    column_six.append(winners)    
    
 

#print(column_five)
#print(column_six)

i = 0
for row in rows:
    row.append(str(column_five[i]))
    row.append(str(column_six[i]))
    i += 1

print(rows)

with open("brandeisbabsonwinners.txt", "w") as file:
    for row in rows:
        new_text_file = " ".join(row)
        file.write(new_text_file + "\n")
        

    


