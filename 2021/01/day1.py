#!/usr/bin/python3

import aocd
from icecream import ic
import itertools
import math
import operator



def test():
	with open('test.txt', 'r') as fin:
		depths = [int(d) for d in fin.readlines()]

	### PART A ###
	depths2 = list(zip(depths, depths[1:]))
	increases = len(list(filter(lambda d: d[0] < d[1], depths2)))
	assert(increases == 7)

	### PART B ###
	depths3 = list(zip(depths, depths[1:], depths[2:]))
	depthsums = [sum(tup) for tup in depths3]
	depthsums2 = list(zip(depthsums, depthsums[1:]))
	increases = len(list(filter(lambda d: d[0] < d[1], depthsums2)))
	assert(increases == 5)

def main():
	depths = aocd.numbers

	### PART A ###
	depths2 = list(zip(depths, depths[1:]))
	increases = len(list(filter(lambda d: d[0] < d[1], depths2)))
	aocd.submit(increases, year=2021, day=1, part='a')

	### PART B ###
	depths3 = list(zip(depths, depths[1:], depths[2:]))
	depthsums = [sum(tup) for tup in depths3]
	depthsums2 = list(zip(depthsums, depthsums[1:]))
	increases = len(list(filter(lambda d: d[0] < d[1], depthsums2)))
	aocd.submit(increases, year=2021, day=1, part='b')

if __name__ == '__main__':
	test()
	main()