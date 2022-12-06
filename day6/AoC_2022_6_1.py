# Advent of Code 2022, Day 6, Puzzle 1

endOfPacket = 0

with open("input.txt") as f:
    line = f.readline()
    for x in range(len(line) - 4):
        if len(set(line[x:x+4])) == 4:
            endOfPacket = x+4
            break
        

print(endOfPacket)
