#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()
from collections import defaultdict
import graphlib
from math import prod

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

testdataB = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
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

    # Calculate path table
    def count_paths(device:str) -> int:
        if paths[device] == None:
            paths[device] = sum([count_paths(source) for source in predecessors[device]])
        return paths[device] # pyright: ignore[reportReturnType]
    return(count_paths("out"))

def solveB(data: str) -> int | None:
    # Parse data successors mapping
    graph:dict[str,set[str]] = dict()
    for line in data.splitlines():
        key = line.split()[0].rstrip(":")
        values = set(val for val in line.split()[1:])
        graph[key] = values
        
    # Topological sort to determine whether
    # svr->dac->fft->out or svr->fft->dac->out
    devices:tuple[str,...] = tuple()
    so:tuple = ("svr", "dac", "fft", "out")
    ts = graphlib.TopologicalSorter(graph)
    try:
        devices = tuple(ts.static_order())
        so = tuple(filter(lambda item: item in so, reversed(devices)))
        ic(so)
    except graphlib.CycleError:
        print("Cycle error, cannot sort!")

    # Invert successors mapping in predecessors
    predecessors = defaultdict(list)
    for key in graph:
            for val in graph[key]:
                predecessors[val].append(key)
    
    def count_paths(device:str) -> int:
        if paths[device] == None:
            paths[device] = sum([count_paths(source) for source in predecessors[device]])
        return paths[device] # pyright: ignore[reportReturnType]
    ans = [0,0,0]

    # Get number of paths from svr->dac/fft
    paths:dict[str,int|None] = {key:None for key in devices}
    paths[so[0]] = 1
    ans[0] = count_paths(so[1])

    # Get number of paths from dac/fft->fft/dac
    paths:dict[str,int|None] = {key:None for key in devices}
    paths[so[1]] = 1
    ans[1] = count_paths(so[2])

    # Get number of paths from fft/dac->out
    paths:dict[str,int|None] = {key:None for key in devices}
    paths[so[2]] = 1
    ans[2] = count_paths(so[3])

    # Get total paths from svr->out
    return prod(ans)
    

if __name__ == "__main__":
    assert solveA(testdataA) == 5
    submit(str(solveA(data)), part='a')
    assert solveB(testdataB) == 2
    submit(str(solveB(data)), part='b')
