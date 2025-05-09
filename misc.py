import numpy as np

def init_grid_random(size = 100):
    grid = np.zeros((size,size))
    num_random_spots = int(size * size * 0.1)  # Adjust the percentage (e.g., 0.1 for 10%)
    random_index = np.random.choice(size * size, num_random_spots, replace=False)
    grid.flat[random_index] = 1
    return grid

def next_step(grid):
    next_grid = np.zeros(grid.shape)
    population = np.argwhere(grid == 1)
    already_checked = []

    for alive in population :
        alive = tuple(alive)
        already_checked.append(alive)

        neighborhood = get_neighbors(alive,grid)
        neighbors_nb = alive_neighbours_count(neighborhood,grid)

        if neighbors_nb < 2:
            next_grid[alive] = 0
        elif neighbors_nb > 3:
            next_grid[alive] = 0
        elif neighbors_nb == 3 or neighbors_nb == 2:
            next_grid[alive] = 1
        
        for neighbor in neighborhood:
            neighbor = tuple(neighbor)
            if grid[neighbor] == 0 and neighbor not in already_checked:
                already_checked.append(neighbor)
                neighbor_s_hood = get_neighbors(neighbor,grid)
                neighbors_nb = alive_neighbours_count(neighbor_s_hood,grid)
                if neighbors_nb == 3:
                    next_grid[neighbor] = 1
                else :
                    next_grid[neighbor] = 0
    return next_grid


def get_neighbors(alive, grid):
    x, y = alive
    neighbors = []
    rows, cols = grid.shape

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbors.append((nx, ny))
    
    return neighbors

def alive_neighbours_count(neighbors, grid):
    count = 0
    for neighbor in neighbors:
        if grid[neighbor] == 1:
            count += 1
    return count