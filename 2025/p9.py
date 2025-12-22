#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
from itertools import chain,combinations
from shapely import Polygon, contains

testdata = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

def area(p1:tuple[int,int], p2:tuple[int,int]) -> int:
    x1,y1,x2,y2 = *p1,*p2
    return (abs(x2-x1)+1)*(abs(y2-y1)+1) 


def solveA(data:str) -> int:
    # Parse input
    tiles = [(int(x),int(y)) for x,y in [line.split(',') for line in data.splitlines()]]
    
    # Make iterator of all pairs of tiles on floor
    pairs = list(combinations(tiles, 2))
    
    # Get area of rectangle for each pair and return max area
    areas = [area(p1,p2) for p1,p2 in pairs]
    return max(areas)


def solveB(data:str) -> int:
    # Parse input for red tiles
    reds = [(int(x),int(y)) for x,y in [line.split(',') for line in data.splitlines()]]

    # Construct polygon from colored tiles
    colored = Polygon(reds)

    # Make iterator of all rectangles of 2 red tiles on floor
    redpairs = list(combinations(reds, 2))

    # Make a rectangular polygon from each red pair,
    # Add to list of candidates if the rectangle fits in the colored polygon
    candidates = list()
    for pair in redpairs:
        x1,y1 = pair[0]
        x2,y2 = pair[1]
        rectangle = Polygon([(x1,y1), (x2,y1), (x2,y2), (x1,y2)])
        if contains(colored, rectangle):
            candidates.append(pair)

    # Get the maximal area
    return max(area(p1,p2) for p1,p2 in candidates)


if __name__ == "__main__":
    assert solveA(testdata) == 50
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 24
    submit(str(solveB(data)), part='b')
