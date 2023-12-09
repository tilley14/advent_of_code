# Advent of Code 2022, Day 12, Puzzle 1
from collections import deque

lowest = ord('a')
highest = ord('z')

elevations = {
    "S": lowest,
    "E": highest
}

for o in range(lowest, highest + 1):
    elevations[chr(o)] = o


grid = []
with open("input.txt") as f:
    grid = [[c for c in line] for line in f.read().strip().splitlines()]


START = ()
END = ()
for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        if grid[y][x] == "S":
            START = (x, y)
        elif grid[y][x] == "E":
            END = (x, y)


q = deque()
q.append((0, START[0], START[1]))

VISITED = set()
VISITED.add((START[0], START[1]))


while q:
    d, x, y = q.popleft()
    # print(f"x,y {(x,y)}")

    for xx, yy in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:  # right, down, left, up
        # valid next move
        if xx < 0 or xx > len(grid[0]) - 1 or yy < 0 or yy > len(grid) - 1:
            continue

        if (xx, yy) in VISITED:  # repeats
            continue

        if elevations[grid[yy][xx]] > elevations[grid[y][x]] + 1:
            continue

        if grid[yy][xx] == "E":
            print("AT END")
            print(d+1)
            break

        VISITED.add((xx, yy))
        q.append((d + 1, xx, yy))
