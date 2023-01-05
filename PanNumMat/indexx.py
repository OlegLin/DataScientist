import pandas as pd
import numpy as np


pd.options.display.max_rows = 10
readcsv = pd.read_csv('sp500.csv', index_col='Symbol', usecols=['Symbol', 'Sector', 'Price', 'Book Value']).head(10)


np.random.seed(123)

df = pd.DataFrame({'value': np.random.random(10000), 'key': range(100, 10100)})
print(df[df.key == 10099])
print(readcsv)
readcsv_new = readcsv.reset_index()
readcsv_new.set_index('Sector', inplace=True)
print(readcsv_new)
print(readcsv)
