#!/usr/bin/python3
import copy

class Intcode(object):
	
	def __init__(self, memory=list(), ip=int()):
		self.memory = memory
		self.restore = copy.deepcopy(self.memory)
		self.ip = ip	
	
	def getInst(self, addr):
		if self.memory[addr] == 99:
				return str(addr)+":\t99,"
		else:
				return str(addr)+":\t"+",".join(str(op) for op in self.memory[addr:addr+4])
							
	def __str__(self):
		addr = 0
		output = "ip: %s\n" % self.ip
		while addr < len(self.memory):
			output += self.getInst(addr) + "\n"
			if self.memory[addr] == 99:
				addr += 1
			else:
				addr += 4
		return output
	
	def __repr__(self):
		return f'IntCode(memory={self.memory!r},ip={self.ip!r})'
		
	def reset(self, *args):
		"""
		Reset the Intcode machine
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
			raise Exception("Unexpected opcode: %i!" % self.memory[self.ip])
		
	def run(self):
		"""
		Execute instructions until a fault occurs or reaching a halting state.
		"""
		while True:
			if self.ip > len(self.memory):
				return
			if self.memory[self.ip] == 99:
#				print(self.getInst(self.ip))
				self.step()
				return
			else:
#				print(self.getInst(self.ip))
				self.step()
