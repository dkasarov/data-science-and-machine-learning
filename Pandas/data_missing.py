import numpy as np
import pandas as pd

dict = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'c': [1, 2, 3]}

df = pd.DataFrame(dict)

print(df)

# Изчистване на празни полета
print(df.dropna())
print(df.dropna(axis=1))

# Задължителен брой not null полета
print(df.dropna(thresh=2))

# Запълване на прадните полета
print(df.fillna(value='FILL VALUE'))
# Заместване със средната стойност на колоната - A
print(df['A'].fillna(value=df['A'].mean()))
