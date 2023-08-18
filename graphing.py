import numpy as np
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
    total_time: float

    fig, ax = graph.subplots()
    ln, = ax.plot([], [])
    x, y = [], []

    def __init__(self, speed, angle, height = 0):
        self.x, self.y = [], []
        self.angle = np.deg2rad(angle)
        self.x_speed = np.cos(self.angle) * speed
        self.y_speed = np.sin(self.angle) * speed
        self.height = height

        self.time_max = (0 - self.y_speed)/(-GRAVITY)
        self.height_max = self.function(self.time_max, self.y_speed)
        self.total_time = self.time_max + np.sqrt(abs(2 * self.height_max/-GRAVITY))

    def function(self, t, Vi):
        number = ((Vi * t) + (1/2 * -GRAVITY * (t ** 2))) + self.height
        return number   

    def create_graph(self):
        self.ax.set_xlim(0, self.total_time * 1)
        self.ax.set_ylim(0, self.height_max * 1.01)
        self.ax.grid()
        self.ax.set_xlabel('time (s)')
        self.ax.set_ylabel('height (m)')

        return self.ln,

    def run_graph(self):
        self.create_graph()
        t = np.linspace(0, self.total_time, 120)
        for i in t:
            self.x.append(i)
            self.y.append(self.function(i, self.y_speed))
            self.ax.plot(self.x, self.y)

            filename = f'frame_{next(a for a, x in enumerate(t) if x == i) + 1}.png'
            self.fig.savefig(f'graphs/simulation/{filename}')

            print(f'frame_{next(a for a, x in enumerate(t) if x == i) + 1}.png generated')
