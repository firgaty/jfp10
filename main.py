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
		GET(grid, commande[1], commande[2])
	elif commande[0] == "SET":
		SET(grid, commande[1], commande[2], commande[3])
	elif commande[0] == "CLIC":
		CLIC(grid, commande[1], commande[2])

