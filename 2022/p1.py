#!/usr/bin/python3

import aocd
import typing

from icecream import ic
ic.enable()

testdata = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

def test():
	elves = [tuple(int(e) for e in elf.split()) for elf in testdata.split("\n\n")]
	sums = [sum(elf) for elf in elves]
	assert max(sums) == 24000
	assert(sum(sorted(sums,reverse=True)[:3]) == 45000)

def main():
	elves = [tuple(int(e) for e in elf.split()) for elf in aocd.data.split("\n\n")]
	sums = [sum(elf) for elf in elves]
	aocd.submit(max(sums),part='a')
	aocd.submit(sum(sorted(sums,reverse=True)[:3]), part='b')

if __name__ == '__main__':
	test()
	main()