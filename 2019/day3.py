#!/usr/bin/python3

import operator
import functools
import itertools

# Returns the Manhattan distance between two points expressed 
# as two-dimensional sequence type (usually a tuple)
distance = lambda a,b: abs(a[0]-b[0]) + abs(a[1]-b[1])
assert distance((0,0),(3,5)) == 8

# Add two tuples together element-wise
tupadd = lambda a,b: tuple(map(operator.add,a,b))
assert tupadd((1,-1),(3,5)) == (4,4)

def convert(s):
	"""
	Convert a vector string into a 2-tuple vector
	"""
	direction,distance = s[0],int(s[1:])
	if direction == 'L':
		return ((-1,0),distance)
	elif direction == 'R':
		return ((1,0), distance)
	elif direction == 'D':
		return ((0,-1), distance)
	elif direction == 'U':
		return ((0,1), distance)
	else:
		raise ValueError("Unknown direction %s" % direction)

if __name__ == "__main__":
	
	# Read inputs
	with open('inputs/day3.txt', 'r') as f:
		vs1 = [convert(v) for v in f.readline().rstrip('\n').split(',')]
		vs2 = [convert(v) for v in f.readline().rstrip('\n').split(',')]
	
	# Trace wires. Each wire starts at origin.
	w1 = [(0,0)]
	# For each vector, add the next point to the wire list, until remaining
	# distance to add in that direction is zero.
	for v in vs1:
		tup, dist = v
		while dist > 0:
			w1.append(tupadd(w1[-1], tup))
			dist -= 1
	# Repeat for wire 2.
	w2 = [(0,0)]
	for v in vs2:
		tup, dist = v
		while dist > 0:
			w2.append(tupadd(w2[-1], tup))
			dist -= 1
	
	# Find the set of all intersections of the wires
	intersections = [w for w in (set(w1) & set(w2)) - {(0,0)}]
	
	# Find the distance to the closest intersection
	print("Closest intersection: ", 
		min(map(lambda i: distance(i,(0,0)), intersections)))
	
	# Find combined wire distance for each intersection
	distances = [w1.index(i) + w2.index(i) for i in intersections]
	print("Closest intersection by wire distance: ", min(distances))
	
	
	