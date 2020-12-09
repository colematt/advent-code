#!/usr/bin/env python3

import itertools
import typing

def validate(numbers:list, index:int, lookback:int=25):
	"""
	Return true if numbers[index] is the sum of two numbers in the lookback slice
	"""
	if index >= lookback:
		try:
			preamble = numbers[index-lookback:index]
			number = numbers[index]
			return any(list(filter(lambda c:sum(c)==number,itertools.combinations(preamble, 2))))
		except IndexError:
			return False
	else:
		# Indices less than the lookback window are in the preamble and always validate
		return True

def allSlices(iterable):
	for start,stop in itertools.permutations(range(len(iterable)),2):
		yield iterable[start:stop]

def main():
	with open('inputs/input9-test.txt','r') as fin:
		numbers = [int(line) for line in fin.readlines()]
		lookback = 5
		
		# Part 1
		assert [numbers[index] for index in range(lookback,len(numbers)) if not validate(numbers,index,lookback)][0] == 127
		
		# Part 2
		weakness = [sl for sl in allSlices(numbers) if sum(sl) == 127 and len(sl) >= 2]
		assert min(weakness[0]) + max(weakness[0]) == 62
	
	with open('inputs/input9.txt','r') as fin:
		numbers = [int(line) for line in fin.readlines()]
		lookback = 25
		
		# Part 1
		invalid = [numbers[index] for index in range(lookback,len(numbers)) if not validate(numbers,index,lookback)][0]
		print(invalid)
		
		# Part 2
		weakness = [sl for sl in allSlices(numbers) if sum(sl) == invalid and len(sl) >= 2]
		print(min(weakness[0]) + max(weakness[0]))
	
if __name__ == "__main__":
	main()
	