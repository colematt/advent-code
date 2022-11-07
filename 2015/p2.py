#!/usr/bin/python3

import aocd
from icecream import ic
import itertools
import math
import typing

testdata = ["2x3x4","1x1x10"]

def read_present(present:str) -> tuple[int]:
	return tuple(int(side) for side in present.split('x'))

def paper(present:tuple[int]) -> int:
	sides = tuple(side for side in itertools.combinations(present,2))
	areas = tuple(math.prod(side) for side in sides)
	return min(areas) + sum(2*area for area in areas)

def ribbon(present:tuple[int]) -> int:
	sides = tuple(side for side in itertools.combinations(present,2))
	perimeters = tuple(2 * (h+w)for h,w in sides)
	return min(perimeters) + math.prod(present)

def test():
	assert sum([paper(read_present(line)) for line in testdata]) == 58 + 43
	assert sum([ribbon(read_present(line)) for line in testdata]) == 34 + 14

def main():
	presents = tuple(read_present(line) for line in aocd.lines)
	aocd.submit(sum(paper(present) for present in presents),part='a')
	aocd.submit(sum(ribbon(present) for present in presents), part='b')

if __name__ == '__main__':
	test()
	main()