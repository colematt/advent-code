#!/usr/bin/python3

import aocd
import typing
import itertools

from icecream import ic
ic.disable()

testdata = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

def parse(data:str) -> typing.Tuple :
	stacks,moves = data.split("\n\n")
	
	# Split the rows to columns
	stacks = stacks.splitlines()
	stacks = [line[1::4] for line in stacks[:-1]]
	# Read the rows into stacks
	stacks = list(itertools.zip_longest(*stacks))
	# Filter empty strings (absence of a crate)
	stacks = [list(itertools.filterfalse(lambda crate:crate == " ", stack)) 
		for stack in stacks]
	# Create a zero-index stacks collection
	stacks.insert(0,list())

	moves = tuple(line.split() for line in moves.splitlines())
	moves = tuple((int(amt),int(src),int(dst)) 
			for _,amt,_,src,_,dst in moves) 
	
	return (stacks,moves)

def solve_a(data:str) -> str:
	stacks, moves = parse(data)
	ic(stacks[1:])
	
	for amt,src,dst in moves:
		ic(amt,src,dst)
		for _ in range(amt):
			stacks[dst].insert(0,stacks[src].pop(0))			
			
	ic(stacks[1:])
	return "".join(stack[0] for stack in filter(lambda s:s, stacks[1:]))

def solve_b(data:str) -> str:
	stacks, moves = parse(data)
	ic(stacks[1:])
	
	for amt,src,dst in moves:
		ic(amt,src,dst)
		stacks[dst][0:0] = stacks[src][:amt]
		stacks[src][:amt] = []	
	
	ic(stacks[1:])
	return "".join(stack[0] for stack in filter(lambda s:s, stacks[1:]))

if __name__ == '__main__':
	assert solve_a(testdata) == "CMZ"
	aocd.submit(solve_a(aocd.data),part='a')
	assert solve_b(testdata) == "MCD"
	aocd.submit(solve_b(aocd.data),part='b')
	