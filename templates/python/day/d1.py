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
        p1("input.txt")
    if args.input == "p2":
        p1("input.txt")
    if args.input == "t1":
        p2("test1.txt")
    if args.input == "t2":
        p2("test2.txt")
