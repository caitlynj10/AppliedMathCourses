# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:13:43 2024

@author: caitlyn jones
"""
import networkx as nx
import matplotlib.pyplot as plt

words = open("words.txt", "r").read().split()
frequencies = open("frequencies.txt", "r").read().split()
index1 = open("word1_index.txt", "r").read().split()
index2 = open("word2_index.txt", "r").read().split()

'''
the following lines print out the 100 most 
common word pairs in the English language
'''
frequency = [int(f) for f in frequencies]
word_pairs = [(words[int(index1[i])], words[int(index2[i])]) for i in range(len(index1))]


for i in range(100):
    print(f"{word_pairs[i][0]} -> {word_pairs[i][1]}: {frequency[i]}")

'''
the following lines are generating a diagram
containing the 20 most common pairs
'''
twenty_common = [(word_pairs[i][0], word_pairs[i][1], frequency[i]) for i in range(20)]
for word_one, word_two, freq in twenty_common:
    print(f"{word_one} -> {word_two}: {freq}")

G = nx.DiGraph()

for word_one, word_two, freq in twenty_common:
    G.add_edge(word_one, word_two)
  
plt.figure(figsize = (10,10))
pos = nx.spring_layout(G, k=5.0)

nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=8, font_weight='bold', arrows=True)

plt.show()

print(nx.dag_longest_path(G))