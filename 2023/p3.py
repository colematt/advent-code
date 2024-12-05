#!/usr/bin/env python3

from aocd import data,submit
import string
NUMBERS = set(string.digits)
SYMBOLS = set(string.punctuation).difference(".")

testdata = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def canonicalize(data):
    # Get full manifest from data
    manifest = [row for row in data.splitlines()]

    # Find parts
    parts = list()
    for row in range(len(manifest)):
        part,start,stop = 0,None,None
        for col in range(len(manifest[row])):
            # Read a part
            if manifest[row][col] in NUMBERS:
                # Start reading
                if start == None: start = col
                # Continue reading
                part = part*10 + int(manifest[row][col])
            else:
                # Stop reading
                if start != None:
                    stop = col-1
                    parts.append((part,(row,start),(row,stop)))
                    # Reset for next part
                    part,start,stop = 0,None,None
    return parts


def solveA(data):
    parts = canonicalize(data)
    return None


if __name__ == "__main__":
    assert solveA(testdata) == 4361
