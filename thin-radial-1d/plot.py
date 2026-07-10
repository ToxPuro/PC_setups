import pencil as pc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

os.system("./src/read_all_videofiles.x")
slices = pc.read.slices()

phi = slices.xy.phi   # shape: (nt, 1, nx)
phi = phi[:, 0, :]

nt, nx = phi.shape

x = np.arange(nx)

fig, ax = plt.subplots()
line, = ax.plot(x, phi[0])

ax.set_ylim(phi.min(), phi.max())
title = ax.text(0.5, 1.05, "", transform=ax.transAxes, ha="center")

def update(i):
    line.set_ydata(phi[i])
    title.set_text(f"t = {slices.t[i]:.3f}")
    return line, title


ani = FuncAnimation(fig, update, frames=nt, interval=30, blit=False)

plt.show()
