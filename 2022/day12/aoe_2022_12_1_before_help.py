# Advent of Code 2022, Day 12, Puzzle 1

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


VISITED = set()
PATH = []
DIRECTIONS = []


def walk(x, y):
    VISITED.add((x, y))
    PATH.append((x, y))

    # print(f"x,y {(x,y)}")

    if grid[y][x] == "E":
        print("AT END")
        return True

    for xx, yy in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:  # right, down, left, up

        direction = ">" if (xx, yy) == (x + 1, y) else "v" if (xx,
                                                               yy) == (x, y + 1) else "<" if (xx, yy) == (x - 1, y) else "^"

        # valid next move
        if xx in range(0, len(grid[0])) and yy in range(0, len(grid)):
            if (xx, yy) not in VISITED:  # No going back
                if elevations[grid[yy][xx]] <= elevations[grid[y][x]] + 1:
                    DIRECTIONS.append(direction + " " + grid[yy][xx])
                    if walk(xx, yy):
                        return True
                    else:
                        # print("POP")
                        PATH.pop()
                        DIRECTIONS.pop()
                        VISITED.remove((xx, yy))

    # ALL Directions exhausted
    return False


walk(*START)


print(PATH)
print(DIRECTIONS)
print(len(PATH) - 1)  # Dont count starting position
