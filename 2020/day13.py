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
		# Solve using wolfram:
		# Reduce[{17 a == t, -11 + 37 b == t, -17 + 449 c == t, -25 + 23 d == t, -30 + 13 f == t, -36 + 19 g == t, -48 + 607 h == t, -58 + 41 j == t, -77 + 29 k == t}, {a, b, c, d, f, g, h, j, k, t}, Integers]
		# := {{a == 42657009605014 + 68115100234519 C[1], b == 19599166575277 + 31296127134779 C[1], c == 1615076087495 + 2578968160327 C[1], d == 31529094055881 + 50345943651601 C[1], f == 55782243329636 + 89073592614371 C[1], g == 38166798067646 + 60945089683517 C[1], h == 1194677369498 + 1907671670489 C[1], j == 17687052763056 + 28242846438703 C[1], k == 25005833216735 + 39929541516787 C[1], t == 725169163285238 + 1157956703986823 C[1], Element[C[1], Integers]}}
		# Since t == 725169163285238 + 1157956703986823 C[1], and C[1]== 0 is the first integral solution,
		# The answer is 725169163285238 
		print(earliest(schedule))
		
if __name__ == "__main__":
#	test()
	main()
	