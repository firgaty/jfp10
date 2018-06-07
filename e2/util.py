def toString (grid):
    s = ""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
                  c = grid[i][j]
                  s += str(c) if c != 0 else "."
        s += "\n"
    return s
