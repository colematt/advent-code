#!/usr/bin/env python3

from aocd import data, submit
import copy

from icecream import ic

testdata = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
# Shorthand lambda to check if a tuple is inbounds
inbounds = lambda m,r,c: all([r >= 0, r < len(m), c >= 0, c < len(m[0])])

def canonicalize(data):
    return [[col for col in row] for row in data.splitlines()]


def walk(lab,include_vector=False):
    """
    Yield the spaces that a guard in the lab walks
    """
    # Initialize guard position, vector
    r,c,dr,dc = 0,0,0,0
    for row in range(len(lab)):
        for col in range(len(lab[row])):
            if lab[row][col] in ('^','>','v','<'):
                 r,c = row,col
                 match (lab[row][col]):
                    case '^': dr,dc = -1,0
                    case '>': dr,dc = 0,1
                    case 'v': dr,dc = 1,0
                    case '<': dr,dc = 0,-1
                    case _: raise ValueError("Unexpected vector: %s" % lab[row][col])

    # Perform the walk
    while inbounds(lab, r,c):
        # Yield the coordinates
        if include_vector:
           yield (r,c, dr, dc)
        else:
            yield (r,c)

        # Check to see if next coordinate is an obstacle, adjust vector if so
        if inbounds(lab, r+dr, c+dc) and lab[r+dr][c+dc] == '#':
            match (dr,dc):
                case (-1,0): dr,dc = 0,1   # ^ -> >
                case (0,1):  dr,dc = 1,0   # > -> v
                case (1,0):  dr,dc = 0,-1  # v -> <
                case (0,-1): dr,dc = -1,0  # < -> ^
                case _: pass

        # Move (potentially exiting the lav)
        r,c = r+dr, c+dc

def solveA(data):
    # Read in the lab
    lab = canonicalize(data)

    # Get the set of tiles visited using the walk generator
    visited = set(walk(lab))
    return len(visited)

if __name__ == "__main__":
    assert solveA(testdata) == 41
    submit(solveA(data), part='a')

