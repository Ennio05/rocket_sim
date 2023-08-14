import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as graph

GRAVITY = 9.80665

class simulate():

    speed: float
    angle: int
    height: float
    x_speed: float
    y_speed: float
    time_max: float
    height_max: float

    fig, ax = graph.subplots()
    ln, = ax.plot([], [])
    x, y = [], []

    def __init__(self, speed, angle, height):
        self.angle = np.deg2rad(angle)
        self.x_speed = np.cos(self.angle) * speed
        self.y_speed = np.sin(self.angle) * speed
        self.height = height

        self.time_max = -((0 - self.y_speed)/GRAVITY)
        self.height_max = self.function(self.time_max, self.y_speed)

    def function(self, t, Vi):
        number = ((Vi * t) + (1/2 * -GRAVITY * (t ** 2)))
        return number

    def create_graph(self):
        self.ax.set_xlim(0, 2 * self.time_max)
        self.ax.set_ylim(0, self.function(self.time_max, self.y_speed))
        self.ax.grid()
        self.ax.set_xlabel('time (s)')
        self.ax.set_ylabel('height (m)')

        return self.ln,

    def run_graph(self):
        self.create_graph()
        t = np.linspace(0, self.time_max * 2, 120)
        for i in t:
            self.x.append(i)
            self.y.append(self.function(i, self.y_speed))
            self.ax.plot(self.x, self.y)

            filename = f'{next(a for a, x in enumerate(t) if x == i) + 1}.png'
            self.fig.savefig(f'graphs/simulation/{filename}')

            print(next(a for a, x in enumerate(t) if x == i) + 1)
