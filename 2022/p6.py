#!/usr/bin/python3

import aocd
import typing
import itertools
import more_itertools

from icecream import ic
ic.enable()

testdata = (
	("bvwbjplbgvbhsrlpgdmjqwftvncz",5),
	("nppdvjthqldpwncqszvftbrmjlhg",6),
	("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",10),
	("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",11)
)

def find_start_buf(buffer:str) -> int:
	for index,window in enumerate(more_itertools.sliding_window(buffer,4)):
		if more_itertools.all_unique(window):
			return index+4

def find_start_msg(buffer:str) -> int:
	for index,window in enumerate(more_itertools.sliding_window(buffer,14)):
		if more_itertools.all_unique(window):
			return index+14

if __name__ == '__main__':
	for buffer,exp in testdata:
		assert(find_start_buf(buffer) == exp)
	aocd.submit(find_start_buf(aocd.data),part='a')
	aocd.submit(find_start_msg(aocd.data),part='b')