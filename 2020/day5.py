#!/usr/bin/python3

import typing

def getID(p:str) -> int:
	# Convert pass string into two binary values,
	# Then use row,col addressing to get an id
	row, col = p[:7], p[7:]
	table = str.maketrans({'F':'0','B':'1','L':'0','R':'1'})  
	row = int(row.translate(table),2)
	col = int(col.translate(table),2)
	return 8*row + col

def findSeat(ids:typing.Iterable) -> int:
	# Construct a set of all valid seats
	seats = set(i for i in range(min(ids),max(ids)+1))
	# Find the difference (the unfilled seat)
	return seats.difference(ids).pop()

def main():
	with open('inputs/input5.txt') as fin:
		passes = [line.rstrip() for line in fin.readlines()]
		
		# Part 1
		assert(getID('FBFBBFFRLR') == 357)
		ids = set(getID(p) for p in passes)
		print(max(ids))
		
		# Part 2
		print(findSeat(ids))

if __name__ == '__main__':
	main()