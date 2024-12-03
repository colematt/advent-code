#!/usr/bin/env python3

from aocd import data, submit
import re
import itertools

testdata_a = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
testdata_b = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
def solveA(data):
    matches = [(int(x),int(y)) for x,y in re.findall(r"mul\((\d+),(\d+)\)", data)]
    return sum(map(lambda t: t[0]*t[1], matches))
    
def solveB(data):
    matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data)

    keeping, keepers = True, list()
    for m in matches:
        if m[2] == "do()": keeping = True
        elif m[3] == "don't()": keeping = False
        elif keeping:
            keepers.append((int(m[0]),int(m[1])))
    return sum(map(lambda t: t[0]*t[1], keepers))

if __name__ == "__main__":
    assert solveA(testdata_a) == 161
    submit(solveA(data), part='a')
    
    assert solveB(testdata_b) == 48
    submit(solveB(data), part='b')