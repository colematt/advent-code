#!/usr/bin/env python3

from webbrowser import get
from aocd import data,submit
from icecream import ic
from itertools import batched, chain
from math import inf

testdata = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

def getAlmanac(data:str):
    pages = [page for page in data.split("\n\n")]
    seeds = tuple(int(s) for s in pages[0].split(":")[1].strip().split())
    
    # Get seed to soil map
    lines = [line.split() for line in pages[1].splitlines()[1:]]
    lines = tuple(tuple(int(n) for n in line) for line in lines)
    f1 = dict()
    for line in lines:
        dst,src,sz = line
        for i in range(sz):
            f1[src+i] = dst+i
    for seed in seeds:
        if seed not in f1:
            f1[seed] = seed
    ic(len(f1.keys()))

    # Get soil to fertilizer map
    lines = [line.split() for line in pages[2].splitlines()[1:]]
    lines = tuple(tuple(int(n) for n in line) for line in lines)
    f2 = dict()
    for line in lines:
        dst,src,sz = line
        for i in range(sz):
            f2[src+i] = dst+i
    for key in f1:
        if key not in f2:
            f2[key] = key
    ic(len(f2.keys()))
    
    # Get fertilizer to water map
    lines = [line.split() for line in pages[3].splitlines()[1:]]
    lines = tuple(tuple(int(n) for n in line) for line in lines)
    f3 = dict()
    for line in lines:
        dst,src,sz = line
        for i in range(sz):
            f3[src+i] = dst+i
    for key in f2:
        if key not in f3:
            f3[key] = key
    ic(len(f3.keys()))

    # Get water to light map
    lines = [line.split() for line in pages[4].splitlines()[1:]]
    lines = tuple(tuple(int(n) for n in line) for line in lines)
    f4 = dict()
    for line in lines:
        dst,src,sz = line
        for i in range(sz):
            f4[src+i] = dst+i
    for key in f3:
        if key not in f4:
            f4[key] = key
    ic(len(f4.keys()))

    # Get light to temperature map
    lines = [line.split() for line in pages[5].splitlines()[1:]]
    lines = tuple(tuple(int(n) for n in line) for line in lines)
    f5 = dict()
    for line in lines:
        dst,src,sz = line
        for i in range(sz):
            f5[src+i] = dst+i
    for key in f4:
        if key not in f5:
            f5[key] = key
    ic(len(f5.keys()))

    # Get temperature to humidity map
    lines = [line.split() for line in pages[6].splitlines()[1:]]
    lines = tuple(tuple(int(n) for n in line) for line in lines)
    f6 = dict()
    for line in lines:
        dst,src,sz = line
        for i in range(sz):
            f6[src+i] = dst+i
    for key in f5:
        if key not in f6:
            f6[key] = key
    ic(len(f6.keys()))

    # Get humidity to location map
    lines = [line.split() for line in pages[7].splitlines()[1:]]
    lines = tuple(tuple(int(n) for n in line) for line in lines)
    f7 = dict()
    for line in lines:
        dst,src,sz = line
        for i in range(sz):
            f7[src+i] = dst+i
    for key in f6:
        if key not in f7:
            f7[key] = key
    ic(len(f7.keys()))
    
    def almanac(seed:int) -> int:
        return f7[f6[f5[f4[f3[f2[f1[seed]]]]]]]
    
    return almanac


def naiveA(data:str) -> int:
    pages = [page for page in data.split("\n\n")]
    seeds = tuple(int(s) for s in pages[0].split(":")[1].strip().split())
    almanac = getAlmanac(data)
    locations = [almanac(seed) for seed in seeds]
    return min(locations)

def solveA(data:str) -> int | float:
    # Parse input sections for seeds and mappings
    sections = [section for section in data.split("\n\n")]
    seeds = tuple(int(seed) for seed in sections[0].split(":")[1].strip().split())
    mappings = [[tuple(map(int,lines.split())) 
                 for lines in mapping.splitlines()[1:]] 
                 for mapping in sections[1:]]
    minseed = inf
    
    # Perform translation
    for seed in seeds:
        for mapping in mappings:
            for rtup in mapping:
                dst, src, sz = rtup
                if seed in range(src,src+sz):
                    offset = seed - src
                    seed = dst + offset
                    mapped = True
                    break
        if seed < minseed:
            minseed = seed
    return minseed


if __name__ == "__main__":
    assert naiveA(testdata) == 35
    assert solveA(testdata) == 35
    submit(str(solveA(data)), part='a')

    
