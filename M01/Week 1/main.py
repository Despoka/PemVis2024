import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


# x = np.linspace(0,2*np.pi,200)
# y=np.sin(x)
#
# fig, ax = plt.subplots()
# ax.plot(x,y)
# plt.show()
#
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
# ax.set_ylabel("Tinggi")
# ax.set_xlabel("Lebar")
# plt.show()
#
# fig, ax = plt.subplots(figsize=(5, 2.7))
#
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2 * np.pi * t)
# line, = ax.plot(t, s, lw=2)
#
# ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05))
#
# ax.set_ylim(-2, 2)
# plt.show()

# fig, ax = plt.subplots(facecolor='lightskyblue',
#                        figsize=(3,3))
# plt.show()

fig, ax = plt.subplots()
t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t

v02 = 5
z2 = g * t**2 / 2 + v02 * t

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()


def update(frame):
    # for each frame, update the data stored on each artist.
    x = t[:frame]
    y = z[:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    # update the line plot:
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return (scat, line2)


ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
plt.show()