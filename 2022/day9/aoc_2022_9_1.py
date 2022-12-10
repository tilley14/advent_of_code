# Advent of Code 2022, Day 9, Puzzle 1

import math

ret = 0

input = []

with open("input.txt") as f:
    input = [l.strip() for l in f.readlines() if l.strip()]


uniquePositions = set([(0, 0)])

hx = hy = 0
tx = ty = 0


def distance(x1: float, x2: float, y1: float, y2: float):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def move(direction, steps):
    global hx
    global hy
    global tx
    global ty
    global uniquePositions
    remainingSteps = steps

    while remainingSteps != 0:
        remainingSteps -= 1

        if direction == "U":
            hy += 1
        if direction == "D":
            hy -= 1
        if direction == "L":
            hx -= 1
        if direction == "R":
            hx += 1

        if distance(hx, tx, hy, ty) > math.sqrt(2):
            if direction == "U":
                ty = hy - 1
                tx = hx
            if direction == "D":
                ty = hy + 1
                tx = hx
            if direction == "L":
                tx = hx + 1
                ty = hy
            if direction == "R":
                tx = hx - 1
                ty = hy

            uniquePositions.add((tx, ty))


for line in input:
    direction, step = line.split(" ")
    move(direction, int(step))


print(len(uniquePositions))
