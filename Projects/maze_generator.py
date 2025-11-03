#BH 2nd maze_generator.py

import random
import turtle
screen = turtle.Screen()
screen.setup(1000,1000)
grid = []
#Maze needs to be at least 6x6 

def create_wall():
    wall_artist = turtle.Turtle()
    wall_artist.penup()
    wall_artist.setpos(100,100)
    wall_artist.pendown()
    wall_artist.forward(600)
    wall_artist.right(90)
    wall_artist.forward(600)
    wall_artist.right(90)
    wall_artist.forward(600)
    wall_artist.right(90)
    wall_artist.forward(600)
    wall_artist.right(90)
create_wall()

def create_maze():
    maze_artist = turtle.Turtle()
    maze_artist.penup()


def create_maze_grid(rows, cols):
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
create_maze_grid(6,6)

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

        for direction in directions:
            target_cell_row = None
            target_cell_col = None

            if direction == "up" and row > 0:
                target_cell_row = row - 1
                target_cell_col = col
            elif direction == "down" and row < len(grid) - 1:
                target_cell_row = row + 1
                target_cell_col = col
            elif direction == "left" and col > 0:
                target_cell_row = row
                target_cell_col = col - 1
            elif direction == "right" and col < len(grid[0]) - 1:
                target_cell_row = row
                target_cell_col = col + 1
            else:
                continue
        current_cell = grid[row][col]
        target_cell = grid[target_cell_row][target_cell_col]
        if target_cell in grid:
            if not moved:
                route.pop()
                route += target_cell
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



# cell = {
#     "visited": True, 
#     "walls": {
#         "top": False, 
#         "bottom": True, 
#         "left": False, 
#         "right": True
#     }
# }

turtle.done()