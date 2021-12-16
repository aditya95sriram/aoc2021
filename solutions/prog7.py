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

def f(x):
    return x*(x+1)//2

def solve(input_fname):
    orig = []
    with open(input_fname) as ifile:
        orig = lmapi(ifile.readline().strip().split(","))
    avg = sum(orig)/len(orig)
    print("avg", avg)
    mindist = 1e9
    for i in range(min(orig), max(orig)+1):
        dist = sum(f(abs(x-i)) for x in orig)
        mindist = min(dist, mindist)
        print(i, dist)
    return mindist
