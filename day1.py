import sys
import math

fuel = lambda m: max(math.floor(m/3)-2,0)

if __name__ == "__main__":
	# Read the input
	with open('day1.txt', 'r') as f:
		modules = [int(line) for line in f.readlines()]
	
	# Fuel for just the modules
	print("Just modules: ", sum(map(lambda m: fuel(m), modules)))
	
	# Fuel for modules + fuel for fuel
	for	m in modules:
		if fuel(m) > 0:
			modules.append(fuel(m))	
	print("Modules plus fuel: ", sum(map(fuel,modules)))