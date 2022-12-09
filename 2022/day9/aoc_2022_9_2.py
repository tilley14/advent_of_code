# Advent of Code 2022, Day 9, Puzzle 1

import math

ret = 0

input = []

with open("test.txt") as f:
    input = [l.strip() for l in f.readlines() if l.strip()]


uniquePositions = set([(0, 0)])


KNOTS = []
for i in range(0, 10):
    KNOTS.append([0, 0])

print(KNOTS)

HEAD = 0
TAIL = 9
X = 0
Y = 1


def distance(x1: float, x2: float, y1: float, y2: float):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def draw():
    g = [["." for i in range(26)] for i in range(22)]
    # g = [["." for i in range(100)] for i in range(100)]

    for x, y in uniquePositions:
        g[15 - y][11 + x] = "x"
        # g[50 - y][50 + x] = "x"

    for i in reversed(range(10)):
        ch = str(i)
        if i == HEAD:
            ch = "H"
        # elif i == TAIL:
        #     ch = "T"
        x, y = KNOTS[i]

        # print("y{},x{}".format((15 - y), (11 + x)))
        g[15 - y][11 + x] = ch
        # g[50 - y][50 + x] = ch

    print("\n".join("".join(r) for r in g))
    print("\n")


def move(direction, steps):
    global KNOTS
    global uniquePositions
    remainingSteps = steps

    print(
        "====================== {} {} ======================\n\n".format(
            direction, steps
        )
    )

    while remainingSteps != 0:
        remainingSteps -= 1

        # Move head
        if direction == "U":
            KNOTS[HEAD][Y] += 1
        if direction == "D":
            KNOTS[HEAD][Y] -= 1
        if direction == "L":
            KNOTS[HEAD][X] -= 1
        if direction == "R":
            KNOTS[HEAD][X] += 1

        draw()

        for i in range(HEAD, TAIL):
            K1 = i
            K2 = i + 1

            if distance(
                KNOTS[K1][X], KNOTS[K2][X], KNOTS[K1][Y], KNOTS[K2][Y]
            ) > math.sqrt(2):

                dx = KNOTS[K1][X] - KNOTS[K2][X]
                dy = KNOTS[K1][Y] - KNOTS[K2][Y]

                if dy == 2:
                    KNOTS[K2][Y] += 1
                    KNOTS[K2][X] += dx
                elif dy == -2:
                    KNOTS[K2][Y] -= 1
                    KNOTS[K2][X] += dx
                elif dx == 2:
                    KNOTS[K2][Y] += dy
                    KNOTS[K2][X] += 1
                elif dx == -2:
                    KNOTS[K2][Y] += dy
                    KNOTS[K2][X] -= 1

                if K2 == TAIL:
                    uniquePositions.add((KNOTS[K2][X], KNOTS[K2][Y]))

                draw()
            else:
                break  # if the knot ahead didn't move, then no need to keep checking for move


draw()

for line in input:
    direction, step = line.split(" ")
    move(direction, int(step))

print(len(uniquePositions))
