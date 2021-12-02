#!/usr/bin/python3

import aocd
from icecream import ic

def test():
	with open('test.txt', 'r') as fin:
		lines = [line for line in fin.readlines()]
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