#!/usr/bin/python3

import aocd
import typing
import itertools

from icecream import ic
ic.disable()

testdata = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def solve_a(data:str) -> int:
	pairs = [tuple(tuple(int(i) for i in r.split('-')) for r in line.split(',')) 
		for line in data.splitlines()]
	pairs = [((i[0],i[1]+1),(j[0],j[1]+1)) for i,j in pairs]
	ic(pairs)
	ranges = [(set(range(*left)),set(range(*right))) for left,right in pairs]
	ic(ranges)
	fulldups = list(filter(lambda s: s[0].issubset(s[1]) or s[1].issubset(s[0]), ranges))
	return len(fulldups)

def solve_b(data:str) -> int:
	pairs = [tuple(tuple(int(i) for i in r.split('-')) for r in line.split(',')) 
		for line in data.splitlines()]
	pairs = [((i[0],i[1]+1),(j[0],j[1]+1)) for i,j in pairs]
	ic(pairs)
	ranges = [(set(range(*left)),set(range(*right))) for left,right in pairs]
	ic(ranges)
	somedups = list(itertools.filterfalse(lambda s: s[0].isdisjoint(s[1]), ranges))
	return len(somedups)

if __name__ == "__main__":
	assert solve_a(testdata) == 2
	solve_a(aocd.data)
	aocd.submit(solve_a(aocd.data),part='a')
	assert solve_b(testdata) == 4
	aocd.submit(solve_b(aocd.data),part='b')
