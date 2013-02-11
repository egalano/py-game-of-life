import random

def oscillator(grid):
    grid[5][5].create()
    grid[6][5].create()
    grid[7][5].create()

def block(grid):
    for y in xrange(len(grid)/8, len(grid) - len(grid)/ 8):
        for x in xrange(len(grid[y])/8,len(grid) - len(grid)/8):
            grid[y][x].create()

def toad(grid):
    raise NotImplementedError

def boat(grid):
    raise NotImplementedError

def tug(grid):
    raise NotImplementedError

def square(grid, height, width):
    raise NotImplementedError

def rand(grid):
    for row in grid:
        for cell in row:
            if random.getrandbits(1):
                cell.create()
