#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()

testdata = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

def isValidA(line:str) -> bool:
	count,letter,password = line.split()
	count = range(int(count.split('-')[0]), int(count.split('-')[1])+1)
	letter = letter.rstrip(':')
	password = password.rstrip('\n')
	return password.count(letter) in count


def isValidB(line:str) -> bool:
	indexes,letter,password = line.split()
	i,j = int(indexes.split('-')[0]) - 1, int(indexes.split('-')[1]) - 1
	letter = letter.rstrip(':')
	password = password.rstrip('\n')
	return (password[i] == letter) ^ (password[j] == letter)

def solveA(data:str):
	return len(list(filter(isValidA, data.splitlines())))


def solveB(data:str):
    return len(list(filter(isValidB, data.splitlines())))


if __name__ == '__main__':
	assert(solveA(testdata) == 2)
	submit(str(solveA(data)), part='a')
	assert(solveB(testdata) == 1)
	submit(str(solveB(data)), part='b')
