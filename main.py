import sys
from sg import *

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
	
	commande = lignes[5].split(" ")
	if commande[0] == "GET":
		print(GET(grid, int(commande[1]), int(commande[2])))
	elif commande[0] == "SET":
		print(SET(grid, int(commande[1]), int(commande[2]), int(commande[3])), end="")

lines = ""
for line in sys.stdin:
  lines += line

read(lines)

