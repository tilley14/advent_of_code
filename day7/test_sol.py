# This is a fun solution! - This guy is fast and I like his style.
#
# Some of the solutions I saw in the top leaderboards made an assumption that there would be no repeat ls'ing of a dir.
# This assumption turns out to be true! In the original input, there was no repeating ls'ing of dirs.
# What an odd assumption since that was not a given and the directions sugest that the
# exact opposite assumption should be made. I was able to break some of the solutions using my modified test_input.txt.
# (Yea... I am salty... HTF u make that assumption - your able to get out of tracking the parent/child relationship in the filesystem)
#
# This one does not make this assumption and if you run it with the modified input it still returns the correct answer.
# Yay this one!

# I made slight modification to feed in the input and to test the solution [lines 18-22, 64], but otherwise this is from
# https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day07p2.py

cwd = root = {}
stack = []

lines = []
with open("test_input.txt") as f:
    lines = f.readlines()
 
for line in lines:
    line = line.strip()
    if line[0] == "$":
        if line[2] == "c":
            dir = line[5:]
            if dir == "/":
                cwd = root
                stack = []
            elif dir == "..":
                cwd = stack.pop()
            else:
                if dir not in cwd:
                    cwd[dir] = {}
                stack.append(cwd)
                cwd = cwd[dir]
    else:
        x, y = line.split()
        if x == "dir":
            if y not in cwd:
                cwd[y] = {}
        else:
            cwd[y] = int(x)

def size(dir = root):
    if type(dir) == int:
        return dir
    return sum(map(size, dir.values()))

t = size() - 40_000_000

def solve(dir = root):
    ans = float("inf")
    if size(dir) >= t:
        ans = size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        q = solve(child)
        ans = min(ans, q)
    return ans

print(solve())
assert(solve() == 942298)
