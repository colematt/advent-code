#!/usr/bin/python3

import string
import re
import operator
from aocd import data, submit
from icecream import ic

testdata_a = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

testdata_b = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

# Useful getters for the rule value-tuples
count = operator.itemgetter(0)
color = operator.itemgetter(1)

def parseRule(rule):
    head, tail = tuple(bag for bag in 
        re.split(r'\s*contains?\s*',rule.strip(string.punctuation+string.whitespace)))
    outer = re.match(r'(\w+ \w+) bags',head).group(1) # pyright: ignore[reportOptionalMemberAccess]
    if tail == "no other bags":
        inner = (0,''),
    else:
        inner = tuple((int(i.group(1)),i.group(2)) for i in 
            re.finditer(r'(\d) (\w+ \w+) bags?',tail))
    return(outer,inner)


def traverseA(graph,curr,leaf):
    if curr == leaf:
        return True
    elif curr == '':
        return False
    else:
        return any(traverseA(graph,node,leaf) for node in graph[curr])


def solveA(data:str) -> int:
    rules = [parseRule(line) for line in data.splitlines()]
    graph = {key:tuple(map(color,values)) for key,values in rules}
    return sum(traverseA(graph,key,'shiny gold') for key in graph) - 1


def traverseB(graph,curr):
    if curr == '':
        return 0
    else:
        return 1 + sum(list(next[0]*traverseB(graph,next[1]) for next in graph[curr]))
    

def solveB(data:str) -> int:
    rules = [parseRule(line) for line in data.splitlines()]
    graph = {key:value for key,value in rules}
    return traverseB(graph,'shiny gold') - 1


if __name__ == "__main__":
    assert(solveA(testdata_a) == 4)
    submit(str(solveA(data)), part='a')
    assert(solveB(testdata_b) == 126)
    submit(str(solveB(data)), part='b')