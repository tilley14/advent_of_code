# Advent of Code 2022, Day 3, Puzzle 1

asciAlphStart = ord("a")
asciAlphEnd = ord("z")

asciAlphUpStart = ord("A")
asciAlphUpEnd = ord("Z")

# Build Priority Map
priority = {}
p = 1
for i in range(asciAlphStart, asciAlphEnd + 1):
    priority[chr(i)] = p
    p = p + 1

for i in range(asciAlphUpStart, asciAlphUpEnd + 1):
    priority[chr(i)] = p
    p = p + 1

total = 0
with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            items = [c for c in line]
            totalItems = len(items)
            itemsPerPocket = int(totalItems / 2)

            pocket1 = set([i for i in items[:itemsPerPocket]])
            pocket2 = set([i for i in items[itemsPerPocket:]])

            duplicateItems = pocket1.intersection(pocket2)
            total = total + sum([priority[i] for i in duplicateItems])


print(total)
