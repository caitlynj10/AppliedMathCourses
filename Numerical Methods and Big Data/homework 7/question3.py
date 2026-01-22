# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 23:14:32 2024

@author: caitlyn jones
"""

import numpy as np
import pandas as pd


file = "ratings-train.csv"
data = pd.read_csv(file)
users = np.array(data.iloc[:, 0])
movies = np.array(data.iloc[:, 1])
movie_ratings = np.array(data.iloc[:, 2])

test_file = "ratings-test.csv"
test_data = pd.read_csv(test_file)
test_users = np.array(test_data.iloc[:, 0])
test_movies = np.array(test_data.iloc[:, 1])
test_movie_ratings = np.array(test_data.iloc[:, 2])

num_users = users.max() + 1
num_movies = movies.max() + 1

n = 10
X = np.random.rand(num_users,n)
Y = np.random.rand(num_movies,n)

reg = 0.1
iterations = 20

for i in range(iterations):
    for u in range(num_users):
        rated_movies = movies[users == u]
        ratings = movie_ratings[users == u]
        
        if len(rated_movies) > 0:
            Y_rated = Y[rated_movies]  
            X[u] = np.linalg.solve(Y_rated.T @ Y_rated + reg * np.eye(n), Y_rated.T @ ratings)
     
    for m in range(num_movies):
        rated_users = users[movies == m]
        ratings = movie_ratings[movies == m]
        
        if len(rated_users) > 0:
            X_rated = X[rated_users] 
            Y[m] = np.linalg.solve(X_rated.T @ X_rated + reg * np.eye(n), X_rated.T @ ratings)

def predict_rating(user_id, movie_id):
    return X[user_id] @ Y[movie_id].T

print(predict_rating(test_users[0][0],test_movies[0][0]))