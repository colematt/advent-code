#!/usr/bin/python3

from intcode import *
import itertools

if __name__ == "__main__":
	# Build the machine
	with open('day2.txt','r') as f:
		ic = Intcode([int(inst) for inst in f.read().split(',')])
	
	# Reset the 1202 error and run the machine,
	# then log final machine state
	ic.reset((1,12),(2,2))
	ic.run()
	print(repr(ic), "Memory[0] = %i" % ic.memory[0])
	
	# Iteratively guess values, run the machine
	for i,j in itertools.product(range(len(ic.memory)),range(len(ic.memory))):
		ic.reset((1,i),(2,j))
		ic.run()
		if ic.memory[0] == 19690720: 
			print("Memory[0] = 19690720 at i: %i, j: %i, 100*i+j = %i" % (i,j,100*i+j))
			break
			