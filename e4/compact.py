# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:54:13 2018

@author: tp-b171_c4
"""

def compact (T) :
    for i in range (5) :
        last = -1
        if j in range (5, 0, -1) :
            if T[j][i] == 0 and last == -1:
                last = j
            if T[j][i] != 0 and last != -1:
                T[last][i], T[j][i] = T[j][i], 0
                j, last = last, -1
                
            