import numpy as np
import pandas as pd

data = pd.read_csv('ratings_small.csv', usecols = ['userId', 'movieId', 'rating'])
userrat = pd.pivot_table(data, values='rating', index='userId', columns='movieId', aggfunc='mean', fill_value=0)
c = userrat.to_numpy()
n = 0
ocenkauser = c[n]
for user in c:
    print(np.dot(user, ocenkauser))