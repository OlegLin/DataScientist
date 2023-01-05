import pandas as pd
import numpy as np

my_dict = {'Mom': 'Nat',
                    'Dad': 'Oleg',
                    'Sis': 'Kate',
                    'daught': 'Mia'}

# Myself index array
s = pd.Series(data=[10, 11, 12, 13, 14],
              index=[1, 2, 3, 5, 7])
print(s)


# Autonum index array
s = pd.Series(data=[10, 11, 12, 13, 14])
print(s)
s = pd.Series(['Blue', 'Yellow', 'Green'])
print(s)


#DataFrame - table, matrix
df = pd.DataFrame([[10, 11], [20, 21], [30, 31]])
print(df)
#DataFrame - table, matrix in line
df = pd.DataFrame([[10, 11] * 5])
print(df)
#DataFrame - table, matrix in column
df = pd.DataFrame([[10, 11]] * 5)
print(df)

#Name columns
MY_BASE = pd.DataFrame([[1, 2, 3]] * 5, columns=['this 1', 'this 2', 3], index=[1, 3, 4, 5, 3])
print(MY_BASE)
print(MY_BASE['this 2'][3])

#dict in series
my_ser = pd.Series({'Mom': 'Nat',
                    'Dad': 'Oleg',
                    'Sis': 'Kate',
                    'daught': 'Mia'})
print(my_ser)

# dict in DataFrame
my_frame = pd.DataFrame({'Mom': ['Nat','asd'],
                    'Dad': ['Oleg','asd'],
                    'Sis': ['Kate','asdf'],
                    'daught': ['Mia','sdafds']})
print(my_frame)
#