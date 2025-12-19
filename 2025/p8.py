#!/usr/bin/env python3

from operator import attrgetter, itemgetter
from aocd import data, submit
from icecream import ic
from math import dist, prod

# Box is an enumeration of the box and its 3D coordinate
type Box = tuple[int,tuple[int,int,int]]
# Distance is the enumerator index of two boxes and their euclidean distance
type Distance = tuple[int,int,float]

testdata = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

def solveA(data: str, n:int) -> int:
    # Parse input data
    boxes:list[Box] = list(enumerate(eval(line) for line in data.splitlines()))
    dists:list[Distance] = list(sorted([(p,q,dist(boxes[p][1], boxes[q][1]))
             for p in range(len(boxes)) for q in range(len(boxes)) if p < q], key=itemgetter(2)))
    
    # Build a network of connected boxes
    network: list[set[int]] = list()
    for p,q,_ in dists[:n]:
        superset = set((p,q))
        for circuit in network:
            if p in circuit or q in circuit:
                superset |= circuit
                network.remove(circuit)
        network.append(superset)
    
    # Sort the network by lengths of circuits
    network = sorted(network, key=len, reverse=True)
    return prod(len(circuit) for circuit in network[:3])

def solveB(data:str) -> int:
    # Parse input data
    boxes:list[Box] = list(enumerate(eval(line) for line in data.splitlines()))
    dists:list[Distance] = list(sorted([(p,q,dist(boxes[p][1], boxes[q][1]))
             for p in range(len(boxes)) for q in range(len(boxes)) if p < q], key=itemgetter(2)))
    
    # Build a network of connected boxes
    network:list[set[int]] = list()
    for p,q,_ in dists:
        collected = set((p,q))
        worklist = network.copy()
        for circuit in worklist:
            if (p in circuit) or (q in circuit):
                collected |= circuit
                network.remove(circuit)
        network.insert(0,collected)

        # Stop adding lists as soon as there is a circuit of all boxes
        if len(network[0]) == len(boxes):
            return boxes[p][1][0] * boxes[q][1][0]
    
    return 0

if __name__ == "__main__":
    assert solveA(testdata,10) == 40
    submit(str(solveA(data,1000)), part='a')
    assert solveB(testdata) == 25272
    submit(str(solveB(data)), part='b')