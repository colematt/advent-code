#!/usr/bin/python3
import copy
import pprint
import string
from collections import namedtuple

"""
Instruction set specification
"""
Instruction = namedtuple('Instruction', ('opcode','mnemonic','parameters'))
Instructions = {
	1 : Instruction(1,'ADD',('op','src1','src2','dst')),
	2 : Instruction(2,'MUL',('op','src1','src2','dst')),
	3 : Instruction(3,'GETS',('op','dst')),
	4 : Instruction(4,'PUTS',('op','src')),
	5 : Instruction(5,'JMPTRUE',('op','src','loc')),
	6 : Instruction(6,'JMPFALSE',('op','src','loc')),
	7 : Instruction(7,'LT',('op','src1','src2','dst')),
	8 : Instruction(8,'EQ',('op','src1','src2','dst')),
	99: Instruction(99,'HLT',('op'))
}

class Intcode(object):
	"""
	Representation of an Intcode machine.
	"""	
	def __init__(self, memory=list(), ip=int()):
		self.memory = memory
		self.restore = copy.deepcopy(self.memory)
		self.ip = ip	
	
	def __repr__(self):
		return f'IntCode(memory={self.memory!r},ip={self.ip!r})'
	
	def __str__(self):
		return pprint.pformat(self)
		
	def disassemble(self, addr):
		"""
		Return a string representation of the instruction at addr
		using Intel syntax (mnemonic dst, src, ...).
		"""
		try:
			modes, opcode = divmod(self.memory[addr], 100)
			modes = tuple(modes//10**i % 10 for i in range(2,-1,-1))[::-1]
			instruction = Instructions[opcode]
		except IndexError:
			raise IndexError("Address %i out of bounds" % addr)
		except KeyError:
			raise KeyError("Invalid opcode %i" % opcode)
		
		output = string.Template('${addr}:  ${values}\t${mnemonic} ${parameters}')
		return output.substitute({
			'addr':str(addr),
			'values':" ".join(str(o) for o in self.memory[addr:addr+len(instruction.parameters)]),
			'mnemonic':instruction.mnemonic,
			'parameters':",".join(str(z) for z in zip(modes,self.memory[addr+1:addr+len(instruction.parameters)]))
			})
		
	def reset(self, *args):
		"""
		Reset the Intcode machine to its initial memory state,
		then override the state using arguments in args.
		"""
		self.memory = copy.deepcopy(self.restore)
		self.ip = 0
		if args:
			for arg in args:
				addr, value = arg
				self.memory[addr] = value
			
	def step(self):
		"""
		Execute one instruction cycle. 
		Return True if not halted. Return False if halted or an error occurs.
		"""		
		try:
			# Fetch stage 
			# Print the fetched instruction
	#		print(self.disassemble(self.ip))
			opcode = self.memory[self.ip] % 100
			if opcode == 99:
				return False
			elif opcode in Instructions:
				values = self.memory[self.ip:self.ip+len(Instructions[opcode].parameters)]
				self.ip += len(Instructions[opcode].parameters)
			else:
				raise ValueError("Unexpected opcode: %i" % opcode)
			
			# Decode stage
			# Get modes 
			# 0: position mode, 1: immediate mode
			modes, opcode = divmod(values[0], 100)
			modes = (1,) + tuple(modes//10**i % 10 for i in range(2,-1,-1))[::-1]
			
			# Fill operands
			# dst operand must always be in position mode
			inst = {p:(self.memory[v] if m==0 and p != "dst" else v) for p,v,m in zip(Instructions[opcode].parameters,values,modes)}
			inst['op'] = opcode
						
			# Execute stage
			if inst['op'] == 1:
				self.memory[inst['dst']] = inst['src1'] + inst['src2']
				return True
			elif inst['op'] == 2:
				self.memory[inst['dst']] = inst['src1'] * inst['src2']
				return True
			elif inst['op'] == 3:
				self.memory[inst['dst']] = int(input("Gets? "))
				return True
			elif inst['op'] == 4:
				print("Puts: ", inst['src'])
				return True
			elif inst['op'] == 5:
				if inst['src'] != 0: self.ip = inst['loc']
				return True
			elif inst['op'] == 6:
				if inst['src'] == 0: self.ip = inst['loc']
				return True
			elif inst['op'] == 7:
				if inst['src1'] < inst['src2']:
					self.memory[inst['dst']] = 1
				else:
					self.memory[inst['dst']] = 0
				return True
			elif inst['op'] == 8:
				if inst['src1'] == inst['src2']:
					self.memory[inst['dst']] = 1
				else:
					self.memory[inst['dst']] = 0
				return True
		except IndexError:
			raise IndexError("Instruction pointer out of bounds at %i" % self.ip)
		
	def run(self):
		"""
		Execute instructions until a fault occurs or reaching a halting state.
		"""
		# Loop while execution continues
		while self.step():
			continue

		# Exit from halting state
#		print(self)
