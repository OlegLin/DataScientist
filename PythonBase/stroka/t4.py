import pandas as pd

s = pd.Series(data=['1', 2, 3.1, 'hi!', 5,-512, 12.42, 'sber', 10.10, 98],
              index=range(6, 26, 2))
print(s)

new_s = pd.Series(s, index=range(2,12))
print(new_s)