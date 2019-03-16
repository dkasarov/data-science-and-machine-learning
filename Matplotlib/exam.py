import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x * 2
z = x ** 2

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, y)
ax.set_title('title')
ax.set_xlabel('x')
ax.set_ylabel('y')

fig2 = plt.figure()
ax1 = fig2.add_axes([0, 0, 1, 1])
ax2 = fig2.add_axes([0.2, 0.5, .2, .2])
ax1.plot(x, y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.plot(x, y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')

fig3 = plt.figure()
ax1 = fig3.add_axes([0, 0, 1, 1])
ax2 = fig3.add_axes([0.2, 0.5, .4, .4])
ax1.plot(x, y, 'b')
ax1.plot(x, z, 'g')
ax2.plot(x, y, z, 'b')
ax1.set_xlabel('x')
ax1.set_ylabel('z')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')
ax2.set_xlim([20, 22])
ax2.set_ylim([300, 500])

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 3))
axes[0].plot(x, y, ls='--', color='blue', lw=3)
axes[1].plot(x, z, color='green', lw=3)

plt.show()
