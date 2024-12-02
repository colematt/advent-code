#!/usr/bin/env python3

from aocd import data, submit
from collections import Counter
from more_itertools import transpose

testdata = """3   4
4   3
2   5
1   3
3   9
3   3
"""

def solveA(data):
	# Read from text
	lists = [tuple(int(x) for x in line.split()) for line in data.splitlines()]
	# Transpose and sort for problem description
	left, right = (sorted(l) for l in transpose(lists))
	# Zip and get sum of differences
	zipped = list(zip(left,right))
	return sum((abs(x-y) for x,y in zipped))
	
def solveB(data):
	# Read from text
	lists = [tuple(int(x) for x in line.split()) for line in data.splitlines()]
	# Transpose and sort for problem description
	left,right = (sorted(l) for l in transpose(lists))
	# Count and get sum of similarity scores
	counts = Counter(right)
	return sum(i*counts[i] for i in left)
	
if __name__ == "__main__":
	assert solveA(testdata) == 11
	submit(solveA(data), part='a')
	
	assert solveB(testdata) == 31
	submit(solveB(data), part='b')
