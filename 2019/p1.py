#!/usr/bin/env python3

from aocd import data,submit
from icecream import ic
from math import floor

testdata = """12
14
1969
100756
"""

fuel = lambda m: max(floor(m/3)-2,0)
fuel.__doc__ = "Convert a mass m to a fuel required to launch that mass"

def solveA(data:str) -> int:
    masses = [int(m) for m in data.splitlines()]
    return sum(map(fuel, masses))

def solveB(data:str) -> int:
    masses = [int(m) for m in data.splitlines()]
    for m in masses:
        f = fuel(m)
        if f > 0:
            masses.append(f)
    return sum(map(fuel,masses))

if __name__ == "__main__":
    assert solveA(testdata) == 2+2+654+33583
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 2+2+966+50346
    submit(str(solveB(data)), part='b')
