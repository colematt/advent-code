#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
import itertools
from operator import add, mul
from functools import reduce
from string import digits
from typing import List,Any

testdata = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
"""

def transpose(array):
    T = type(array)
    return T(itertools.zip_longest(*array))

def split_list(source, sep, *, keep_sep=False, maxsplit=-1):
    # Convert to a list once so we can index and slice efficiently.
    data = list(source)

    # Result containers
    chunks: List[List[Any]] = []
    current_chunk: List[Any] = []

    splits_done = 0

    for item in data:
        if item == sep and (maxsplit < 0 or splits_done < maxsplit):
            # End the current chunk
            chunks.append(current_chunk)
            current_chunk = []

            if keep_sep:
                # Start the next chunk with the separator itself.
                # (the first chunk never gets a leading separator)
                current_chunk.append(sep)

            splits_done += 1
        else:
            current_chunk.append(item)

    # Append the final (possibly empty) chunk
    chunks.append(current_chunk)

    return chunks

def solveA(data: str) -> int:
    # Parse data
    lines = [line for line in data.splitlines()]
    ops = [add if op == "+" else mul for op in lines[-1].split()]
    nums = transpose([[int(n) for n in line.split()] for line in lines[:-1]])

    # Do the math
    results = [reduce(op,ns) for op,ns in zip(ops, nums)]
    return sum(results)

def solveB(data: str) -> int:
    # Parse data
    lines = list(data.splitlines())
    ops = [add if op == "+" else mul for op in lines[-1].split()]
    nums = [[int(n) if n in digits else None for n in line] for line in lines[:-1]]
    
    # Transform nums matrix into a list of columns
    cols = list()
    for col in range(len(nums[0])):
        n = 0
        for row in range(len(nums)):
            if type(nums[row][col]) is int:
                n = (n * 10) + nums[row][col] # type: ignore
        cols.append(n)
    
    # Do the math
    cols = split_list(cols,0)
    results = [reduce(op,ns) for op,ns in zip(ops, cols)]
    return sum(results)
    

if __name__ == "__main__":
    assert solveA(testdata) == 4277556
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 3263827
    submit(str(solveB(data)), part='b')
