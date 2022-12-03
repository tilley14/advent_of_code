# Advent of Code 2022, Day 3, Part 2

# Priority Map Building Shortcuts
asciAlphStart = ord('a')
asciAlphEnd = ord('z')

asciAlphUpStart = ord('A')
asciAlphUpEnd = ord('Z')

# Build Priority Map
priority = {}
p = 1
for i in range(asciAlphStart, asciAlphEnd + 1):
    priority[chr(i)] = p
    p = p + 1

for i in range(asciAlphUpStart, asciAlphUpEnd + 1):
    priority[chr(i)] = p
    p = p + 1

# Read Elf Ruck Manifest
total = 0
elves = []
with open("ruck.txt") as f:
    elves = [l.strip() for l in f.readlines() if l.strip()]

# Find Badge and add its priority to the total
for i in range(0, len(elves), 3):
    group = [set([item for item in elf]) for elf in elves[i:i+3]]
    badge = list(set.intersection(*group))[0] # Assuming 1 Badge per group
    total = total + priority[badge]

print(total)
