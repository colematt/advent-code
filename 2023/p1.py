#!/usr/bin/python3

import aocd
import re
from icecream import ic
ic.disable()

digitpattern = re.compile('(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))')
digitvalues = {
	'one':1,
	'two':2,
	'three':3,
	'four':4,
	'five':5,
	'six':6,
	'seven':7,
	'eight':8,
	'nine':9,
	'zero':0,
	'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0
}

testdata = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

testdata2="""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

def test():
	lines = [line for line in testdata.split("\n")]
	digits = [tuple(int(i) for i in filter(str.isdigit, line)) for line in lines]
	values = [10*t[0] + t[-1] for t in digits]
	assert sum(values) == 142

	lines = [line for line in testdata2.split("\n")]
	finds = [tuple(digitpattern.findall(line)) for line in lines]
	ic(finds)
	digits = [tuple(digitvalues[i] for i in tup) for tup in finds]
	values = [10*tup[0] + tup[-1] for tup in digits]
	ic(list(zip(lines,values)))
	assert sum(values) == 281

def main():
	lines = [line for line in aocd.data.split("\n")]
	digits = [tuple(int(i) for i in filter(str.isdigit, line)) for line in lines]
	values = [10*t[0] + t[-1] for t in digits]
	aocd.submit(sum(values),year=2023,day=1,part="a")

	finds = [tuple(digitpattern.findall(line)) for line in lines]
	ic(finds)
	digits = [tuple(digitvalues[i] for i in tup) for tup in finds]
	values = [10*tup[0] + tup[-1] for tup in digits]
	ic(list(zip(lines,values)))
	aocd.submit(sum(values),year=2023,day=1,part="b")

if __name__ == '__main__':
	test()
	main()