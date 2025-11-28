#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
from operator import add, mul
from itertools import product
from functools import reduce

testdata = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

def concat(x,y):
    return int(str(x) + str(y))

def parse(data):
    return [(int(lhs),[int(operand) for operand in rhs.split()]) 
            for lhs,rhs in [line.split(": ") 
                            for line in data.splitlines()]]

def iterreduce(operators, operands):
    if not operands:
        return None
    else:
        res = operands.pop(0)
        while operands:
            op, x = operators.pop(0), operands.pop(0)
            res = op(res,x)
        return res

def solveA(data):
    # Get input
    equations = parse(data)
    
    # Attempt to solve each equation
    testlist = list()
    for equation in equations:
        target, operands = equation
        
        # Get operators generator
        operators = product((add, mul), repeat=len(operands)-1)

        # Test each operator selection
        for optup in operators:
            oplist = list(optup)
            if reduce(lambda x, y: oplist.pop()(x,y), operands) == target:
                testlist.append(target)
                break
        
    # Get answer by sum of testlist
    return sum(testlist)

def solveB(data):
    # Get input
    equations = parse(data)
    
    # Attempt to solve each equation
    testlist = list()
    for equation in equations:
        target, operands = equation
        
        # Get operators generator
        operators = product((add, mul, concat), repeat=len(operands)-1)

        # Test each operator selection
        for optup in operators:
            oplist = list(optup)
            if reduce(lambda x, y: oplist.pop()(x,y), operands) == target:
                testlist.append(target)
                break
        
    # Get answer by sum of testlist
    return sum(testlist)
    
if __name__ == "__main__":
    assert solveA(testdata) == 3749
    submit(solveA(data), part='a')

    assert solveB(testdata) == 11387
    submit(solveB(data), part='b')
