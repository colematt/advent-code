#!/usr/bin/python3

import aocd
from icecream import ic
import itertools

ic.disable()

testcases = (
	"(())",
	"()()",
	"(((",
	"(()(()(",
	"))(((((",
	"())",
	"))(",
	")))",
	")())())"
)
test_outputs = (0,0,3,3,3,-1,-1,-3)

def test():
	steptups = tuple(tuple(1 if s=='(' else -1 for s in ti) for ti in testcases)
	locations = tuple(tuple(itertools.accumulate(st)) for st in steptups)
	stops = [loc[-1] for loc in locations]
	for s,to in zip(stops,test_outputs):
		assert s == to

def main():
	steptup = tuple(1 if s == '(' else -1 for s in aocd.data)
	locations = tuple(itertools.accumulate(steptup))

	### PART A ###
	aocd.submit(locations[-1],part='a')

	### PART B ###
	ic(locations,locations.index(-1))
	aocd.submit(locations.index(-1)+1,part='b')

if __name__ == '__main__':
	test()
	main()