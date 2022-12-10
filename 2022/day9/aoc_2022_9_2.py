# Advent of Code 2022, Day 9, Puzzle 1

import math
import os
from time import sleep
import signal

ret = 0

INPUT = []

FN = "input.txt"
with open(FN) as f:
    INPUT = [l.strip() for l in f.readlines() if l.strip()]


UNIQUE_POINTS = set([(0, 0)])


GX = 80  # 31
GY = 31
MX = GX // 2
MY = GY // 2

KNOTS = []
for i in range(0, 10):
    KNOTS.append([0, 0])


# rope head is the center
MOVING_CENTER = True
CENTER = [MX, MY]
MARGIN = 2

HEAD = 0
TAIL = 9
X = 0
Y = 1


def distance(x1: float, x2: float, y1: float, y2: float):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def doRender(x, y):
    return (0 <= x < GX) and (0 <= y < GY)


def draw(onlyXs):
    # if "test" not in FN:
    #     return

    g = [["." for i in range(GX)] for i in range(GY)]

    for x, y in UNIQUE_POINTS:
        if doRender(CENTER[X] + x, CENTER[Y] - y):
            g[CENTER[Y] - y][CENTER[X] + x] = "x"

    if not onlyXs:
        for i in reversed(range(10)):
            ch = str(i)
            if i == HEAD:
                ch = "H"
            # elif i == TAIL:
            #     ch = "T"
            x, y = KNOTS[i]

            if doRender(CENTER[X] + x, CENTER[Y] - y):
                g[CENTER[Y] - y][CENTER[X] + x] = ch

    os.system("cls")
    print("\n".join("".join(r) for r in g))
    print("\n")
    sleep(.02)


def move(direction, steps):
    global KNOTS
    global UNIQUE_POINTS
    global CENTER
    remainingSteps = steps

    # print(
    #     "====================== {} {} ======================\n\n".format(
    #         direction, steps
    #     )
    # )

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

        if MOVING_CENTER:
            if direction == "U" and CENTER[Y] - KNOTS[HEAD][Y] < MARGIN:
                CENTER[Y] += 1
            if direction == "D" and CENTER[Y] - KNOTS[HEAD][Y] >= GY - MARGIN:
                CENTER[Y] -= 1
            if direction == "L" and CENTER[X] + KNOTS[HEAD][X] < MARGIN:
                CENTER[X] += 1
            if direction == "R" and CENTER[X] + KNOTS[HEAD][X] >= GX - MARGIN:
                CENTER[X] -= 1

        draw(False)

        for i in range(HEAD, TAIL):
            K1 = i
            K2 = i + 1

            if distance(
                KNOTS[K1][X], KNOTS[K2][X], KNOTS[K1][Y], KNOTS[K2][Y]
            ) > math.sqrt(2):

                dx = KNOTS[K1][X] - KNOTS[K2][X]
                dy = KNOTS[K1][Y] - KNOTS[K2][Y]

                if abs(dy) == 2 and abs(dx) == 2:  # diagonal move
                    KNOTS[K2][Y] += dy // 2
                    KNOTS[K2][X] += dx // 2
                elif abs(dy) > abs(dx):  # Up/Down
                    KNOTS[K2][Y] += dy // 2
                    KNOTS[K2][X] += dx
                elif abs(dy) < abs(dx):  # Left/Right
                    KNOTS[K2][Y] += dy
                    KNOTS[K2][X] += dx // 2

                if K2 == TAIL:
                    UNIQUE_POINTS.add((KNOTS[K2][X], KNOTS[K2][Y]))

                draw(False)
            else:
                break  # if the knot ahead didn't move, then no need to keep checking for move


def handleExit(signum, frame):
    print("Exit y/n?")
    answer = input()
    if answer.lower() == 'y':
        exit(1)


signal.signal(signal.SIGINT, handleExit)

draw(False)

for line in INPUT:
    direction, step = line.split(" ")
    move(direction, int(step))

# print(len(UNIQUE_POINTS))

draw(True)

print("Now count the Xs if you want your answer bud...")


# minx = min([x for x, _ in UNIQUE_POINTS])
# maxx = max([x for x, _ in UNIQUE_POINTS])
# miny = min([y for _, y in UNIQUE_POINTS])
# maxy = max([y for _, y in UNIQUE_POINTS])

# lx = maxx - minx + 1
# ly = maxy - miny + 1

# dx = 0 - minx
# dy = 0 - miny

# g = [["." for i in range(lx)] for i in range(ly)]
# for x, y in UNIQUE_POINTS:
#     g[dy + y][dx + x] = "x"

# print("\n".join("".join(r) for r in g))
