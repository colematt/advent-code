#!/usr/bin/env python3

import aocd
from icecream import ic
import itertools
import re
import typing

testdata_a = (
	("ugknbfddgicrmopn", True),
	("aaa", True),
	("jchzalrnumimnmhp", False),
	("haegwjzuvuyypxyu", False),
	("dvszwmarrgswjxmb", False)
)

testdata_b = (
	("qjhvhtzxzqqjkmpb", True),
	("xxyxx", True),
	("uurcxstgmygtbstg", False),
	("ieodomkazucvgmuy", False)
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

def is_nice_a(string:str) -> bool:
	return vowel_count(string) >= 3 and repeat(string) and not forbid(string)

def is_nice_b(string:str) -> bool:
	rule1 = re.compile(r'([a-z])([a-z]).*\1\2')
	rule2 = re.compile(r'([a-z]).\1')
	return bool(rule1.search(string)) and bool(rule2.search(string))

def test():
	for string,answer in testdata_a:
		assert is_nice_a(string) == answer
	for string,answer in testdata_b:
		assert is_nice_b(string) == answer

def main():
	### PART A ###
	count = 0
	for line in aocd.lines:
		if is_nice_a(line):
			count += 1
	aocd.submit(count,part='a')

	### PART B ###
	count = 0
	for line in aocd.lines:
		if is_nice_b(line):
			count += 1
	aocd.submit(count,part='b')

if __name__ == "__main__":
	test()
	main()