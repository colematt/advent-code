#!/usr/bin/python3

from math import prod

def count_trees(forest, start, slope):
	x,y = start
	dx,dy = slope
	height = len(forest)
	width = len(forest[0])
	count = 0
	
	while y < height:
		if forest[y][x] == '#': count += 1
		x = (x + dx) % width
		y = (y + dy)

	return count

def main():
	with open('input3.txt', 'r') as fin:
		forest = [[c for c in line.strip('\n')] for line in fin.readlines()]
		slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

		# Part 1
		print(count_trees(forest,(0,0),(3,1)))
		# Part 2
		print(prod(count_trees(forest,(0,0),slope) for slope in slopes))

if __name__ == '__main__':
	main()