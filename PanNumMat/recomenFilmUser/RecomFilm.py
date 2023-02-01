import numpy as np
import pandas as pd

data = pd.read_csv('ratings_small.csv', usecols = ['userId', 'movieId', 'rating'])
userrat = pd.pivot_table(data, values='rating', index='userId', columns='movieId', aggfunc='mean', fill_value=0)
c = userrat.to_numpy()
n = 0
ocenkauser = c[n]
for user in c:
    print(np.dot(user, ocenkauser))

print('qqqqqqqqqqq')
a = pd.Series(np.linspace(0, 10, 15))
print(a[1])


data = pd.Series([0.25, 0.5, 0.75, 1.0])
print('data[1]:')
print(data[1])
print('data[1:3]:')
print(data[1:3])
