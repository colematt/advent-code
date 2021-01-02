#!/usr/bin/python3

import aocd
import itertools
import math

def traverse(cups:dict, start:int=1):
	"""
	Traverse a circular linked list beginning at start
	
	:param      cups:   { Mapping of a circular linked list's node:next }
	:type       cups:   dict
	:param      start:  { Key of current cup within the linked list }
	:type       start:  int
	"""
	curr = start
	yield curr
	curr = cups[curr]

	while curr != start:
		yield curr
		curr = cups[curr]

cupsToStr = lambda c,s: " ".join(str(i) for i in traverse(c, start=int(s)))

def canonical(cups:dict) -> str:
	"""
	{ Return the canonical representation of circular linked list.
	  This consists of a clockwise traversal beginning at index 1.
	}

	:param      cups:  The cups
	:type       cups:  dict

	:returns:   { description_of_the_return_value }
	:rtype:     str
	"""
	return "".join(str(i) for i in itertools.takewhile(lambda x: x != 1, traverse(cups, start=cups[1])))

def move(cups:dict, curr:int, low:int, high:int) -> int:
	"""
	{ function_description }

	:param      cups:  { Mapping of a circular linked list's node:next }
	:type       cups:  dict
	:param      curr:  { Key of current cup within the linked list }
	:type       curr:  int

	:returns:   { The current cup for the next move }
	:rtype:     int
	"""
	# Display pre-move state if icecream is enabled
	# ic(cupsToStr(cups, curr))
	# ic(curr)

	# Pickup the three cups immediately clockwise of current
	# Update curr to point to last pickup cup's next
	pickup = (cups[curr], cups[cups[curr]], cups[cups[cups[curr]]])
	# ic(pickup)
	cups[curr] = cups[pickup[2]]

	# Select a destination cup
	# If this destination cup is in pickup, keep subtracting one
	# If this destination cup is less than min cup, wrap around to max cup
	dest = curr - 1
	if dest < low: dest = high
	while dest in pickup:
		dest -= 1
		if dest < low: dest = high
	# ic(dest)

	# Place the pickup cups immediately clockwise of destination cup
	temp = cups[dest]
	cups[dest] = pickup[0]
	cups[pickup[2]] = temp

	# Select the next current cup, return its value
	return cups[curr]

def test():

	#### PART A ####
	data = "389125467"
	cups = {int(c):int(n) for c,n in 
		itertools.zip_longest(data,data[1:],fillvalue=data[0])}
	curr = int(data[0])
	
	# Perform the specified moves
	for _ in range(1,11):
		curr = move(cups,curr,1,9)

	# Read the cups' canonical value
	assert canonical(cups) == "92658374"
	
	# Perform more specified moves
	for _ in range(11,101):
		curr = move(cups, curr,1,9)
	
	# Read the cups' canonical value
	assert canonical(cups) == "67384529"

	#### PART B ####
	cups = {int(c):int(n) for c,n in 
		itertools.zip_longest(data,data[1:],fillvalue=data[0])}
	cups.update({int(data[-1]):max(cups)+1, 1000000:int(data[0])})
	cups.update({i:i+1 for i in range(10,1000000)})
	curr = int(data[0])

	# Perform the specified moves
	for m in range(10000000):
		curr = move(cups,curr,1,1000000)

	# Read the star cups
	stars = cups[1], cups[cups[1]]
	assert math.prod(stars) == 149245887792

def main():
	data = aocd.get_data(year=2020, day=23)

	#### PART A ####
	cups = {int(c):int(n) for c,n in itertools.zip_longest(data,data[1:],fillvalue=data[0])}
	curr = int(data[0])
	
	# Perform the specified moves
	for _ in range(100):
		curr = move(cups, curr,1,9)
	
	# Read the cups' canonical value
	aocd.submit(canonical(cups), year=2020,day=23,part='a')

	#### PART B ####
	cups = {int(c):int(n) for c,n in itertools.zip_longest(data,data[1:],fillvalue=data[0])}
	cups.update({int(data[-1]):max(cups)+1, 1000000:int(data[0])})
	cups.update({i:i+1 for i in range(10,1000000)})
	curr = int(data[0])

	# Perform the specified moves
	for m in range(10000000):
		curr = move(cups,curr,1,1000000)

	# Read the star cups
	stars = cups[1], cups[cups[1]]
	aocd.submit(math.prod(stars),year=2020,day=23,part='b')

if __name__ == '__main__':
	test()
	main()
