# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 10:26:38 2024

@author: caitlyn jones
"""

import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.colors import ListedColormap

def create_lattice(sz, prob):
    lattice = np.random.choice(["C", "S", "R", "E"], size = sz, p = prob)
    return lattice
    
    


def get_neighbors(lattice, x, y, neighborhood="local"):
    if neighborhood == "local":
        neighbors = []
        grid = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for rel_x, rel_y in grid:
            abs_x, abs_y = (x + rel_x) % lattice.shape[0], (y + rel_y) % lattice.shape[1]
            neighbors.append((abs_x, abs_y))
        return neighbors
    elif neighborhood == "global":
        a, b = range(lattice.shape[0]), range(lattice.shape[1])
        return [(i,j) for i in a for j in b if (i,j) != (x,y)]
    

def update_cell(lattice, x, y, death_rates, effect, neighborhood = "local"):
    cell = lattice[x,y]
    if cell == "E":
        neighbors = get_neighbors(lattice, x, y, neighborhood)
        count_neighbors = {"C": 0, "S": 0, "R": 0}
        for abs_x, abs_y in neighbors:
            if lattice[abs_x, abs_y] in count_neighbors:
                count_neighbors[lattice[abs_x, abs_y]] += 1
        total_neighbors = sum(count_neighbors.values())
        if total_neighbors > 0:
            probabilities = {
                "C": count_neighbors["C"] / total_neighbors,
                "S": count_neighbors["S"] / total_neighbors,
                "R": count_neighbors["R"] / total_neighbors
            }
            lattice[x,y] = random.choices(["C", "S", "R"], weights=probabilities.values())[0]
            
    else:
        dr = death_rates[cell]
        if random.random() < dr:
            lattice[x,y] = "E"
        else:
            neighbors = get_neighbors(lattice, x, y, neighborhood)
            for abs_x, abs_y in neighbors:
                if lattice[abs_x, abs_y] == "C" and cell == "S" and random.random() < effect:
                    lattice[x, y] = "E" 
                elif lattice[abs_x, abs_y] == "S" and cell == "R":
                    lattice[x, y] = "E"
                elif lattice[abs_x, abs_y] == "R" and cell == "C":
                    lattice[x, y] = "E"  


def run_simulation(lattice, steps, death_rate, effect, neighborhood = "local"):
    density = {"C": [], "S": [], "R": [], "E": []}
    for _ in range(steps):
        x, y = random.randint(0, lattice.shape[0]-1), random.randint(0, lattice.shape[1]-1)
        update_cell(lattice, x, y, death_rate, effect, neighborhood)
        unique, counts = np.unique(lattice, return_counts = True)
        count_dict = dict(zip(unique,counts))
        for k in ["C", "S", "R", "E"]:
            density[k].append(count_dict.get(k,0))
    return lattice, density

size = (250,250)
probs = [0.40, 0.10, 0.20, 0.30]
death_rates = {"C": .01, "S": 0.05, "R": 0.08}
effect = .3
steps = 3000

'''
probs = [0.30, 0.30 0.30, 0.01
death_rates = {"C": .05, "S": 0.05, "R": 0.05}
effect = .3
steps = 3200
'''

lattice = create_lattice(size, probs)
local_lattice, d = run_simulation(lattice, steps, death_rates, effect, neighborhood = "local")

color_map = {"C": 0, "S": 1, "R": 2, "E": 3}
colors = ["red", "blue", "green", "white"]
custom_cmap = ListedColormap(colors)
int_lattice = np.vectorize(color_map.get)(local_lattice)
plt.imshow(int_lattice, cmap=custom_cmap, interpolation="nearest")
plt.show()

time_steps = np.arange(steps)

plt.plot(d["C"], label = "C")
plt.plot(d["S"], label = "S")
plt.plot(d["R"], label = "R")
plt.xlabel("Time")
plt.ylabel("Abundance")
plt.legend()
plt.show()



    



