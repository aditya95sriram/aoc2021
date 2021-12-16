#!/usr/bin/python3

def solve(input_fname):
    lines = []
    pos = depth = 0
    with open(input_fname) as ifile:
        for line in ifile:
            lines.append(line.strip().split())
    for cmd, unit in lines:
        unit = int(unit)
        if cmd == "forward":
            pos += unit
        elif cmd == "up":
            depth -= unit
        elif cmd == "down":
            depth += unit
    return pos * depth


if __name__ == "__main__":
    print(solve("../inputs/day2-demo.in"))
