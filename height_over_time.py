import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as graph

GRAVITY = 9.80665

x, y = [], []

def function(t, Vi):
    number = ((Vi * t) + (1/2 * -GRAVITY * (t ** 2)))
    return number

initial = int(input('enter initial speed: '))
angle = np.deg2rad(int(input('enter an angle: ')))

x_speed = np.cos(angle) * initial
y_speed = np.sin(angle) * initial

print(x_speed, y_speed)

time_max = -((0 - y_speed)/GRAVITY)
height_max = function(time_max, y_speed)

fig, (axt, axd) = graph.subplots(2, gridspec_kw=dict(wspace=0, hspace=0.2))
timeD, heightD, distanceD = [], [], []
dt, = axt.plot([], [])
dh, = axd.plot([], [])

def init():
    axt.set_xlim(0, 2 * time_max)
    axt.set_ylim(0, function(time_max, y_speed))
    axt.grid()
    axt.set_xlabel('time (s)')
    axt.set_ylabel('height (m)')

    axd.set_ylim(0, function(time_max, y_speed))
    axd.set_xlim(0, time_max * 2 * x_speed)
    axd.grid()
    axd.set_xlabel('hori. dist. (m)')
    axd.set_ylabel('vert. dist. (m)')

    return dt, dh,

def update(frame):
    timeD.append(frame)
    heightD.append(function(frame, y_speed))
    distanceD.append(frame * x_speed)
    dt.set_data(timeD, heightD)
    dh.set_data(distanceD, heightD)
    return dt, dh,

ani = FuncAnimation(fig, update, interval=33, frames=np.linspace(0, 2 * time_max, 128),
                    init_func=init, blit=True)
graph.show()

