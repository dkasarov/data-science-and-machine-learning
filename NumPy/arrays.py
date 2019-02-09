import numpy as np

my_list = [1, 2, 3]
arr = np.array(my_list)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.array(my_mat)

np.arange(0, 11, 2)

np.zeros(3)
# np.zeros(2, 3)
np.ones(4)

np.linspace(0, 5, 10)

np.eye(4)

rand = np.random.rand(5)
for i in rand:
    print(i)
print(rand.min())

np.random.randn(5)
ranint = np.random.randint(1, 501, 4)
print(list(ranint))
print(ranint.min())
print(ranint.argmin())
print(ranint.max())
print(ranint.argmax())

#asdf
