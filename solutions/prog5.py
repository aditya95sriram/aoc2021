import re, os, sys
from functools import reduce
from itertools import combinations as comb, permutations as perm, combinations_with_replacement as combr
from operator import itemgetter
from pprint import pprint
from math import *
from collections import defaultdict
import networkx as nx
import numpy as np

def dprint(d):
    pprint(dict(d))
def lmap(*args, **kwargs):
    return list(map(*args, **kwargs))
def lmapi(*args, **kwargs):
    return list(map(int, *args, **kwargs))
def enum(*args, **kwargs):
    return enumerate(*args, **kwargs)
def prod(l):
    return reduce(lambda a,b: a*b, l, 1)

def sign(x):
    if x == 0: return 0
    else: return 1 if x > 0 else -1
def solve(input_fname):
    lines = []
    M = -1
    with open(input_fname) as ifile:
        for line in ifile:
            start, end = line.strip().split(" -> ")
            start = lmapi(start.split(","))
            end = lmapi(end.split(","))
            M = max(M, max(start))
            M = max(M, max(end))
            #if start[0] == end[0] or start[1] == end[1]:
            lines.append((start, end))
    cover = np.zeros((M+1, M+1))
    for (sx, sy), (ex, ey) in lines:
        linec = np.zeros_like(cover)
        cx, cy = sx, sy
        dx = ex - sx
        dy = ey - sy
        linec[cy,cx] = 1
        while (cx, cy) != (ex, ey):
            cx += sign(dx)
            cy += sign(dy)
            linec[cy,cx] = 1
        print(linec)
        cover += linec
        print(cover)
    return np.sum(cover >= 2)

        

