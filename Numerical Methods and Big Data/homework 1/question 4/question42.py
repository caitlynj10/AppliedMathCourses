import pandas as pd
import matplotlib.pyplot as plt

df  = pd.read_csv("brandeisbabson (1).txt", sep = "\t", header = None, encoding = "utf-16")



df[4] = (df[2] - df[3]).abs()
df[5] = (df[2] > df[3]).astype(int) - (df[2] < df[3]).astype(int)

df.to_csv('brandeisbabsonwinners.txt', sep='\t', header=False, index=False, encoding='utf-16')

wins = df[5].value_counts()
brandeis_wins = wins.get(1,0)
babson_wins = wins.get(-1,0)
ties = wins.get(0,0)

brandeis_average = df[2].mean()
babson_average = df[3].mean()

print(brandeis_average)
print(babson_average)

latest_year = df[1].max()
last_30 = df[df[1] >= latest_year - 30]

brandeis_average_30 = last_30[2].mean()
babson_average_30 = last_30[3].mean()

print(brandeis_average_30)
print(babson_average_30)


plt.figure(figsize = (20,15))
plt.scatter(df[1], df[5], color = "blue", marker = "o")
plt.title("Winner vs Year")
plt.xlabel("Year")
plt.ylabel("Winner")
plt.xticks(df[1], rotation=45)  
plt.yticks([-1, 0, 1], ['Babson: ' + str(babson_wins), 'Tie: ' + str(ties), 'Brandeis: ' + str(brandeis_wins)]) 
plt.grid()
plt.tight_layout()
plt.show()
