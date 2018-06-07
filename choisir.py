def choisir(tab, grid):
	#On garde les plus grands groupes	
	max = 0	
	for t in tab:
		if len(t) > max:
			max = len(t)
	T = []
	for t in tab:
		if len(t) == max:
			T.append(t)
	for t in T
	#On garde les groupes de valeurs max
	max = 0
	for t in T:
		if grid[t[0][1]][t[0][0]] > max:
			max = grid[t[0][1]][t[0][0]]
	T2 = []	
	for t in T:
		if grid[t[0][1]][t[0][0]] == max
			T2.append(t)
	#On garde les cases les plus basses
	max = 0
	for t in T2:
		for (x,y) in t:
			if y > max:
				maxY = y
	T3 = []	
	for t in T2:
		for (x,y) in t:
			if y == max:
				T3.append([x,y])
	Y = max
	#On garde les cases les plus à droites
	X = -1	
	for t in T3:
		for (x,y) in t:
			if x > X:
				X = x
	print("CLIC " + str(X) + " " + str(Y)) 
			
	

