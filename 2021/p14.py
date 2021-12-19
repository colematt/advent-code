#!/usr/bin/python3

import aocd
from collections import Counter
from functools import lru_cache
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
	poly,rules = data.split("\n\n")
	poly = list(poly)
	rules = {tuple(lhs):rhs for lhs,rhs in 
		[rule.split(' -> ') for rule in rules.splitlines()]}
	return poly,rules

def expand(poly,rules):
	for i in range(len(poly)-1,0,-1):
		if (poly[i-1],poly[i]) in rules:
			poly.insert(i,rules[(poly[i-1],poly[i])])

def test():
	poly,rules = parse(TESTDATA)
	for step in range(10):
		expand(poly,rules)
	assert len(poly) == 3073
	most,*others,least = Counter(poly).most_common()
	assert most == ('B',1749)
	assert least == ('H',161)
	assert most[1] - least[1] == 1588
	
def main():
	poly,rules = parse(aocd.data)
	
	### PART A ###
	for step in range(10):
		expand(poly,rules)
	most,*others,least = Counter(poly).most_common()
	aocd.submit(most[1] - least[1], part='a')

if __name__ == '__main__':
	test()
	main()
