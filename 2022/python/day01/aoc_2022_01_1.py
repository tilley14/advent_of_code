# Advent of Code 2022, Day 1, Puzzle 1

cals = []  # To Do Quick Sanity Check
maxCal = 0
with open("input.txt") as f:
    sum = 0
    for line in f.readlines():
        line = line.strip()
        if line:
            sum = sum + int(line)
        else:
            maxCal = max(sum, maxCal)
            cals.append(sum)
            sum = 0

    maxCal = max(sum, maxCal)
    cals.append(sum)

print(cals)
print(maxCal)
