import argparse


def p1(fname: str) -> int:
    l1 = []
    l2 = []
    with open(fname) as f:
        for line in f.readlines():
            elm1, elm2 = line.split()
            l1.append(int(elm1))
            l2.append(int(elm2))

    l1.sort()
    l2.sort()

    dif = [abs(e1 - e2) for e1, e2 in zip(l1, l2)]

    return sum(dif)


def p2(fname: str):
    l1 = []
    appearances = dict()
    with open(fname) as f:
        for line in f.readlines():
            elm1, elm2 = line.split()
            l1.append(int(elm1))

            n = int(elm2)
            if n in appearances:
                appearances[n] += 1
            else:
                appearances[n] = 1

    ret = 0

    for e in l1:
        if e in appearances:
            ret += e * appearances[e]
        # else its e*0 = 0

    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input == "p1":
        print(p1("input.txt"))  # answer 1222801
    elif args.input == "p2":
        print(p2("input.txt"))  # answer 22545250
    elif args.input == "t1":
        print(p1("test1.txt") == 11)
    elif args.input == "t2":
        print(p2("test2.txt") == 31)
