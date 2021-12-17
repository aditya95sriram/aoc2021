#!/usr/bin/python3

from math import sqrt

def lmapi(*args, **kwargs):
    return list(map(int, *args, **kwargs))

def sign(x):
    return 0 if x == 0 else x // abs(x)

def test(vx, vy, sx, ex, sy, ey):
    x, y = 0, 0
    ymax = 0
    while True:
        x += vx
        y += vy
        ymax = max(ymax, y)
        if sx <= x <= ex and sy <= y <= ey:
            return ymax
        vx -= sign(vx)
        vy -= 1
        if vx >= 0 and x > ex: return -1
        if vx <= 0  and x < sx: return -1
        if vy <= 0  and y < sy: return -1
    
def solve(input_fname):
    with open(input_fname) as ifile:
        line = ifile.readline().strip().strip("target area: ")
        lx, ly = line.split(", ")
        sx, ex = lmapi(lx[2:].split(".."))
        sy, ey = lmapi(ly[2:].split(".."))
    target = sx, ex, sy, ey

    gymax = 0
    for vx in range(6,200):  # was run with 22, 200 for main input
        for vy in range(1,200):
            ymax = test(vx, vy, *target)
            gymax = max(ymax, gymax)

    return gymax


if __name__ == "__main__":
    print(solve("../inputs/day17-demo.in"))
