# Advent of Code 2022, Day 6, Puzzle 2

endOfPacket = 0

with open("input.txt") as f:
    line = f.readline()
    for x in range(len(line) - 14):
        if len(set(line[x:x+14])) == 14:
            endOfPacket =  x+14
            break
        

print(endOfPacket)
