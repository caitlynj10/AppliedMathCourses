import wordcount as wc
#import operator
results, freq,_ , _ = wc.wordcount('gettysburg.txt')
sorted_words = list(reversed(sorted(results.items(), key=lambda kv: kv[1])))
print(sorted_words)
