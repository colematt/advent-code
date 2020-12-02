#!/usr/bin/python3

import itertools
import math

def main():
	with open('input1.txt') as fin:
		# Part 1 
		entries = [int(line) for line in fin.readlines()]
		combs = [(sum(p),math.prod(p)) for p in itertools.combinations(entries,2)]
		solution = list(filter(lambda c:c[0]==2020, combs))
		for s,p in solution:
			print(p)

		# Part 2
		combs = [(sum(p),math.prod(p)) for p in itertools.combinations(entries,3)]
		solution = list(filter(lambda c:c[0]==2020, combs))
		for s,p in solution:
			print(p)

if __name__ == '__main__':
	main()