import argparse


def p1(fname: str):
    with open(fname) as f:
        for line in f.readlines():
            pass


def p2(fname: str):
    with open(fname) as f:
        for line in f.readlines():
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    args = parser.parse_args()

    if args.input == "p1":
        print(p1("input.txt"))  # answer
    elif args.input == "p2":
        print(p2("input.txt"))  # answer
    elif args.input == "t1":
        print(p1("test1.txt") == -1)
    elif args.input == "t2":
        print(p2("test2.txt") == -1)
