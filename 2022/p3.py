#!/usr/bin/python3

import aocd
import typing
import itertools
from more_itertools import grouper

from icecream import ic
ic.disable()

testdata = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

def priority(c:str) -> int:
	if ord(c) >= 97:
		return ord(c) - 96
	else:
		return ord(c) - 65 + 27

def solve_a(data:str) ->int:
	rucksacks = tuple((line[:len(line)//2],line[len(line)//2:]) 
		for line in data.splitlines())
	ic(rucksacks)
	dups = tuple((set(first) & set(second)).pop() for first,second in rucksacks)
	ic(dups)
	return sum(priority(dup) for dup in dups)

def solve_b(data:str) ->int:
	rucksacks = [set(line) for line in data.splitlines()]
	groups = list(grouper(rucksacks,3))
	ic(groups)
	badges = [set.intersection(*group) for group in groups]
	return sum(priority(badge.pop()) for badge in badges)

if __name__ == "__main__":
	assert solve_a(testdata) == 157
	aocd.submit(solve_a(aocd.data),part='a')
	assert solve_b(testdata) == 70
	aocd.submit(solve_b(aocd.data),part='b')