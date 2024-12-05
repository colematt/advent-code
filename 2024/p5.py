#!/usr/bin/env python3

from aocd import data, submit
from collections import defaultdict
from functools import cmp_to_key
from icecream import ic

testdata = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

ORDERINGS = defaultdict(list)

def canonicalize(data):
    rules, updates = data.split("\n\n")
    rules = tuple(tuple(int(n) for n in rule.split("|")) for rule in rules.splitlines())
    updates = [[int(n) for n in line.split(",")] for line in updates.splitlines()]
    return rules,updates


def validate(rule,update):
    left, right = rule
    if (not left in update) or (not right in update):
        return True
    else:
        return update.index(left) < update.index(right)
    

def solveA(data):
    rules,updates = canonicalize(data)
    correct = [update for update in updates if all(validate(rule,update) for rule in rules)]
    return sum(update[len(update)//2] for update in correct)


def solveB(data):
    rules,updates = canonicalize(data)
    for k,v in rules:
        ORDERINGS[k].append(v)
    incorrect = [update for update in updates if not all(validate(rule,update) 
                                                         for rule in rules)]
    incorrect = [sorted(update, key=cmp_to_key(lambda x,y: 1-2*((x,y) in rules))) 
                 for update in incorrect]
    return sum([update[len(update)//2] for update in incorrect])


if __name__ == "__main__":
    assert solveA(testdata) == 143
    submit(solveA(data),part='a')

    assert solveB(testdata) == 123
    # ic(solveB(data))
    submit(solveB(data), part='b')
    