#!/usr/bin/python3

import aocd
from icecream import ic

TESTDATA = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""

def countdots(paper):
	return sum([row.count('#') for row in paper])

def printpaper(paper):
	return "\n".join(["".join([col for col in row]) for row in paper])

def parse(data):
	dots,folds = data.split("\n\n")
	dots = [tuple(map(int,line.split(","))) for line in dots.splitlines()]
	instructions = [(coord,int(val)) for coord,val in 
		[line.split()[-1].split('=') for line in folds.splitlines()]]
	return dots,instructions

def setup(dots):
	xsize = max([x for x,_ in dots])
	ysize = max([y for _,y in dots])
	paper = [['#' if ((x,y) in dots) else '.' for x in range(xsize+1)] 
		for y in range(ysize+1)]
	return paper

def fold(paper, instruction):
	axis,idx = instruction
	ysize = len(paper)
	xsize = len(paper[0])
	if axis == 'y':
		# Walk rows from the fold
		for dy in range(1,ysize-idx):
			for col in range(xsize):
				if paper[idx+dy][col] == "#":
					paper[idx-dy][col] = "#"

		# Update ysize to idx
		ysize = idx

	elif axis == 'x':
		# Walk columns from the fold, copy from (idx+dx) to (idx-dx)
		for dx in range(1,xsize-idx):
			for row in range(ysize):
				if paper[row][idx+dx] == "#":
					paper[row][idx-dx] = "#"

		# Update sizex to idx
		xsize = idx
	else:
		raise ValueError("Encountered unexpected axis: %s" % axis)

	return [paper[row][:xsize] for row in range(ysize)]

def test():
	dots,instructions = parse(TESTDATA)
	paper = setup(dots)
	for instruction in instructions:
		paper = fold(paper,instruction)
		print(countdots(paper))
	print(printpaper(paper),end="\n\n")

def main():
	dots,instructions = parse(aocd.data)
	paper = setup(dots)
	for instruction in instructions:
		paper = fold(paper,instruction)
		print(countdots(paper))
	print(printpaper(paper),end="\n\n")

if __name__ == '__main__':
	# test()
	main()