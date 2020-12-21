#!/usr/bin/env python3

import aocd
from icecream import ic
import re
import string

SYMBOLS = "ab()|"

"""
Non-terminating rule
$0 : entire rule string
$1 : key string
$2 : value string
"""
re_nonterm = r'^(\d+):((?: [\d+|\|]){1,5})$'

"""
Terminating rule
$0 : entire rule string
$1 : key string
$2 : value string
"""
re_term = r'^(\d+): .?([ab]+).?$'

"""
Message rule
$0 : message
"""
re_message = r'^[ab]+$'

def isTerminal(item):
	_,v = item
	return all(c in string.ascii_lowercase+'|' for c in "".join(v))

def make_terminals(rules):
	"""
	Given a list of rules, continue substituting from terminal rules into
	non-terminal rules until no non-terminal rules remain
	"""
	terminals = dict()
	
	while rules:
		# For each rule in rules
			# if rule is terminal, pop it from rules
			
			# Add it to the terminals
			
			# Reduce the non-terminals by replacement
		
	return terminals

def test():
	with open('test.txt', 'r') as fin:
		lines = [line for line in fin.readlines()]
	
	messages = [match.strip() 
		for match in filter(
			lambda x: re.match(re_message, x, flags=re.M), lines)]
	rules = {k.strip():[v.strip('"') for v in vs.split()] 
		for k,vs in [(match.split(':')) 
			for match in filter(
				lambda x: re.match(re_nonterm, x, flags=re.M) 
				or re.match(re_term, x, flags=re.M), lines)]}

	# Convert all rules into terminals
	ic(messages)
	ic(rules)
	make_terminals(rules)
	
def main():
	lines = aocd.get_data(day=19, year=2020).splitlines()

if __name__ == "__main__":
	test()
#	main()
	