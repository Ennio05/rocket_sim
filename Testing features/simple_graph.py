import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)

l1 = [1, 2 ,3]
print(4 * t)
print(4 * l1)

x, y = [0, 1, 2, 3, 4], [1, 3, 5.5, 7, 9]

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='time(s)', ylabel='bozometer(mB)')
ax.grid()

fig.savefig('test.png')
plt.show()