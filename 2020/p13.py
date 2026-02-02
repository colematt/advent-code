#!/usr/bin/env python3

from aocd import data, submit
from functools import reduce
from itertools import filterfalse
from operator import mul
from sympy.ntheory.modular import crt

testdata = """939
7,13,x,x,59,x,31,19
"""

def prod(sequence, start=1):
    return reduce(mul, sequence, start)


def wait(bus, timestamp):
    """
    Return the wait in minutes for a bus given a timestamp
    """
    return (bus - (timestamp % bus)) % bus


def nextbus(buses, timestamp):
    """
    Return the next bus out of buses and its wait in minutes from timestamp 
    as a 2-tuple.
    """
    waits = [(bus, wait(bus,timestamp)) for bus in buses]
    return min(waits, key= lambda w:w[1])


def sync(schedule):
    """
    Find the earliest timestamp where all buses in the schedule will leave in
    a number of minutes equal to their zero-based offset in the list.
    The schedule contains commas and "don't cares" ('x') but no whitespace.
    """
    # Process the buses from the schedule in the form of 
    # buses = [(offset,busid), (offset,busid), ...(offset,busid)], which is
    # buses = [(v0,m0),(v1,m1), ... (vn,mn)]
    buses = [tuple(int(x) for x in b) 
        for b in filterfalse(
            lambda b: b[1] == 'x', enumerate(schedule.split(',')))]
    vs = [t[0] for t in buses]
    ms = [t[1] for t in buses]
    
    # Use CRT to get a (A,b) tuple. Use their difference to get timestamp t
    # We presume all bus IDs are coprime in order to accelerate computation
    try:
        a,b = crt(ms,vs,check=False) # pyright: ignore[reportGeneralTypeIssues]
        return int(b) - int(a)
    except:
        print("No CRT solution")
        exit(0)
    

def solveA(data:str) -> int:
    timestamp, schedule = int(data.splitlines()[0]), data.splitlines()[1].strip()
    buses = [int(bus) for _,bus in 
            filterfalse(lambda b: b[1]=='x', 
                list(enumerate(schedule.split(','))))]
    return prod(nextbus(buses,timestamp))


"""
Part B can also be solved directly using diophantine equations in Mathematica:
Reduce[{17 a == t, -11 + 37 b == t, -17 + 449 c == t, -25 + 23 d == t, 
    -30 + 13 f == t, -36 + 19 g == t, -48 + 607 h == t, -58 + 41 j == t, 
    -77 + 29 k == t}, {a, b, c, d, f, g, h, j, k, t}, Integers]
:= {{a == 42657009605014 + 68115100234519 C[1], 
    b == 19599166575277 + 31296127134779 C[1], 
    c == 1615076087495 + 2578968160327 C[1], 
    d == 31529094055881 + 50345943651601 C[1], 
    f == 55782243329636 + 89073592614371 C[1], 
    g == 38166798067646 + 60945089683517 C[1], 
    h == 1194677369498 + 1907671670489 C[1], 
    j == 17687052763056 + 28242846438703 C[1], 
    k == 25005833216735 + 39929541516787 C[1], 
    t == 725169163285238 + 1157956703986823 C[1], Element[C[1], Integers]}}
Since t == 725169163285238 + 1157956703986823 C[1], and C[1]== 0 is the first 
integral solution, the answer is 725169163285238 
"""

def solveB(data:str) -> int:
    timestamp, schedule = int(data.splitlines()[0]), data.splitlines()[1].strip()
    return sync(schedule)


if __name__ == "__main__":
    assert solveA(testdata) == 295
    submit(str(solveA(data)), part='a')
    assert solveB(testdata) == 1068781
    submit(str(solveB(data)), part='b')