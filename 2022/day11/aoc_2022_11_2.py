# Advent of Code 2022, Day 11, Puzzle 2
from operator import mul
from functools import reduce

# All the Tests have division by a prime factor.
# Once an item gets larger than the LCM we
# can mod it and the rules will still evaluate the same
TEST_LCM = 1


class Monkey():
    def __init__(self, id: int) -> None:
        self.id = id
        self.items = None
        self.operation = None
        self.testVal = None
        self.truthyTarget = None
        self.falsyTarget = None
        self.totalItemsInspected = 0
        self.isMult = False

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

        self.simplify()

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

    def simplify(self):
        if self.items[0] % TEST_LCM == 0:
            self.items[0] = self.items[0] // TEST_LCM
        else:
            self.items[0] = self.items[0] % TEST_LCM

    def applyRelief(self):
        pass  # No more relief


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
    TEST_LCM *= testVal


def takeTurn(monkey: Monkey):
    while monkey.hasItems():
        monkey.inspect()
        MONKEYS[monkey.test()].catch(monkey.throw())


# print("round 0")
# for m in MONKEYS:
#     print("Monkey {}:{}".format(m.id, m.items))

ROUNDS = 10000
for i in range(ROUNDS):
    for monkey in MONKEYS:
        takeTurn(monkey)
    # print("round {}".format(i + 1))
    # for m in MONKEYS:
    #     print("Monkey {}:{}".format(m.id, m.items))

    # print([m.totalItemsInspected for m in MONKEYS])


mm = [m.totalItemsInspected for m in MONKEYS]
mm.sort(reverse=True)
print(reduce(mul, mm[0:2]))
