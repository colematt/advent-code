#!/usr/bin/python3

import aocd
from icecream import ic
from collections import Counter

DATA = """3,4,3,1,2"""

def runNaive(fish, days):
	for day in range(days):
		# Count fishes at 0 for new fishes tomorrow
		newfish = fish.count(0)

		# Age each fish by one day,
		# mod 7 to avoid negative fish timers,
		# ignore timers > 7 to avoid short circuiting
		fish = [(f-1)%7 if f < 7 else f-1 for f in fish]

		# Birth new fishes
		fish.extend([8]*newfish)

		# Get status of fish
		if len(fish) <= 25: 
			ic(day, fish)

	return len(fish)

def run(fish, days):
	# Get count of fish at each day
	fish = {i:fish.count(i) for i in range(9)}
	ic(fish)

	for day in range(days):
		
		# Age each fish at age > 1 by one day
		newfish = {i:fish[i+1] for i in range(8)}

		# Add breeding fish to count at age 6
		newfish[6] = newfish[6] + fish[0]

		# Birth zerofish new fish at 8
		newfish[8] = fish[0]

		# Get status of fish
		fish = newfish
		if(day <= 18):
			ic(day, fish)

	return sum(fish.values())
		
def test():
	fish = [int(n) for n in DATA.split(',')]
	assert run(fish, 18) == 26
	assert run(fish, 80) == 5934

def main():
	ic.disable()

	fish = [int(n) for n in aocd.data.split(',')]
	aocd.submit(run(fish, 80), part='a')
	aocd.submit(run(fish, 256), part='b')

if __name__ == '__main__':
	test()
	main()