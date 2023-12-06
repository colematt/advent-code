#!/usr/bin/python3

import aocd
import string
from icecream import ic
ic.enable()

testdata = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def check(cubes):
	for cube in cubes:
		if cube.endswith(" red"):
			if int(cube[:-4]) > 12:
				return False
		elif cube.endswith(" green"):
			if int(cube[:-6]) > 13:
				return False
		elif cube.endswith(" blue"):
			if int(cube[:-5]) > 14:
				return False
	else:
		return True

def test():
	lines = [line for line in testdata.splitlines()]
	games = [line.partition(":")[-1] for line in lines]
	games = list(enumerate((tuple(hand.lstrip() for hand in tuple(game.split(";"))) 
		for game in games),start=1))
	
	# Part A
	count = 0
	for id, hands in games:
		possible = True
		for hand in hands:
			cubes = tuple(cubes.lstrip() for cubes in hand.split(','))
			possible = possible and check(cubes)
			ic(hand, check(cubes), possible)
		if possible: count += id
		ic(count)
	assert count == 8

def main():
	lines = [line for line in aocd.data.get_data]
	games = [line.partition(":")[-1] for line in lines]
	games = list(enumerate((tuple(hand.lstrip() for hand in tuple(game.split(";"))) 
		for game in games),start=1))
	
	# Part A
	count = 0
	for id, hands in games:
		possible = True
		for hand in hands:
			cubes = tuple(cubes.lstrip() for cubes in hand.split(','))
			possible = possible and check(cubes)
			ic(hand, check(cubes), possible)
		if possible: count += id
		ic(count)

if __name__ == '__main__':
	test()
	main()