# Advent of Code 2022, Day 7, Puzzle 2


class Node:
    def __init__(self, name: str) -> None:
        self.parent = None
        self.name = name
        self.children = {}

    def isLeaf(self) -> bool:
        return len(self.children) == 0

    def getSize(self) -> int:
        return 0

    def isRoot(self) -> bool:
        return self.parent is None

    def getPath(self):
        if self.parent == None:
            return self.name
        elif self.parent.isRoot():
            return self.parent.getPath() + self.name
        else:
            return self.parent.getPath() + "/" + self.name

    def addChild(self, child):
        if child.name not in self.children.keys():
            child.parent = self
            self.children[child.name] = child

    def equals(self, other) -> bool:
        return self.getPath == other.getPath()

    def isDir(self) -> bool:
        return False


class aFile(Node):
    def __init__(self, fname: str, fsize: int) -> None:
        super().__init__(fname)
        self.size = fsize

    def getSize(self) -> int:
        return self.size

    def isDir(self) -> bool:
        return False


class aDir(Node):
    def __init__(self, fname: str) -> None:
        super().__init__(fname)

    def getSize(self) -> int:
        totalSize = 0
        for _, child in self.children.items():
            totalSize += child.getSize()
        return totalSize

    def isDir(self) -> bool:
        return True


ROOT_DIR = aDir("/")
CURRENT_DIR = ROOT_DIR
DIR_SIZES = {}


def cd(path: str):
    global CURRENT_DIR
    global ROOT_DIR
    if path == "/":
        CURRENT_DIR = ROOT_DIR
    elif path == "..":
        if not CURRENT_DIR.equals(ROOT_DIR):
            CURRENT_DIR = CURRENT_DIR.parent
        else:
            CURRENT_DIR = ROOT_DIR
    else:
        if path not in CURRENT_DIR.children:
            CURRENT_DIR.addChild(aDir(path))

        CURRENT_DIR = CURRENT_DIR.children[path]


def depthFirstSize(node: Node):
    global DIR_SIZES
    if not node.isLeaf():
        for _, child in node.children.items():
            depthFirstSize(child)

    if node.isDir():
        DIR_SIZES[node.getPath()] = node.getSize()


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
        else:  # a file
            size, path = line.split(" ")
            CURRENT_DIR.addChild(aFile(path, int(size)))


depthFirstSize(ROOT_DIR)

TOTAL_DISK_SPACE = 70000000
SPACE_REQUIRED_FOR_UPDATE = 30000000
CURRENT_DISK_SPACE = ROOT_DIR.getSize()
FREE_DISK_SPACE = TOTAL_DISK_SPACE - CURRENT_DISK_SPACE
REMAINING_SPACE_REQUIRED = SPACE_REQUIRED_FOR_UPDATE - FREE_DISK_SPACE

print(min([v for _, v in DIR_SIZES.items() if v >= REMAINING_SPACE_REQUIRED]))
