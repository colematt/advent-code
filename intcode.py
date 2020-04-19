#!/usr/bin/python3
import copy
import pprint
import string
from collections import namedtuple

"""
Instruction set specification
"""
Instruction = namedtuple('Instruction', ('opcode','mnemonic','length'))
Instructions = {
	1 : Instruction(1,'ADD',4),
	2 : Instruction(2,'MUL',4),
	99: Instruction(99,'HLT',1),
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
		output = string.Template('${addr}\t${opcode} ${operands}')
		try:
			opcode = self.memory[addr]
			operands = self.memory[addr:addr+Instructions[opcode].length-1]
			return output.substitute(
				addr=str(addr),
				opcode=str(self.memory[addr]),
				operands=" ".join(str(o) for o in operands))
		except IndexError:
			raise IndexError("Address %i out of bounds" % addr)
		except KeyError:
			raise KeyError("Invalid opcode %i" % opcode)	
		
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
		Execute the next instruction.
		"""
		if self.memory[self.ip] == 1:
			op,src1,src2,dst = self.memory[self.ip:self.ip+4]
			self.memory[dst] = self.memory[src1] + self.memory[src2]
			self.ip += 4
		elif self.memory[self.ip] == 2:
			op,src1,src2,dst = self.memory[self.ip:self.ip+4]
			self.memory[dst] = self.memory[src1] * self.memory[src2]
			self.ip += 4
		elif self.memory[self.ip] == 99:
			pass
		else:
			raise ValueError("Unexpected opcode: %i" % self.memory[self.ip])
		
	def run(self):
		"""
		Execute instructions until a fault occurs or reaching a halting state.
		"""
		# Loop while execution continues
		while True:
			try:
#				print(self.disassemble(self.ip))
				if self.memory[self.ip] == 99:
					self.step()
					break
				else:
					self.step()
			except IndexError:
				raise IndexError("Instruction pointer out of bounds at %i" % self.ip)
		
		# Exit from function
#		print(self)
		return