# Advent of Code 2022, Day 13, Puzzle 1

# 0 equal, < 0 left is smaller than right, > 0 left is larger than right
def compare_packet_data(left, right) -> int:
    print(f"Compare {left} vs {right}")
    if type(left) is int and type(right) is int:
        return left - right
    elif type(left) is list and type(right) is int:
        return compare_packet_data(left, [right])
    elif type(left) is int and type(right) is list:
        return compare_packet_data([left], right)
    elif type(left) is list and type(right) is list:
        ll = len(left)
        rl = len(right)

        if ll == 0 and rl != 0:
            return -1
        if ll == 0 and rl == 0:
            return 0
        elif ll != 0 and rl == 0:
            return 1
        else:  # Both have data to compare still
            i = 0
            while i < ll and i < rl:
                ret = compare_packet_data(left[i], right[i])
                if ret != 0:
                    return ret
                i += 1

            return ll - rl  # 0 if same length, < 0 if left is shorter than right, > 0 if left is longer than right


input = ""

with open("input.txt") as f:
    input = f.read().strip()

packet_pairs = input.split("\n\n")


# without eval, would have to parse packets with rpn
count = 0
for i, pp in enumerate(packet_pairs):
    l, r = pp.strip().splitlines()
    if compare_packet_data(eval(l), eval(r)) <= 0:
        print("Left is smaller or equal so packets are in right order")
        count += (i + 1)  # index in enumerate starts at 0
    else:
        print("Out of ORDER!")

print(count)
