#!/usr/bin/env python3

from itertools import count
import aocd
from icecream import ic
import re
import typing

# x1,y1,x2,y2 = *(660, 55), *(986, 197)
# ic(x1,y1,x2,y2)

testlines = (
	"turn on 0,0 through 999,999",
	"toggle 0,0 through 999,0",
	"turn off 499,499 through 500,500",
)

def parse_line(line:str) -> tuple[str,tuple[int,int],tuple[int,int]]:
	p = re.compile(r'(turn on|toggle|turn off)\s(\d{1,3},\d{1,3})\sthrough\s(\d{1,3},\d{1,3})')
	m = p.match(line)
	return (m.group(1), tuple(eval(m.group(2))), tuple(eval(m.group(3))))

def do_action(grid:list[list[bool]],command:str,p1:tuple[int,int],p2:tuple[int,int], digital:bool=False) -> None:
	x1,y1,x2,y2 = *p1,*p2
	for x in range(x1,x2+1):
		for y in range(y1,y2+1):
			if digital:
				match(command):
					case "turn on": grid[x][y] += 1
					case "toggle": grid[x][y] += 2
					case "turn off": grid[x][y] = max(0,grid[x][y]-1)
					case _: raise ValueError("Command %s is invalid" % command)
			else:
				match(command):
					case "turn on": grid[x][y] = True
					case "toggle": grid[x][y] = not grid[x][y]
					case "turn off": grid[x][y] = False
					case _: raise ValueError("Command %s is invalid" % command)

def count_on(grid:list[list[bool]]) -> int:
	return sum(row.count(True) for row in grid)

def count_off(grid:list[list[bool]]) -> int:
	return sum(row.count(False) for row in grid)

def brightness(grid:list[list[bool]]) -> int:
	return sum(sum(row) for row in grid)

def test():
	actions = tuple(parse_line(line) for line in testlines)
	grid = [[False for _ in range(1000)] for _ in range(1000)]
	for command,p1,p2 in actions:
		do_action(grid,command,p1,p2)
	ic(count_on(grid),count_off(grid))
	assert count_on(grid) == 0 + 1000000 - 1000 - 4

def main():
	actions = tuple(parse_line(line) for line in aocd.lines)
	ic(len(actions))
	
	### PART A ###
	grid = [[False for _ in range(1000)] for _ in range(1000)]
	for command,p1,p2 in actions:
		do_action(grid,command,p1,p2,digital=False)
	aocd.submit(count_on(grid),part='a')

	### PART B ###
	grid = [[0 for _ in range(1000)] for _ in range(1000)]
	for command,p1,p2 in actions:
		do_action(grid,command,p1,p2,digital=True)
	aocd.submit(brightness(grid),part='b')

if __name__ == '__main__':
	test()
	main()