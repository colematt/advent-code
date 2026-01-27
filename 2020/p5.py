#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()

testdata = """FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
"""

def getID(seat:str) -> int:
    """
    Convert seat to ID.
    """
    row, col = seat[:7], seat[7:]
    table = str.maketrans({'F':'0','B':'1','L':'0','R':'1'})  
    row = int(row.translate(table),2)
    col = int(col.translate(table),2)
    return (8 * row) + col

def solveA(data:str) -> int:
    seats = list(data.splitlines())
    ids = [getID(seat) for seat in seats]
    return max(ids)


def solveB(data:str) -> int:
    seats = list(data.splitlines())
    ids = set(getID(seat) for seat in seats)
    seats = set(i for i in range(min(ids),max(ids)+1))
    return seats.difference(ids).pop()


if __name__ == "__main__":
    assert getID("FBFBBFFRLR") == 357
    assert solveA(testdata) == 820
    submit(str(solveA(data)), part='a')
    submit(str(solveB(data)), part='b')
