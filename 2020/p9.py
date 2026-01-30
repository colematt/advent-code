#!/usr/bin/env python3

from aocd import data, submit
from itertools import permutations
from icecream import ic

testdata="""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

def solveA(data:str, lookback:int) -> int:
    # Read in the numbers
    numbers = [int(n) for n in data.splitlines()]
    invalid = None

    # Find the first number in numbers that is not the sum of two integers in 
    # the lookback window
    for i in range(lookback,len(numbers)):
        window = numbers[i-lookback:i]
        if numbers[i] in set(x+y for x,y in permutations(window,2)):
            continue
        else:
            invalid = numbers[i]
            break
    
    if invalid:
        return invalid
    else:
        raise ValueError("invalid number not found")
    
def allSlices(iterable):
	for start,stop in permutations(range(len(iterable)),2):
		yield iterable[start:stop]

def solveB(data:str, lookback:int) -> int:
    # Read in the numbers
    numbers = [int(n) for n in data.splitlines()]
    invalid = None
    
    # Find the first number in numbers that is not the sum of two integers in 
    # the lookback window
    for i in range(lookback,len(numbers)):
        window = numbers[i-lookback:i]
        if numbers[i] in set(x+y for x,y in permutations(window,2)):
            continue
        else:
            invalid = numbers[i]
            break
    if not invalid:
        raise ValueError("Invalid number not found")
    
    # Find the encryption weakness
    weakness = [sl for sl in allSlices(numbers) if sum(sl) == invalid and len(sl) >= 2]
    if len(weakness) > 1:
        raise ValueError("Multiple weaknesses found!")
    else:
        return min(*weakness) + max(*weakness) # pyright: ignore[reportReturnType]

if __name__ == "__main__":
    assert solveA(testdata,5) == 127
    submit(str(solveA(data,25)), part='a')
    assert(solveB(testdata,5) == 62)
    submit(str(solveB(data,25)), part='b')