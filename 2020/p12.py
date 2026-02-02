#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()

testdata = """F10
N3
F7
R90
F11
"""

class Ferry:
    def __init__(self, x=0, y=0, h=90, wx=10, wy=1):
        self.x = x
        self.y = y
        self.h = h
        self.wx = wx
        self.wy = wy
        
    def __repr__(self):
        return "Ferry(x=%i, y=%i, course=%i)" % (self.x, self.y, self.h)
    
    def go(self,action,value):
        if action == 'N':   self.y += value
        elif action == 'E': self.x += value
        elif action == 'S': self.y -= value
        elif action == 'W': self.x -= value
        elif action == 'L': self.h = (self.h - value + 360) % 360
        elif action == 'R': self.h = (self.h + value) % 360
        elif action == 'F':
            if self.h == 0: self.go('N',value)
            elif self.h == 90: self.go('E',value)
            elif self.h == 180: self.go('S',value)
            elif self.h == 270: self.go('W',value)
            else: raise ValueError("Unrecognized ship heading %i" % self.h)
        else:
            raise ValueError("Unrecognized action %s" % action)
    
    def way(self,action,value):
        if action == 'N':   self.wy += value
        elif action == 'E': self.wx += value
        elif action == 'S': self.wy -= value
        elif action == 'W': self.wx -= value
        elif action == 'L': 
            if value == 0: pass
            elif value == 90: self.wx, self.wy = -self.wy, self.wx
            elif value == 180: self.wx, self.wy = -self.wx, -self.wy
            elif value == 270: self.wx, self.wy = self.wy, -self.wx
            else: raise ValueError("Unrecognized translation angle %i" % value)
        elif action == 'R': 
            if value == 0: pass
            elif value == 90: self.wx, self.wy = self.wy, -self.wx
            elif value == 180: self.wx, self.wy = -self.wx, -self.wy
            elif value == 270: self.wx, self.wy = -self.wy, self.wx
            else: raise ValueError("Unrecognized translation angle %i" % value)		
        elif action == 'F':
            self.x += value * self.wx
            self.y += value * self.wy
        else:
            raise ValueError("Unrecognized action %s" % action)
            
    def manDist(self):
        return abs(self.x) + abs(self.y)
    
def solveA(data:str) ->int:
    instructions = [(i[0],int(i[1:])) for i in data.splitlines()]
    ferry = Ferry()
    for inst in instructions:
        action,value = inst
        ferry.go(action,value)
    return ferry.manDist()


def solveB(data:str) ->int:
    instructions = [(i[0],int(i[1:])) for i in data.splitlines()]
    ferry = Ferry()
    for inst in instructions:
        action,value = inst
        ferry.way(action,value)
    return ferry.manDist()


if __name__ == "__main__":
    assert solveA(testdata) == 25
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 286
    submit(str(solveB(data)), part='b')