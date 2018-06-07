# -*- coding: utf-8 -*-

import erase

def isInBoundBis(x, y) :
    return x >= 0 and x < 5 and y >=0 and y < 5

def groupes (T) :
    # Copy of the array with a bool added
    T2 = []    
    for j in range (5) :
        Temp = []
        for i in range (5) :
           Temp2 = [0, False]
           Temp2[0] = T[j][i]
           Temp.append(Temp2)
        T2.append(Temp)
        
    return splitGroupes(T2)
        
def splitGroupes (T) :
    grps = []
    for j in range(5) :
        for i in range(5) :
            if(T[j][i][1] == False) :
                grp = []
                getGroupe (T, grp, T[j][i][0], i, j)
                grps.append(grp)
    
    return grps
        
def getGroupe (T, grp, val, x, y) :
    if(not isInBoundBis(x, y)) : 
        return
    if(T[y][x][1] != True and T[y][x][0] == val) :
        grp.append([x, y])
        T[y][x][1] = True
        
        getGroupe(T, grp, val, x + 1, y)
        getGroupe(T, grp, val, x - 1, y)
        getGroupe(T, grp, val, x, y + 1)
        getGroupe(T, grp, val, x, y - 1)


     
#test = [[1,2,3,4,1], [1,1,1,1,1], [2,2,2,2,2], [1,1,1,2,1], [1,2,3,1,2]]
#
#print (groupes(test))