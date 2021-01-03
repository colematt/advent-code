#!/usr/bin/python3

import aocd
import copy
from collections import namedtuple
from icecream import ic
import itertools
import math

Tile = namedtuple('Tile', ['id','image'])

def rotate(tile):
	"""
	Return a copy of a tile whose image has been rotated 90 degrees clockwise
	"""
	return Tile(id=tile.id, image=list(''.join(x[::-1]) for x in zip(*tile.image)))

def flip(tile):
    """
    Return a copy of a Tile whose image has been flipped about the x-axis
    """

    return Tile(id=tile.id, image=list(reversed(copy.copy(tile.image))))

def top(tile):
	"""
	Return the top slice of tile's image
	"""
	return tile.image[0]

def bottom(tile):
	"""
	Return the bottom slice of tile's image
	"""
	return tile.image[-1]

def left(tile):
	"""
	Return the left slice of tile's image
	"""
	return "".join([row[0] for row in tile.image])

def right(tile):
	"""
	Return the right slice of tile's image
	"""
	return "".join([row[-1] for row in tile.image])

def tile_test():
	"""
	Test tile transforms and rotations
	
	:raises     AssertionError:  { If any transform or rotation fails. }
	"""
	# Test tile transforms and slices
	testtile = Tile(id=2311, image=['..##.#..#.', '##..#.....', '#...##..#.', '####.#...#', '##.##.###.', '##...#.###', '.#.#.#..##', '..#....#..', '###...#.#.', '..###..###'])
	assert rotate(testtile) == Tile(id=2311, image=['.#..#####.', '.#.####.#.', '###...#..#', '#..#.##..#', '#....#.##.', '...##.##.#', '.#...#....', '#.#.##....', '##.###.#.#', '#..##.#...'])
	assert flip(testtile) == Tile(id=2311, image=['..###..###', '###...#.#.', '..#....#..', '.#.#.#..##', '##...#.###', '##.##.###.', '####.#...#', '#...##..#.', '##..#.....', '..##.#..#.'])
	assert top(testtile) == "..##.#..#."
	assert bottom(testtile) == "..###..###"
	assert left(testtile) == ".#####..#."
	assert right(testtile) == "...#.##..#"

def get_transformations(tile:Tile) -> list:
	"""
	Return a list of all transformations of a given tile
	"""
	tile90 = rotate(tile)
	tile180 = rotate(tile90)
	tile270 = rotate(tile180)
	return [tile, tile90, tile180, tile270, 
		flip(tile), flip(tile90), flip(tile180), flip(tile270)]

def get_neighbors(tiles:list) -> dict:
	"""
	Return a dictionary of the set of all neighbors of a given tile
	"""
	neighbors = dict()
	for tile in tiles:
		tile_neighbors = set()
		others = list(filter(lambda n: n!= tile, tiles))
		for other in others:
			trans_prods = itertools.product(get_transformations(tile), get_transformations(other))
			for t_trans, o_trans in trans_prods:
				if right(t_trans) == left(o_trans): tile_neighbors.add(other.id)
		neighbors[tile.id] = tile_neighbors
	return neighbors

def test():
	tile_test()
	with open('test.txt', 'r') as fin:
		data = fin.read()
	tiles = [tile for tile in data.split('\n\n')]
	tiles = [tile.split() for tile in tiles]
	tiles = [Tile(id=int(i.rstrip(':')), image=rows) for _,i,*rows in tiles]

	#### PART A ####
	neighbors = get_neighbors(tiles)
	assert math.prod(n for n in neighbors if len(neighbors[n]) == 2) == 20899048083289

def main():
	data = aocd.get_data(year=2020, day=20)
	tiles = [tile for tile in data.split('\n\n')]
	tiles = [tile.split() for tile in tiles]
	tiles = [Tile(id=int(i.rstrip(':')), image=rows) for _,i,*rows in tiles]

	#### PART A ####
	neighbors = get_neighbors(tiles)
	aocd.submit(math.prod(n for n in neighbors if len(neighbors[n]) == 2), year=2020, day=20, part='a')

if __name__ == '__main__':
	test()
	main()
