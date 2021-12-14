#!/usr/bin/python3

import aocd
from collections import deque
from functools import partial
from icecream import ic
from itertools import chain, filterfalse
from operator import getitem, setitem
import copy

TESTDATA = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

getter = partial(lambda matrix,row,col: getitem(getitem(matrix,row),col))
setter = partial(lambda matrix,row,col,val: 
  setitem(getitem(matrix,row),col,val))

def adjacent(grid,row,col):
	return list(filterfalse(
		lambda c: c[0] < 0 or c[1] < 0 or c[0] >= len(grid) or c[1] >= len(grid[c[0]]),
		[(row+dr, col+dc) for dr in (-1,0,1) for dc in (-1,0,1) if dr != 0 or dc != 0]))

def step(grid):
	"""
	Advance the grid one time step
	"""
	flash_set = set() 	# Set of (row,col) that have flashed
	flash_queue = deque() 	# Ordered deque of (row,col) ready to flash

	# Increase energy level of all by one,
	# collecting flashers (energy level > 9)
	for row in range(len(grid)):
		for col in range(len(grid[row])):
			val = getter(grid,row,col) + 1
			setter(grid,row,col,val)
			if val > 9:
				flash_queue.append((row,col))
	ic(flash_queue)

	# Perform flashes while there are still flashers left,
	# adding new flashers as they reach level > 10
	while flash_queue:
		try:
			flasher = flash_queue.popleft()
		except IndexError as ie:
			print("Attempted pop from empty flashers deque!", ie)

		# If this flasher hasn't already flashed, flash it
		if flasher not in flash_set:
			flash_set.add(flasher)

			# Increase energy level of adjacents by 1
			for adj in adjacent(grid,*flasher):
				val = getter(grid,*adj) + 1
				setter(grid,*adj,val)

				# Add adjacents to flashers if they level-up
				if val > 9:
						flash_queue.append(adj)

	# Flashing has completed, reset flashers to zero
	for flasher in flash_set:
		setter(grid,*flasher,0)

	# Return count of octopii that flashed
	return len(flash_set)

def solveA(grid):
	flash_count = 0
	for timestep in range(100):
		if timestep <= 10 or timestep % 10 == 0:
			ic(timestep)
			flash_count += step(grid)
		else:
			flash_count += step(grid)
	
	# Return the flash count for Part A
	return flash_count

def solveB(grid):
	timestep = 0
	while any(cell!=0 for cell in chain(*grid)):
		timestep += 1
		step(grid)

	ic(timestep, grid)
	return timestep

def test():
	ic.enable()
	grid = [[int(n) for n in line] for line in TESTDATA.splitlines()]
	assert solveA(copy.deepcopy(grid)) == 1656
	assert solveB(copy.deepcopy(grid)) == 195

def main():
	ic.disable()
	grid = [[int(n) for n in line] for line in aocd.data.splitlines()]
	aocd.submit(solveA(copy.deepcopy(grid)), part='a')
	aocd.submit(solveB(copy.deepcopy(grid)), part='b')

if __name__ == '__main__':
	test()
	main()