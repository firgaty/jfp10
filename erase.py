# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:24:11 2018

@author: tp-b171_c4
"""

def erase (T, x, y) :
    val = T[x][y]
    eraseBis(T, val, x + 1, y, x, y)
    eraseBis(T, val, x - 1, y, x, y)
    eraseBis(T, val, x, y + 1, x, y)
    eraseBis(T, val, x, y - 1, x, y) 
    
def eraseBis (T, val, x, y, x0, y0) :
    if(!isInBound(x, y)) :
        return
    if(x != x0 and y != y0 and T[y][x] == val) :
        T[y][x] = 0
        eraseBis(T, val, x + 1, y, x0, y0)
        eraseBis(T, val, x - 1, y, x0, y0)
        eraseBis(T, val, x, y + 1, x0, y0)
        eraseBis(T, val, x, y - 1, x0, y0)        
            
def isInBound(x, y) :
    return x >= 0 and x < 5 and y >=0 and y < 5 