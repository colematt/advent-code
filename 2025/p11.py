#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()
from collections import defaultdict
import functools

testdata = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

def count_paths(device:str, mapping: dict[str,list[str]]) -> int:
    if device == "you":
        return 1
    else:
        return sum([count_paths(source, mapping) for source in mapping[device]])

def solveA(data: str) -> int | None:
    # Parse data successors mapping
    successors = dict()
    for line in data.splitlines():
        key = line.split()[0].rstrip(":")
        values = tuple(val for val in line.split()[1:])
        successors[key] = values
    ic(successors)

    # Invert successors mapping in predecessors
    predecessors = defaultdict(list)
    for key in successors:
            for val in successors[key]:
                predecessors[val].append(key)
    ic(predecessors)

    return(count_paths("out", predecessors))

if __name__ == "__main__":
    assert solveA(testdata) == 5
    # submit(str(solveA(data)), part='a')
