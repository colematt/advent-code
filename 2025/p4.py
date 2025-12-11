#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
import typing
import functools
import operator

testdata = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

def arrget(arr:typing.Sequence,pos:tuple[int,...]) -> typing.Any:
	"""
	Given a tuple containing the dimensional indices, retrieve that element 
    from a multidimensional array.

    Examples:
    arrget([[1,2],[3,4]], (0,0)) == 1
    arrget([[1,2],[3,4]], (1)) == [3,4]
    arrget([[1,2],[3,4]], (0,0,0)) => TypeError: 'int' object is not subscriptable
	"""
	return functools.reduce(lambda a, i: operator.getitem(a,i), pos, arr)

def neighbors(pos:tuple[int,int], nrows:int, ncols:int) -> list[tuple[int,int]]:
    row,col = pos
    return [(row+r,col+c) for r in (-1,0,1) for c in (-1,0,1)
            if row+r >= 0 and row+r < nrows
            and col+c >= 0 and col+c < ncols
            and (row+r,col+c) != pos]

def solveA(data: str) -> int:
    # Parse the grid, get rolls
    grid = [[col for col in row] for row in data.splitlines()]
    rolls = list()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                rolls.append((row,col))
    # Count accessible rolls
    count = 0
    for roll in rolls:
         adjs = list(neighbors(roll, len(grid), len(grid[0])))
         adjs = [arrget(grid, pos) for pos in adjs]
         if adjs.count('@') < 4:
              count += 1 
    return count


def solveB(data: str) -> int:
    # Parse the grid, get rolls
    grid = [[col for col in row] for row in data.splitlines()]
    rolls = set()
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                rolls.add((row,col))
    startsz = len(rolls) 

    # Find removable rolls
    removables = set()
    for roll in rolls:
         adjs = list(neighbors(roll, len(grid), len(grid[0])))
         adjs = [arrget(grid, pos) for pos in adjs]
         if adjs.count('@') < 4:
              removables.add(roll)

    # While there are removable rolls,
    while removables:
        # remove removables from grid and rolls
        for roll in removables:
            row, col = roll
            grid[row][col] = '.'
            rolls.discard(roll)

        # update removables
        removables.clear()
        for roll in rolls:
            adjs = list(neighbors(roll, len(grid), len(grid[0])))
            adjs = [arrget(grid, pos) for pos in adjs]
            if adjs.count('@') < 4:
                removables.add(roll)
    
    # Return number of removed rolls
    finishsz = len(rolls)
    return startsz - finishsz
    

if __name__ == "__main__":
    assert solveA(testdata) == 13
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 43
    submit(str(solveB(data)), part='b')