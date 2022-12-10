# Advent of Code 2022, Day 10, Puzzle 1

CYCLES = 0
X = 1
SIG_STRENGTH = []


def sigStr():
    return CYCLES * X


def incrementCycles():
    global CYCLES
    CYCLES += 1
    if (CYCLES % 20 == 0):
        print("c{} x{} ss {}".format(CYCLES, X, sigStr()))
        SIG_STRENGTH.append(sigStr())


def addV(v):
    global x
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


print(sum(SIG_STRENGTH[0:12:2]))
print(len(SIG_STRENGTH[0:12:2]))
