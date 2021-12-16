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

def clone(g, node):
    newname = (node, len(g))
    g.add_edges_from((newname, nbr) for nbr in g.neighbors(node))

def solve2(input_fname):
    edges = []
    with open(input_fname) as ifile:
        for line in ifile:
            edges.append(line.strip().split("-"))
    g = nx.Graph()
    g.add_edges_from(edges)

    bigs = list(filter(str.isupper, g.nodes))
    clonecount = 3
    for big in bigs:
        for _ in range(clonecount):
            clone(g, big)

    cutoff = 20

    lpaths = []
    for i in range(10):
        paths = list(nx.all_simple_paths(g, "start", "end", cutoff=5*i))
        print("cutoff:", 5*i, "#paths:", len(paths))
        if lpaths and len(paths) == lpaths[-1]: break
        lpaths.append(len(paths))
        #pprint(paths)
        #print()

    for e in g.edges:
        g.edges[e]["cap"] = 1
    flow, fd = nx.maximum_flow(g, "start", "end", "cap")
    print("max flow", flow)
    pprint(fd)
    return lpaths

def bfs(graph, start, end, maxdepth):
    #visited = set()
    paths = []
    queue = [(start, 0, {start}, False)]
    count = defaultdict(int)
    while queue:
        cur, depth, visited, smallv = queue.pop()
        if depth > maxdepth: continue
        for nbr in graph.neighbors(cur):
            if nbr == end:
                paths.append((depth, visited))
                count[depth] += 1
                continue
            if nbr == start: continue
            if nbr.islower() and nbr in visited and smallv: 
                #print(nbr, visited, smallv)
                continue
            queue.append((nbr, depth+1, visited | {nbr}, smallv or (nbr.islower() and nbr in visited)))
    pprint(sorted(paths))
    for length in sorted(count):
        print(f"paths of length {length}: {count[length]}")
    return count
        
    
def solve(input_fname):
    edges = []
    with open(input_fname) as ifile:
        for line in ifile:
            edges.append(line.strip().split("-"))
    g = nx.Graph()
    g.add_edges_from(edges)

    return(sum(bfs(g, "start", "end", 35).values()))
    

if __name__ == "__main__":
    solve("../inputs/day12.in")

