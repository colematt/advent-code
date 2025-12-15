#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
from copy import deepcopy

testdata = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

def solveA(data:str) -> int:
    # Parse data
    diagram = [[col for col in row] for row in data.splitlines()]

    # Initialize intensity diagram
    nrows, ncols = len(diagram), len(diagram[0])
    intensities = [[0 for _ in range(ncols)] for _ in range(nrows)]
    for row in range(nrows):
        for col in range(ncols):
            if diagram[row][col] == 'S':
                intensities[row][col] = 1
    
    # Propagate beams downward
    nsplits = 0
    for row in range(1,nrows):
        for col in range(ncols):
            if diagram[row][col] == '^':
                if intensities[row-1][col] > 0: 
                    nsplits += 1
                intensities[row][col-1] += (intensities[row-1][col]) + intensities[row-1][col-1]
                intensities[row][col+1] += (intensities[row-1][col]) + intensities[row-1][col+1]
                intensities[row][col] = 0
            else:
                intensities[row][col] += intensities[row-1][col]
    return nsplits

def solveB(data:str) -> int:
    # Parse data
    diagram = [[col for col in row] for row in data.splitlines()]

    # Initialize intensity diagram
    nrows, ncols = len(diagram), len(diagram[0])
    intensities = [[1 if diagram[row][col] == "S" else 0 
                    for col in range(ncols)] for row in range(nrows)]
    
    # Propagate beams downward
    for row in range(1,nrows):
        for col in range(ncols):
            if diagram[row][col] == ".":
                intensities[row][col] += intensities[row-1][col]
            elif diagram[row][col] == "^":
                intensities[row][col] = 0
                intensities[row][col-1] += intensities[row-1][col]
                intensities[row][col+1] += intensities[row-1][col]
            else:
                raise ValueError("Unexpected diagram value at (%i,%i): %s" % (row,col,diagram[row][col]))
            
    # Count paths to bottom row
    return sum(intensities[-1])

if __name__ == "__main__":
    assert solveA(testdata) == 21
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 40
    submit(str(solveB(data)), part='b')
