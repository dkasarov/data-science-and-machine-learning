import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2
print(y)

fig, axes = plt.subplots(nrows=1, ncols=2)
# print(axes) В момента axes се съхраняват в array

axes[0].plot(x, y)
axes[0].set_title('first plot')
axes[1].plot(y, x)
axes[1].set_title('second plot')

# figure size and DPI
fig = plt.figure(figsize=(8, 5), dpi=100)  # fig size = width and height in inches, dpi = pixel per inch

ax = fig.add_axes([0.1, 0.1, 0.8, 0.9])
ax.plot(x, x ** 2, label='X Square')
ax.plot(x, x ** 3, label='X Cubed')
# legends
ax.legend(loc=0, fontsize=10, title='legend', facecolor='gray')  # https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend

# fig.savefig('my_picture.png', dpi=50) # запазване на фигурата

plt.show()
