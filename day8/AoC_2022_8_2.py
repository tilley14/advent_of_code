# Advent of Code 2022, Day 8, Puzzle 2

ret = 0

grid = []

with open("input.txt") as f:
    grid = [[t for t in r.strip()] for r in f.readlines() if r.strip()]

rows = len(grid)
cols = len(grid[0])


def scenicScore(r, c):
    global grid
    val = grid[r][c]

    top = 0
    bot = 0
    left = 0
    right = 0

    for v in [grid[rr][c] for rr in range(0, r)][::-1]:
        top += 1
        if v >= val:
            break

    for v in [grid[rr][c] for rr in range(r + 1, rows)]:
        bot += 1
        if v >= val:
            break

    for v in [grid[r][cc] for cc in range(0, c)][::-1]:
        left += 1
        if v >= val:
            break

    for v in [grid[r][cc] for cc in range(c + 1, cols)]:
        right += 1
        if v >= val:
            break

    return top * bot * left * right


scores = []
for r in range(0, len(grid)):
    for c in range(0, len(grid[0])):
        scores.append(scenicScore(r, c))


print(max(scores))
