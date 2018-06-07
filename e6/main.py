import sys
from util import *
from sg import *
from clic import *
from choisir import choisir_coup

def getReserve(lignes, n, k):
    reserve = []
    for i in range(k, k+n):
        tab = []
        for j in range(5):
            if lignes[k][j] != ".":			
                tab.append(int(lignes[i][j]))
            else : 
                tab.append(0)
        reserve.append(tab)
    return reserve

def contient(grid, n):
	for i in range(5):
		for j in range(5):
			if grid[i][j] == n:
				return True
	return False

def score(grid, reserve, n):
	while not contient(grid, n):
		x, y = choisir_coup(grid)
		CLIC(grid, x, y, reserve)

def read(str):
    lignes = str.split("\n")
    grid = []
    reserve = []
    for i in range(5):
        tab = []
        for j in range(5):
            if lignes[i][j] != ".":			
                tab.append(int(lignes[i][j]))
            else : 
                tab.append(0)
        grid.append(tab)
	
    res = ""
    if len(lignes) == 5:
        choisir_coup(grid)
    i = 5
    while i < len(lignes):	
        commande = lignes[i].split(" ")
        if commande[0] == "GET":
            res = GET(grid, int(commande[1]), int(commande[2])) + "\n"
        elif commande[0] == "SET":
            res = SET(grid, int(commande[1]), int(commande[2]), int(commande[3]))
        elif commande[0] == "CLIC":
            res = CLIC(grid, int(commande[1]), int(commande[2]), reserve)
        elif commande[0] == "RESERVE":
            reserve = getReserve(lignes, int(commande[1]), i+1)
            i += int(commande[1])
        elif commande[0] == "SCORE":
            score(grid, reserve, int(commande[1]))
        i += 1
    print(res, end="")

lines = ""
for line in sys.stdin:
    lines += line

read(lines)

