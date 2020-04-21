#!/usr/bin/python3

from intcode import Intcode

if __name__ == "__main__":
	with open('day5.txt','r') as f:
		ic = Intcode([int(inst) for inst in f.read().split(',')])
#	print(ic)
	ic.run()