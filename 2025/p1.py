#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
from itertools import accumulate

testdata = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

def solveA(data:str) -> int:
    # Parse rotations list
    rotations = tuple(int(r[1:]) if r[0]=="R" else -1*int(r[1:]) 
                 for r in data.splitlines())
    
    # Calculate positions after rotation
    positions = tuple(accumulate(rotations, lambda p,r: (p + r) % 100, initial= 50))
    
    # Count number of zero positions
    return positions.count(0)


def solveB(data:str) -> int:
    # Parse rotations list, count full rotations and modularize their rotations
    rotations = tuple(int(r[1:]) if r[0]=="R" else -1*int(r[1:]) 
                 for r in data.splitlines())
    
    # Count clicks from full spins
    clicks = 0
    spins = tuple(abs(r) // 100 for r in rotations)
    clicks += sum(spins)

    # Normalize all rotations to L99 to R99
    rotations = tuple(r % 100 if r >= 0 else -1*(abs(r) % 100) for r in rotations)

    # Calculate positions after rotation
    positions = tuple(accumulate(rotations, lambda p,r: (p + r) % 100, initial= 50))

    # Count clicks from passing or stopping at zero
    zipped = tuple(zip(positions, rotations))
    clicked = tuple(1 if ((p + r <= 0 or p + r >= 100) and (p != 0 or r >= 100)) else 0 
                    for p,r in zipped)
    clicks += clicked.count(1)
    
    return clicks

if __name__ == "__main__":
    assert solveA(testdata) == 3
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 6
    submit(str(solveB(data)), part='b')