#!/usr/bin/python3

import math

def makeAdjacencyMatrix(orbits):
	index = {key:value for value,key in enumerate(sorted(
				set(ctr for ctr,_ in orbits) 
				| set(sat for _,sat in orbits)))}
	print(index)
	am = [[0 for _ in range(len(index))] for _ in range(len(index))]
	for orbit in orbits:
		ctr,sat = orbit
		am[index[ctr]][index[sat]] = 1
		am[index[sat]][index[ctr]] = 1
	return am

def makeAdjacencyList(orbits,directed=True):
	al = dict()
	for orbit in orbits:
		ctr,sat = orbit
		if directed:
			if ctr not in al:
				al[ctr] = [sat]
			else:
				al[ctr] = al[ctr]+[sat]
		else:
			if ctr not in al:
				al[ctr] = [sat]
			else:
				al[ctr] = al[ctr]+[sat]
			if sat not in al:
				al[sat] = [ctr]
			else:
				al[sat] = al[sat]+[ctr]
	return al

def dijkstra(orbits, start='COM',directed=True):
	adjList = makeAdjacencyList(orbits,directed)

	# Mark all nodes unvisited. Create a set of all the unvisited nodes 
	# called the unvisited set.
	unvisited = set(ctr for ctr,_ in orbits) | set(sat for _,sat in orbits)

	# Assign to every node a tentative distance value: 
	# Set distance to zero for initial node and to infinity for all other nodes. 
	# Set the initial node as current.
	distances = {body:math.inf for body in unvisited}
	distances[start] = 0
	current = start

	while current:
		# For the current node, consider all of its unvisited neighbours and 
		# calculate their tentative distances through the current node. 
		# Compare the newly calculated tentative distance to the current assigned 
		# value and assign the smaller one.
		if current in adjList:
			for neighbor in adjList[current]:
				distances[neighbor] = min(distances[neighbor], distances[current]+1)

		# Mark the current node as visited and remove it from the unvisited set.
		unvisited.remove(current)

		# select the unvisited node that is marked with the smallest tentative 
		# distance, set it as the new "current node"
		# If there are no more reachable satellites, then current=None and the 
		# outer while loop terminates.
		mindist = math.inf
		current = None
		for body in unvisited:
			if distances[body] < mindist:
				current = body

	return distances

def main():
	with open('inputs/day6.txt') as fin:
		orbits = [tuple(line.rstrip().split(')')) for line in fin.readlines()]

		# Part 1
		distances = dijkstra(orbits,start='COM',directed=True)
		print(sum(distances[d] for d in distances))

		# Part 2
		distances = dijkstra(orbits,start='YOU',directed=False)
		print(distances['SAN']-2)

if __name__ == '__main__':
	main()