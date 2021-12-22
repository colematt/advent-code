#!/usr/bin/python

import aocd
from icecream import ic 
from functools import partial
import math
from queue import PriorityQueue

TEST_DATA = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""

getter = partial(lambda matrix,row,col: getitem(getitem(matrix,row),col))
setter = partial(lambda matrix,row,col,val: 
  setitem(getitem(matrix,row),col,val))

def parse(data):
	return [[int(col) for col in row] for row in data.splitlines()]

def neighbors(graph,row,col):
	"""
	Return a list of index 2-tuples of neighboring cells in
	heightmap to the cell located at (row,col)
	"""
	return filterfalse(lambda c: c[0] < 0 or c[1] < 0 or c[0] >= len(graph) or c[1] >= len(graph[c[0]]),
		[(row+r, col+c) for r,c in ((-1,0),(1,0),(0,-1),(0,1))])

def explore(graph, source):
	"""
	Perform Dijkstra's shortest path algorithm on graph starting at source.
	Return dist[cell], the minimum total risk level to reach that point
	Return prev[cell], the predecessor minimum total risk level point
	"""
	# Initialization:
	# Set dist[source] to 0, all others to infinity
	# Set prev[source] to tuple(), all others to None
	# For each cell in graph, add to priority queue Q, priority=dist[cell]
	
	# While there are unexplored cells in Q:
		# Remove and return the min priority vertex u from Q
		# For each neighbor v of u:
	# 	# Calculate alt = dist[u] + graph[v]
	# 	# if alt < dist[v]:
	# 		# Update dist[v] = alt, prev[v] = u
	
	# Return dist[], prev[]

def test():
	graph = parse(TEST_DATA)
	explore(graph,(0,0))

def main():
	pass

if __name__ == '__main__':
	test()
	main()