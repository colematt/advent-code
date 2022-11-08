#!/usr/bin/python3

import aocd
import collections
import ctypes

import typing
UnaryInstruction = tuple[str,str,str]           # op src dst
BinaryInstruction = tuple[str,str,str, str]    	# op src1 src2 dst
TernaryInstruction = tuple[str,str,str,str,str] # op src1 src2 src3 dst

from icecream import ic
ic.disable()

testlines = (
	"123 -> x",
	"456 -> y",
	"x AND y -> d",
	"x OR y -> e",
	"x LSHIFT 2 -> f",
	"y RSHIFT 2 -> g",
	"NOT x -> h",
	"NOT y -> i"
	)

testsignals = {
	"d": 72,
	"e": 507,
	"f": 492,
	"g": 114,
	"h": 65412,
	"i": 65079,
	"x": 123,
	"y": 456
	}

def parse(line:str) -> UnaryInstruction | BinaryInstruction | TernaryInstruction | None:
	lhs,rhs = line.split(" -> ")
	lhs = lhs.split()
	if len(lhs) == 1:
		return ("MOV", lhs[0], rhs)
	if len(lhs) == 2:
		return ("NOT", lhs[1], rhs)
	if len(lhs) == 3:
		return (lhs[1], lhs[0], lhs[2], rhs)
	return None

def connect(gates:list[UnaryInstruction | BinaryInstruction | TernaryInstruction | None], overrides:dict = dict()) -> dict[str,int]:
	# Initialize the connections dictionary
	signals = collections.defaultdict(type(None))
	signals.update(overrides)

	# Iteratively construct gates while any remain unconstructed
	while gates:
		ic(len(gates))
		unconstructed = list()
		for gate in gates:
			# Unpack the gate and fetch concrete values for wires
			opcode, *srcs, dst = gate
			srcs = [int(src) if src.isdigit() else signals[src] for src in srcs]
			# Can't satisfy the gate if an input is missing
			if any(src == None for src in srcs):
				unconstructed.append(gate)
			# Don't allow an instruction to replace an override
			elif dst in overrides.keys():
				pass
			else:
				match(opcode):
					case "MOV": signals[dst] = srcs[0]
					case "NOT": signals[dst] = ~(srcs[0])
					case "AND": signals[dst] = (srcs[0] & srcs[1]) 
					case "OR":  signals[dst] = (srcs[0] | srcs[1]) 
					case "LSHIFT": signals[dst] = (srcs[0] << srcs[1]) 
					case "RSHIFT": signals[dst] = (srcs[0] >> srcs[1]) 
					case _: raise ValueError("Unrecognized opcode: %s" % opcode)
		# If gates remain unsatisfied, repeat iteration
		gates = unconstructed
		continue

	# Signal outputs emulate unsigned 16-bit integers
	signals = {key:(signals[key] & 0xffff) for key in signals}
	return signals

def test() -> None:
	gates = [parse(line) for line in testlines]
	signals = connect(gates)
	assert signals == testsignals

def main() -> None:
	### PART A ###
	gates = [parse(line) for line in aocd.lines]
	signal = connect(gates)['a']
	aocd.submit(signal, part='a')

	### PART B ###
	gates = [parse(line) for line in aocd.lines]
	signal = connect(gates, overrides={'b':signal})['a']
	aocd.submit(signal, part='b')

if __name__ == '__main__':
	test()
	main()