#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()

from math import prod

testdata = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

def count_trees(forest:list[list[str]], start:tuple[int,int], slope:tuple[int,int]) -> int:
    # Initialize
    x,y = start
    dx,dy = slope
    height,width = len(forest), len(forest[0])
    count = 0
    
    # Move Santa counting trees
    while y < height:
        if forest[y][x] == '#': count += 1
        x = (x + dx) % width
        y = (y + dy)
    return count


def solveA(data:str) -> int:
    forest = [[c for c in line.strip('\n')] for line in data.splitlines()]
    return count_trees(forest,(0,0),(3,1))

def solveB(data:str) -> int:
    forest = [[c for c in line.strip('\n')] for line in data.splitlines()]
    slopes = ((1,1),(3,1),(5,1),(7,1),(1,2))
    return prod(count_trees(forest,(0,0),slope) for slope in slopes)

if __name__ == "__main__":
    assert(solveA(testdata) == 7)
    submit(str(solveA(data)), part='a')
    assert(solveB(testdata) == 336)
    submit(str(solveB(data)), part='b')
