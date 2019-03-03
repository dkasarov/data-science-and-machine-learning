import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': [444, 555, 666, 444],
                   'col3': ['abc', 'def', 'ghi', 'xyz']})

print(df)

# Find unique value in data frames

print(df['col2'].unique())
# length of array
print(df['col2'].nunique())
print(df['col2'].value_counts())

print(df[(df['col1'] < 5) & (df['col2'] == 444)])


# Apply method

def times2(x):
    return x * 2


print(df['col1'].apply(times2))

print(df['col2'].apply(lambda x: x * 2))

# Return columns and index
print(df.columns)

print(df.index)

print(df.sort_values(['col2']))  # or by='col2'
print(df.sort_index(ascending=False))

print(df.isnull())

# Pivot table
data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(data)

print(df)
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))
