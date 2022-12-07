# Advent of Code 2022, Day 7, Puzzle 1

ret = 0


class Node:
    def __init__(self, name) -> None:
        self.parent = None
        self.name = name
        self.children = {}
        
    def isLeaf(self):
        return len(self.children) == 0
        
    def getSize(self) -> int:
        return 0
    
    def isRoot(self)-> bool:
        return self.parent is None
    
    def getPath(self):
        if self.parent == None:
            return self.name
        return self.parent.getPath() + "/" + self.name
    
    def addChild(self, child):
        if child.name not in self.children.keys():
            child.parent = self
            self.children[child.name] = child
    
class aFile(Node):
    def __init__(self, fname, fsize) -> None:
        super().__init__(fname)
        self.size = fsize
        
    def getSize(self) -> int:
        return self.size


class aDir(Node):
    def __init__(self, fname) -> None:
        super().__init__(fname)
        
    def getSize(self) ->int:
        totalSize = 0
        for k, v in self.children.items():
            totalSize += v.getSize()
        return totalSize
    

ROOT_DIR = aDir("/")
CURRENT_DIR = ROOT_DIR

def cd(path : str):
    global CURRENT_DIR
    
    if path == "/":
        CURRENT_DIR = ROOT_DIR
    elif path == "..":
        CURRENT_DIR = CURRENT_DIR.parent
    else:
        if path in CURRENT_DIR.children.keys():
            CURRENT_DIR = CURRENT_DIR.children[path]
        else:
            CURRENT_DIR.addChild(aDir(path))
            CURRENT_DIR = CURRENT_DIR.children[path]
            


MAX_SIZE=10000
totalSizesLessThan10000 = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("$ cd"):
            _, _, path = line.split(" ")
            cd(path)
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            _, path = line.split(" ")
            CURRENT_DIR.addChild(aDir(path))
        else:
            size, path = line.split(" ")
            CURRENT_DIR.addChild(aFile(path, int(size)))
                

ALL_SIZES = {}

def depthFirstSize(node: Node):
    global ALL_SIZES
    if not node.isLeaf():
        for _, n in node.children.items():
            depthFirstSize(n)
            
    ALL_SIZES[node.getPath()] = node.getSize()


depthFirstSize(ROOT_DIR)



for path, sz in ALL_SIZES.items():
    print('{} {}'.format(path, size))
