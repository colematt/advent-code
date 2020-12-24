#!/usr/bin/python3

import aocd
from collections import deque
from icecream import ic
import itertools
import typing

def _score(deck):
	return sum(map(lambda x: x[0]*x[1], (enumerate(reversed(deck),start=1))))

def combat(deck1, deck2):
	"""
	Play a game of standard Combat!
	
	:param      deck1:  Player 1's deck
	:type       deck1:  typing.Deque
	:param      deck2:  Player 2's deck
	:type       deck2:  typing.Deque
	
	:returns:   Winning player's score
	:rtype:     int
	"""

	# Opening
	ic("Player 1's deck: ", ", ".join(str(card) for card in deck1))
	ic("Player 2's deck: ", ", ".join(str(card) for card in deck2))

	# Play rounds until one player has all cards
	r = 0
	while deck1 and deck2:
		# Round header
		r += 1
		ic("-- Round {} --".format(r))

		# Play card from top of the deck
		c1 = deck1.popleft()
		c2 = deck2.popleft()
		ic("Player 1 plays: {}".format(c1))
		ic("Player 2 plays: {}".format(c2))

		# Comparison and resolution
		if c1 > c2:
			deck1.extend([c1,c2])
			ic("Player 1 wins the round!")
		if c2 > c1:
			deck2.extend([c2,c1])
			ic("Player 2 wins the round")
	
	# Report winner
	ic("== Post-game results ==")
	ic("Player 1's deck: ", deck1)
	ic("Player 2's deck: ", deck2)
	return max(_score(deck1), _score(deck2))

def recursive_combat(deck1, deck2):
	"""
	Play a game of recursive Combat!
	
	:param      deck1:  Player 1's deck
	:type       deck1:  typing.Deque
	:param      deck2:  Player 2's deck
	:type       deck2:  typing.Deque
	
	:returns:   Winning player's score
	:rtype:     int
	"""

	# Round counter and deck state memory
	r = 0
	states = set()

	# Opening
	ic("Player 1's deck: ", ", ".join(str(card) for card in deck1))
	ic("Player 2's deck: ", ", ".join(str(card) for card in deck2))

	# Play rounds until a victory condition
	while deck1 and deck2:
		# Prevent infinite recursion
		state = (tuple(deck1),tuple(deck2))
		if state in states:
			ic("Previous round's decks encountered!")
			ic("Player 1 wins!")
			return _score(deck1)
		else:
			states.add(state)

		# Round header
		r += 1
		ic("-- Round {} --".format(r))

		# Play card from top of the deck
		c1 = deck1.popleft()
		c2 = deck2.popleft()
		ic("Player 1 plays: {}".format(c1))
		ic("Player 2 plays: {}".format(c2))

		# Winner of this round is determined by 
		# recursive Combat
		if c1 > len(deck1) and c2 > len(deck2):

		# Otherwise, at least one player doesn't have enough
		# cards for recursive combat. The winner of the round
		# is player with the higher value card
		else:
			pass

		# Comparison and resolution
		if c1 > c2:
			deck1.extend([c1,c2])
			ic("Player 1 wins the round!")
		if c2 > c1:
			deck2.extend([c2,c1])
			ic("Player 2 wins the round")
	
	# Report winner
	ic("== Post-game results ==")
	ic("Player 1's deck: ", deck1)
	ic("Player 2's deck: ", deck2)
	return max(_score(deck1), _score(deck2))
	

def test():
	with open('test.txt', 'r') as fin:
		data = fin.read()
	
	#### PART A ####
	player1, player2 = data.split('\n\n')
	player1 = deque(int(card) for card in player1.split('\n')[1:])
	player2 = deque(int(card) for card in player2.split('\n')[1:])
	assert combat(player1, player2) == 306

	#### PART B ####
	player1, player2 = data.split('\n\n')
	player1 = deque(int(card) for card in player1.split('\n')[1:])
	player2 = deque(int(card) for card in player2.split('\n')[1:])
	assert recursive_combat(player1, player2) == 291

def main():
	data = aocd.get_data(year=2020, day=22, block=True)

	player1, player2 = data.split('\n\n')
	player1 = deque(int(card) for card in player1.split('\n')[1:])
	player2 = deque(int(card) for card in player2.split('\n')[1:])

	aocd.submit(combat(player1, player2), part="a", day=22, year=2020)
	
if __name__ == '__main__':
	test()
	main()