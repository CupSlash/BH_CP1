#BH 2nd maze_generator.py

import random
import turtle
num_rows = 100
num_cols = 100
screen_width = 1000
screen_height = 1000
screen = turtle.Screen()
screen.setup(screen_width, screen_height)
#Maze needs to be at least 6x6 

def create_maze_grid(rows, cols):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            cell = {
                "visited": False,
                "walls": {
                    "top": True,
                    "bottom": True,
                    "left": True,
                    "right": True
                }
            }
            row.append(cell)
        grid.append(row)
    return grid
grid = create_maze_grid(num_rows,num_cols)

def create_route(grid):
    route = []
    start_coords = (0, 0)
    start_cell = grid[start_coords[0]][start_coords[1]]
    start_cell["visited"] = True
    route.append(start_coords)
    while len(route) > 0:
        current_cell_coords = route[-1]
        row, col = current_cell_coords
        directions = ["up", "down", "left", "right"]
        random.shuffle(directions)
        moved = False
        current_cell = grid[row][col]
        new_cell = None

        for direction in directions:
            candidate_cell_row = None
            candidate_cell_col = None

            if direction == "up" and row > 0:
                candidate_cell_row = row - 1
                candidate_cell_col = col
            elif direction == "down" and row < len(grid) - 1:
                candidate_cell_row = row + 1
                candidate_cell_col = col
            elif direction == "left" and col > 0:
                candidate_cell_row = row
                candidate_cell_col = col - 1
            elif direction == "right" and col < len(grid[0]) - 1:
                candidate_cell_row = row
                candidate_cell_col = col + 1
            else:
                pass

            if candidate_cell_row is None or candidate_cell_col is None:
                continue

            candidate_cell = grid[candidate_cell_row][candidate_cell_col]

            if candidate_cell["visited"]:
                continue
            else:
                new_cell = candidate_cell
                new_cell_coords = (candidate_cell_row, candidate_cell_col)

                if direction == "up":
                    current_cell["walls"]["top"] = False
                    new_cell["walls"]["bottom"] = False
                elif direction == "down":
                    current_cell["walls"]["bottom"] = False
                    new_cell["walls"]["top"] = False
                elif direction == "left":
                    current_cell["walls"]["left"] = False
                    new_cell["walls"]["right"] = False
                elif direction == "right":
                    current_cell["walls"]["right"] = False
                    new_cell["walls"]["left"] = False
                else:
                    pass

                new_cell["visited"] = True
                route.append(new_cell_coords)
                moved = True
                break

        if moved == False:
            route.pop() 

create_route(grid)

# Use nested loops to create a list of lists representing the maze grid (outer list will be rows, inner lists will be columns)
# Each cell in the grid can be represented as a dictionary
# - Cell has properties like 'visited' (boolean) and 'walls' (with properties top, bottom, left, right which are booleans)
# Start at top-left cell of the maze
# Create route list to keep track of the path taken (initially contains starting cell)
# Loop until route list is empty:
# - Choose a random direction (up, down, left, right) to create a path
# - Check if the chosen direction is valid (has a removable wall and the target cell has not been visited)
# - If we can move in the chosen direction, remove the wall from the current cell and the target cell, mark the target cell as visited, add the target cell to the route
# - If we cannot move in the chosen direction, choose a different direction
# - If all directions are blocked, backtrack to the previous cell and try again
# Set the top wall of the top-left cell to False
# Set the bottom wall of the bottom-right cell to False
# Draw the maze using the cell wall information

# Functions
# - create_maze_grid(rows, cols)
# - create_route(grid)
# - draw_maze(grid)
# - find_target_cell(current_cell, direction, grid)

def draw_maze(grid, screen_width, screen_height):
    # Speed up drawing
    turtle.speed(0)
    turtle.tracer(0)
    turtle.hideturtle()
    
    turtle.penup()
    smallest_dimension = min(screen_width, screen_height)
    num_rows = len(grid)
    num_cols = len(grid[0])
    cell_size = smallest_dimension / max(num_rows, num_cols) * 0.8
    start_x = (num_cols * cell_size) / -2
    start_y = (num_rows * cell_size) / 2

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            cell = grid[row][col]
            x = start_x + col * cell_size
            y = start_y - row * cell_size
            turtle.goto(x, y)

            if cell["walls"]["top"]:
                turtle.pendown()
                turtle.goto(x + cell_size, y)
                turtle.penup()
                turtle.goto(x, y)

            if cell["walls"]["right"]:
                turtle.goto(x + cell_size, y)
                turtle.pendown()
                turtle.goto(x + cell_size, y - cell_size)
                turtle.penup()
                turtle.goto(x, y)

            if cell["walls"]["bottom"]:
                turtle.goto(x + cell_size, y - cell_size)
                turtle.pendown()
                turtle.goto(x, y - cell_size)
                turtle.penup()
                turtle.goto(x, y)

            if cell["walls"]["left"]:
                turtle.goto(x, y - cell_size)
                turtle.pendown()
                turtle.goto(x, y)
                turtle.penup()
    turtle.update()
    

# Set entrance and exit
grid[0][0]["walls"]["left"] = False
grid[-1][-1]["walls"]["right"] = False

draw_maze(grid, screen_width, screen_height)

turtle.done()