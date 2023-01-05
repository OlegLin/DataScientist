import pandas as pd
import numpy as np

readcsv = pd.read_csv('sp500.csv', usecols=['Symbol', 'Sector', 'Price', 'Book Value'])

Simpsons = pd.Series({'Homer': 120,
                      'Marge': 60,
                      'Bart': 35,
                      'Lisa': 30,
                      'Maggie': 7})
np.random.seed(123)
numbers = pd.Series(data=np.random.normal(size=10), index=np.arange(25, 35))
print(Simpsons.size)
print(readcsv.shape)

print(readcsv.nunique())
print(Simpsons.index)
print(readcsv.index, readcsv.values)
print(readcsv.columns)
print('--------------')
print(Simpsons)
Simpsons.name = 'Weight'
Simpsons.index.name = 'FirstName'
print(Simpsons)

print(readcsv.columns)
readcsv.rename(columns= {'Book Value': 'BookValue'}, inplace=True)
print(readcsv.columns)
#print(numbers)