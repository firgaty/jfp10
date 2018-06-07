from util import *

def GET(grid, x, y):
	return grid[y][x]

def SET(grid, x, y, val):
    grid[y][x] = val
    return toString(grid)
	
