from polya.distributions import Distribution
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


fig,ax = plt.subplots()
dist = Distribution(2)
    
line, = ax.plot(0, 0, 'o')
def init():
    line, = ax.plot(dist.pos[0],dist.pos[1])
    return line,

def animate(i):
    dist.update_pos()
    x = dist.pos[0]
    y = dist.pos[1]
    line.set_data(x,y)
    return line,
ax.axis([-5,5,-5,5])
anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=1000, blit=True)
FFMpegWriter = animation.writers['ffmpeg']
writer = animation.FFMpegWriter()

anim.save('polya.mp4', writer=writer)

