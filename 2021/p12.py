#!/usr/bin/python3

import aocd
from collections import deque
from functools import partial
from icecream import ic
from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase

isSmall = partial(lambda s: all([c in lowercase for c in s]))
isBig = partial(lambda s: all([c in uppercase for c in s]))

TESTDATA1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

TESTDATA2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""

TESTDATA3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""

def parse(data):
	"""
	Parse a collection of graph edges from data,
	where each line is an edge of two vertices,
	separated by a hyphen
	"""
	# Read the edges from the data, then duplicate the backwards edges
	edges = [tuple(line.split("-")) for line in data.splitlines()]
	edges.extend([(v2,v1) for v1,v2 in edges])
	
	# Collect the vertices set
	vertices = {v for v,_ in edges} 

	# Construct an adjacency list mapping of the graph
	graph = {vertex:{sink for source,sink in edges if (vertex,sink) in edges} 
		for vertex in vertices}
	
	return graph

def traverse(graph, repeat=False):
	"""
	Traverse the graph using a breadth-first search, 
	returning a list of paths from 'start' to 'end'
	"""
	paths = list() # a list of n-tuple paths from 'start' to 'end'

	# Initialize search at 'start'
	visitors = deque([('start',)])

	# While there are visitors that haven't terminated, pop from visitors queue
	while visitors:
		visitor = visitors.popleft()
		curr = visitor[-1] 
		ic(visitor)

		# If the visitor reaches the end, add it to the paths list,
		# Otherwise, BFS to its valid neighbors
		if curr == 'end': 
			paths.append(visitor)
		else:
			# Attempt to extend the visitor to neighboring nodes
			for neighbor in graph[curr]:
				# Big caves can always be revisited
				if isBig(neighbor):
					newvisitor = visitor+(neighbor,)
					visitors.append(newvisitor)
				
				# Unvisited small caves can always be revisited
				elif neighbor not in visitor:
					newvisitor = visitor+(neighbor,)
					visitors.append(newvisitor)
				
				# If we reach this, a repeat is requested. Check for validity
				elif repeat:
					smallvisits = tuple(
						filter(isSmall,visitor))
					ic(smallvisits)
					if all([smallvisits.count(v) < 2 for v in smallvisits]) and neighbor not in {'start','end'}:
							newvisitor = visitor+(neighbor,)
							visitors.append(newvisitor)
				# This neighbor cannot be visited 
				else:
					pass
						

	ic(len(paths))
	return paths

def solveA(data):
	graph = parse(data)
	paths = traverse(graph)
	ic(len(paths))
	return len(paths)

def solveB(data):
	graph = parse(data)
	paths = traverse(graph, repeat=True)
	return len(paths)

def test():
	ic.disable()
	assert solveA(TESTDATA1) == 10
	assert solveA(TESTDATA2) == 19
	assert solveA(TESTDATA3) == 226
	assert solveB(TESTDATA1) == 36
	assert solveB(TESTDATA2) == 103
	assert solveB(TESTDATA3) == 3509

def main():
	ic.disable()
	aocd.submit(solveA(aocd.data),part='a')
	aocd.submit(solveB(aocd.data),part='b')

if __name__ == '__main__':
	test()
	main()