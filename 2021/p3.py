#!/usr/bin/python3

import aocd
from icecream import ic
from collections import Counter

TEST_INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

# We have to override most_common, since it orders by first found, 
# not "prefer 1"
def most_common(counter):
	if counter['1'] == counter['0']:
		return '1'
	else:
		return counter.most_common(1)[0][0]

# We have to implement least_common since collections.Counter doesn't
def least_common(counter):
	if counter['0'] == counter['1']:
		return '0'
	else:
		return counter.most_common()[-1][0]

def power_consumption(lines):
	ziplines = list(zip(*lines))

	# For each zipline, calculate the most common bit
	mcb = [most_common(Counter(zl)) for zl in ziplines]
	lcb = [least_common(Counter(zl)) for zl in ziplines]

	gamma = int("".join(mcb),2)
	epsilon = int("".join(lcb),2)

	return epsilon*gamma

def life_support(lines):
	# Filter O2 values by most common value at bit
	# Determine the oxygen generator rating
	o2values = [tuple(line) for line in lines]
	bit = 0
	while(len(o2values) > 1):
		ziplines = list(zip(*o2values))
		mcb = [most_common(Counter(zl)) for zl in ziplines][bit]
		o2values = list(filter(lambda val: val[bit] == mcb, o2values))
		bit += 1
	generator = int("".join(o2values[0]),2)

	# Filter CO2 values by most common value at bit
	# Determine the oxygen generator rating
	co2values = [tuple(line) for line in lines]
	bit = 0
	while(len(co2values) > 1):
		ziplines = list(zip(*co2values))
		mcb = [least_common(Counter(zl)) for zl in ziplines][bit]
		co2values = list(filter(lambda val: val[bit] == mcb, co2values))
		bit += 1
	scrubber = int("".join(co2values[0]),2)

	return generator * scrubber

def test():
	lines = [tuple(line) for line in TEST_INPUT.splitlines()]
	assert(power_consumption(lines) == 198)
	assert(life_support(lines) == 230)

def main():
	lines = aocd.lines
	aocd.submit(power_consumption(lines), year=2021, day=3, part='a')
	aocd.submit(life_support(lines), year=2021, day=3, part='b')

if __name__ == '__main__':
	test()
	main()