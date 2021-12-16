#!/usr/bin/python3

def lmap(*args, **kwargs):
    return list(map(*args, **kwargs))

def solve(input_fname):
    lines = []
    with open(input_fname) as ifile:
        for line in ifile:
            lines.append(int(line.strip()))
    windows = zip(lines, lines[1:], lines[2:])
    sums = lmap(sum, windows)
    pairs = zip(sums, sums[1:])
    return sum(a[1] > a[0] for a in pairs)


if __name__ == "__main__":
    print(solve("../inputs/day1-demo.in"))
