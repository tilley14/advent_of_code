# Advent of Code 2022, Day 9, Puzzle 1

import math

ret = 0

input = []

with open("test.txt") as f:
    input = [l.strip() for l in f.readlines() if l.strip()]
    

uniquePositions = set([(0,0)])


KNOTS = []
for i in range(0, 10):
    KNOTS.append([0, 0])
    
HEAD = 0
TAIL = 9
X = 0
Y = 1

def distance(x1: float, x2: float, y1: float, y2: float):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def move(direction, steps):
    global KNOTS
    global uniquePositions
    remainingSteps = steps
        
    while remainingSteps != 0:
        remainingSteps -= 1
        
        # Move head
        if direction == "U":
            KNOTS[HEAD][Y] += 1
        if direction == "D":
            KNOTS[HEAD][Y] -= 1
        if direction == "L":
            KNOTS[HEAD][X] -= 1
        if direction == "R":
            KNOTS[HEAD][X] += 1
            
        print([i for i in range(HEAD, TAIL)])
                    
        for i in range(HEAD, TAIL):
            K1 = i
            K2 = i + 1
            
            
            if distance(KNOTS[K1][X], KNOTS[K2][X], KNOTS[K1][Y], KNOTS[K2][Y]) > math.sqrt(2):
                
                dx = KNOTS[K1][X] - KNOTS[K2][X]
                dy = KNOTS[K1][Y] - KNOTS[K2][Y]
                
                if dy == 2:
                    KNOTS[K2][Y] += 1
                    KNOTS[K2][X] += dx
                if dy == -2:
                    KNOTS[K2][Y] -= 1
                    KNOTS[K2][X] += dx
                if dx == 2:
                    KNOTS[K2][Y] += dy
                    KNOTS[K2][X] += 1
                if dx == -2:
                    KNOTS[K2][Y] += dy
                    KNOTS[K2][X] -= 1

                                        
                if K2 == TAIL: 
                    uniquePositions.add((KNOTS[K2][X], KNOTS[K2][Y]))
            else:
                break # if the knot ahead didn't move, then no need to keep checking for move
        
for line in input:
    direction, step = line.split(" ")
    move(direction, int(step))
    
print(len(uniquePositions))
