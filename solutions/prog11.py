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

def find(ar):
    return set(zip(*np.where(ar>9)))

def window(mask):
    pmask = np.pad(mask, 1).astype(int)
    s = pmask[:,:][:-2,:-2] + pmask[2:,2:][:,:] + pmask[2:,:][:,:-2] + pmask[:,2:][:-2,:]
    s += pmask[:,1:][:-2,:-1] + pmask[1:,:][:-1,:-2] + pmask[2:,1:][:,:-1] + pmask[1:,2:][:-1,:]
    #print("window for")
    #print(mask)
    #print("is")
    #print(s)
    return s

def update(ar):
    #print("\n", ar, "start")
    ar = ar + 1
    #print(ar, "after +1")
    flash = find(ar)
    fmask = allfmask = ar>9
    ar[fmask] = 0
    while True:
        #print("loop")
        ar += window(fmask)
        #print(ar, "after adding window")
        ar[allfmask] = 0
        #print(ar, "zeroing all flashed")
        newflash = find(ar)
        fmask = ar>9
        if not newflash - flash: break
        flash.update(newflash)
        #print("flash updated", newflash)
        ar[fmask] = 0
        #print(ar, "after zeroing flashes")
        allfmask |= fmask
    return ar, len(flash)

    
def solve(input_fname):
    lines = []
    with open(input_fname) as ifile:
        for line in ifile:
            lines.append(lmapi(list(line.strip())))
    ar = np.array(lines)
    totalflashes = 0
    for i in range(1000):
        ar, flashes = update(ar)
        if flashes == ar.size: return i+1
        totalflashes += flashes
    #return totalflashes

