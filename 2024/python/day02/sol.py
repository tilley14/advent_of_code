import argparse


def p1(fname: str):
    total_safe = 0
    with open(fname) as f:
        for line in f.readlines():
            levels = [int(x) for x in line.split()]
            incrementing = False
            for i in range(len(levels) - 1):
                if i == 0:
                    if levels[i] < levels[i + 1]:
                        incrementing = True
                    elif levels[i] > levels[i + 1]:
                        incrementing = False
                    else:
                        break

                if incrementing:
                    dif = levels[i] - levels[i + 1]
                    if dif > -1 or dif < -3:
                        break
                else:
                    dif = levels[i] - levels[i + 1]
                    if dif < 1 or dif > 3:
                        break

                if i == len(levels) - 2:
                    total_safe += 1

    return total_safe


def p2_helper(levels):
    safe = False
    idx = -1
    incrementing = False
    for i in range(len(levels) - 1):
        if i == 0:
            if levels[i] < levels[i + 1]:
                incrementing = True
            elif levels[i] > levels[i + 1]:
                incrementing = False
            else:


        if incrementing:
            dif = levels[i] - levels[i + 1]
            if dif > -1 or dif < -3:
                if dampened:
                    break
                else:
                    dampened = True
        else:
            dif = levels[i] - levels[i + 1]
            if dif < 1 or dif > 3:
                if dampened:
                    break
                else:
                    dampened = True

        if i == len(levels) - 2:
            total_safe += 1


    return safe, idx


def p2(fname: str):
    total_safe = 0
    with open(fname) as f:
        for line in f.readlines():
            levels = [int(x) for x in line.split()]
            success, idx = p2_helper(levels)
            if not success:
                del levels[idx]
                success, idx = p2_helper(levels)

            if success:
                total_safe += 1




    return total_safe


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input == "p1":
        print(p1("input.txt"))  # answer 639
    elif args.input == "p2":
        print(p2("input.txt"))  # answer
    elif args.input == "t1":
        print(p1("test1.txt") == 2)
    elif args.input == "t2":
        print(p2("test2.txt"))
