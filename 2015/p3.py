#!/usr/bin/python3

import aocd
from icecream import ic
import collections
import itertools
import typing

ic.disable()

testdata_a = [
	(">",2),
	("^>v<",4),
	("^v^v^v^v^v",2)
]

testdata_b = [
	("^v",3),
	("^>v<",3),
	("^v^v^v^v^v",11)
]

def visited(data:str) -> int:
	x,y = 0,0
	visits = collections.defaultdict(int)
	visits[(x,y)] += 1
	
	for move in data:
		match(move):
			case '^': y+=1
			case 'v': y-=1
			case '>': x+=1
			case '<': x-=1
			case _: raise ValueError("%s not valid move" % move)
		visits[(x,y)] += 1
	ic(visits)
	return len(visits)

def robovisited(data: str) -> int:
	visits = collections.defaultdict(int)

	# Santa's moves
	x,y = 0,0
	visits[(x,y)] += 1
	for move in itertools.islice(data,0,None,2):
		match(move):
			case '^': y+=1
			case 'v': y-=1
			case '>': x+=1
			case '<': x-=1
			case _: raise ValueError("%s not valid move" % move)
		visits[(x,y)] += 1

	# RoboSanta's moves
	x,y = 0,0
	visits[(x,y)] += 1
	for move in itertools.islice(data,1,None,2):
		match(move):
			case '^': y+=1
			case 'v': y-=1
			case '>': x+=1
			case '<': x-=1
			case _: raise ValueError("%s not valid move" % move)
		visits[(x,y)] += 1

	ic(visits)
	return len(visits)

def test():
	for data,output in testdata_a:
		assert(visited(data) == output)
	for data,output in testdata_b:
		assert(robovisited(data) == output)

def main():
	aocd.submit(visited(aocd.data),part='a')
	aocd.submit(robovisited(aocd.data), part='b')

if __name__ == '__main__':
	test()
	main()