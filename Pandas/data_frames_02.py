import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)
booldj = df > 0
print(booldj)
print(df[booldj])

print(df['W'] > 0)
print(df[df['W'] > 0])
resultdf = df[df['Z'] < 0]
print(resultdf)
print(resultdf['X'])

print(df[df['W'] > 0]['X'])
print(df[df['W'] > 0][['X', 'Z']])

# test with string
arr_2d = np.array([['Dennis', 25, 185], ['Victoria', 25, 165], ['Kim', 30, 168]])
dfstr = pd.DataFrame(arr_2d, [1, 2, 3], ['Name', 'Age', 'Height'])
print(dfstr)
print(dfstr[dfstr['Name'] == 'Dennis'])
print(dfstr.iloc[0])

# Multiple conditions
# 'and' in pandas is '&' sign, and for 'or' is '|' sign
print(df[(df['W'] > 0) & (df['Y'] > 1)])

print(df.reset_index())

newind = 'CA NY WY OR CO'.split()
df['States'] = newind
print(df)
print(df.set_index('States', inplace=True))
print(df)
