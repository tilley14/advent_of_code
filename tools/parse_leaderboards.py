import json
from datetime import datetime


def getStartDt(day):
    datetime.datetime(2022, 12, day, 0, 0, 0)


def printProb(probJson: dict) -> None:
    # ts = datetime.fromtimestamp(
    #     probJson["get_star_ts"]).strftime('%Y-%m-%d %H:%M:%S')
    ts = datetime.fromtimestamp(
        probJson["get_star_ts"]).strftime('%H:%M:%S')
    print("\t\tTime {} ".format(ts))


def printDays(dayJson: dict) -> None:
    def getId(e):
        return int(list(e)[0])

    probs = list(dayJson.items())
    probs.sort(key=getId)
    for id, prob in probs:
        print("\t\tProb {}".format(id))
        printProb(prob)


DATA = []

with open("./2022/leader_board.json") as f:
    DATA = json.loads(f.read())


def getName(e):
    return e[1]["name"].lower()


MEMBERS = list((k, v) for k, v in DATA["members"].items())
MEMBERS.sort(key=getName)


for id, prof in MEMBERS:
    def getDay(e):
        return int(e[0])
    days = list((k, v) for k, v in prof["completion_day_level"].items())
    days.sort(key=getDay)

    print(prof["name"])
    for day, dayJson in days:
        print("\tDay {}".format(day))
        printDays(dayJson)


# todo: lap leaderboard
