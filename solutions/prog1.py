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

def solve(input_fname):
    lines = []
    with open(input_fname) as ifile:
        for line in ifile:
            lines.append(int(line.strip()))
    windows = zip(lines, lines[1:], lines[2:])
    sums = lmap(sum, windows)
    cons = zip(sums, sums[1:])
    return sum(a[1] > a[0] for a in cons)
