#!/usr/bin/env python3

import collections
import itertools
import math
import operator

memos = dict()

def chain(iterable):
	head,tail = iterable[0],iterable[1:]

	# Memo case
	if head in memos:
		return memos[head]
	# Base case: 
	# head is within 3 jolts of the last item of the tail (the built in adaptor)
	if tail[-1] - head <= 3:
		memos[head] = 1
		return 1
	# Recursive case: 
	# head is within 3 jolts of each of the first three adaptors in tail
	chains = 0
	if len(tail) > 0 and tail[0] - head <= 3:
		chains += chain(tail[0:])
	if len(tail) > 1 and tail[1] - head <= 3:
		chains += chain(tail[1:])
	if len(tail) > 2 and tail[2] - head <= 3:
		chains += chain(tail[2:])
	memos[head] = chains
	return chains

def main():
	with open('inputs/input10-test.txt') as fin:
		# Get the collection of adaptors, 
		# add the builtin adaptor and wall outlet 
		adaptors = sorted(int(line) for line in fin.readlines())
		adaptors.append(max(adaptors) + 3)
		adaptors.insert(0,0)

		# Find differences between each step
		# Count distribution of steps
		differences = list(itertools.starmap(
			operator.sub, zip(adaptors[1:], adaptors)))
		counter = collections.Counter(differences)
		assert counter[1],counter[3] == (7,5)

		# Find count of possible adaptor chains
		memos.clear()
		assert chain(adaptors) == 8

	with open('inputs/input10.txt') as fin:
		# Get the collection of adaptors, 
		# add the builtin adaptor and wall outlet 
		adaptors = sorted(int(line) for line in fin.readlines())
		adaptors.append(max(adaptors) + 3)
		adaptors.insert(0,0)

		# Find differences between each step
		# Count distribution of steps
		differences = list(itertools.starmap(
			operator.sub, zip(adaptors[1:], adaptors)))
		counter = collections.Counter(differences)
		print(math.prod((counter[1],counter[3])))

		# Find count of possible adaptor chains
		memos.clear()
		print(chain(adaptors))
		
if __name__ == "__main__":
	main()
	