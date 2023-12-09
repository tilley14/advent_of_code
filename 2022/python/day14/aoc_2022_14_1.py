# Advent of Code 2022, Day 14, Puzzle 1

import os
from time import sleep
import signal

# sand source
source_x = 500
source_y = 0

input = ""
with open("input.txt") as f:
    input = f.read().strip()

rock_paths = [[list(map(int, coord.split(","))) for coord in coords] 
              for coords in [path.split(" -> ")
                             for path in input.splitlines()]]


G_WID = 700
G_HIG = 200
grid = [["." for _ in range(G_WID)] for _ in range(G_HIG)]

grid[source_y][source_x] = "+"


floor_y = 0

min_x = 100000000
max_x = 0

for i in range(0, len(rock_paths)):
    for j in range(1, len(rock_paths[i])):
        x1, y1 = rock_paths[i][j - 1]
        x2, y2 = rock_paths[i][j]
        
        floor_y = max(floor_y, y1, y2)
        min_x = min(min_x, x1, x2)
        max_x = max(max_x, x1, x2)
        
        if x1 == x2: # Vertical Line
            for rock_y in range(min(y1, y2), max(y1, y2) + 1):
                grid[rock_y][x1] = "#"
        elif y1 == y2: # Horizontal Line
            for rock_x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][rock_x] = "#"
        else:
            assert(False)
            
            
def handleExit(signum, frame):
    print("Exit y/n?")
    answer = input()
    if answer.lower() == 'y':
        exit(1)

signal.signal(signal.SIGINT, handleExit)
        
        
        
def draw():
    os.system("cls")
    print("\n".join("".join([rr for rr in r[min_x - 2 : max_x + 3 ]]) for r in grid[0:floor_y+ 2]))
    # print("\n\n")
    sleep(.02)
        

sand_obstructions = set(["o", "#"])

sand_count = 0

while True: # Time to rain sand
    sand_count += 1
    
    next_x = source_x 
    next_y = source_y
    
    while True:        
        # print(f"next_x {next_x} next_y {next_y}")
        
        if grid[next_y + 1][next_x] not in sand_obstructions: # fall down
            next_y += 1
            
            if next_y >= floor_y + 1:
                print(sand_count - 1)
                exit(0)
            
        elif grid[next_y + 1][next_x - 1] not in sand_obstructions:  # blocked down, fall diagonal left
            next_y += 1
            next_x -= 1
        elif grid[next_y + 1][next_x + 1] not in sand_obstructions: # blocked down, blocked diagonal left, fall right
            next_y += 1
            next_x += 1
        else:
            grid[next_y][next_x] = "o"
            draw()
            break
            

# print("\n".join("".join(r) for r in grid))
