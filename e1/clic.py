from util import *

def isGroup (grid, x, y):
  return ((y > 0 and grid[y-1][x]==grid[y][x]) or
          (y < 4 and grid[y+1][x]==grid[y][x]) or
          (x > 0 and grid[y][x-1]==grid[y][x]) or
          (x < 4 and grid[y][x+1]==grid[y][x+1]))


def CLIC (grid, x, y):
    if isGroup(grid, x, y) and grid[y][x] != 0 and grid[y][x] < 9:
        grid[y][x] += 1
    return toString(grid)

