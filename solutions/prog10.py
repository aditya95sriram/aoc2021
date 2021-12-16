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

CS = "[(<{"
CE = "])>}"
CM = dict(zip(CS, CE))
points = {")":3, "]": 57, "}":1197, ">":25137}
cpoints = dict(zip(")]}>", [1,2,3,4]))

def corrupted(line):
    stack = []
    for c in line:
        if c in CS:
            stack.append(c)
        else:
            if c!=CM[stack.pop()]:
                #return points[c]
                return 0
    # line is not corrupted
    #print(stack)
    return reduce(lambda a,b: a*5+b, (cpoints[CM[c]] for c in stack[::-1]), 0)

def solve(input_fname):
    lines = []
    with open(input_fname) as ifile:
        for line in ifile:
            lines.append(line.strip())
    #return(sum(map(corrupted, lines)))
    scores = lmap(corrupted, lines)
    print(scores)
    scores = sorted(filter(lambda a: a, scores))
    return scores[len(scores)//2]

