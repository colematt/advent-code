#!/usr/bin/env python3

import itertools
import math
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

def parse(filename):
	with open(filename, 'r') as fin:
		lines = [line.rstrip() for line in fin.readlines()]
		
		# Read rules out of input file. A rule is a dictionary entry of:
		#     key: the field name
		#     value: a set of valid values
		rules = dict()
		for match in filter(lambda x: x, (rule_re.match(line) for line in lines)):
			field = match.groups()[0]
			v1, v2, v3, v4 = (int(v) for v in match.groups()[1:])
			rules[field] = set(range(v1, v2+1)) | set(range(v3, v4+1))
			
		# Read tickets out of input file
		# tickets[0] is always "your ticket"
		# tickets[1:] are "nearby tickets"
		tickets = [[int(x) for x in match.group().split(',')] 
			for match in filter(lambda x: x, (ticket_re.match(line) for line in lines))]
		
	return rules, tickets

def isValidTicket(ticket, valids):
	"""
	Return whether a particular ticket can be validated against valids
	"""
	return all(val in valids for val in ticket)

def getInvalids(ticket, valids):
	"""
	Return a list of all values in ticket which cannot be valid.
	"""
	return list(itertools.filterfalse(lambda val: val in valids, ticket))

def validate(rules, key, value):
	return value in rules[key]

def solve(rules, tickets):
	# For each field name, get the positions in which that field name can 
	# validate for all valid tickets.
	unsolved = dict()
	for field in rules.keys():
		valids = set()
		for i in range(len(tickets[0])):
				if all([validate(rules, field, ticket[i]) for ticket in tickets]):
					valids.add(i)
		unsolved[field]= valids
		
	# Solve for each field's position while there are still unsolved fields
	solved = dict()
	tried = dict()
	while True:
		# Destructively consume unsolved,
		# Placing the contents in either solved or tried
		while unsolved:
			key,val = unsolved.popitem()
			# This item is solved!
			if len(val) == 1:
				val = val.pop()
				for us in unsolved:
					unsolved[us].discard(val)
				for t in tried:
					tried[t].discard(val)
				solved[key] = val
			# This item can't be solved, put it in the tried bin for next loop
			else:
				#TODO
				tried[key] = val
		# If elements remain in tried, try again
		if tried:
			unsolved = tried
			tried = dict()
		else:
			break
	return solved	
	

def test():
	#### PART 1 ####
	rules, tickets = parse('inputs/input16-test.txt')
	allvalids = frozenset(itertools.chain.from_iterable(rules.values()))
	errors = list(itertools.chain.from_iterable([getInvalids(ticket, allvalids) for ticket in tickets[1:]]))
	assert sum(errors) == 71
	
	#### PART 2 ####
	rules, tickets = parse('inputs/input16-test2.txt')
	allvalids = frozenset(itertools.chain.from_iterable(rules.values()))

	# Filter invalid tickets
	tickets = list(filter(lambda t: isValidTicket(t, allvalids), tickets))
	assert tickets == [[11, 12, 13], [3, 9, 18], [15, 1, 5], [5, 14, 9]]
	
	# Solve field to index mapping
	fieldmap = solve(rules, tickets)
	assert fieldmap == {'row': 0, 'class': 1, 'seat': 2}
	
			
def main():
	rules, tickets = parse('inputs/input16.txt')
	
	#### PART 1 ####
	allvalids = frozenset(itertools.chain.from_iterable(rules.values()))
	errors = list(itertools.chain.from_iterable([getInvalids(ticket, allvalids) for ticket in tickets[1:]]))
	print(sum(errors))
	
	#### PART 2 ####
	allvalids = frozenset(itertools.chain.from_iterable(rules.values()))
	
	# Filter invalid tickets
	tickets = list(filter(lambda t: isValidTicket(t, allvalids), tickets))
	
	# Solve field to index mapping
	fieldmap = solve(rules, tickets) 
	
	# Get product of departure fields
#	for key in fieldmap:
#		print(key)
	print(math.prod(tickets[0][fieldmap[k]] for k in fieldmap if k[:9] == 'departure')) 

if __name__ == "__main__":
#	test()
	main()
	