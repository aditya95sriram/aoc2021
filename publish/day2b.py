#!/usr/bin/python3

def solve(input_fname):
    lines = []
    pos = depth = aim = 0
    with open(input_fname) as ifile:
        for line in ifile:
            lines.append(line.strip().split())
    for cmd, unit in lines:
        unit = int(unit)
        if cmd == "forward":
            pos += unit
            depth += aim * unit
        elif cmd == "up":
            aim -= unit
        elif cmd == "down":
            aim += unit
    return pos * depth


if __name__ == "__main__":
    print(solve("../inputs/day2-demo.in"))
