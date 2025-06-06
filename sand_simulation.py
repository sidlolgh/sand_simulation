import py5
import random

width, height = 500, 500
size = 10
columns = width // size
rows = height // size

grid = [[0 for _ in range(columns)] for _ in range(rows)]


def setup():
    py5.size(500, 500)
    py5.background(255)

def draw():
    global grid

    for i in range(columns):
        for j in range(rows):
            if grid[i][j] == 1:
                py5.fill(0)
            else:
                py5.fill(255,255,255)

            py5.rect(i * size, j * size, size, size)
    
    next_grid = [[0 for _ in range(columns)] for _ in range(rows)]

    for i in range(columns):
        for j in range(rows):
            if grid[i][j] == 1:
                # Fall straight down
                if j + 1 < rows and grid[i][j + 1] == 0:
                    next_grid[i][j + 1] = 1
                else:
                    # Try diagonals in random order
                    directions = [1, -1]
                    random.shuffle(directions)
                    moved = False
                    for dir in directions:
                        ni = i + dir
                        if 0 <= ni < columns and j + 1 < rows and grid[ni][j + 1] == 0:
                            next_grid[ni][j + 1] = 1
                            moved = True
                            break
                    if not moved:
                        next_grid[i][j] = 1  # Stay in place
    grid = next_grid


def set_sand_at_mouse():
    x = py5.mouse_x // size
    y = py5.mouse_y // size
    if 0 <= x < columns and 0 <= y < rows:
        grid[x][y] = 1


def mouse_pressed():
    set_sand_at_mouse()

def mouse_dragged():
    set_sand_at_mouse()
  
py5.run_sketch()
