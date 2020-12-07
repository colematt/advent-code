#!/usr/bin/python3

import string
import re
import operator

def parseRule(rule):
	head, tail = tuple(bag for bag in 
		re.split(r'\s*contains?\s*',rule.strip(string.punctuation+string.whitespace)))
	outer = re.match(r'(\w+ \w+) bags',head).group(1)
	if tail == "no other bags":
		inner = (0,''),
	else:
		inner = tuple((int(i.group(1)),i.group(2)) for i in 
			re.finditer(r'(\d) (\w+ \w+) bags?',tail))
	return(outer,inner)

assert parseRule('light red bags contain 1 bright white bag, 2 muted yellow bags.') \
== ('light red',((1,'bright white'),(2,'muted yellow')))
assert parseRule('dotted black bags contain no other bags.') \
== ('dotted black', ((0,''),))

# Useful getters for the rule value-tuples
count = operator.itemgetter(0)
color = operator.itemgetter(1)

def traverse(graph,curr,leaf):
	if curr == leaf:
		return True
	elif curr == '':
		return False
	else:
		return any(traverse(graph,node,leaf) for node in graph[curr])

def traverse2(graph,curr):
	if curr == '':
		return 0
	else:
		return 1 + sum(list(next[0]*traverse2(graph,next[1]) for next in graph[curr]))

def main():

	with open('inputs/input7-test.txt') as fin:
		rules = [parseRule(line) for line in fin.readlines()]
		graph = {key:tuple(map(color,values)) for key,values in rules}
		assert sum(traverse(graph,key,'shiny gold') for key in graph) - 1 == 4
		graph = {key:value for key,value in rules}
		assert traverse2(graph,'shiny gold') - 1 == 32

	with open('inputs/input7-test2.txt') as fin:
		rules = [parseRule(line) for line in fin.readlines()]
		graph = {key:value for key,value in rules}
		assert traverse2(graph,'shiny gold') - 1 == 126

	with open('inputs/input7.txt') as fin:
		rules = [parseRule(line) for line in fin.readlines()]
		graph = {key:tuple(map(color,values)) for key,values in rules}
		# Part 1: We subtract one because a shiny gold bag by itself doesn't count
		print(sum(traverse(graph,key,'shiny gold') for key in graph) - 1)
		# Part 2: We subtract one because we don't count the shiny gold bag itself
		graph = {key:value for key,value in rules}
		print(traverse2(graph,'shiny gold') - 1)

if __name__ == '__main__':
	main()
