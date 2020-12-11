#!/usr/bin/env python3

from collections import Counter
import copy
import itertools

def getAdjacent(grid,row,col):
	"""
	Generate the (row,col) tuples which are adjacent to grid[row][col]
	"""
	try:
		for r,c in itertools.product(range(row-1,row+2),range(col-1,col+2)):
			if all((r >= 0, r < len(grid), c >= 0, c < len(grid[0]), not (r == row and c == col))):
				yield(r,c)
	except IndexError as ie:
		if row >= len(grid) and col >= len(grid[row]):
			raise IndexError("row %i and col %i out of range" % (row,col))
		elif row >= len(grid):
			raise IndexError("row %i out of range" % row)
		elif col >= len(grid[row]):
			raise IndexError("col %i out of range" % col)
		else:
			raise ie
			
def countAdjacent(grid,row,col):
	"""
	Return a count of each type of seat or floor in the adjacent seats as a Counter object. 
	"""
	return Counter([grid[r][c] for r,c in list(getAdjacent(grid, row, col))])
			
def nextGrid(grid):
	"""
	Model grid after one round of movement.
	"""
	ng = copy.deepcopy(grid)
	
	# For each seat in grid, if a condition is met, swap its value in the next grid ng
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			# Floor Seat
			if grid[row][col] == '.': 
				pass
			# Empty Seat
			elif grid[row][col] == 'L':
				if countAdjacent(grid, row, col)['#'] == 0:
					ng[row][col] = '#'
			# Occupied Seat
			elif grid[row][col] == '#':
				if countAdjacent(grid, row, col)['#'] >= 4:
					ng[row][col] = 'L'
			else:
				raise ValueError("Encountered a seat with value %s" % grid[row][col])
	return ng

def countGrid(grid):
	"""
	Return a count of each type of seat or floor in grid as a Counter object.
	"""
	return Counter(list(itertools.chain(*grid)))

def printGrid(grid):
	"""
	Pretty print a grid and its counts.
	"""
	for row in grid:
		print("".join(row))
	cg = countGrid(grid)
	print("Empty: %i Occupied: %i Floor: %i" % (cg['L'], cg['#'], cg['.']))

def main():
	with open('inputs/input11-test.txt', 'r') as fin:
		grid = [[col for col in row.strip()] for row in fin.readlines()]
		assert list(getAdjacent(grid, 0, 0)) == [(0, 1), (1, 0), (1, 1)]
		assert list(getAdjacent(grid, 1, 1)) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
		assert list(getAdjacent(grid,len(grid)-1,len(grid[-1])-1)) == [(8, 8), (8, 9), (9, 8)]
		assert countGrid(grid)['L'] == 71
		assert dict(countAdjacent(grid, 1, 1)) == {'L':6, '.':2}

		# Part 1
		ng = nextGrid(grid)
		while ng != grid:
			grid = ng
			ng = nextGrid(grid)
		assert countGrid(grid)['#'] == 37
				
	with open('inputs/input11.txt', 'r') as fin:
		grid = [[col for col in row.strip()] for row in fin.readlines()]
		
		# Part 1
		ng = nextGrid(grid)
		while ng != grid:
			grid = ng
			ng = nextGrid(grid)
		print(countGrid(grid)['#'])
		
if __name__ == "__main__":
	main()	