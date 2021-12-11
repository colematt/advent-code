#!/usr/bin/python3

import aocd
from icecream import ic
from collections import deque
from functools import reduce
from itertools import filterfalse
from operator import add,mul
from statistics import median

DATA = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

openings = set(char for char in '([{<')
closings = set(char for char in ')]}>')
scores = {
	')' : 3,
	']' : 57,
	'}' : 1197,
	'>' : 25137,
	'(' : 1,
	'[' : 2,
	'{' : 3,
	'<' : 4
}

class Stack:
	def __init__(self, iterable=list()):
		self.storage = deque(iterable)

	def __repr__(self):
		return 'Stack(storage=%s)' % repr(self.storage)

	def __str__(self):
		return "size: {} \ntop: {}".format(
			len(self.storage), "\n".join(reversed([str(c) for c in self.storage])))

	def __len__(self):
		return len(self.storage)

	def __nonzero__(self):
		return len(self.storage) > 0

	def size(self):
		return len(self.storage)

	def push(self,char):
		self.storage.append(char)

	def pop(self):
		if self.size() > 0:
			return self.storage.pop()
		else:
			return None

	def reverse(self):
		self.storage.reverse()
		return None

	def peek(self):
		if self.size() > 0:
			return self.storage[-1]
		else:
			return None

def check(str,isComplete=False):
	"""
	Return true if the string is syntax-correct
	although not necessarily complete
	"""
	tokens = [char for char in str]
	stack = Stack()
	for token in tokens:
		if token in openings:
			stack.push(token)
		elif token in closings:
			top = stack.peek()
			if (top,token) not in set(zip('([{<',')]}>')):
				return False
			else:
				stack.pop()
	if isComplete and stack.size() > 0:
		return False
	else:
		return True

def score(str):
	stack = Stack()

	# Syntax error score
	tokens = [char for char in str]
	for token in tokens:
		if token in openings:
			stack.push(token)
		elif token in closings:
			top = stack.peek()
			if (top,token) not in set(zip('([{<',')]}>')):
				return scores[token]
			else:
				stack.pop()

	# Completion error score
	stack.reverse()
	return reduce(
		lambda total,char:add(mul(5,total),scores[char]),
		list(stack.storage),0)

def solveA(data):
	lines = data.splitlines()
	return sum([score(str) 
		for str in filterfalse(check,lines)])

def solveB(data):
	lines = data.splitlines()
	lines = list(filter(check,lines))
	scores = list(filterfalse(lambda s: s==0, [score(line) for line in lines]))
	return median(scores)

def test():
	assert check("[<>({}){}[([])<>]]")
	assert score("[<>({}){}[([])<>]]") == 0
	assert score("{([(<{}[<>[]}>{[]{[(<()>") == 1197
	assert score("<{([{{}}[<[[[<>{}]]]>[]]") == 294
	assert solveA(DATA) == 26397
	assert solveB(DATA) == 288957

def main():
	aocd.submit(solveA(aocd.data), part='a')
	aocd.submit(solveB(aocd.data), part='b')

if __name__ == '__main__':
	test()
	main()