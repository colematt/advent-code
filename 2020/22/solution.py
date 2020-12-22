#!/usr/bin/python3

import aocd
from icecream import ic

def main():
	data = aocd.get_data(year=2020, day=22, block=True)
	ic(data)

if __name__ == '__main__':
	main()