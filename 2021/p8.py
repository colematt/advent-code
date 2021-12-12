#!/usr/bin/python3

import aocd
from icecream import ic

SINGLE_DATA = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
TEST_DATA = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

def entries(lines):
	return tuple((patterns.rstrip().split(),value.lstrip().split()) 
		for patterns,value in [line.split('|') for line in lines])

def solveA(entries):
	filtered = [list(
		filter(lambda v: len(v) in {2,3,4,7},value)) for _,value in entries]
	return sum([len(f) for f in filtered])

def solveB(entries):
	total = 0
	
	# split signal and output
	for signals,outputs in entries:
		# get number of segments
		l = {len(s): set(s) for s in signals}    

		# accumulate solved outputs
		n = ''

		for o in map(set, outputs):              # loop over output digits
			lo,lol4,lol2 = len(o), len(o&l[4]), len(o&l[2]) # mask with known digits
			if lo == 2: n += '1'
			elif lo == 3: n += '7'
			elif lo == 4: n += '4'
			elif lo == 7: n += '8'
			elif lo == 5 and lol4 == 2: n += '2'
			elif lo == 5 and lol4 == 3 and lol2 == 1: n += '5'
			elif lo == 5 and lol4 == 3 and lol2 == 2: n += '3'
			elif lo == 6 and lol4 == 4: n += '9'
			elif lo == 6 and lol4 == 3 and lol2 == 1: n += '6'
			elif lo == 6 and lol4 == 3 and lol2 == 2: n += '0'
			else: raise Error("Reached default case! %s" % o)

		# convert string to int
		n = int(n)
		ic(n)

		# accumulate total
		total += n
	return total

def test():
	lines = TEST_DATA.splitlines()
	assert solveA(entries(lines)) == 26
	assert solveB(entries(lines)) == 61229

def main():
	ic.disable()
	lines = aocd.data.splitlines()
	aocd.submit(solveA(entries(lines)), part="a")
	aocd.submit(solveB(entries(lines)), part="b")

if __name__ == '__main__':
	test()
	main()