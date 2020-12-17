#!/usr/bin/python3

import collections

def game(opening):
	"""
	Generate the terms in a memory game sequence.
	- Opening is always generated in that order.
	- Subsequently, for the most recently generated number:
		- If that was the first time the number has been spoken, 
		  the current player next says 0.
		- Otherwise, the number had been spoken before; the current player 
		  next announces how many turns apart the number is from when it was 
		  previously spoken.
	"""
	
	# Build the initial spoken numbers dictionary
	spoken = collections.defaultdict(int)
	spoken.clear()
	for turn, num in list(enumerate(opening[:-1], start=1)):
		spoken[num] = turn

	# Fast forward gamestate, generate the opening
	last = opening[-1]
	turn = len(opening) + 1
	while opening:
		yield (opening.pop(0))
		
	while True:
		# Generate the subsequent turn
		val = spoken[last]
		if val == 0: speak = 0
		else: speak = turn - 1 - val
		yield speak
		
		# Update gamestate
		spoken[last] = turn - 1
		last = speak
		turn += 1
		
def test():
	#### PART 1 ####
	turns = [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]
	game1 = game(turns[:3])
	for t in range(10):
		assert next(game1) == turns[t]

	openings = [
		[1,3,2],
		[2,1,3],
		[1,2,3],
		[2,3,1],
		[3,2,1],
		[3,1,2]]
	answers = [1, 10, 27, 78, 438, 1836]
	for opening,answer in zip(openings,answers):
		game1 = game(opening)
		for _ in range(2020):
			last = next(game1)
		assert last == (answer)
	
		#### PART 2 ####
		pass
	
def main():
	opening = [8,11,0,19,1,2]
	
	#### PART 1 ####
	gg = game(opening)
	for _ in range(1,2020):
		next(gg)
	print(next(gg))
	
	#### PART 2 ####
	for _ in range(2021,30000000):
		next(gg)
	print(next(gg))

if __name__ == '__main__':
	test()
	main() 