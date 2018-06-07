from util import *

def GET(grid, x, y):
	return str(grid[y][x])

def SET(grid, x, y, val):
    grid[y][x] = val
    return toString(grid)
	
