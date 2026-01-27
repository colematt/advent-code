#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()

testdata = """1721
979
366
299
675
1456
"""

def solveA(data:str) -> int | None:
    entries = list(sorted([int(n) for n in data.splitlines()]))
    i,j = 0,len(entries)-1
    while entries[i] + entries[j] != 2020:
        if i == j:
            return None
        elif entries[i] + entries[j] < 2020:
            i += 1
        elif entries[i] + entries[j] > 2020:
            j -= 1
    return entries[i] * entries[j]


def solveB(data:str) -> int | None:
    entries = list(sorted([int(n) for n in data.splitlines()]))
    i,j,k = 0,1,len(entries)-1
    while i < k:
        if entries[i] + entries[k-1] + entries[k] < 2020: i += 1
        elif entries[i] + entries[i+1] + entries[k] > 2020: k -= 1
        else:  
            for j in range(i,k):
                if entries[i] + entries[j] + entries[k] == 2020:
                    return entries[i] * entries[j] * entries[k]
    return None


if __name__ == "__main__":
    assert(solveA(testdata) == 514579)
    submit(str(solveA(data)), part='a')
    assert(solveB(testdata) == 241861950)
    submit(str(solveB(data)), part='b')
