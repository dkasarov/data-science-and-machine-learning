import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])

print(df)

print(df['W'])  # preferably
print(type(df['W']))
print(type(df))

print(df.X)

print(df[['W', 'Z']])

# new column
df['new'] = df['W'] + df['Y']
print(df)

# drop column
df.drop('new', axis=1, inplace=True)
print(df)

# drop row
df.drop('D', axis=0, inplace=True)
print(df)

print(df.shape)

# select row
# label based location
print(df.loc['E'])
# integer based location
print(df.iloc[3])

# selecting subsets of rows and columns
print(df)
print(df.loc['B', 'Y'])
print(df.iloc[1, 2])
print(df.loc[['A', 'B'], ['W', 'Y']])
print(df.iloc[[0, 1], [0, 2]])
