#!/usr/bin/python3

import aocd
from icecream import ic
from collections import Counter

DATA = """3,4,3,1,2"""

def main():
	ic.disable()

	### PART A ###
	fish = [int(n) for n in aocd.data.split(',')]
	newfish = 0

	for day in range(81):
		# Birth new fishes
		fish.extend([8]*newfish)

		# Get status of fishes
		if len(fish) <= 25: 
			ic(day, fish)
		elif day == 80:
			ic(day, len(fish)) 
			aocd.submit(len(fish), part="a")

		# Count fishes at 0 for new fishes tomorrow
		newfish = fish.count(0)
		
		# Age each fish by one day,
		# mod 7 to avoid negative fish timers,
		# ignore timers > 7 to avoid short circuiting
		fish = [(f-1)%7 if f < 7 else f-1 for f in fish]


if __name__ == '__main__':
	# test()
	main()