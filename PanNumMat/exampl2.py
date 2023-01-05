import pandas as pd
import numpy as np

readcsv = pd.read_csv('sp500.csv', usecols=['Symbol', 'Sector', 'Price', 'Book Value'], index_col='Symbol')

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
print('asdfasdfasdf', readcsv.columns)
#print(numbers)
#Output
print('------------')
print(readcsv.head())
print(readcsv.head(3))
print(readcsv.tail(3))
print(readcsv['Sector'].head())
print(readcsv.Price.head())
print('------------')
print(readcsv.loc[['ADBE', 'A']])

print(readcsv.iloc[range(10)])
print('------------')
i1 = readcsv.index.get_loc('A')
i2 = readcsv.index.get_loc('ADBE')
print(readcsv.iloc[[i1, i2]])
print(readcsv.at['A', 'Price'])
print(readcsv.iat[3, 0])

rexindex = readcsv.reindex(index=['A', 'ADBE', 'NEW VALUE'])
print(rexindex)
readcsv_copy = readcsv.iloc[:5].copy()
readcsv_copy = readcsv_copy.drop(['MMM', 'ACN'], axis=0)
print(readcsv_copy)
print(numbers)
logic_num = (numbers > 0) & (numbers < 1)
print(numbers[logic_num])
print(readcsv[readcsv.Price < 100].head())
