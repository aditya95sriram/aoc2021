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

M=5
def solve(input_fname):
    graph = nx.DiGraph()
    R, C = 0, 0
    with open(input_fname) as ifile:
        for _r, line in enumerate(ifile):
            R = C = len(line.strip())
            for _c, _cell in enumerate(lmapi(line.strip())):
                for nr in range(M):
                    for nc in range(M):
                        r = _r + nr*R
                        c = _c + nc*C
                        cell = (_cell + nr + nc - 1) % 9 + 1
                        if r > 0    : graph.add_edge((r-1,c), (r,c), weight=cell)
                        if c > 0    : graph.add_edge((r,c-1), (r,c), weight=cell)
                        if r < 5*R-1: graph.add_edge((r+1,c), (r,c), weight=cell)
                        if c < 5*C-1: graph.add_edge((r,c+1), (r,c), weight=cell)
    print(graph.number_of_nodes(), graph.number_of_edges())
    #print(graph.edges())


    spath = nx.shortest_path(graph, (0,0), (M*R-1, M*C-1), weight="weight")
    #weights = graph.edges(data="weight")
    length = 0
    for u, v in zip(spath, spath[1:]):
        #print(graph.edges[u,v]["weight"])
        length += graph.edges[u,v]["weight"]
    return length






if __name__ == "__main__":
    print(solve("../inputs/day15.in"))
