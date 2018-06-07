import sys
from util import *
from sg import *
from clic import *

def read(str):
    lignes = str.split("\n")
    grid= []
    for i in range(5):
        tab = []
        for j in range(5):
            if lignes[i][j] != ".":			
                tab.append(int(lignes[i][j]))
            else : 
                tab.append(0)
        grid.append(tab)

    res = ""
    for i in range(5, len(lignes)):
        commande = lignes[i].split(" ")
        if commande[0] == "GET":
            res = GET(grid, int(commande[1]), int(commande[2])) + "\n"
        elif commande[0] == "SET":
            res = SET(grid, int(commande[1]), int(commande[2]), int(commande[3]))
        elif commande[0] == "CLIC":
            res = CLIC(grid, int(commande[1]), int(commande[2]))
    print(res, end="")

lines = ""
for line in sys.stdin:
    lines += line

read(lines)

