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
        else:
            # Move (potentially exiting the lav)
            r,c = r+dr, c+dc

def solveA(data):
    # Read in the lab
    lab = canonicalize(data)

    # Get the set of tiles visited using the walk generator
    visited = set(walk(lab))
    return len(visited)

def solveB(data):
    # Read in the lab map
    lab = canonicalize(data)

    # Get the list of tiles visited plus vectors while walking without cycles
    states = list(walk(lab, include_vector=True))

    # Look for potential obstacle points for creating cycles.
    # An obstacle point occurs if walk initiated from the start would cycle
    obstacles = set()
    for state in states:
        # Copy the map and add an obstacle at the "next" tile
        copylab = copy.deepcopy(lab)
        r,c,dr,dc = state
        if inbounds(copylab, r+dr,c+dc):
            obstacle = (r+dr,c+dc)
            copylab[r+dr][c+dc] = '#'
        else:
            continue  

        # Perform the walk looking for a cycle
        visited = set()
        for step in walk(copylab,include_vector=True):
            if (step in visited):
                obstacles.add(obstacle)
                break
            else:
                visited.add(step)

    # Return the solution
    # The initial position cannot be an obstacle
    obstacles = set(filter(lambda ob: lab[ob[0]][ob[1]] not in ('^','>','v','<'), obstacles))
    return len(obstacles)

if __name__ == "__main__":
    assert solveA(testdata) == 41
    submit(solveA(data), part='a')

    assert solveB(testdata) == 6
    submit(solveB(data), part='b')