import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from misc import *  # suppose que tu as init_grid_random() et next_step()
import time

grid = init_grid_random(size = 400)
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='gray', interpolation='nearest')
plt.axis('off')
title = ax.set_title("Step 0")

def update(frame):
    global grid
    grid = next_step(grid)
    img.set_data(grid)
    title.set_text(f"Step {frame}")
    return [img, title]

ani = animation.FuncAnimation(
    fig, update, frames=5000, interval=100, blit=True
)

ani.save(f'game_of_life/Game_of_Life/output/{time.time()}.gif', writer='pillow')