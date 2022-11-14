#!/usr/bin/env python3

import aocd
from icecream import ic
import hashlib

testdata = [(b'abcdef',609043),(b'pqrstuv',1048970)]

def test():
	for key,answer in testdata:
		hasher = hashlib.md5(key)
		number = 1
		while(True):
			clone = hasher.copy()
			clone.update(bytes(str(number),'ascii'))
			if clone.hexdigest()[:5] == '00000':
				break
			else:
				number += 1
		assert answer == number
	
def main():
	### PART A ###
	key = b'iwrupvqb'
	hasher = hashlib.md5(key)
	number = 1
	while(True):
		clone = hasher.copy()
		clone.update(bytes(str(number),'ascii'))
		if clone.hexdigest()[:5] == '00000':
			break
		else:
			number += 1
	aocd.submit(number,part='a')
	
	### PART B ###
	key = b'iwrupvqb'
	hasher = hashlib.md5(key)
	number = 1
	while(True):
		clone = hasher.copy()
		clone.update(bytes(str(number),'ascii'))
		if clone.hexdigest()[:6] == '000000':
			break
		else:
			number += 1
	aocd.submit(number,part='b')
	
if __name__ == "__main__":
	test()
	main()