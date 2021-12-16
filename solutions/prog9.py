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

def shift(orig, shifted, sx, sy):
    dx, dy = orig.shape
    sign = -1 if (sx < 0 or sy < 0) else 1
    if sign == 1:
        #print("pos", sx,sy,dx,dy)
        print( shifted[sx:,sy:][:dx,:dy] )
        return shifted[sx:,sy:][:dx,:dy] > orig
    else:
        if sx == 0: sx = dx
        if sy == 0: sy = dy
        print("neg", sx,sy,dx,dy)
        print( shifted[-sx:,-sy:][-dx:,-dy:] )
        return shifted[-sx:,-sy:][-dx:,-dy:] > orig
    
def basin_size(g, sink):
    ht = g.nodes(data="ht")
    basin = {sink}
    tree = nx.bfs_tree(g, sink)
    queue = [sink]
    visited = set()
    while queue:
        cur = queue.pop()
        basin.add(cur)
        visited.add(cur)
        #print("cur", cur, queue, ht[cur], list(tree.successors(cur)))
        for c in g.neighbors(cur):
            if c in visited: continue
            if ht[c] != 9:
                queue.append(c)
    #print("for sink", sink, "\tbasin", [ht[b] for b in basin], basin)
    return len(basin)


def solve(input_fname):
    heights = []
    with open(input_fname) as ifile:
        for line in ifile:
            heights.append(lmapi(line.strip()))
    hts = np.array(heights)
    phts = np.pad(hts, 1, constant_values=42)
    shfts = dict()
    dx, dy = hts.shape
    shfts["l"] = phts[ :,1:][:dx,:dy]
    shfts["r"] = phts[1:,1:][-dx:,:dy]
    shfts["u"] = phts[1:, :][:dx,:dy]
    shfts["d"] = phts[1:,1:][:dx,-dy:]
    #print(shfts)
    lows = reduce(lambda a,b: a & b, (s > hts for s in shfts.values()))
    #print(lows)

    lowhts = hts[lows]+1

    sinks = [(x,y) for x in range(dx) for y in range(dy) if lows[x,y]]
    g = nx.Graph()
    g.add_nodes_from(((x,y),{"ht":hts[x,y]}) for x in range(dx) for y in range(dy))

    for x in range(dx):
        for y in range(dy):
            if (x-1,y) in g: g.add_edge((x-1,y),(x,y))
            if (x,y-1) in g: g.add_edge((x,y-1),(x,y))
            if (x+1,y) in g: g.add_edge((x+1,y),(x,y))
            if (x,y+1) in g: g.add_edge((x,y+1),(x,y))
    
    print(sinks)
    print(g)

    sizes = []
    for sink in sinks:
        b = basin_size(g, sink)
        sizes.append(b)

    print(sizes)
    return prod(sorted(sizes, reverse=True)[:3])


    #return sum(lowhts)
