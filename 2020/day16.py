#!/usr/bin/env python3

import itertools
import re

"""
$0: Entire rule
$1: Field name
$2, $3: first range low/hi
$4, $5: second range low/hi
"""
rule_re = re.compile(r'(.*): (\d+)-(\d+) or (\d+)-(\d+)')

"""
$0: Entire ticket
$1: Last field
"""
ticket_re = re.compile(r'(\d{1,3},?)+')

def isValid(ticket, valids):
	"""
	Return whether a particular ticket can be validated against valids
	"""
	return all(int(val) in valids for val in ticket)

def getInvalids(ticket, valids):
	return list(itertools.filterfalse(lambda val: int(val) in valids, ticket))

def test():
	with open('inputs/input16-test.txt', 'r') as fin:
		lines = [line.rstrip() for line in fin.readlines()]
		
	# Read rules out of input file. A rule is a tuple consisting of:
	# [0]: the field name
	# [1]: an itertools chain object containing all valid values
	rules = [(rule[0], itertools.chain(range(int(rule[1]),int(rule[2])+1), range(int(rule[3]),int(rule[4])+1)))
		for rule in [match.groups() 
			for match in filter(lambda x: x, 
								(rule_re.match(line) for line in lines))]]
	
	# Construct the set of all valid values from all rules
	chains = itertools.chain(frozenset(r[1]) for r in rules)
	allvalids = frozenset.union(*chains)
	
	# Read tickets out of input file
	# tickets[0] is always "your ticket"
	# tickets[1:] are "nearby tickets"
	tickets = [match.group().split(',') for match in filter(lambda x: x, (ticket_re.match(line) for line in lines))]
	
	#### PART 1 ####
	errors = [int(x) for x in itertools.chain.from_iterable([getInvalids(ticket, allvalids) for ticket in tickets[1:]])]
	assert sum(errors) == 71
	
	#### PART 2 ####
	pass
		
def main():
	with open('inputs/input16.txt', 'r') as fin:
		lines = [line.rstrip() for line in fin.readlines()]
		
	# Read rules out of input file. A rule is a tuple consisting of:
	# [0]: the field name
	# [1]: an itertools chain object containing all valid values
	rules = [(rule[0], itertools.chain(range(int(rule[1]),int(rule[2])+1), range(int(rule[3]),int(rule[4])+1)))
		for rule in [match.groups() 
			for match in filter(lambda x: x, 
								(rule_re.match(line) for line in lines))]]
	
	# Construct the set of all valid values from all rules
	chains = itertools.chain(frozenset(r[1]) for r in rules)
	allvalids = frozenset.union(*chains)
	
	# Read tickets out of input file
	# tickets[0] is always "your ticket"
	# tickets[1:] are "nearby tickets"
	tickets = [match.group().split(',') for match in filter(lambda x: x, (ticket_re.match(line) for line in lines))]
	
	#### PART 1 ####
	errors = [int(x) for x in itertools.chain.from_iterable([getInvalids(ticket, allvalids) for ticket in tickets[1:]])]
	print(sum(errors))
	
	#### PART 2 ####
	pass

if __name__ == "__main__":
	test()
	main()
	