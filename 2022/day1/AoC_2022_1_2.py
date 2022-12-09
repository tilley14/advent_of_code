# Advent of Code 2022, Day 1, Puzzle 2

cals = []
maxCal = 0
with open("cal.txt") as f:
    calSum = 0
    for line in f.readlines():
        line = line.strip()
        if line:
            calSum = calSum + int(line)
        else:
            maxCal = max(calSum, maxCal)
            cals.append(calSum)
            calSum = 0

    maxCal = max(calSum, maxCal)
    cals.append(calSum)

cals.sort(reverse=True)

print(cals)
print("Max Calories {}".format(maxCal))  # or cals[0]
print("TOP 3 Calories SUM {}".format(sum(cals[0:3])))
