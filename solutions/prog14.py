import re, os, sys
from functools import reduce
from itertools import combinations as comb, permutations as perm, combinations_with_replacement as combr
from operator import itemgetter
from pprint import pprint
from math import *
from collections import defaultdict, Counter
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
    start = ""
    rules = dict()
    with open(input_fname) as ifile:
        start = ifile.readline().strip()
        ifile.readline()
        for line in ifile:
            pair, mid = line.strip().split(" -> ")
            rules[pair] = (pair[0] + mid, mid+pair[1])
    #print(rules)

    #cur = start
    #for _ in range(40):
        #nxt = "".join(rules[cur[i:i+2]] for i in range(len(cur)-1))
        #nxt += cur[-1]
        #print(nxt)
        #cur = nxt       

    #ctr = Counter(cur)
    #return max(ctr.values()) - min(ctr.values())

    startpairs = [start[i:i+2] for i in range(len(start)-1)]
    cur = Counter(startpairs)
    print(cur)
    for _ in range(40):
        nxt = Counter()
        for pair, value in cur.items():
            p1, p2 = rules[pair]
            nxt.update({p1: value, p2: value})
        print(nxt)
        cur = nxt

    lc = Counter(start[-1])
    for pair, value in cur.items():
        lc.update({pair[0]: value}) #, pair[1]: value})
        print(lc)

    return max(lc.values()) - min(lc.values())

    





if __name__ == "__main__":
    print(solve("../inputs/day14.in"))
