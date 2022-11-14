#!/usr/bin/python3

import aocd

import typing

from icecream import ic
ic.enable()

line1 = "hello \n world"
line2 = r"hello \n world"

ic(line1 == line2)
ic(line1.encode('unicode-escape').decode() == line2)


testlines = (
	r'""',
	r'"abc"',
	r'"aaa\"aaa"',
	r'"\x27"'
	)

def strlen(s:str) -> int:
	return len(s.encode('unicode-escape'))

def evalstrlen(s:str) -> int:
	return len(eval(s.encode('unicode-escape')))

def test() -> None:
	for line in testlines:
		ic(strlen(line),evalstrlen(line))

def main() -> None:
	pass

if __name__ == '__main__':
	test()
	main()