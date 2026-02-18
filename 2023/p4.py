#!/usr/bin/env python3

from aocd import data,submit
from icecream import ic

testdata = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

CardType = tuple[set[int],set[int]]

def canonicalize(data:str) -> list[CardType]:
    lines = [line.split(":")[1].split("|") for line in data.splitlines()]
    cards = [(set(int(n) for n in lhs.strip().split()),set(int(n) for n in rhs.strip().split())) for lhs,rhs in lines]
    return cards
    

def solveA(data:str) -> int:
    cards = canonicalize(data)
    matches = [len(winners.intersection(holds)) for winners,holds in cards]
    values = [2**(m-1) if m>=1 else 0 for m in matches]
    return sum(values)


def solveB(data:str) -> int:
    cards = canonicalize(data)
    ncards = [1 for card in cards]
    matches = [len(winners.intersection(holds)) for winners,holds in cards]
    for i in range(len(cards)):
        for j in range(i+1,i+1+matches[i]):
            ncards[j] += ncards[i]
    return sum(ncards)


if __name__ == "__main__":
    assert solveA(testdata) == 13
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 30
    submit(str(solveB(data)), part='b')
