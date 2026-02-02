#!/usr/bin/env python3

from aocd import data, submit
import collections
import itertools
import re
from icecream import ic

mask_re = re.compile(r'^mask = ([X01]{36})$', re.M)
mem_re = re.compile(r'^mem\[(\d+)\] = (\d+)$', re.M)

testdata = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

class Machine:
    def __init__(self, program=list()):
        self.mask = None
        self.memory = collections.defaultdict(int)
        self.program = program
        
    def __repr__(self):
        attrs = list()
        for item in vars(self).items():
            k,v = item
            attrs.append("%s=%s" % (k,repr(v)))
        return 'Machine(%s)' % ', '.join(attrs)
    
    def reset(self):
        """
        Reset the machine's mask and memory.
        Program is not reset because it cannot be reconstructed.
        """
        self.mask = None
        self.memory.clear()
    
    def checksum(self):
        """
        Return the memory's checksum
        """
        return sum(self.memory.values())
    
    def setter(self,addr,val):
        """
        Set memory[addr] to the composition of val and mask
        """
        addr = int(addr)
        res = int(val)
        mask1 = int(self.mask.replace('X','0'),2) # OR this value to set 1s
        mask0 = int(self.mask.replace('X','1'),2) # AND this value to set 0s
        res |= mask1 
        res &= mask0
        self.memory[addr] = res
    
    def decoder(self,addr,val):
        """
        Decode addr's floating bits and set memory to val
        """
        val = int(val)
        addr = bin(int(addr))[2:].rjust(36,'0')
        addr = "".join(map(lambda t: t[0] if t[1] == '0' else t[1], (tup for tup in zip(addr,self.mask))))
        count = addr.count('X')
        for rc in itertools.product('01', repeat=count):
            res = addr
            for c in rc:
                res = res.replace('X', c, 1)
            self.memory[int(res,2)] = val
                
    def run(self, decode=False):
        """
        Run Machine's program, either setting or decoding each mem line
        """
        self.reset()
        for line in self.program:
            # If we find a mask, update Machine's mask
            if (m := mask_re.match(line)):
                self.mask = m.group(1)
            # If we find a mem, update the Machine's memory by decoding or setting
            elif (m := mem_re.match(line)):
                if not self.mask:
                    raise ValueError("mask not set prior to one or more `mem` operations")
                addr, val = m.group(1), m.group(2)
                if decode: 
                    self.decoder(addr, val)
                else: 
                    self.setter(addr,val)
            else:
                raise ValueError("Unrecognized program line: %s" % line)


def solveA(data:str) -> int:
    machine = Machine(program=[line.rstrip() for line in data.splitlines()])
    machine.run(decode=False)
    return machine.checksum()


def solveB(data:str) -> int:
    machine = Machine(program=[line.rstrip() for line in data.splitlines()])
    machine.run(decode=True)
    return machine.checksum()

if __name__ == "__main__":
    assert solveA(testdata) == 165
    submit(str(solveA(data)), part='a')
    # assert solveB(testdata) == 208
    # submit(str(solveB(data)), part='b')
