#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
import numpy as np
from collections import defaultdict
from itertools import combinations

testdata = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

def get_antennas(map: str) -> dict:
    nodes = np.ndenumerate(np.array(
       [[col for col in row] for row in map.splitlines()]))
    antennas = defaultdict(list)
    for idx, freq in nodes:
        if freq != '.':
            antennas[str(freq)].append(idx)
    return dict(antennas)


def get_antinodes(antennas: dict, nrows: int, ncols: int) -> dict:
    antinodes = defaultdict(set)
    for freq in antennas:
        for pair in combinations(antennas[freq], r=2):
            # Calculate antenna locations/displacement
            ((r1, c1), (r2, c2)) = pair
            dr, dc = r2 - r1, c2 - c1

            # Naively add antinodes
            antinodes[freq].add((r1-dr, c1-dc))
            antinodes[freq].add((r2+dr, c2+dc))
            
        # Filter antinodes for out-of-bounds position
        for freq in antinodes.keys():
            antinodes[freq] = set(filter(lambda n: n[0] < 0 
                                                or n[1] < 0
                                                or n[0] >= nrows
                                                or n[1] >= ncols, antinodes[freq]))
    return dict(antinodes)


def solveA(data:str) -> str:
    antennas = get_antennas(data)
    antinodes = get_antinodes(antennas, len(data), len(data[0]))
    ic(antinodes)
    
    return ""

if __name__ == "__main__":
    solveA(testdata)