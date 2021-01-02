#!/usr/bin/python3

import aocd
import collections
from icecream import ic
import itertools
import math
import typing

def rotate_to_head(deque:typing.Deque, x:typing.Any) -> None:
	"""
	Rotate a deque inplace until value is at the head/left position
	
	:param      deque:       the deque
	:type       deque:       typing.Deque
	:param      value:       the value within the deque
	:type       value:       typing.Any
	
	:returns:   { no return value; deque is rotated in place }
	:rtype:     None
	
	:raises     ValueError:  { value is not in deque }
	"""
	try:
		i = deque.index(x)
	except ValueError:
		raise ValueError("%s not found in %s" % (str(x), repr(deque))) 
	
	if i <= len(deque) // 2:
		deque.rotate(-i)
	else:
		i = len(deque) - i
		deque.rotate(i)

def rotate_to_tail(deque:typing.Deque, x:typing.Any) -> None:
	"""
	Rotate a deque inplace until value is at the tail/right position
	
	:param      deque:       the deque
	:type       deque:       typing.Deque
	:param      value:       the value within the deque
	:type       value:       typing.Any
	
	:returns:   { no return value; deque is rotated in place }
	:rtype:     None
	
	:raises     ValueError:  { value is not in deque }
	"""
	try:
		i = deque.index(x)
	except ValueError:
		raise ValueError("%s not found in %s" % (str(x), repr(deque))) 
	
	if i >= len(deque) // 2:
		i = len(deque) - i
		deque.rotate(i-1)
	else:
		deque.rotate(-i-1)

def canonical(cups:typing.Deque) -> str:
	rotate_to_head(cups,1)
	return "".join(str(cup) for cup in list(cups)[1:])

def move(cups):
	"""
	{ Perform one move of the cups by crab's rules.
	  "Current" is assumed to be at left side of 
	  the deque at function call.}
	
	:param      cups:  The cups
	:type       cups:  Typing.deque
	"""
	# Save icecream state?
	restore = ic.enabled
	ic.disable()

	# Get current cup
	current = cups[0]
	ic(cups)
	ic(current)

	# Rotate the current cup to tail, pop the pickup cups
	cups.rotate(-1)
	pickup = (cups.popleft(), cups.popleft(), cups.popleft())
	ic(pickup)

	# Get destination cup,
	destination = current - 1
	if destination < min(cups): destination = max(cups)
	while destination in pickup:
		destination -= 1
		if destination < min(cups): destination = max(cups)
	ic(destination)
	
	# Rotate cups until destination is at tail
	rotate_to_tail(cups, destination)

	# Insert slice at tail 
	cups.extend(pickup)

	# Rotate cups so that the old current cup is at tail,
	# placing the new current cup at head
	rotate_to_tail(cups, current)

	# Restore icecream state?
	if restore:
		ic.enable()

def test():

	#### PART A ####
	data = "389125467"
	cups = collections.deque([int(n) for n in data])
	
	# Perform the specified moves
	for m in range(100):
		move(cups)

	# Read the cups' canonical value
	assert canonical(cups) == "67384529"

def main():
	data = aocd.get_data(year=2020, day=23)
	cups = collections.deque([int(n) for n in data])
	
	#### PART A ####
	# Perform the specified moves
	for m in range(100):
		move(cups)

	# Read the cups' canonical value
	aocd.submit(canonical(cups), year=2020, day=23, part='a')

if __name__ == '__main__':
	test()
	main()