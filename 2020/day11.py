#!/usr/bin/env python3

from collections import Counter
import copy
import itertools

def getAdjacent(grid,row,col,strict=True):
	"""
	Generate the (row,col) tuples which are adjacent to grid[row][col].
	"Strictly adjacent" means seats one space away.
	"Not strictly adjacent" follows the rule set in part 2.
	"""
	try:
		for dr,dc in itertools.product((-1,0,1),(-1,0,1)):
			# Avoid considering products which won't find adjacent seats:
			# 0) Won't traverse
			# 1) Would traverse off top
			# 2) Would traverse off bottom
			# 3) Would traverse off left
			# 4) Would traverse off right
			if (dr,dc) == (0,0) or \
				dr < 0 and row == 0 or \
				dr > 0 and row == len(grid) - 1 or \
				dc < 0 and col == 0 or \
				dc > 0 and col == len(grid[row]) - 1: 
				continue
			
			# Calculate the neighbors for strict (part 1)
			if strict:
				r = row + dr
				c = col + dc
				if (0 <= r < len(grid)) and (0 <= c < len(grid[r])):
					yield(r,c)
			# Calculate the neighbors for not strict (part 2)
			else:
				r = row + dr
				c = col + dc
				while grid[r][c] == '.':
					if (dr < 0 and r == 0) or (dr > 0 and r == len(grid) - 1):
						break
					if (dc < 0 and c == 0) or (dc > 0 and c == len(grid[r]) - 1):
						break
					r += dr
					c += dc					
				if (0 <= r < len(grid)) and (0 <= c < len(grid[r])):
					yield(r,c)
	except IndexError as ie:
		if row >= len(grid) and col >= len(grid[row]):
			raise IndexError("row %i and col %i argument out of range" 
				% (row,col))
		elif row >= len(grid):
			raise IndexError("row %i argument out of range" % row)
		elif col >= len(grid[row]):
			raise IndexError("col %i argument out of range" % col)
		else:
			raise ie
				
def countAdjacent(grid,row,col,strict=True):
	"""
	Return a count of each type of seat or floor in the adjacent seats as a Counter object.
	"Strictly adjacent" means seats one space away.
	"Not strictly adjacent follows the rule set in part 2.
	"""
	return Counter([grid[r][c] for r,c in list(getAdjacent(grid, row, col, strict))])
	
def nextGrid(grid,strict=True):
	"""
	Model grid after one round of movement.
	"Strictly adjacent" means seats one space away.
	"Not strictly adjacent follows the rule set in part 2.
	"""
	ng = copy.deepcopy(grid)
	
	# For each seat in grid, if a condition is met, swap its value in the next grid ng
	if strict:
		for row in range(len(grid)):
			for col in range(len(grid[row])):
				# Floor Seat
				if grid[row][col] == '.': 
					pass
				# Empty Seat
				elif grid[row][col] == 'L':
					if countAdjacent(grid, row, col, strict)['#'] == 0:
						ng[row][col] = '#'
				# Occupied Seat
				elif grid[row][col] == '#':
					if countAdjacent(grid, row, col, strict)['#'] >= 4:
						ng[row][col] = 'L'
				else:
					raise ValueError("Encountered a seat with value %s" % grid[row][col])
	else:
		for row in range(len(grid)):
			for col in range(len(grid[row])):
				# Floor Seat
				if grid[row][col] == '.':
					pass
				# Empty Seat
				elif grid[row][col] == 'L':
					if countAdjacent(grid, row, col, strict)['#'] == 0:
						ng[row][col] = '#'
				# Occupied Seat
				elif grid[row][col] == '#':
					if countAdjacent(grid, row, col, strict)['#'] >= 5:
						ng[row][col] = 'L'
				else:
					raise ValueError("Encountered a seat at [%i][%i] with value %s" % 
						(row,col,grid[row][col]))
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
		startGrid = [[col for col in row.strip()] for row in fin.readlines()]
		
		#### PART 1 ####
		prevGrid = None
		currGrid = copy.deepcopy(startGrid)
		
		assert list(getAdjacent(currGrid, 0, 0)) == [(0, 1), (1, 0), (1, 1)]
		assert list(getAdjacent(currGrid, 1, 1)) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
		assert list(getAdjacent(currGrid, 9, 9)) == [(8, 8), (8, 9), (9, 8)]
		assert dict(countAdjacent(currGrid, 1, 1)) == {'L':6, '.':2}
		assert dict(countAdjacent(currGrid, 9, 9)) == {'L':2, '.':1}
		assert countGrid(currGrid)['L'] == 71
		
		while currGrid != prevGrid:
			prevGrid = currGrid
			currGrid = nextGrid(prevGrid)
		assert countGrid(currGrid)['#'] == 37
		
		#### PART 2 ####
		prevGrid = None
		currGrid = copy.deepcopy(startGrid)
		
		# Test upper left corner
		assert list(getAdjacent(currGrid, 0, 0, strict=False)) == [(0, 2), (1, 0), (1, 1)]
		assert dict(countAdjacent(currGrid, 0, 0, strict=False)) == {'L':3}
		# Test lower right corner
		assert list(getAdjacent(currGrid, 9, 9, strict=False)) == [(7, 7), (8, 9), (9, 8)]
		assert dict(countAdjacent(currGrid, 9, 9, strict=False)) == {'L':3}
		# Test floor, surrounded by chairs in all directions
		assert list(getAdjacent(currGrid, 2, 4, strict=False)) == [(1, 3), (1, 4), (1, 5), (2, 2), (2, 7), (3, 3), (5, 4), (3, 5)]
		assert dict(countAdjacent(currGrid, 2, 4, strict=False)) == {'L':8}
		# Test floor, goes to right boundary without a chair
		assert list(getAdjacent(currGrid, 6, 6, strict=False)) == [(5, 5), (5, 6), (4, 8), (6, 4), (6, 9), (7, 5), (7, 6), (7, 7)]
		assert dict(countAdjacent(currGrid, 6, 6, strict=False)) == {'L':7, '.':1}
		# Test floor, goes to lower boundary without a chair
		assert list(getAdjacent(currGrid, 8, 1, strict=False)) == [(7, 0), (7, 1), (7, 2), (8, 0), (8, 2), (9, 0), (9, 1), (9, 2)]
		assert dict(countAdjacent(currGrid, 8, 1, strict=False)) == {'L':7, '.':1}
		
		# Generate the next graph until no changes occur
		while currGrid != prevGrid:
			prevGrid = currGrid
			currGrid = nextGrid(prevGrid, strict=False)
		assert countGrid(currGrid)['#'] == 26
		
				
	with open('inputs/input11.txt', 'r') as fin:
		startGrid = [[col for col in row.strip()] for row in fin.readlines()]
		
		#### PART 1 ####
		prevGrid = None
		currGrid = copy.deepcopy(startGrid)
		while currGrid != prevGrid:
			prevGrid = currGrid
			currGrid = nextGrid(prevGrid)
		print(countGrid(currGrid)['#'])
		
		#### PART 2 ####
		prevGrid = None
		currGrid = copy.deepcopy(startGrid)
		while currGrid != prevGrid:
			prevGrid = currGrid
			currGrid = nextGrid(prevGrid, strict=False)
		print(countGrid(currGrid)['#'])
		
		
if __name__ == "__main__":
	main()	