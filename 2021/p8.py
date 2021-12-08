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

DIGITS = {
	0 : 'abcefg', 	#6
	1 : 'cf',		#2 unique
	2 : 'acdeg',	#5
	3 : 'acdfg',	#5
	4 : 'bcdf',		#4 unique
	5 : 'abdfg',	#5
	6 : 'abdefg',	#6
	7 : 'acf',		#3 unique
	8 : 'abcdefg',	#7 unique
	9 : 'abcdfg',	#6
}
INV_DIGITS = {DIGITS[key]:key for key in DIGITS}

def test():
	lines = TEST_DATA.splitlines()
	entries = tuple((patterns.rstrip().split(),value.lstrip().split()) 
		for patterns,value in [line.split('|') for line in lines])
	ic(entries)

	### PART A ###
	filtered = [list(filter(lambda v: len(v) in {2,3,4,7},value)) for _,value in entries]
	ic(filtered)
	assert sum([len(f) for f in filtered]) == 26

def main():
	ic.disable()

	lines = aocd.data.splitlines()
	entries = tuple((patterns.rstrip().split(),value.lstrip().split()) 
		for patterns,value in [line.split('|') for line in lines])

	### PART A ###
	filtered = [list(filter(lambda v: len(v) in {2,3,4,7},value)) for _,value in entries]
	aocd.submit(sum([len(f) for f in filtered]), part="a")

if __name__ == '__main__':
	test()
	main()