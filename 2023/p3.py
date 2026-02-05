#!/usr/bin/env python3

from aocd import data,submit
from operator import itemgetter
from icecream import ic
from math import prod
import string
NUMBERS = set(string.digits)
SYMBOLS = set(string.punctuation).difference(".")

NumberType = tuple[int,tuple[int,int], tuple[int,int]]
SchematicType = list[str]

testdata = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

def getNumbers(schematic:SchematicType) -> list[NumberType]:
    numbers = list()
    for row in range(len(schematic)):
        num,start,stop = 0,None,None
        for col in range(len(schematic[row])):
            # Read a part
            if schematic[row][col] in NUMBERS:
                # Start reading
                if start == None: start = col
                # Continue reading
                num = num*10 + int(schematic[row][col])
                # Edge case: col is final col in row
                if col == len(schematic[row])-1:
                    stop = col
                    numbers.append((num,(row,start),(row,stop)))
                    num,start,stop = 0,None,None
            else:
                # Stop reading
                if start != None:
                    stop = col-1
                    numbers.append((num,(row,start),(row,stop)))
                    # Reset for next part
                    num,start,stop = 0,None,None
    return numbers

def getAdjacent(num:NumberType, sch:SchematicType):
    _, start, stop = num
    # Get over-approximation of adjacents
    adjs = ((r,c) for r in range(start[0]-1, stop[0]+2) 
             for c in range(start[1]-1, stop[1]+2))
    # Filter for index errors
    adjs = filter(lambda idx: idx[0] >= 0 and idx[0] < len(sch) and idx[1] >= 0 and idx[1] < len(sch[0]), adjs)
    # Filter for indexes inside num itself
    adjs = filter(lambda idx: idx[0] != start[0] or idx[1] < start[1] or idx[1] > stop[1], adjs)
    return tuple(adjs)

def isPart(num:NumberType, sch:SchematicType) -> bool:
    # get adjacent cells to the number
    adjs = getAdjacent(num, sch)
    for adj in adjs:
        row,col = adj
        if sch[row][col] in SYMBOLS:
            return True
    return False

def isAdjacent(gear:tuple[int,int], part:NumberType) -> bool:
    i,j = gear
    row = part[1][0]
    for col in range(part[1][1], part[2][1]+1):
        if abs(i-row) <= 1 and abs(j-col) <= 1:
            return True
    return False

def solveA(data:str) -> int:
    # Read schematic
    schematic = [row for row in data.splitlines()]

    # Get numbers
    numbers = getNumbers(schematic)

    # Filter numbers for parts
    parts:list[NumberType] = list(filter(lambda n: isPart(n,schematic), numbers))

    # Sum part numbers
    return sum([pnum for pnum,_,_ in parts])

def solveB(data:str) -> int:
    # Read schematic
    schematic = [row for row in data.splitlines()]

    # Get numbers
    numbers = getNumbers(schematic)

    # Filter numbers for parts
    parts:list[NumberType] = list(filter(lambda n: isPart(n,schematic), numbers))

    # Get the potential gears' locations in schematic
    gears = list()
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j] == "*":
                gears.append((i,j))
    
    # For each gear, check if adjacent to two numbers
    ratios = list()
    for gear in gears:
        ratio = list()
        for part in parts:
            if isAdjacent(gear,part): ratio.append(part[0])
        if len(ratio) == 2: ratios.append(ratio)
    return sum(map(prod,ratios))

if __name__ == "__main__":
    assert solveA(testdata) == 4361
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 467835
    submit(str(solveB(data)), part='b')

