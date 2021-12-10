#!/usr/bin/python3

import aocd
from collections import deque
from functools import partial
from icecream import ic
from itertools import filterfalse

DATA = """2199943210
3987894921
9856789892
8767896789
9899965678
"""

look = partial(lambda matrix,tup: matrix[tup[0]][tup[1]])

def neighbors(heightmap,row,col):
	return filterfalse(lambda c: c[0] < 0 or c[1] < 0 or c[0] >= len(heightmap) or c[1] >= len(heightmap[c[0]]),
		[(row+r, col+c) for r,c in ((-1,0),(1,0),(0,-1),(0,1))])

def neighborlooks(heightmap,row,col):
	return [look(heightmap,neighbor) for neighbor in neighbors(heightmap,row,col)]

def risklevel(heightmap):
	risks = 0
	for row in range(len(heightmap)): 
		for col in range(len(heightmap[row])):
			if all(heightmap[row][col] < n for n in neighborlooks(heightmap,row,col)):
				risks += heightmap[row][col] + 1
	return risks

def test():
	heightmap = [[int(n) for n in line] for line in DATA.splitlines()]
	ic(heightmap)

	### PART A ###
	assert risklevel(heightmap) == 15


def main():
	heightmap = [[int(n) for n in line] for line in aocd.data.splitlines()]
	ic(heightmap)
	
	aocd.submit(risklevel(heightmap), part='a')

if __name__ == '__main__':
	ic.disable()
	test()
	main()
