#!/usr/bin/python3

import typing
import string
import re

def parseRule(rule):
	head, tail = tuple(bag for bag in 
		re.split(r'\s*contains?\s*',rule.strip(string.punctuation+string.whitespace)))
	outer = re.match(r'(\w+ \w+) bags',head).group(1)
	if tail == "no other bags":
		inner = tuple()
	else:
		inner = tuple(i.group(2) for i in 
			re.finditer(r'(\d) (\w+ \w+) bags?',tail))
	return(outer,inner)


assert parseRule('light red bags contain 1 bright white bag, 2 muted yellow bags.') \
	== ('light red',('bright white','muted yellow'))
assert parseRule('dotted black bags contain no other bags.') \
	== ('dotted black', tuple())

def traverse(graph,curr,leaf):
	if curr == leaf:
		return 1
	elif graph[curr] == tuple():
		return 0
	else:
		return max(traverse(graph,node,leaf) for node in graph[curr])

def main():
	with open('inputs/input7.test.txt') as fin:
		rules = [parseRule(line) for line in fin.readlines()]
		graph = {key:value for key,value in rules}
		# Part 1. We subtract one because a shiny gold bag by itself
		# doesn't count
		assert sum(traverse(graph,key,'shiny gold') for key in graph) - 1 == 4

	with open('inputs/input7.txt') as fin:
		rules = [parseRule(line) for line in fin.readlines()]
		graph = {key:value for key,value in rules}
		# Part 1. We subtract one because a shiny gold bag by itself
		# doesn't count
		print(sum(traverse(graph,key,'shiny gold') for key in graph) - 1)
		
if __name__ == '__main__':
	main()
