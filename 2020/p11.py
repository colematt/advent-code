#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()
from collections import Counter
import copy
import itertools

testdata = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

def getAdjacent(grid, row, col, strict=True):
    """
	Generate the (row,col) tuples which are adjacent to grid[row][col].
	"Strictly adjacent" means seats one space away.
	"Not strictly adjacent" follows the rule set in part 2.
	"""
    try:
        for dr, dc in itertools.product((-1, 0, 1), (-1, 0, 1)):
            # Avoid considering products which won't find adjacent seats:
            # 0) Won't traverse
            # 1) Would traverse off top
            # 2) Would traverse off bottom
            # 3) Would traverse off left
            # 4) Would traverse off right
            if (dr, dc) == (0, 0) or \
                    dr < 0 and row == 0 or \
                    dr > 0 and row == len(grid) - 1 or \
                    dc < 0 and col == 0 or \
                    dc > 0 and col == len(grid[row]) - 1:
                continue

            # Calculate the neighbors for strict (part 1)
            if strict:
                r = row + dr
                c = col + dc
                if (0 <= r < len(grid)) and (0 <= c < len(grid[r])):
                    yield (r, c)
            # Calculate the neighbors for not strict (part 2)
            else:
                r = row + dr
                c = col + dc
                while grid[r][c] == '.':
                    if (dr < 0 and r == 0) or (dr > 0 and r == len(grid) - 1):
                        break
                    if (dc < 0 and c == 0) or (dc > 0 and c == len(grid[r]) - 1):
                        break
                    r += dr
                    c += dc
                if (0 <= r < len(grid)) and (0 <= c < len(grid[r])):
                    yield (r, c)
    except IndexError as ie:
        if row >= len(grid) and col >= len(grid[row]):
            raise IndexError("row %i and col %i argument out of range"
                             % (row, col))
        elif row >= len(grid):
            raise IndexError("row %i argument out of range" % row)
        elif col >= len(grid[row]):
            raise IndexError("col %i argument out of range" % col)
        else:
            raise ie


def countAdjacent(grid, row, col, strict=True):
    """
	Return a count of each type of seat or floor in the adjacent seats as a Counter object.
	"Strictly adjacent" means seats one space away.
	"Not strictly adjacent follows the rule set in part 2.
	"""
    return Counter([grid[r][c] for r, c in list(getAdjacent(grid, row, col, strict))])


def nextGrid(grid, strict=True):
    """
	Model grid after one round of movement.
	"Strictly adjacent" means seats one space away.
	"Not strictly adjacent follows the rule set in part 2.
	"""
    ng = copy.deepcopy(grid)

    # For each seat in grid, if a condition is met, swap its value in the next grid ng
    if strict:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # Floor Seat
                if grid[row][col] == '.':
                    pass
                # Empty Seat
                elif grid[row][col] == 'L':
                    if countAdjacent(grid, row, col, strict)['#'] == 0:
                        ng[row][col] = '#'
                # Occupied Seat
                elif grid[row][col] == '#':
                    if countAdjacent(grid, row, col, strict)['#'] >= 4:
                        ng[row][col] = 'L'
                else:
                    raise ValueError("Encountered a seat with value %s" % grid[row][col])
    else:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # Floor Seat
                if grid[row][col] == '.':
                    pass
                # Empty Seat
                elif grid[row][col] == 'L':
                    if countAdjacent(grid, row, col, strict)['#'] == 0:
                        ng[row][col] = '#'
                # Occupied Seat
                elif grid[row][col] == '#':
                    if countAdjacent(grid, row, col, strict)['#'] >= 5:
                        ng[row][col] = 'L'
                else:
                    raise ValueError("Encountered a seat at [%i][%i] with value %s" %
                                     (row, col, grid[row][col]))
    return ng


def countGrid(grid):
    """
	Return a count of each type of seat or floor in grid as a Counter object.
	"""
    return Counter(list(itertools.chain(*grid)))


def printGrid(grid):
    """
	Pretty print a grid and its counts.
	"""
    for row in grid:
        print("".join(row))
    cg = countGrid(grid)
    print("Empty: %i Occupied: %i Floor: %i" % (cg['L'], cg['#'], cg['.']))

def solveA(data:str) -> int:
    startGrid = [[col for col in row.strip()] for row in data.splitlines()]
    prevGrid = None
    currGrid = copy.deepcopy(startGrid)
    while currGrid != prevGrid:
        prevGrid = currGrid
        currGrid = nextGrid(prevGrid)
    return countGrid(currGrid)['#']

def solveB(data:str) -> int:
    startGrid = [[col for col in row.strip()] for row in data.splitlines()]
    prevGrid = None
    currGrid = copy.deepcopy(startGrid)
    while currGrid != prevGrid:
        prevGrid = currGrid
        currGrid = nextGrid(prevGrid, strict=False)
    return countGrid(currGrid)['#']

if __name__ == "__main__":
    assert solveA(testdata) == 37
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 26
    submit(str(solveB(data)), part='b')
