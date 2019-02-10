import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

print(pd.Series(data=my_data))
print(pd.Series(data=my_data, index=labels))
print(pd.Series(arr, labels))
print(pd.Series(data=labels))

ser1 = pd.Series([1, 2, 2, 4], ['USA', 'Japan', 'Italy', 'Germany'])
print(ser1)
print(ser1['Japan'])

ser2 = pd.Series([1, 2, 3, 5], ['USA', 'Japan', 'USSR', 'Germany'])

print(ser1 * ser2)

ser3 = pd.Series(data=labels)
print(ser3[1])

print(pd.Series(d))
