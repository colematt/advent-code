#!/usr/bin/python3

import collections

def game(opening):
	"""
	Generate the terms in a memory game sequence, where at each turn, the term
	is (step, number).
	
	:param      opening:  The opening
	:type       opening:  { type_description }
	"""
	# Initialize gamestate
	turn = 0
	last = None

	# Build the initial spoken dictionary
	spoken = collections.defaultdict(int)
	spoken.clear()
	for turn, num in list(enumerate(opening[:-1], start=1)):
		spoken[num] = turn
	print(spoken)

	# Generate the opening
	while opening:
		yield (last := opening.pop(0))
		turn += 1

	while True:
		# Generate the subsequent turn
		if last not in spoken: curr = 0
		else: curr = turn - spoken[last]

		# Update gamestate
		spoken[last] = turn - 1
		last = curr
		turn += 1

		print(spoken)
			

def test():

	#### PART 1 ####
	turns = [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]
	game1 = game(turns[:3])
	for t in range(10):
		print(t+1, curr := next(game1))
		assert curr == turns[t]

	# openings = [
	# 	[1,3,2],
	# 	[2,1,3],
	# 	[1,2,3],
	# 	[2,3,1],
	# 	[3,2,1],
	# 	[3,1,2]
	# ]
	# answers = [1, 10, 27, 78, 438, 1836]
	# for opening,answer in zip(openings,answers):
	# 	game1 = game(opening)
	# 	for turn in range(2020):
	# 		last = next(game1)
	# 	assert last == (answer)


def main():
	opening = [8,11,0,19,1,2]

if __name__ == '__main__':
	test()
	main() 