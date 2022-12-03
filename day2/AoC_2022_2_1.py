# Advent of Code, Day 2, Problem 1


ROCK = "A"
PAPER = "B"
SCISSORS = "C"

ENCRYPTED_ROCK = "X"
ENCRYPTED_PAPER = "Y"
ENCRYPTED_SCISSORS = "Z"

WIN_SCORE = 6
DRAW_SCORE = 3
LOSS_SCORE = 0

SCORE_KEY = {ROCK: 1, PAPER: 2, SCISSORS: 3}

ENCRYPTION_KEY = {
    ENCRYPTED_ROCK: ROCK,
    ENCRYPTED_PAPER: PAPER,
    ENCRYPTED_SCISSORS: SCISSORS,
}


def evalWLD(player, opponent):
    if player == opponent:
        return DRAW_SCORE
    elif player == ROCK and opponent == SCISSORS:
        return WIN_SCORE
    elif player == PAPER and opponent == ROCK:
        return WIN_SCORE
    elif player == SCISSORS and opponent == PAPER:
        return WIN_SCORE
    else:
        return LOSS_SCORE


def evalMatch(matchLine: str):
    opponent, cheaterEncrypt = matchLine.strip().split(" ")
    cheater = ENCRYPTION_KEY[cheaterEncrypt]
    cheaterMatchPoints = SCORE_KEY[cheater] + evalWLD(cheater, opponent)
    return cheaterMatchPoints


cheaterTotalPoints = 0
with open("rps.txt") as f:
    cheaterTotalPoints = sum([evalMatch(m) for m in f.readlines()])

print('The Rock Paper Scissor Cheater Scored {} points'.format(cheaterTotalPoints))
