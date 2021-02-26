from polya.distributions import Distribution
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from mpl_toolkits import mplot3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
dist = Distribution(3)
    
line, = ax.plot(0, 0, 'o')
def init():
    line, = ax.plot(dist.pos[0],dist.pos[1])
    return line,

def animate(i):
    dist.update_pos()
    x = dist.pos[0]
    y = dist.pos[1]
    z = dist.pos[2]
    line.set_data(np.asarray([x]),np.asarray([y]))
    line.set_3d_properties(np.asarray([z]),'z')
    return line,

ax.set_xlim3d([-5.0, 5.0])
ax.set_ylim3d([-5.0, 5.0])
ax.set_zlim3d([-5.0, 5.0])

ax.axis([-5,5,-5,5])
anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=1000, blit=True)
FFMpegWriter = animation.writers['ffmpeg']
writer = animation.FFMpegWriter()

anim.save('polya.mp4', writer=writer)

