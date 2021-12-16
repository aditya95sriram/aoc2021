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
    pop = None
    with open(input_fname) as ifile:
        pop = Counter(lmapi(ifile.readline().strip().split(",")))
    DAYS = 18 if "demo" in input_fname else 80
    print(pop)
    for day in range(256):
        newpop = Counter({i-1: pop[i] for i in pop if i > 0})
        newpop.update({6: pop[0], 8: pop[0]})
        if day == 17: print(newpop)
        pop = newpop
    return sum(pop.values())
