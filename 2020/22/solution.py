#!/usr/bin/python3

import aocd
from collections import deque
from icecream import ic
import itertools
from math import prod
import typing

# Global gamestate
games = 0

def _str(deck):
	if deck:
		return "top=" + ", ".join(str(card) for card in deck)
	else:
		return "empty"

def score(deck):
	"""
	Return the deck's score. Empty decks are worth zero.
	The bottom card in the deck is worth its face value.
	The nth card in the deck from the bottom is worth
	n times its face value.

	:param      deck:  The deck
	:type       deck:  typing.deque

	:returns:   Deck score
	:rtype:     int
	"""

	return sum(map(prod, (enumerate(reversed(deck),start=1))))

def combat(deck1, deck2, recursive=False, debug=False, caller=None):
	"""
	Play a game of Combat!
	
	:param      deck1:      Player 1's deck
	:type       deck1:      typing.Deque
	:param      deck2:      Player 2's deck
	:type       deck2:      typing.Deque
	:param      recursive:  Enable recursive gameplay
	:type       recursive:  boolean
	:param      debug:      Log gameplay to stdout
	:type       debug:      boolean
	:param      caller:     The caller game's ID in recursive Combat!
	:type       caller:     int
	
	:returns:   Players' decks as a 2-tuple
	:rtype:     (typing.Deque, typing.Deque)
	"""

	# Local game state
	global games
	games += 1; game = games
	rounds = 0
	states = set()
	dbg = debug

	# Opening
	if debug:
		print("=== Game {} ===".format(game))

	# Play rounds until one player has all cards
	while deck1 and deck2:
		# Round header
		rounds += 1
		if debug:
			print("-- Round {} (Game {}) --".format(rounds, game))
			print("Player 1's deck: {}".format(_str(deck1)))
			print("Player 2's deck: {}".format(_str(deck2)))

		# Check for repeated gamestate.
		# if repeated, player 1 immediately wins.
		# Return player 1's deck and an empty deck to represent
		# player 2 having "lost"
		if recursive:
			state = (tuple(deck1), tuple(deck2))
			if state in states:
				return (deck1, deque())
			else:
				states.add(state)

		# Play card from top of the deck
		c1 = deck1.popleft()
		c2 = deck2.popleft()
		if debug:
			print("Player 1 plays: {}".format(c1))
			print("Player 2 plays: {}".format(c2))

		# Comparison and resolution
		if recursive:
			# Check whether to descend into sub-game
			if len(deck1) >= c1 and len(deck2) >= c2:
				if debug: print("Playing a sub-game to determine the winner...")

				# Make copies of the decks by slicing
				copy1 = deque(itertools.islice(deck1, c1))
				copy2 = deque(itertools.islice(deck2, c2))

				# Launch a recursive sub-game
				copy1, copy2 = combat(copy1, copy2, recursive=True, debug=dbg, caller=game)
				if copy1:
					deck1.extend([c1,c2])
					if debug: print("Player 1 wins the subgame and round!")
				else:
					deck2.extend([c2,c1])
					if debug: print("Player 2 wins the subgame and round!")
			else:
				if c1 > c2:
					deck1.extend([c1,c2])
					if debug: print("Player 1 wins the round!")
				if c2 > c1:
					deck2.extend([c2,c1])
					if debug: print("Player 2 wins the round")
		else:
			if c1 > c2:
				deck1.extend([c1,c2])
				if debug: print("Player 1 wins the round!")
			if c2 > c1:
				deck2.extend([c2,c1])
				if debug: print("Player 2 wins the round")
		
	# Report winner
	if debug:
		print("== Post-game results ==")
		print("Player 1's deck: {}".format(_str(deck1)))
		print("Player 2's deck: {}".format(_str(deck2)))
		if caller: print("\n...anyway, back to game {}.".format(caller))
	return (deck1, deck2)

def test():
	data = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""
	
	#### PART A ####
	player1, player2 = data.split('\n\n')
	player1 = deque(int(card) for card in player1.split('\n')[1:])
	player2 = deque(int(card) for card in player2.split('\n')[1:])
	assert max(map(score, combat(player1, player2, debug=True))) == 306

	#### PART B ####
	player1, player2 = data.split('\n\n')
	player1 = deque(int(card) for card in player1.split('\n')[1:])
	player2 = deque(int(card) for card in player2.split('\n')[1:])
	assert max(map(score, combat(player1, player2, recursive=True, debug=True))) == 291

def main():
	data = aocd.get_data(year=2020, day=22, block=True)

	player1, player2 = data.split('\n\n')
	player1 = deque(int(card) for card in player1.split('\n')[1:])
	player2 = deque(int(card) for card in player2.split('\n')[1:])
	winner_score = max(map(score, combat(player1, player2)))
	aocd.submit(winner_score, part="a", day=22, year=2020)

	player1, player2 = data.split('\n\n')
	player1 = deque(int(card) for card in player1.split('\n')[1:])
	player2 = deque(int(card) for card in player2.split('\n')[1:])
	winner_score = max(map(score, combat(player1, player2, recursive=True)))
	aocd.submit(winner_score, part="b", day=22, year=2020)
	
if __name__ == '__main__':
	# test()
	main()