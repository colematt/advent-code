#!/usr/bin/env python3

import itertools
import typing

testdata = (
	("ugknbfddgicrmopn", True),
	("aaa", True),
	("jchzalrnumimnmhp", False),
	("haegwjzuvuyypxyu", False),
	("dvszwmarrgswjxmb", False)
)

def vowel_count(string:str) -> int:
	return len("".join(filter(lambda c: c in set('aeiou'), string)))

def pairwise(iterable):
	a, b = itertools.tee(iterable)
	next(b, None)
	return zip(a, b)

def repeat(string:str) -> bool:
	return any(a==b for a,b in pairwise(string))

def forbid(string:str) -> bool:
	forbidden = { "ab", "cd", "pq", "xy" }
	return any ("".join(tup) in forbidden for tup in pairwise(string))

def is_nice(string:str) -> bool:
	return vowel_count(string) >= 3 and repeat(string) and not forbid(string)

def test():
	for string,answer in testdata:
		assert is_nice(string) == answer

def main():
	### PART A ###
	with open('data5.txt', 'r') as fin:
		count = 0
		for line in fin.readlines():
			if is_nice(line):
				count += 1
		print(count)

if __name__ == "__main__":
	test()
	main()