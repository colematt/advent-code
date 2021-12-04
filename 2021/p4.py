#!/usr/bin/python3

import aocd
from icecream import ic
import itertools
import more_itertools as mit

DATA = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

def make_game(input):
	lines = input.splitlines()
	draws = [int(i) for i in lines[0].split(",")]
	boards = [[list(int(n) for n in row.split()) for row in board] 
		for board in mit.grouper(
			itertools.filterfalse(lambda line: line == '', lines[1:]),5)]
	return draws,boards

def check(board):
	for row in board:
		if all(x == None for x in row): return True
	for col in zip(*board):
		if all(x == None for x in col): return True
	return False 

def score(board,draw):
	remainder = sum(filter(lambda x:x, itertools.chain(*board)))
	final = remainder*draw
	ic(remainder, draw, final)
	return remainder*draw

def playA(draws,boards):
	for draw in draws:
		ic(draw)
		for board in boards:
			# Mark the space if it's drawn
			for row in range(5):
				for col in range(5):
					if board[row][col] == draw: board[row][col] = None
			ic(board)

			# Check for a winner
			if check(board): 
				final = score(board,draw)
				ic("Winner!", draw, board, final)
				return final
	ic("No winner :(")

def playB(draws, boards):
	for draw in draws:
		ic(draw)
		
		# Play the round, recording the last winner encountered
		winners = list()

		for index,board in enumerate(boards):
			ic("Boards remaining", len(boards))
			# Mark the space if it's drawn
			for row in range(5):
				for col in range(5):
					if board[row][col] == draw: board[row][col] = None
			ic(board)

			# Check if winner, remove from boards
			if check(board):
				lastwin = (board,draw)
				winners.insert(0,index)
				ic("Winner!", lastwin)
		
		# Delete the winners from the boards list
		# and reset the list
		ic(winners)
		for i in winners:
			ic(i)
			boards.pop(i)
		winners.clear()

	# Finish the game
	final = score(*lastwin)
	ic(lastwin, final)
	return final

def test():
	draws,boards = make_game(DATA)
	playA(draws,boards)
	playB(draws,boards)

def main():
	draws,boards = make_game(aocd.data)
	aocd.submit(playA(draws,boards), part='a')
	aocd.submit(playB(draws,boards), part='b')

if __name__ == '__main__':
	ic.disable()
	test()
	main()