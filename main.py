# IMPORTS
from misc import *
import matplotlib.pyplot as plt

# VARIABLES INITIALIZATION
is_playing = True
step = 0

grid = init_grid_random(size = 200)

# INITIALIZE THE GAME FIGURE
plt.ion()  
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='gray', interpolation='nearest')
plt.axis('off')
title = ax.set_title(f"Step {step}")

# GAME LOOP
while is_playing:
    grid = next_step(grid).copy()
    step += 1

    img.set_data(grid)
    title.set_text(f"Step {step}")
    plt.draw()
    plt.pause(0.1)  

    if step >= 500:
        is_playing = False

# END OF GAME
plt.ioff()
plt.imshow(grid, cmap='gray', interpolation='nearest')
plt.title(f"Step {step}")
plt.axis('off')
plt.show()