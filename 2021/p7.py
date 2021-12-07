#!/usr/bin/python3

import aocd
from icecream import ic
from math import floor, ceil
from statistics import median, mean

DATA = "16,1,2,0,4,2,7,1,2,14"

def getFuelA(crabs,i):
	return sum(abs(crab-i) for crab in crabs)

def solveA(crabs):
	return min(
		getFuelA(crabs,floor(median(crabs))),
		getFuelA(crabs,ceil(median(crabs))))

def getFuelB(crabs,i):
	return int(sum((abs(crab-i))*((abs(crab-i))+1)/2 for crab in crabs))

def solveB(crabs):
	return min(
		getFuelB(crabs,floor(mean(crabs))),
		getFuelB(crabs,ceil(mean(crabs))))

def test():
	crabs = [int(n) for n in DATA.split(',')]
	assert solveA(crabs) == 37
	assert solveB(crabs) == 168

def main():
	crabs = [int(n) for n in aocd.data.split(',')]
	aocd.submit(solveA(crabs), part='a')
	aocd.submit(solveB(crabs), part='b')

if __name__ == '__main__':
	test()
	main()