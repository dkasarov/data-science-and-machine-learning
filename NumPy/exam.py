# 1.
import numpy as np

# 2.
zeros = np.zeros(10)
print(zeros)

# 3.
ones = np.ones(10)
print(ones)

# 4.
fives = np.repeat(5, 10)
print(fives)

# 5.
array = np.arange(10, 51)
print(array)

# 6.
array = np.arange(10, 51, 2)
print(array)

# 7.
matrix = np.arange(9).reshape(3, 3)
print(matrix)

# 8.
np.eye(3)

# 9.
random = np.random.rand(1)
print(random)

# 10.
random2 = np.random.randn(25).reshape(5, 5)
print(random2)

# 11.
arr_2d = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(arr_2d)

# 12.
linearly = np.linspace(0, 1, 20)
print(linearly.reshape(4, 5))

# 13.
mat = np.arange(1, 26).reshape(5, 5)
print(mat)
print(mat[2:, 1:])

# 14.
print(mat[0:3, 1:2])

# 15.
print(mat[4, :])

# 16.
print(mat[3:5, :])

# 17.
sum = np.sum(mat)
print(f'Sum is {sum}')

# 18.
print(np.std(mat))

# 19.
sum_of_columns = 0
for i in mat:
    sum_of_columns += i

print(sum_of_columns)

axis = mat.sum(axis=0)
print(axis)
