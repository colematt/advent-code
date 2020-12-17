#!/usr/bin/python3

import typing

def validate_old(password:tuple):
	# Extract policy
	limit,substring,pw = password
	limit = tuple(int(n) for n in limit.split('-'))
	substring = substring.rstrip(":")
	
	# Perform validation
	count = pw.count(substring)
	return count >= min(limit) and count <= max(limit)

def validate_new(password:tuple):
	# Extract policy
	indices,substring,pw = password
	indices = tuple(int(n)-1 for n in indices.split('-'))
	substring = substring.rstrip(":")

	# Perform validation
	i1, i2 = indices
	return (pw[i1] == substring) ^ (pw[i2] == substring)


def main():
	with open('inputs/input2.txt','r') as fin:
		passwords = [tuple(line.split()) for line in fin.readlines()]
		print(len(list(filter(validate_old,passwords))))
		print(len(list(filter(validate_new,passwords))))


if __name__ == '__main__':
	main()