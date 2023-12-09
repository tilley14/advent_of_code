# Advent of Code 2022, Day 5, Puzzle 1

STACKS = [[c for c in "dtwnl"[::-1]], 
          [c for c in "hpc"[::-1]],
          [c for c in "jmgdnhpw"[::-1]],
          [c for c in "lqtnswc"[::-1]], 
          [c for c in "nchp"[::-1]],
          [c for c in "bqwmdnht"[::-1]],
          [c for c in "lsgjrbm"[::-1]], 
          [c for c in "trbvgwnz"[::-1]],
          [c for c in "lpndgw"[::-1]]]

def move(count, src, dest):
    print(count, src, dest)
    for i in range(count):
        # print(i)
        # print(count)
        # print(STACKS)
        # print(STACKS[src - 1])
        STACKS[dest - 1].append(STACKS[src - 1].pop())

with open("input.txt") as f:
    for line in f.readlines()[10:]:
        line = line.replace("move ", "").replace("from ", "").replace("to ", "")
        c, s, d = map(int, line.split(" "))
        move(c, s, d)

print("".join([i[-1].capitalize() for i in STACKS]))
