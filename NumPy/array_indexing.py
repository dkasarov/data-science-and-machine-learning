import numpy as np

arr = np.arange(0, 5)

arr[1:5]

arr[3:] = 999

for i in arr:
    print(i)

arr_copy = arr.copy()

# 2d array
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

for i in arr_2d:
    print(i)

# 2d array slicing
print(arr_2d[1][1])
print(arr_2d[1, 2])  # Preferably

print(arr_2d[:3, 1:])

# conditional selection
arr = np.arange(1, 11)
for i in arr:
    print(i)

bool_arr = arr > 5
print(bool_arr)

for i in arr[bool_arr]:
    print(i)

arr_2d = np.arange(1, 46).reshape(3, 15)

for i in arr_2d:
    print(i)

print(arr_2d[1:3, 9:11])
