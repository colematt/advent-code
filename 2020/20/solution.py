#!/usr/bin/python3

import aocd
import copy
from collections import namedtuple
from icecream import ic
import itertools 

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

def build_tile_transformations(tile):
	tile90 = rotate(tile)
	tile180 = rotate(tile90)
	tile270 = rotate(tile180)
	return [tile, tile90, tile180, tile270, flip(tile), flip(tile90), flip(tile180), flip(tile270)]

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

def test():
	with open('test.txt', 'r') as fin:
		data = fin.read()
	tiles = list()
	for tile in data.split('\n\n'):
		_, i, *rows = tile.split()
		tiles.append(Tile(id=int(i.rstrip(':')), image=rows))

	# Test tile transforms and slices
	assert tiles[0] == Tile(id=2311, image=['..##.#..#.', '##..#.....', '#...##..#.', '####.#...#', '##.##.###.', '##...#.###', '.#.#.#..##', '..#....#..', '###...#.#.', '..###..###'])
	assert rotate(tiles[0]) == Tile(id=2311, image=['.#..#####.', '.#.####.#.', '###...#..#', '#..#.##..#', '#....#.##.', '...##.##.#', '.#...#....', '#.#.##....', '##.###.#.#', '#..##.#...'])
	assert flip(tiles[0]) == Tile(id=2311, image=['..###..###', '###...#.#.', '..#....#..', '.#.#.#..##', '##...#.###', '##.##.###.', '####.#...#', '#...##..#.', '##..#.....', '..##.#..#.'])
	assert top(tiles[0]) == "..##.#..#."
	assert bottom(tiles[0]) == "..###..###"
	assert left(tiles[0]) == ".#####..#."
	assert right(tiles[0]) == "...#.##..#"

def main():
	data = aocd.get_data(year=2020, day=20)
	tiles = list()
	for tile in data.split('\n\n'):
		_, i, *rows = tile.split()
		tiles.append(Tile(id=int(i.rstrip(':')), image=rows))	

if __name__ == '__main__':
	test()
	# main()
