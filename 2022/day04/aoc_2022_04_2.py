# Advent of Code 2022, Day 4, Puzzle 2

redundantAssignments = 0
with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        assignments = line.split(",")

        assignmentBounds = [
            [int(bound) for bound in assignment.split("-")]
            for assignment in assignments
        ]

        assignmentSets = [
            set([i for i in range(bound[0], bound[1] + 1)])
            for bound in assignmentBounds
        ]

        if set.intersection(*assignmentSets):
            redundantAssignments += 1

print(redundantAssignments)
