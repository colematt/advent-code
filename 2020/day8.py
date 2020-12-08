#!/usr/bin/python3

def run(program,acc=0,pc=0):
	"""
	{Execute a program with initialized values, until a cycle is encountered or
	the program terminates. Return the final accumulator and pc values.}
	
	:param      program:     The program instruction stream
	:type       program:     {list[str]}
	:param      acc:         The accumulator initial value
	:type       acc:         int
	:param      pc:          The program counter initial value
	:type       pc:          int
	
	:returns:   { Final program state (acc,pc) }
	:rtype:     { tuple }
	
	:raises     ValueError:  { Raises exception if an unidentified opcode is encountered }
	"""
	unvisited = set(program)
	
	# While loop checks to make sure we aren't beginning a cycle
	# or that the program has terminated (ie. pc is out of bounds)
	while pc < len(program) and program[pc] in unvisited:
		address,(opcode,operand) = program[pc]
		operand = int(operand)
		unvisited.remove(program[pc])

		# Execute the instruction
		if opcode == 'acc':
			acc += operand
			pc += 1
		elif opcode == 'jmp':
			pc += operand
		elif opcode == 'nop':
			pc += 1
		else:
			raise ValueError("Unrecognized opcode %s" % opcode)

	# Return a 2-tuple of the final accumulator value and program counter value
	return acc,pc

def debug(program,acc=0,pc=0):
	"""
	{ For each instruction in a program, try permuting its opcode to see if 
	  infinite loops can be resolved. If so, return the final accumulator and 
	  program counter value when the loop is fixed. Otherwise, return None.

	:param      program:  The program
	:type       program:  { type_description }
	:param      acc:      The acc
	:type       acc:      number
	:param      pc:       { parameter_description }
	:type       pc:       number

	:returns:   Final program state or None
	:rtype:     { {tuple, None} }
	"""

	# For each address, permute if a 'jmp' or 'nop',
	# then run the program. If it halts properly, report the accumulator
	for addr in range(len(program)):
		# Fetch the instruction to be permuted
		inst = program[addr]
		address,(opcode,operand) = inst
		
		# Permute the instruction if needed
		if opcode == 'jmp':
			opcode = 'nop'
			program[addr] = (address,(opcode,operand))
		elif opcode == 'nop':
			opcode = 'jmp'
			program[addr] = (address,(opcode,operand))
		else:
			pass

		# Execute the program
		acc,pc = run(program)

		# Report if fixed, restore otherwise
		if pc >= len(program):
			return acc,pc
		else: 
			program[addr] = inst

	# If we reach this, we could not fix the cycle with one swap
	return None

def printState(program,state):
	"""
	Pretty prints a program state.

	:param      program:  The program
	:type       program:  { list[str] }
	:param      state:    Program state to be unpacked
	:type       state:    { tuple }
	"""
	try:
		print("acc: %i, pc: %i is %s" % (*tup,repr(program[tup[1]])))
	except IndexError:
		print("acc: %i, pc: %i Terminated" % (tup))

def main():
	"""
	Open input files, run them, and debug them.

	:raises     AssertionError:  { Raises exception if the test cases fail.}
	"""
	with open('inputs/input8-test.txt','r') as fin:
		program = list(enumerate(tuple(line.split()) for line in fin.readlines()))
		assert run(program) == (5,1)
		assert debug(program) == (8,9)

	with open('inputs/input8.txt','r') as fin:
		program = list(enumerate(tuple(line.split()) for line in fin.readlines()))
		printState(program,run(program))
		printState(program,debug(program))

if __name__ == '__main__':
	main()