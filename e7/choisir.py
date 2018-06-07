from groupes import groupes

def choisir_coup(grid):
	choisir(groupes(grid), grid)

def choisir(tab, grid):
	#On garde les groupes de valeurs max
	max = 0
	for t in tab:
		if grid[t[0][1]][t[0][0]] > max:
			max = grid[t[0][1]][t[0][0]]
	T = []	
	for t in tab:
		if grid[t[0][1]][t[0][0]] == max:
			T.append(t)
	#On garde les plus grands groupes	
	max = 0	
	for t in T:
		if len(t) > max:
			max = len(t)
	T2 = []
	for t in T:
		if len(t) == max:
			T2.append(t)	
	#On garde les cases les plus basses
	max = 0
	for t in T2:
		for case in t:
			x,y = case
			if y > max:
				max = y
	T3 = []	
	for t in T2:
		for case in t:
			x,y = case
			if y == max:
				T3.append([x,y])
	Y = max
	#On garde les cases les plus à droites
	X = -1	
	for case in T3:
		x,y = case
		if x > X:
			X = x
	print("CLIC " + str(X) + " " + str(Y)) 
			
	

