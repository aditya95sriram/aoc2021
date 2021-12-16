#!/usr/bin/python3

from functools import reduce

def prod(l):
    return reduce(lambda a,b: a*b, l, 1)

def packet(out):
    global totalver
    spl = lambda n: ("".join(out[:n]), out[n:])
    ver, out = spl(3)
    ver = int(ver, 2)
    typ, out = spl(3)
    typ = int(typ, 2)
    print(f"<packet {ver=} {typ=}>")
    if typ == 4:
        res, nbits, out = literal(out)
    else:
        res, nbits, out = operator(out, typ)
    nbits += 6
    print(f"</packet>")
    return res, nbits, out

def literal(out):
    nums = []
    spl = lambda n: ("".join(out[:n]), out[n:])
    nbits = 0
    while True:
        num, out = spl(5)
        nbits += 5
        if num.startswith("0"):
            nums.extend(num[1:])
            break
        nums.extend(num[1:])
    res = int("".join(nums),2)
    print("<lit/>", res, nbits, out)
    return res, nbits, out

def operator(out, typ):
    spl = lambda n: ("".join(out[:n]), out[n:])
    ltyp, out = spl(1)
    totbits = 0
    if ltyp == "0":
        nbits, out = spl(15)
        nbits = int(nbits, 2)
        print(f"<op {typ=} {ltyp=:s} {nbits=}>")
        subs = []
        while totbits < nbits:
            sub, conbits, out = packet(out)
            totbits += conbits
            subs.append(sub)
        totbits += 1 + 15
    else:
        nsub, out = spl(11)
        nsub = int(nsub, 2)
        print(f"<op {typ=} {ltyp=:s} {nsub=}>")
        subs = []
        totsub = 0
        while totsub < nsub:
            sub, conbits, out = packet(out)
            totsub += 1
            totbits += conbits
            subs.append(sub)
        totbits += 1 + 11 
    print(f"</op {typ=}>", subs, totbits, out)
    if typ == 0:
        res = sum(subs)
    elif typ == 1:
        res = prod(subs)
    elif typ == 2:
        res = min(subs)
    elif typ == 3:
        res = max(subs)
    elif typ == 5:
        res = int(subs[0] > subs[1])
    elif typ == 6:
        res = int(subs[0] < subs[1])
    elif typ == 7:
        res = int(subs[0] == subs[1])
    else:
        raise ValueError(f"unknown operator type {typ}")
    return res, totbits, out

def solve(input_fname):
    out = None
    with open(input_fname) as ifile:
        for line in ifile:
            out = "".join(f"{int(c,16):04b}" for c in line.strip())
    res, _, _ = packet(out)
    return res

if __name__ == "__main__":
    print(solve("../inputs/day16-demo.in"))
