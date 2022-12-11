# Advent of Code 2022, Day 8, Puzzle 1

ret = 0


grid = []
with open("input.txt") as f:
    grid = [[t for t in r.strip()] for r in f.readlines() if r.strip()]

rows = len(grid)
cols = len(grid[0])

ret = ((rows + cols) * 2) - 4 # perimeter trees

def isVisible(r, c):
    global grid
    val = grid[r][c]
    
    top = max([grid[rr][c] for rr in range(0, r)])
    bot = max([grid[rr][c] for rr in range(r+1, rows)])
    left = max([grid[r][cc] for cc in range(0, c)])
    right = max([grid[r][cc] for cc in range(c+1, cols)])
    
    return val > min(top, bot, left, right)


for r in range(1, len(grid) - 1):
    for c in range (1, len(grid[0]) - 1):
        if isVisible(r,c):
            ret += 1


print(ret)
