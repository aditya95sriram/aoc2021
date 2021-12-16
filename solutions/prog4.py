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

def check(numbers, board):
    marked = np.zeros_like(board)
    for num in numbers:
        marked |= board == num
    bingo = False
    if 5 in np.sum(marked, axis=0):
        bingo = True
    elif 5 in np.sum(marked, axis=1):
        bingo = True
    if bingo:
        msum = np.sum(np.where(marked, board, np.zeros_like(board)))
        return np.sum(board) - msum
    return None

def solve(input_fname):
    lines = []
    numbers = []
    with open(input_fname) as ifile:
        numbers = lmapi(ifile.readline().strip().split(","))
        ifile.readline()
        boards = []
        cboard = []
        rownum = 0
        for line in ifile:
            cboard.append(lmapi(line.strip().split()))
            rownum += 1
            if rownum >= 5:
                boards.append(np.array(cboard))
                #print(cboard)
                cboard = []
                rownum = 0
                ifile.readline()
        #print(boards)

    last = None
    lastboard = None
    boardswon = set()
    print("all", numbers)
    for i, number in enumerate(numbers, start=1):
        for boardid, board in enum(boards):
            res = check(numbers[:i], board)
            if res is not None and boardid not in boardswon:
                print(board)
                print(number, res, res * number)
                lastboard = board
                last = res * number
                boardswon.add(boardid)
    return last

