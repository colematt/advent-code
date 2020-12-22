#!/usr/bin/python3

import aocd
from collections import namedtuple
from icecream import ic
import itertools 

Tile = namedtuple('Tile', ['id','image'])

def rotate(tile):
    return list(''.join(x[::-1]) for x in zip(*tile))

def flip(tile):
    return list(reversed(tile.copy()))

def build_tile_transformations(tile):
    tile90 = rotate(tile)
    tile180 = rotate(tile90)
    tile270 = rotate(tile180)
    return [tile, tile90, tile180, tile270, flip(tile), flip(tile90), flip(tile180), flip(tile270)]

def top(tile):
	return tile[0]

def bottom(tile):
	return tile[-1]

def left(tile):
	return [row[0] for row in tile]

def right(tile):
	return [row[-1] for row in tile]

def test():
	with open('test.txt', 'r') as fin:
		data = fin.read()
	tiles = list()
	for tile in data.split('\n\n'):
		_, i, *rows = tile.split()
		tiles.append(Tile(id=int(i.rstrip(':')), image=[[char for char in row] for row in rows]))
	ic(tiles)

def main():
	data = aocd.get_data(year=2020, day=20)
	tiles = list()
	for tile in data.split('\n\n'):
		_, i, *rows = tile.split()
		tiles.append(Tile(id=int(i.rstrip(':')), image=[[char for char in row] for row in rows]))	

if __name__ == '__main__':
	test()
	# main()
