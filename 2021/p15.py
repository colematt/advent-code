#!/usr/bin/python

from aocd import data, submit
from icecream import ic 
from functools import partial
from itertools import filterfalse
from operator import getitem,setitem
from DataStructures.AbstractDataStructures import DuplicatePriorityQueue

testdata = """1163751742
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
wrapper = partial(lambda n: n if (n > 0 and n <=9) else (n-1) % 9 + 1)

def strGraph(graph):
	return "\n".join(
		"".join(str(col) for col in row) for row in graph)


def parse(data):
	return [[int(col) for col in row] for row in data.splitlines()]


def expand(graph):
	"""
	{ Expand an n x n graph into a 5n x 5n graph
	  following increasing risk level rule. }
	"""
	# Initialization:
	nrows = len(graph)												# number of rows in graph
	ncols = max([len(row) for row in graph])	# number of cols in each row of graph

	# Copy graph -> expanded
	expanded = [[graph[row][col] if (row < nrows and col < ncols) 
		else wrapper(graph[row % nrows][col % ncols] + row // nrows + col // ncols) 
		for col in range(ncols * 5)] for row in range(nrows * 5)]
	
	return expanded


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
	nrows = len(graph)							# number of rows in graph
	ncols = max([len(row) for row in graph])	# number of cols in each row
	maxpri = sum(map(sum,graph)) + 1 			# maximum queue priority 
												# (e.g, the maximum risk level 
												# occurs when a path goes over 
												# each cell once)

	# Set dist[source] to 0, all others to maxpri
	dist = [[maxpri for _ in range(ncols)] for _ in range(nrows)]
	setter(dist,*source,0) # pyright: ignore[reportCallIssue]

	# Set prev[source] to tuple(), all others to None
	prev = [[None for _ in range(ncols)] for _ in range(nrows)]
	setter(prev,*source,tuple()) # pyright: ignore[reportCallIssue]

	# For each cell in graph, add to priority queue Q, priority=dist[cell]
	Q = DuplicatePriorityQueue(reverse=True)
	for row in range(nrows):
		for col in range(ncols):
			Q.enqueue((row,col),getter(dist,row,col))

	# Exploration:
	# While there are unexplored cells in Q:
	while Q:
		# Remove and return the min priority vertex u from Q
		u = Q.dequeue()

		# For each neighbor v of u:
		for v in neighbors(graph,*u): # pyright: ignore[reportOptionalIterable]
			# Calculate alt = dist[u] + graph[v]
			alt = getter(dist,*u) + getter(graph,*v) # pyright: ignore[reportOptionalIterable, reportOperatorIssue]
			
			# Update if alt has found a better path
			if alt < getter(dist,*v):
				setter(dist,*v,alt)
				setter(prev,*v,u)
				Q.enqueue(v,alt)

	return dist,prev


def solveA(data:str) -> int:
	graph = parse(data)
	dist, prev = explore(graph,(0,0))
	return dist[-1][-1]


def solveB(data:str) -> int:
	graph = expand(parse(data))
	dist, prev = explore(graph,(0,0))
	return dist[-1][-1]

	
if __name__ == '__main__':
	assert solveA(testdata) == 40
	submit(str(solveA(data)), part='a')
	assert solveB(testdata) == 315
	submit(str(solveB(data)), part='b')