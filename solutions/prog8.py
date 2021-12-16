import re, os, sys
from functools import reduce
from itertools import combinations as comb, permutations as perm, combinations_with_replacement as combr, product
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

def findlen(patterns, l):
    return [set(pat) for pat in patterns if len(pat) == l]

def remove_all(graph, u, v):
    uv_edges = [(u,v2) for v2 in graph[u]] + [(v,u2) for u2 in graph[v]]
    uve = set(uv_edges)
    graph.remove_edges_from(uve)

def deduce(patterns, output):
    match = {}
    match[1] = findlen(patterns, 2)[0]
    match[4] = findlen(patterns, 4)[0]
    match[7] = findlen(patterns, 3)[0]
    match[8] = findlen(patterns, 7)[0]
    fivesegs = findlen(patterns, 5)
    sixsegs  = findlen(patterns, 6)
    pos = nx.Graph()
    pos.add_nodes_from("abcdefgABCDEFG")
    pos.add_edges_from(product(match[1], "AB"))
    pos.add_edges_from(product(match[4] - match[1], "EF"))
    pos.add_edges_from(product(match[7] - match[1], "D"))
    dseg = (match[7] - match[1])
    fiveseg_common = fivesegs[0] & fivesegs[1] & fivesegs[2]
    pos.add_edges_from(product(fiveseg_common - dseg, "FC"))
    sixseg_common = sixsegs[0] & sixsegs[1] & sixsegs[2]
    pos.add_edges_from(product(sixseg_common - dseg - (fiveseg_common - dseg), "EB"))
    eseg = (sixseg_common - dseg - fiveseg_common - match[1])
    five = [f for f in fivesegs if (eseg|dseg).issubset(f)][0]
    bseg = five - dseg - eseg - fiveseg_common
    fseg = five - sixseg_common
    sol = dict()
    sol["D"] = list(dseg).pop()
    sol["E"] = list(eseg).pop()
    sol["B"] = list(bseg).pop()
    sol["A"] = (match[7] - bseg - dseg).pop()
    sol["F"] = list(fseg).pop()
    for k, v in sol.items():
        remove_all(pos, v, k)
    #print(pos.edges())
    sol["C"] = list(pos["C"]).pop()
    #print(match[8], sol.values())
    sol["G"] = (match[8] - {s for s in sol.values()}).pop()
    #print(sol)
    
    rsol = {v:k for k,v in sol.items()}
    reals = dict(AB=1, ABD=7, ABEF=4, BCDEF=5, ACDFG=2, ABCDF=3, ABCDEFG=8, ABCDEF=9, BCDEFG=6, ABCDEG=0)
    fval = ""
    for o in output:
        val = reals["".join(sorted(map(rsol.get, o)))]
        fval += str(val)
    print(fval)
    return int(fval)

def solve(input_fname):
    lines = []
    countspecial = 0
    total = 0
    with open(input_fname) as ifile:
        for line in ifile:
            pattern, output = line.split(" | ")
            pattern = pattern.split()
            output = output.split()
            lines.append((pattern, output))
            countspecial += len([o for o in output if len(o) in [2,3,4,7]])
    #return countspecial
            val = deduce(pattern, output)
            total += val
    return total

