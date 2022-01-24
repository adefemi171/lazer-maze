from copy import deepcopy
def get_coord(box_num, dim):
    row = box_num // dim
    col = box_num % dim
    return (row, col)

grids = []
def populate_grid(grid, dim, pos):
    print(pos, len(grids), "HERE")
    if pos > dim*dim: return
    if pos == dim*dim:
        grids.append(deepcopy(grid))
        return
    
    row, col = get_coord(pos, dim)
    for choice in ['L', 'R']:
        grid[row][col] = choice
        populate_grid(grid, dim, pos+1)

def createMaze(dim):
    grid = [[None] * dim for i in range(dim)]
    populate_grid(grid, dim, 0)

def is_open_maze(grid, dim, col, row, last_direction):
    if (col >= 0 or col < dim) and row >= dim:
        return True
    
    if row >= dim or row < 0 or col >= dim or col < 0:
        return False

    if grid[row][col] == 'L':
        if last_direction == 'R': return False
        if last_direction == 'L':
            return is_open_maze(grid, dim, row+1, col, 'L')
        return is_open_maze(grid, dim, row, col+1, 'L')
    else:
        if last_direction == 'L':
            return False
        if last_direction == 'R':
            return is_open_maze(grid, dim, row+1, col, 'R')
        return is_open_maze(grid, dim, row, col-1, 'R')

    return False

def calculate_open_mazes(grid, dim):
    for i in range(dim):
        if is_open_maze(grid, dim, i, 0, 'X'):
            return True
    return False
# calculate_open_mazes([['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']], 3)

if __name__ == '__main__':
    dimensions = int(input("please put the grid's dimensions: "))
    createMaze(dimensions)
    result = 0

    for grid in grids:
        if calculate_open_mazes(grid, dimensions) > 0:
            result += 1

    print("The number of open mazes is", result)