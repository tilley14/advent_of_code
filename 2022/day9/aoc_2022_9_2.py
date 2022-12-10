# Advent of Code 2022, Day 9, Puzzle 1

import math
import os
from time import sleep
import signal

ret = 0

INPUT = []

FN = "test.txt"
with open(FN) as f:
    INPUT = [l.strip() for l in f.readlines() if l.strip()]


uniquePositions = set([(0, 0)])


KNOTS = []
for i in range(0, 10):
    KNOTS.append([0, 0])


HEAD = 0
TAIL = 9
X = 0
Y = 1


def distance(x1: float, x2: float, y1: float, y2: float):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def draw(onlyXs):
    # if "test" not in FN:
    #     return

    # gX = gY = 31
    # mX = mY = 31 // 2

    gX = gY = 81
    mX = mY = 81 // 2

    g = [["." for i in range(gX)] for i in range(gY)]

    for x, y in uniquePositions:
        g[mY - y][mX + x] = "x"

    if not onlyXs:
        for i in reversed(range(10)):
            ch = str(i)
            if i == HEAD:
                ch = "H"
            # elif i == TAIL:
            #     ch = "T"
            x, y = KNOTS[i]

            # print("y{},x{}".format((mY - y), (mX + x)))
            g[mY - y][mX + x] = ch


    os.system("cls")
    print("\n".join("".join(r) for r in g))
    # print("\n")
    sleep(.1)



def move(direction, steps):
    global KNOTS
    global uniquePositions
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
                    uniquePositions.add((KNOTS[K2][X], KNOTS[K2][Y]))

                draw(False)
            else:
                break  # if the knot ahead didn't move, then no need to keep checking for move


def handleExit(signum, frame):
    print("Exit y/n?")
    answer = input()
    if answer == 'y':
        exit(1)


signal.signal(signal.SIGINT, handleExit)


draw(False)
print("You might want to make your font smaller (Enter to continue...)")
input()

for line in INPUT:
    direction, step = line.split(" ")
    move(direction, int(step))

# print(len(uniquePositions))

draw(True)

print("Now count the Xs if you want your answer bud...")
