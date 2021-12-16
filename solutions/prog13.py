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

def makefold(paper, axis, loc):
    print("folding paper size", paper.shape, "at", axis, loc)
    if axis == "y":  # bottom folds up
        top = paper[:loc, :]
        bottom = paper[loc+1:, :][::-1,:]
        tr, _ = top.shape
        br, _ = bottom.shape
        if br < tr:
            top, bottom = bottom, top
            tr, br = br, tr
        if tr < br:
            newtop = np.zeros(bottom.shape, dtype=bool)
            newtop[br-tr:,:] = top
            top = newtop
        print(top)
        print(bottom)
        return top | bottom
    else:
        left = paper[:, :loc]
        right = paper[:, loc+1:][:,::-1]
        _, lc = left.shape
        _, rc = right.shape
        if lc < rc:
            left, right = right, left
            lc, rc = rc, lc
        if rc < lc:
            newright = np.zeros(left.shape, dtype=bool)
            newright[:,lc-rc:] = right
            right = newright
        return left | right

def solve(input_fname):
    dots = []
    folds = []
    with open(input_fname) as ifile:
        for line in ifile:
            if not line.strip(): break
            dots.append(lmapi(line.strip().split(",")))
        for line in ifile:
            _, _, fold = line.strip().split()
            axis, loc = fold.split("=")
            folds.append((axis, int(loc)))

    #print(dots)
    #print(folds)

    xmax = max(map(itemgetter(0), dots))
    ymax = max(map(itemgetter(1), dots))
    print(xmax, ymax)

    paper = np.zeros((ymax+1, xmax+1), dtype=bool)
    for dotx, doty in dots:
        paper[doty, dotx] = 1
    print(paper)

    #paper = makefold(paper, *folds[0])

    for fold in folds:
        paper = makefold(paper, *fold)
        print(paper)

    #return paper
    print( "\n".join("".join("#" if el else "." for el in row) for row in paper) )
    return paper


if __name__ == "__main__":
    solve("../inputs/day13.in")
