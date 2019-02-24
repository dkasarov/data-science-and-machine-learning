import numpy as np
import pandas as pd

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 130, 340, 124, 243, 350]}

df = pd.DataFrame(data)
print(df)
byComp = df.groupby('Company')
print(byComp.mean())
print(byComp.sum())
print(byComp.count())
print(byComp.sum().iloc[1])
print(byComp.max())
print(byComp['Person'].max())

# Описване на стойностите. transpose() - преобразува редовете в колони.
print(byComp.describe().transpose())
print(byComp.describe().transpose()['GOOG'])
