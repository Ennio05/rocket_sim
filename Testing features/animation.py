import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as graph

x = []
y = []
max = 10

def function(x):
    number = -abs((x - 5) ** 2)
    return number

for i in range(max + 1):
    x += [i]
    y += [function(i)]

fig, ax = graph.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [])

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, interval=50, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
graph.show()


x = '1'