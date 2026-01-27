#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()

testdata = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def solveA(data:str) -> int:
    """
    Find the sum of the count of answers by group, 
    where the anyone in the group had a particular answer
    """
    groups = [tuple(set(answers) for answers in group.split("\n")) 
                    for group in data.split('\n\n')]
    sets = [set.union(*g) for g in groups]
    counts = [len(s) for s in sets]
    return sum(counts)


def solveB(data:str) -> int:
    """
    Find the sum of the count of answers by group, 
    where the entire group had the same answer
    """
    groups = [tuple(set(answers) for answers in group.split("\n")) 
                    for group in data.split('\n\n')]
    sets = [set.intersection(*g) for g in groups]
    counts = [len(s) for s in sets]
    return sum(counts)


if __name__ == "__main__":
    assert(solveA(testdata) == 11)
    submit(str(solveA(data)), part='a')
    assert(solveB(testdata) == 6)
    submit(str(solveB(data)), part='b')
    
