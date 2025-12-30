#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
from collections import defaultdict

testdataA = """aaa: you hhh
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

def solveA(data: str) -> int:    
    # Parse data successors mapping
    successors = dict()
    for line in data.splitlines():
        key = line.split()[0].rstrip(":")
        values = tuple(val for val in line.split()[1:])
        successors[key] = values
        
    # Invert successors mapping in predecessors
    predecessors = defaultdict(list)
    for key in successors:
            for val in successors[key]:
                predecessors[val].append(key)

    # Build path memo table
    devices:set[str] = set(predecessors.keys()) | set(successors.keys())
    paths:dict[str,int|None] = {key:None for key in devices}
    paths["you"] = 1

    # Calculate shortest path table
    def count_paths(device:str) -> int:
        if paths[device] == None:
            paths[device] = sum([count_paths(source) for source in predecessors[device]])
        return paths[device] # pyright: ignore[reportReturnType]
    return(count_paths("out"))

if __name__ == "__main__":
    assert solveA(testdataA) == 5
    submit(str(solveA(data)), part='a')
