# Advent of Code 2022, Day 2, Puzzle 2

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

ROUND_LOSS = "X"
ROUND_DRAW = "Y"
ROUND_WIN = "Z"

WIN_SCORE = 6
DRAW_SCORE = 3
LOSS_SCORE = 0

SCORE_KEY = {ROCK: 1, PAPER: 2, SCISSORS: 3}

WLD_KEY = {ROUND_WIN: WIN_SCORE, ROUND_LOSS: LOSS_SCORE, ROUND_DRAW: DRAW_SCORE}

RPC_KEY = {
    ROCK: {
        ROUND_WIN: PAPER,
        ROUND_LOSS: SCISSORS,
        ROUND_DRAW: ROCK,
    },
    PAPER: {
        ROUND_WIN: SCISSORS,
        ROUND_LOSS: ROCK,
        ROUND_DRAW: PAPER,
    },
    SCISSORS: {
        ROUND_WIN: ROCK,
        ROUND_LOSS: PAPER,
        ROUND_DRAW: SCISSORS,
    },
}


def getPointsForStrategy(opponent, matchResult):
    return WLD_KEY[matchResult] + SCORE_KEY[RPC_KEY[opponent][matchResult]]


def evalMatch(matchLine: str):
    opponent, matchResult = matchLine.strip().split(" ")
    cheaterMatchPoints = getPointsForStrategy(opponent, matchResult)
    return cheaterMatchPoints


cheaterTotalPoints = 0
with open("rps.txt") as f:
    cheaterTotalPoints = sum([evalMatch(m) for m in f.readlines()])

print("The Rock Paper Scissor Cheater Scored {} points".format(cheaterTotalPoints))
