#!/usr/bin/python3

import aocd
import typing
import re

from icecream import ic
ic.enable()

testlines = (
	"""""""",
	"""abc""",
	"""aaa\"aaa""",
	"""\x27"""
	)

def test() -> None:
	for line in testlines:
		ic(len(line), len(eval("'" + re.escape(line) + "'")))

def main() -> None:
	pass

if __name__ == "__main__":
	test()
	main()
