#!/usr/bin/python3

import itertools
import math
import typing
from collections.abc import Iterable

def solve(entries:Iterable,r:int):
	"""
	Prints the product of r expense entries whose sum is 2020.
	"""
	combs = [(sum(p),math.prod(p)) for p in itertools.combinations(entries,r)]
	solution = list(filter(lambda c:c[0]==2020, combs))
	for s,p in solution:
		print(p)

def main():
	with open('input1.txt') as fin:
		entries = [int(line) for line in fin.readlines()]
		solve(entries,2)
		solve(entries,3)

if __name__ == '__main__':
	main()