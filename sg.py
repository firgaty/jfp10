def GET(grid, x, y):
	return grid[y][x]

def SET(grid, x, y, val):
    grid[y][x] = val
    s = ""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
			      s += str(grid[i][j])
        s += "\n"
    return s
	
	
	
	
