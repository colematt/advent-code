#!/usr/bin/env python3

from functools import cache
from aocd import data, submit
from icecream import ic
ic.disable()
from itertools import pairwise

testdata = """16
10
15
5
1
11
7
19
6
12
4
"""
testdata_large = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

def solveA(data:str) -> int:
    # Read in adapter list, add 0 and max+3 
    adapters = list(sorted(int(n) for n in data.splitlines()))
    adapters.insert(0,0)
    adapters.append(max(adapters) + 3)

    # Get diffs
    diffs = [y-x for x,y in pairwise(adapters)]
    return diffs.count(1) * diffs.count(3)

@cache
def arrangements(adapters:tuple[int]) -> int:
    # Get tail sequence
    head, tail = adapters[0], adapters[1:]
    
    # Use dynamic programming to count the number of arrangements
    # to device (last item in tail)
    # Base case: 
    # head is within 3 jolts of the last item of the tail (the built in adaptor)
    if tail[-1] - head <= 3: # pyright: ignore[reportGeneralTypeIssues]
        return 1
    # Recursive case: 
    # head is within 3 jolts of each of the first three adaptors in tail
    arrs = 0
    if len(tail) > 0 and tail[0] - head <= 3:
        arrs += arrangements(tail[0:])
    if len(tail) > 1 and tail[1] - head <= 3:
        arrs += arrangements(tail[1:])
    if len(tail) > 2 and tail[2] - head <= 3:
        arrs += arrangements(tail[2:])
    return arrs

def solveB(data:str) -> int:
    # Read in adapter list, add 0 and max+3 
    adapters = list(sorted(int(n) for n in data.splitlines()))
    adapters.insert(0,0)
    adapters.append(max(adapters) + 3)
    adapters = tuple(adapters)

    # Find count of possible adaptor chains
    return arrangements(adapters)

if __name__ == "__main__":
    assert solveA(testdata) == 35
    assert solveA(testdata_large) == 220
    submit(str(solveA(data)), part='a')

    assert solveB(testdata) == 8
    assert solveB(testdata_large) == 19208
    submit(str(solveB(data)), part='b')
