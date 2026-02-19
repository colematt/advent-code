#!/usr/bin/python3

import operator
from aocd import data,submit

# Returns the Manhattan distance between two points expressed 
# as two-dimensional sequence type (usually a tuple)
distance = lambda a,b: abs(a[0]-b[0]) + abs(a[1]-b[1])
assert distance((0,0),(3,5)) == 8

# Add two tuples together element-wise
tupadd = lambda a,b: tuple(map(operator.add,a,b))
assert tupadd((1,-1),(3,5)) == (4,4)

def convert(s):
    """
    Convert a vector string into a 2-tuple vector
    """
    direction,distance = s[0],int(s[1:])
    if direction == 'L':
        return ((-1,0),distance)
    elif direction == 'R':
        return ((1,0), distance)
    elif direction == 'D':
        return ((0,-1), distance)
    elif direction == 'U':
        return ((0,1), distance)
    else:
        raise ValueError("Unknown direction %s" % direction)
    
def solveA(data:str) -> int:
    # Read inputs
    vs1 = [convert(v) for v in data.splitlines()[0].rstrip('\n').split(',')]
    vs2 = [convert(v) for v in data.splitlines()[1].rstrip('\n').split(',')]

    # Trace wires. Each wire starts at origin.
    w1 = [(0,0)]
    # For each vector, add the next point to the wire list, until remaining
    # distance to add in that direction is zero.
    for v in vs1:
        tup, dist = v
        while dist > 0:
            w1.append(tupadd(w1[-1], tup))
            dist -= 1
    # Repeat for wire 2.
    w2 = [(0,0)]
    for v in vs2:
        tup, dist = v
        while dist > 0:
            w2.append(tupadd(w2[-1], tup))
            dist -= 1
    
    # Find the set of all intersections of the wires
    intersections = [w for w in (set(w1) & set(w2)) - {(0,0)}]

    # Find the distance to the closest intersection
    return min(map(lambda i: distance(i,(0,0)), intersections))

def solveB(data:str) -> int:
    # Read inputs
    vs1 = [convert(v) for v in data.splitlines()[0].rstrip('\n').split(',')]
    vs2 = [convert(v) for v in data.splitlines()[1].rstrip('\n').split(',')]

    # Trace wires. Each wire starts at origin.
    w1 = [(0,0)]
    # For each vector, add the next point to the wire list, until remaining
    # distance to add in that direction is zero.
    for v in vs1:
        tup, dist = v
        while dist > 0:
            w1.append(tupadd(w1[-1], tup))
            dist -= 1
    # Repeat for wire 2.
    w2 = [(0,0)]
    for v in vs2:
        tup, dist = v
        while dist > 0:
            w2.append(tupadd(w2[-1], tup))
            dist -= 1
    
    # Find the set of all intersections of the wires
    intersections = [w for w in (set(w1) & set(w2)) - {(0,0)}]

    # Find combined wire distance for each intersection
    distances = [w1.index(i) + w2.index(i) for i in intersections]
    return min(distances)

testdata1 = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
"""
testdata2 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
"""

if __name__ == "__main__":
    assert solveA(testdata1) == 159
    assert solveA(testdata2) == 135
    submit(str(solveA(data)), part='a')
    assert solveB(testdata1) == 610
    assert solveB(testdata2) == 410
    submit(str(solveB(data)), part='b')