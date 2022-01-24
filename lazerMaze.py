def get_coord(box_num, dim):
    row = box_num // dim
    col = box_num % dim
    return (row, col)

grids = []
def populate_grid(grid, dim, pos):
    if pos == dim*dim:
        grids.append(list(grid))
    for i in range(pos, dim*dim):
        row, col = get_coord(i, dim)
        for choice in ['L', 'R']:
            grid[row][col] = choice
            populate_grid(grid, dim, pos+1)

def createMaze(dim):
    grid = [[None] * dim for i in range(dim)]
    populate_grid(grid, dim, 0)

def is_open_maze(grid, dim, col, row):
    if col >= 0 or col < dim and row >= dim:
        return True
    
    if row >= dim or row < 0 or col >= dim or col < 0:
        return False

    if grid[row][col] == 'L':
        return is_open_maze(grid, dim, row, col+1)
    else:
        return is_open_maze(grid, dim, row, col-1)

def calculate_open_mazes(grid, dim):
    num_of_open_mazes = 0
    for i in range(dim):
        if is_open_maze(grid, dim, i, 0):
            num_of_open_mazes += 1
    
    return num_of_open_mazes

createMaze(3)
createMaze(4)

for grid in grids:
    calculate_open_mazes(grid, 3)
    calculate_open_mazes(grid, 4)