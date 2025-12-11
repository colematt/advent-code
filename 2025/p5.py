#!/usr/bin/env python3

from operator import itemgetter
from aocd import data, submit
from icecream import ic
from copy import deepcopy

testdata = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

def solveA(data: str) -> int:
    # Parse test data
    ranges, _, ids = data.partition("\n\n")
    ranges = [range(int(start), int(stop)+1) for start,stop in  
              [line.split('-') for line in ranges.splitlines()]]
    ids = [int(i) for i in ids.splitlines()]

    # Filter only fresh ids
    fresh = list(filter(lambda i: any(i in ran for ran in ranges), ids))
    return len(fresh)


def solveB(data: str) -> int:
    # Parse test data
    ranges, _, _ = data.partition("\n\n")
    ranges = list(sorted([(int(start), int(stop)) for start,stop in  
              [line.split('-') for line in ranges.splitlines()]], key=itemgetter(0)))

    # XXX: Naively Count fresh ID ranges' members
    # ids = set(itertools.chain(*ranges))
    # return(len(ids))

    # Coalesce the range start/stop if they overlap
    coalesced = list()
    if len(ranges) >= 1:
        (istart,istop) = ranges.pop(0)
        while ranges:
            # Get next item from the copied list
            (jstart,jstop) = ranges.pop(0)
            # If overlapped, coalesce j in to i
            if jstart >= istart and jstart <= istop:
                istart, istop = min(istart, jstart), max(istop,jstop)
                (jstart,jstop) = (None,None)
            # Else, push i into ranges, move j into i
            else:
                coalesced.append((istart,istop))
                (istart,istop) = (jstart,jstop)
        
        coalesced.append((istart,istop))
        if (jstart,jstop) != (None,None):
            coalesced.append((jstart,jstop))

    # Sum the span of the ranges (without actually generating them)
    return sum((stop-start+1) for start,stop in coalesced)


if __name__ == "__main__":
    assert solveA(testdata) == 3
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 14
    submit(str(solveB(data)), part='b')