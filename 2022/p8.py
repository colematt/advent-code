#!/usr/bin/python3

from itertools import count
import aocd
import typing
import array

from icecream import ic
ic.enable()

testdata = """30373
25512
65332
33549
35390
"""

def get_forest(data:str) -> list[list[int]]:
	forest = [[int(tree) for tree in row] for row in data.splitlines()]
	return forest

def get_row(forest:list[list[int]], row:int) -> list[int]:
	return forest[row]

def get_col(forest:list[list[int]], col:int) -> list[int]:
	return [row[col] for row in forest] 

def is_visible(forest:list[list[int]], row:int, col:int) -> bool:

	# Trees on exterior are always visible
	if row == 0 or row == len(forest)-1: return True
	if col == 0 or col == len(forest[row])-1: return True

	# Trees taller than all trees between it and an edge of the row are visible
	frow = get_row(forest,row)
	if frow[col] > max(frow[:col]) or frow[col] > max(frow[col+1:]):
		return True

	# Trees taller than all trees between it and an edge of the col are visible
	fcol = get_col(forest,col)
	if fcol[row] > max(fcol[:row]) or fcol[row] > max(fcol[row+1:]):
		return True

	# Otherwise the tree is not visible
	return False

def score(forest:list[list[int]], row:int, col:int) -> int:
	height = forest[row][col]
	frow = get_row(forest,row)
	fcol = get_col(forest,col)

	# Looking up
	up = row-1
	while (up > 0) and (frow[up] < height): 
		up -= 1
	ic(up, (up > 0),(frow[up] < height))
	up = row - up

	# Looking left
	left = col-1
	while (left > 0) and (frow[left] < height):
		left -= 1
	ic(left,(left > 0),(frow[left] < height))
	left = col - left

	# Looking down
	down = row+1
	while (down < len(frow)) and (frow[down] < height): 
		down += 1
	ic(down, down < len(frow), frow[down] < height)
	down = down - row

	# Looking right
	right = col+1
	while (right < len(fcol)) and (fcol[right] < height):
		right += 1
	ic(down, down < len(frow), frow[down] < height)
	right = right - col

	ic(up,left,down,right)
	return up * left * down * right

def solve_a(data:str) -> int:
	forest = get_forest(data)
	ic(forest)
	visibles = [[is_visible(forest,row,col) 
		for col in range(len(forest[row]))] 
			for row in range(len(forest))]
	ic(visibles)
	return sum([row.count(True) for row in visibles])

def solve_b(data:str) -> int:
	ic.enable()
	forest = get_forest(data)
	ic(forest)
	score(forest,1,2)

	# scores = [[score(forest,row,col) 
	# 	for col in range(len(forest[row]))] 
	# 		for row in range(len(forest))]
	# ic(scores)
	# return max(max(row) for row in visibles)

if __name__ == '__main__':
	assert solve_a(testdata) == 21
	aocd.submit(solve_a(aocd.data),part='a')
	solve_b(testdata)