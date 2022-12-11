# Advent of Code 2022, Day 11, Puzzle 1
from operator import mul
from functools import reduce


class Monkey():
    def __init__(self, id: int) -> None:
        self.id = id
        self.items = None
        self.operation = None
        self.testVal = None
        self.truthyTarget = None
        self.falsyTarget = None
        self.totalItemsInspected = 0

    def setItems(self, items: list):
        self.items = items

    def setTestVal(self, testVal):
        self.testVal = testVal

    def setTruthyTarget(self, truthyTarget):
        self.truthyTarget = truthyTarget

    def setFalsyTarget(self, falsyTarget):
        self.falsyTarget = falsyTarget

    def setOp(self, x1: str, op: str, x2: str):
        assert(op == "*" or op == "+")

        if not x1.isnumeric() and not x2.isnumeric():
            if op == "*":
                self.operation = lambda old: old * old
            else:
                self.operation = lambda old: old + old

        elif not x1.isnumeric() and x2.isnumeric():
            if op == "*":
                self.operation = lambda old: old * int(x2)
            else:
                self.operation = lambda old: old + int(x2)

        else:
            assert(False)

    def inspect(self):
        assert(len(self.items) != 0)
        assert(self.operation != None)
        self.items[0] = self.operation(self.items[0])
        self.totalItemsInspected += 1

    def test(self):  # returns id of monkey to throw to
        assert(len(self.items) != 0)
        assert(self.truthyTarget != None)
        assert(self.falsyTarget != None)
        if self.items[0] % self.testVal == 0:
            return self.truthyTarget
        else:
            return self.falsyTarget

    def hasItems(self):
        return len(self.items) != 0

    def throw(self):
        assert(len(self.items) != 0)
        return self.items.pop(0)

    def catch(self, item):
        self.items.append(item)

    def applyRelief(self):
        assert(len(self.items) != 0)
        self.items[0] = self.items[0] // 3


INPUT = ""
with open("input.txt") as f:
    INPUT = f.read()

MONKEYS = []

for mNotes in INPUT.split("\n\n"):
    notes = [n.strip() for n in mNotes.splitlines()]
    id = int(notes[0].replace("Monkey ", "").replace(":", ""))
    items = list(map(int, notes[1].replace(
        "Starting items: ", "").split(", ")))
    op = notes[2].replace("Operation: new = ", "").split(" ")
    testVal = int(notes[3].replace("Test: divisible by ", ""))
    truthy = int(notes[4].replace("If true: throw to monkey ", ""))
    falsy = int(notes[5].replace("If false: throw to monkey ", ""))
    # need to learn regex lol

    m = Monkey(id)
    m.setItems(items)
    m.setOp(*op)
    m.setTestVal(testVal)
    m.setTruthyTarget(truthy)
    m.setFalsyTarget(falsy)

    MONKEYS.append(m)


def takeTurn(monkey: Monkey):
    while monkey.hasItems():
        monkey.inspect()
        monkey.applyRelief()
        MONKEYS[monkey.test()].catch(monkey.throw())


ROUNDS = 20
for i in range(ROUNDS):
    for monkey in MONKEYS:
        takeTurn(monkey)
    print("round {}".format(i + 1))
    for m in MONKEYS:
        print("Monkey {}:{}".format(m.id, m.items))


mm = [m.totalItemsInspected for m in MONKEYS]
mm.sort(reverse=True)
print(reduce(mul, mm[0:2]))
