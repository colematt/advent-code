import sys
import math
import aocd
from icecream import ic

fuel = lambda m: max(math.floor(m/3)-2,0)

def main():
	# Read the input
	data = aocd.get_data(year=2019, day=1)
	modules = [int(line) for line in data.splitlines()]
	
	# Fuel for just the modules
	load = sum(map(lambda m: fuel(m), modules))
	ic('part a:', load)
	aocd.submit(load, year=2019, day=1, part='a')

	
	# Fuel for modules + fuel for fuel
	for	m in modules:
		if fuel(m) > 0:
			modules.append(fuel(m))
	load = sum(map(fuel,modules))
	ic('part b:', load)
	aocd.submit(load, year=2019, day=1, part='b')

if __name__ == "__main__":
	main()