#!/usr/bin/python3

import aocd
import string
from icecream import ic
ic.enable()

testdata = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def normalize(game:list[str]) -> list[tuple[int,int,int]]:
    """
    Normalize the representation of a game
    """
    retlist = list()
    for hand in game:
        red: int = 0
        green: int = 0
        blue: int = 0
        for cubes in hand.split(", "):
            count,color = cubes.split(" ")
            if color == "red": 
                red = int(count)
            elif color == "green": 
                green = int(count)
            elif color == "blue":
                blue = int(count)
        retlist.append((red, green, blue))
    return retlist

def validate(hand: tuple[int,int,int], limit: tuple[int,int,int]) -> bool:
    return all(h <= l for h, l in zip(hand,limit))

def test():
    lines = testdata.splitlines()
    games = [line.partition(": ")[2] for line in lines]
    games = [game.split("; ") for game in games]
    games = enumerate([normalize(game) for game in games], start=1)

    # Part A
    count = 0
    for num, hands in games:
        if all([validate(hand, (12,13,14)) for hand in hands]):
            count += num
    assert count == 8

    # Part B
    lines = testdata.splitlines()
    games = [line.partition(": ")[2] for line in lines]
    games = [game.split("; ") for game in games]
    games = enumerate([normalize(game) for game in games], start=1)
    powersum = 0
    
    for num, hands in games:
        red = 0
        green = 0
        blue = 0
        for hand in hands:
            r,g,b = hand
            red = max(red, r)
            green = max(green, g)
            blue = max(blue, b)
        power = red * green * blue
        powersum  += power
    assert powersum == 2286


def main():
    # Part A
    lines = aocd.data.split("\n")
    games = [line.partition(": ")[2] for line in lines]
    games = [game.split("; ") for game in games]
    games = enumerate([normalize(game) for game in games], start=1)
    count = 0

    for num, hands in games:
        if all([validate(hand, (12,13,14)) for hand in hands]):
            count += num
    aocd.submit(count, year=2023, day=2, part="a")

    # Part B
    lines = aocd.data.split("\n")
    games = [line.partition(": ")[2] for line in lines]
    games = [game.split("; ") for game in games]
    games = enumerate([normalize(game) for game in games], start=1)
    powersum = 0
    
    for num, hands in games:
        red = 0
        green = 0
        blue = 0
        for hand in hands:
            r,g,b = hand
            red = max(red, r)
            green = max(green, g)
            blue = max(blue, b)
        power = red * green * blue
        powersum  += power
    aocd.submit(powersum, year=2023, day=2, part="b")

if __name__ == '__main__':
    test()
    main()
