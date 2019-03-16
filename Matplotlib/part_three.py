import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2
print(y)

fig = plt.figure()

ax = fig.add_axes([0.1, 0.1, 0.8, 0.9])

# ax.plot(x, y, color='#333333', linewidth=1, linestyle=':',
#        marker='o', markersize=15,
#        markerfacecolor='blue')  # or color names, alpha - прозрачност, markeredgewidth, markeredgecolor

ax.plot(x, y, lw=2, ls='--')  # lw - linewidth, ls - linestyle

ax.set_xlim([0, 0.2])  # bounds - lower, upper bound
ax.set_ylim([0, 2])

plt.show()
