#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
from itertools import chain

# testdata = "11-22,95-115,998-1012"
testdata = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
    1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
        824824821-824824827,2121212118-2121212124"

def isInvalidA(i:int) -> bool:
    s = str(i)
    if len(s) % 2 == 1:
        return False
    else:
        return s[0:(len(s)//2)] == s[len(s)//2:]


def isInvalidB(i:int) -> bool:
    s = str(i)

    # Split s into n-length substrings 
    for n in range(1,len(s)//2 + 1):
        # If s can't be split into equally sized substrings, continue to next n 
        # (e.g. '123412345' is not invalid at n=4)
        if (len(s) % n) != 0:
            continue
        else:
            splits = tuple(map(''.join, zip(*[iter(s)]*n)))
            # If all of the substrings are the same, it's invalid
            if all(s == splits[0] for s in splits):
                return True
    # If for no value of n are all substrings the same, it's not invalid
    return False

def solveA(data:str) -> int: 
    ranges = tuple(range(int(l),int(r)+1) 
                   for l,_,r in [s.partition("-") for s in data.split(",")])
    ids = [i for i in chain(*ranges)]
    invalids = list(filter(isInvalidA, ids))
    return sum(invalids)


def solveB(data:str) -> int:
    ranges = tuple(range(int(l),int(r)+1) 
                   for l,_,r in [s.partition("-") for s in data.split(",")])
    ids = [i for i in chain(*ranges)]
    invalids = list(filter(isInvalidB, ids))
    return sum(invalids)


if __name__ == "__main__":
    # assert solveA(testdata) == 1227775554
    # submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 4174379265
    submit(str(solveB(data)), part='b')