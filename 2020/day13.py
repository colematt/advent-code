#!/usr/bin/env python3

import functools
import itertools
import math
import operator

def prod(sequence, start=1):
	return functools.reduce(operator.mul, sequence, start)

def wait(bus, timestamp):
	"""
	Return the wait in minutes for a bus given a timestamp
	"""
	return (bus - (timestamp % bus)) % bus

def minwait(buses, timestamp):
	"""
	Return the next bus out of buses and its wait in minutes from timestamp 
	as a 2-tuple.
	"""
	waits = [(bus, wait(bus,timestamp)) for bus in buses]
	return min(waits, key= lambda w:w[1])

def earliest(schedule):
	"""
	Find the earliest timestamp where all buses in the schedule will leave in
	a number of minutes equal to their zero-based offset in the list.
	The schedule contains commas and "don't cares" ('x') but no whitespace.
	"""
	# Process the buses from the schedule
	buses = [tuple(int(x) for x in b) 
		for b in itertools.filterfalse(
			lambda b: b[1] == 'x', enumerate(schedule.split(',')))]
	
	# Find the bus with the longest roundtrip (maxbus),
	# and set up a generator of timestamps (ts) at the correct wait time
	maxbus = max(buses, key=lambda b:b[1]) 
	ts = itertools.count(maxbus[1] - maxbus[0], maxbus[1])
	t = next(ts)
	
	# Generate timestamps until a suitable one is found
	while any(wait(bus, t) != offset for offset,bus in buses):
		t = next(ts)
	return t
	
def test():
	timestamp = 939
	schedules = ['7,13,x,x,59,x,31,19',
				'17,x,13,19',
				'67,7,59,61',
				'67,x,7,59,61',
				'67,7,x,59,61',
				'1789,37,47,1889']
	matches = [1068781,3417,754018,779210,1261476,1202161486]
	
	#### PART 1 ####
	schedule = schedules[0].split(',')
	buses = [int(bus) for bus in itertools.filterfalse(lambda b: b=='x', schedule)]
	assert minwait(buses,timestamp) == (59,5)
	assert prod(minwait(buses,timestamp)) == 295
	
	#### PART 2 ####
	for schedule,match in zip(schedules,matches):
		assert earliest(schedule) == match

def main(): 
	with open('inputs/input13.txt', 'r') as fin:
		timestamp = int(fin.readline())
		schedule = fin.readline().strip()
		
		#### PART 1 ####
		buses = [int(bus) for _,bus in 
			itertools.filterfalse(lambda b: b[1]=='x', 
				list(enumerate(schedule.split(','))))]
		print(prod(minwait(buses,timestamp)))
		
		#### PART 2 ####
		print(earliest(schedule))
		
if __name__ == "__main__":
#	test()
	main()
	