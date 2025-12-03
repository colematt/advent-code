#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic

testdata = """987654321111111
811111111111119
234234234234278
818181911112111
"""


def solveA(data:str) -> int: 
    banks = [[int(i) for i in bank] for bank in data.splitlines()]
    joltages = list()
    for bank in banks:
        i = bank.index(max(bank[:-1]))
        j = bank.index(max(bank[i+1:]))
        joltages.append(10 * bank[i] + bank[j])
    return sum(joltages)


def solveB(data:str) -> int:
    banks = [[int(i) for i in bank] for bank in data.splitlines()]
    joltages = list()
    for bank in banks:
        # Set the index of the first selected battery 
        # in an array of 12 batteries
        idxs = [bank.index(max(bank[:len(bank)-11]))] * 12
        # Set the next 11 batteries
        for i in range(1,12):
            # idxs[i] will be index of max value in the slice
            start = idxs[i-1] + 1
            stop = len(bank)-11+i
            idxs[i] = bank.index(max(bank[start:stop]), start, stop)
        # Calculate the bank's joltage
        js = [bank[i] for i in idxs]
        joltage = 0
        for j in js:
            joltage *= 10
            joltage += j
        joltages.append(joltage)
    return sum(joltages)

if __name__ == "__main__":
    assert solveA(testdata) == 357
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 3121910778619
    submit(str(solveB(data)), part='b')