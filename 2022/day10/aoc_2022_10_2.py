# Advent of Code 2022, Day 10, Puzzle 2

CYCLES = 0
X = 1
CTR_W = 40
CTR_H = 6
PIXES = ["" for i in range(CTR_H*CTR_W)]
LIT = "#"
DARK = "."


def overlaps():
    return CYCLES % CTR_W in [X-1, X, X+1]


def drawPix():
    PIXES[CYCLES] = LIT if overlaps() else DARK


def incrementCycles():
    global CYCLES
    drawPix()
    CYCLES += 1


def addV(v):
    global X
    incrementCycles()
    incrementCycles()
    X += v


def noop():
    incrementCycles()


INPUT = []

with open("input.txt") as f:
    INPUT = [l.strip() for l in f.read().splitlines() if l.strip()]


for l in INPUT:
    instruction = l.split(" ")
    if (instruction[0] == "noop"):
        noop()
    elif instruction[0] == "addx":
        addV(int(instruction[1]))


img = [["" for i in range(CTR_W)] for i in range(CTR_H)]
x = y = 0
for i in range(0, len(PIXES)):
    x = i % CTR_W
    y = i // CTR_W
    img[y][x] = PIXES[i]

print("\n".join("".join(r) for r in img))
