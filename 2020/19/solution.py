#!/usr/bin/env python3

import aocd
from icecream import ic
import itertools

ic.disable()

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

def parse(text):
	"""
	Parse an input into rules and messages.
	"""
	rules, msglist = (group.splitlines() for group in text.split('\n\n'))
	ruledict = dict()
	for rule in rules:
		key, val = rule.split(':')
		# Process key into an integer
		key = int(key)

		# Process value. If value is terminal, add to dict as a string.
		# If value is non-terminal, add to dict as a resolvable list of key ints
		val = val.strip().replace("\"", "").split("|")
		if all(c in "ab" for c in val):
			ruledict[key] = val[0]
		else:
			ruledict[key] = [[int(i) for i in v.split()] for v in val]

	return ruledict,msglist

def resolve(rules,cache=dict(),key=0):
	"""
	Use recursive descent parsing to resolve rules, 
	forming a valid list of all inputs.
	"""
	# Case: rule has already been resolved
	if key in cache:
		return cache[key]
	# Case: rule is terminal
	elif isinstance(rule:= rules[key],str):
		cache[key] = rule
		return rule
	# Case: rule is non-terminal
	else:
		out = list()
		for choice in rule:
			rr = [resolve(rules,cache=cache,key=k) for k in choice]
			out.extend("".join(x) for x in itertools.product(*rr))
		cache[key] = out
		return out

def pump(rules, messages):
	"""
	Return the number of messages matching recursive rules after applying the 
	pumping theorem to resolve the recursion
	"""

	# Find keys that must be resolved by pumping
	pumpset = set()
	for key in rules:
		valset = set(itertools.chain.from_iterable(rules[key]))
		if key in valset:
			valset.remove(key)
			pumpset.update(valset)
	assert 31 in pumpset
	assert 42 in pumpset

	# Calculate the word length to chunk each message
	rule_cache = {}  # share the cache for both searches
	r_31 = set(resolve(rules, rule_cache, 31))
	r_42 = set(resolve(rules, rule_cache, 42))
	ic(r_31)
	ic(r_42)
	len_31 = {len(x) for x in r_31}
	len_42 = {len(x) for x in r_42}
	len_both = len_31 | len_42
	assert len(len_both) == 1
	word_len = len_both.pop()

	# Use pumping against chunks to count the number of valid messages
	valids = 0
	for m in messages:
		words = [m[0+i:word_len+i] for i in range(0, len(m), word_len)]
		n_words = len(words)

		n_31 = 0
		for word in reversed(words):
			if word in r_31:
				n_31 += 1
			else:
				break
		if 0 < n_31 < n_words/2 and all(word in r_42 for word in words[:-n_31]):
			valids += 1

	return valids

def test():
	
	#### PART A ####
	with open('test-a.txt', 'r') as fin:
		text = fin.read()
	rules, messages = parse(text)
	valids = set(resolve(rules, cache=dict()))
	assert sum(message in valids for message in messages) == 2

	#### PART B ####
	with open('test-b.txt', 'r') as fin:
		text = fin.read()
	rules, messages = parse(text)
	valids = set(resolve(rules, cache=dict()))
	assert sum(message in valids for message in messages) == 3

	# Update rules and pump (pump it real good)
	rules[8] = [[42], [42, 8]]
	rules[11] = [[42, 31], [42, 11, 31]]
	assert pump(rules, messages) == 12
	
def main():
	text = aocd.get_data(day=19, year=2020)

	#### PART A ####
	rules, messages = parse(text)
	valids = set(resolve(rules, cache=dict()))
	aocd.submit(sum(message in valids for message in messages), part="a", day=19, year=2020)

	#### PART B ####
	rules, messages = parse(text)
	rules[8] = [[42], [42, 8]]
	rules[11] = [[42, 31], [42, 11, 31]]
	aocd.submit(pump(rules, messages), part="b", day=19, year=2020)

if __name__ == "__main__":
	test()
	main()
	