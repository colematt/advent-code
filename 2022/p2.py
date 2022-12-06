#!/usr/bin/python3

import aocd
import typing

from icecream import ic
ic.enable()

testdata = """A Y
B X
C Z
"""

values_a = {
	# US: ROCK     PAPER    SCISSORS
	'A': {'X':1+3, 'Y':2+6, 'Z':3+0 }, # THEM: ROCK
	'B': {'X':1+0, 'Y':2+3, 'Z':3+6 }, # THEM: PAPER
	'C': {'X':1+6, 'Y':2+0, 'Z':3+3 }  # THEM: SCISSORS
}

values_b = {
	# US: LOSE     DRAW     WIN
	'A': {'X':3+0, 'Y':1+3, 'Z':2+6}, # THEM: ROCK
	'B': {'X':1+0, 'Y':2+3, 'Z':3+6}, # THEM: PAPER
	'C': {'X':2+0, 'Y':3+3, 'Z':1+6}  # THEM: SCISSORS
}

def test():
	guide = tuple(tuple(line.split()) for line in testdata.splitlines())
	scores = tuple(values_a[them][us] for them,us in guide)
	assert(sum(scores) == 15)
	scores = tuple(values_b[them][us] for them,us in guide)
	assert (sum(scores) == 12)
	
def main():
	guide = tuple(tuple(line.split()) for line in aocd.lines)
	scores = tuple(values_a[them][us] for them,us in guide)
	aocd.submit(sum(scores),part='a')
	scores = tuple(values_b[them][us] for them,us in guide)
	aocd.submit(sum(scores),part='b')

if __name__ == '__main__':
	test()
	main()