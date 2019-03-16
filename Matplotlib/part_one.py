# Documentary - https://matplotlib.org/api/pyplot_api.html

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2
print(y)

# functional method

plt.plot(x, y)
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')

# Sub plots, now we have two plots at same time
plt.subplot(1, 2, 1)
plt.plot(x, y, 'r')
plt.title('Title 1')
plt.subplot(1, 2, 2)
plt.plot(y, x, 'g')
plt.title('Title 2')
# OO method

fig = plt.figure()  # figure
# първо създаваме axes двете оси
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

axes.plot(x, y)
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('Title')

fig = plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # първите две числа са location, останалите size в %
axes2 = fig.add_axes([0.2, 0.4, 0.4, 0.4])

axes1.plot(x, y)
axes1.set_title('bigger plot')

axes2.plot(y, x)
axes2.set_title('smaller plat')

plt.show()
