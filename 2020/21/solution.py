#!/usr/bin/python3

import aocd
from icecream import ic

def main():
	lines = aocd.get_data(year=2020, day=21)
	ic(lines)

if __name__ == '__main__':
	main()