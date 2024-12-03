#!/usr/bin/env python3

from aocd import data, submit

testdata = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

def isMonotonic(seq):
	incr = decr = True
	for i in range(len(seq) - 1):
		if seq[i] < seq[i + 1]:
			decr = False
		if seq[i] > seq[i + 1]:
			incr = False
	return incr or decr

def isClamped(seq):
	for i in range(len(seq) - 1):
		if abs(seq[i] - seq[i+1]) > 3 or abs(seq[i] - seq[i+1]) < 1:
			return False
	return True

def isDampened(seq):
	if isMonotonic(seq) and isClamped(seq):
		return True
	else:
		for i in range(len(seq)):
			newseq = list(seq)
			del newseq[i]
			if isMonotonic(newseq) and isClamped(newseq):
				return True
		return False
	
def solveA(data):
	# Parse data into reports
	reports = [[int(n) for n in report.split()] for report in data.splitlines()]
	# Filter reports that aren't monotonic
	reports = list(filter(lambda rep: isMonotonic(rep), reports))
	# Filter reports that aren't clamped
	reports = list(filter(lambda rep: isClamped(rep), reports))
	return len(reports)

def solveB(data):
	# Parse data into reports
	reports = [[int(n) for n in rep.split()] for rep in data.splitlines()]
	# Filter reports that aren't safe (monotonic+clamped or dampened)
	reports = list(filter(lambda rep: isDampened(rep), reports))
	return len(reports)

if __name__ == "__main__":
	assert solveA(testdata) == 2
	submit(solveA(data), part='a')
	
	assert solveB(testdata) == 4
	submit(solveB(data), part='b')