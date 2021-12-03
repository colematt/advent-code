#!/usr/bin/python3

import aocd
from icecream import ic
ic.disable()

TEST_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

def test():
	lines = [line for line in TEST_INPUT.splitlines()]
	commands = [(line.split()[0],int(line.split()[1])) for line in lines]

	### PART A ###
	x,z = 0,0
	for direction,distance in commands:
		if direction == "forward": 
			x += distance
		elif direction == "up": 
			z -= distance
		elif direction == "down": 
			z += distance
		else:
			raise ValueError("Unknown direction %s" % direction)
	assert (x * z == 150)

	### PART B ###
	x,z,aim = 0,0,0
	for direction,distance in commands:
		if direction == "forward": 
			x += distance
			z += (aim * distance)
		elif direction == "up": 
			aim -= distance
		elif direction == "down": 
			aim += distance
		else:
			raise ValueError("Unknown direction %s" % direction)
	ic(x,z,aim)
	assert (x * z == 900)

def main():
	lines = aocd.lines
	commands = [(line.split()[0],int(line.split()[1])) for line in lines]

	### PART A ###
	x,z = 0,0
	for direction,distance in commands:
		if direction == "forward": 
			x += distance
		elif direction == "up": 
			z -= distance
		elif direction == "down": 
			z += distance
		else:
			raise ValueError("Unknown direction %s" % direction)
	aocd.submit(x*z, year=2021, day=2, part='a')

	### PART B ###
	x,z,aim = 0,0,0
	for direction,distance in commands:
		if direction == "forward": 
			x += distance
			z += (aim * distance)
		elif direction == "up": 
			aim -= distance
		elif direction == "down": 
			aim += distance
		else:
			raise ValueError("Unknown direction %s" % direction)
	aocd.submit(x*z, year=2021, day=2, part='b')
		
if __name__ == '__main__':
	test()
	main()