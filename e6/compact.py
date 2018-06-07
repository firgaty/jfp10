# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 11:54:13 2018

@author: tp-b171_c4
"""

def compact (T) :
    for i in range (5) :
        last = -1
        j = 4
        while j >= 0 :
            if T[j][i] == 0 and last == -1:
                last = j
            if T[j][i] != 0 and last != -1:
                T[last][i], T[j][i] = T[j][i], 0
                j, last = last, -1
            j -= 1 
                
def revCompact (T):
    for i in range (5) :
        last = -1
        j = 0
        while j < len(T) :
            if T[j][i] == 0 and last == -1:
                last = j
            if T[j][i] != 0 and last != -1:
                T[last][i], T[j][i] = T[j][i], 0
                j, last = last, -1
            j += 1 
