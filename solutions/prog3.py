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

LEN = 12

def ffil(nums, agg):
    l = nums
    pos = 0
    while True:
        l = fil(l, agg, pos)
        if len(l) == 1:
            print(l[0])
            return int("".join(map(str,l[0])), 2)
        pos += 1

def fil(nums, agg, pos):
    count1 = sum(num[pos] == 1 for num in nums)
    thresh = len(nums)/2
    #print(nums, thresh)
    #print("cmp", pos, count1, thresh, agg)
    # todo: refactor
    if agg == 1:
        if count1 >= thresh:
            return [num for num in nums if num[pos] == 1]
        else:
            return [num for num in nums if num[pos] == 0]
    else:
        if count1 < thresh:
            return [num for num in nums if num[pos] == 1]
        else:
            return [num for num in nums if num[pos] == 0]
            
def solve(input_fname):
    lines = []
    zcount = dict(zip(range(LEN), [0]*LEN))
    total = 0
    with open(input_fname) as ifile:
        for line in ifile:
            num = lmapi(line.strip())
            lines.append(num)
            total += 1
            for pos, bit in enum(num):
                zcount[pos] += (bit == 0)
    thresh = total / 2
    finals = [0 if zcount[pos] > thresh else 1 for pos in range(LEN)]
    gammab = "".join(str(b) for b in finals)
    epsb = "".join(str(1-b) for b in finals)
    print(gammab, epsb)
    gamma = int(gammab, 2)
    eps = int(epsb, 2)
    print("old", gamma * eps)
    ox = ffil(lines, 1)
    co2 = ffil(lines, 0)
    print(ox, co2)
    return ox*co2


