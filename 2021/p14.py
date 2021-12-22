#!/usr/bin/python3

import aocd
from collections import Counter
from functools import cache
from icecream import ic

TESTDATA = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

def parse(data):
    template,_,*rules = data.splitlines()
    rules = {k: v for k, v in (rule.split(" -> ") for rule in rules)}
    return template, rules

def polymerize(template, rules, steps):
    @cache
    def count(pair, step):
        if step == steps or pair not in rules:
            return Counter()
        step += 1
        new_element = rules[pair]
        new_counter = Counter(new_element)
        new_counter.update(count(pair[0] + new_element, step))
        new_counter.update(count(new_element + pair[1], step))
        return new_counter

    counter = Counter(template)
    for left, right in zip(template, template[1:]):
        counter.update(count(left + right, 0))
    return counter

def subtract(counter):
    most,*others,least = counter.most_common()
    return most[1] - least[1]

def solveA(template, rules):
    return subtract(polymerize(template, rules, 10))

def solveB(template, rules):
    return subtract(polymerize(template, rules, 40))

def test():
	template,rules = parse(TESTDATA)
	assert solveA(template,rules) == 1588
	assert solveB(template,rules) == 2188189693529
	
def main():
	template,rules = parse(aocd.data)
	aocd.submit(solveA(template,rules),part='a')
	aocd.submit(solveB(template,rules),part='b')
	
if __name__ == '__main__':
	test()
	main()
