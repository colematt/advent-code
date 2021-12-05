#!/usr/bin/python3

import aocd
from icecream import ic
import collections

DATA = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

def read_data(data):
	return [tuple(tuple(int(x) for x in pair.strip().split(',')) 
			for pair in line.split('->'))
				for line in data.splitlines()]

def get_points(endpoints, diagonals=False):
	points = list()

	for start,stop in endpoints:
		x1,y1 = start
		x2,y2 = stop

		# Horizontal case
		if x1 == x2:
			y = min(y1,y2)
			x = x1 
			while y <= max(y1,y2):
				points.append((x,y))
				y += 1
		# Vertical case
		elif y1 == y2:
			x = min(x1,x2)
			y = y1
			while x <= max(x1,x2):
				points.append((x,y))
				x += 1
		# Diagonal case
		else:
			if diagonals:
				if x1 < x2: 
					dx = 1
					x = x1
				else: 
					dx = -1
					x = x1
				if y1 < y2: 
					dy = 1
					y = y1
				else: 
					dy = -1
					y = y1
				while x != x2 and y != y2:
					points.append((x,y))
					x += dx
					y += dy
				points.append((x2,y2))
	return points

def test():
	endpoints = read_data(DATA)

	### PART A ###
	points = get_points(endpoints)
	counts = collections.Counter(points).values()
	assert(len(list(filter(lambda c: c >= 2, counts))) == 5)

	### PART B ###
	points = get_points(endpoints,diagonals=True)
	counts = collections.Counter(points).values()
	assert(len(list(filter(lambda c: c >= 2, counts))) == 12)

def main():
	endpoints = read_data(aocd.data)

	### PART A ###
	points = get_points(endpoints)
	counts = collections.Counter(points).values()
	aocd.submit(len(list(filter(lambda c: c >= 2, counts))), part="a")

	### PART B ###
	points = get_points(endpoints,diagonals=True)
	counts = collections.Counter(points).values()
	aocd.submit(len(list(filter(lambda c: c >= 2, counts))), part="b")


if __name__ == '__main__':
	test()
	main()