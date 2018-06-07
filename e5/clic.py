# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:24:11 2018

@author: tp-b171_c4
"""

from util import *
from compact import *

def erase (T, x, y) :
    val = T[y][x] - 1
    eraseBis(T, val, x + 1, y, x, y)
    eraseBis(T, val, x - 1, y, x, y)
    eraseBis(T, val, x, y + 1, x, y)
    eraseBis(T, val, x, y - 1, x, y) 
    
def eraseBis (T, val, x, y, x0, y0) :
    if(not isInBound(x, y)) :
        return
    if (x != x0 or y != y0) and T[y][x] == val:
        T[y][x] = 0
        eraseBis(T, val, x + 1, y, x0, y0)
        eraseBis(T, val, x - 1, y, x0, y0)
        eraseBis(T, val, x, y + 1, x0, y0)
        eraseBis(T, val, x, y - 1, x0, y0)        
            
def isInBound(x, y) :
    return x >= 0 and x < 5 and y >=0 and y < 5 

def isGroup (grid, x, y):
  return ((y > 0 and grid[y-1][x]==grid[y][x]) or
          (y < 4 and grid[y+1][x]==grid[y][x]) or
          (x > 0 and grid[y][x-1]==grid[y][x]) or
          (x < 4 and grid[y][x+1]==grid[y][x+1]))


def CLIC (grid, x, y):
    if isGroup(grid, x, y) and grid[y][x] != 0 and grid[y][x] < 9:
        grid[y][x] += 1
        erase(grid, x, y)
        compact(grid)
    return toString(grid)

