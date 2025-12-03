#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
from DataStructures.AbstractDataStructures import Graph

testdata = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
"""

def parse(s:str) -> tuple[str,str,int]:
    cities,_,dist = s.partition(' = ')
    start,_,finish = cities.partition(' to ')
    return (start,finish,int(dist))


def solveA(data:str) -> int | None:
    # Parse the input into a graph
    lines = tuple(line for line in data.splitlines())
    cities = set(city for city,_,_ in [parse(line) for line in lines]).union(
        set(city for _,city,_ in [parse(line) for line in lines]))
    graph = Graph(elements_type=str, weighted=True, initial_edges_size=len(cities))
    for node in cities:
        graph.add_node(node)
    for n1,n2,weight in tuple(parse(line) for line in lines):
        graph.add_edge(n1,n2,weight)
    
    ic(graph.nodes())

if __name__ == "__main__":
    solveA(testdata)