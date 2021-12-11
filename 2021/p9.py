#!/usr/bin/python3

import aocd
from collections import deque
from functools import partial
from icecream import ic
from itertools import filterfalse
from math import prod

DATA = """2199943210
3987894921
9856789892
8767896789
9899965678
"""

def neighbors(heightmap,row,col):
	"""
	Return a list of index 2-tuples of neighboring cells in
	heightmap to the cell located at (row,col)
	"""
	return filterfalse(lambda c: c[0] < 0 or c[1] < 0 or c[0] >= len(heightmap) or c[1] >= len(heightmap[c[0]]),
		[(row+r, col+c) for r,c in ((-1,0),(1,0),(0,-1),(0,1))])

look = partial(lambda matrix,tup: matrix[tup[0]][tup[1]])

def neighborvals(heightmap,row,col):
	"""
	Return the values of neighboring cells to the cell at [row][col]
	"""
	return [look(heightmap,neighbor) for neighbor in neighbors(heightmap,row,col)]

def risklevel(heightmap):
	risks = 0
	for row in range(len(heightmap)): 
		for col in range(len(heightmap[row])):
			if all(heightmap[row][col] < n for n in neighborvals(heightmap,row,col)):
				risks += look(heightmap,(row,col)) + 1
	return risks

def sinks(heightmap):
	return [(row, col) for row in range(len(heightmap)) for col in range(len(heightmap[row])) 
		if all(heightmap[row][col] < n for n in neighborvals(heightmap,row,col))]

def basin(sink, heightmap):
	basinset = set()

	# Perform a breadth first search of the basin
	search = deque([sink])
	while search:
		ic(search)
		
		# If coord hasn't yet been visited, add it to the return set
		coord = search.popleft()
		basinset |= {coord}
		
		# Update the search deque with unvisited, higher neighbors
		for neighbor in neighbors(heightmap, *coord):
			if (look(heightmap, neighbor) > look(heightmap, coord)) and look(heightmap,neighbor) != 9:
					search.append(neighbor)
		ic(basinset)

	# BFS is complete
	return basinset

def basinprod(heightmap):
	sinklist = sinks(heightmap)
	basindict = {sink:basin(sink, heightmap) for sink in sinklist}
	return prod(list(reversed(sorted(
		len(val) for val in basindict.values())))[:3])

def test():
	heightmap = [[int(n) for n in line] for line in DATA.splitlines()]
	ic(heightmap)

	### PART A ###
	assert risklevel(heightmap) == 15
	
	### PART B ###
	assert basinprod(heightmap) == 1134

def main():
	heightmap = [[int(n) for n in line] for line in aocd.data.splitlines()]
	ic(heightmap)
	
	aocd.submit(risklevel(heightmap), part='a')
	aocd.submit(basinprod(heightmap), part='b')

if __name__ == '__main__':
	ic.disable()
	test()
	main()
