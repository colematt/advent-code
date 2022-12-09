#!/usr/bin/python3

import aocd
import typing
from pathlib import Path

from icecream import ic
ic.enable()

testdata = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

def build(data:str) -> dict:
	pwd = Path('/')
	dirs = dict()
	lines = data.splitlines()

	# Process each line of terminal input/outpu
	for line in lines:
		# Process commands
		if line[0] == '$':
			_, cmd, *args = line.split()
			ic(cmd, args)
			# Process cd
			if cmd == "cd":
				if args[0] == '/': pwd = Path('/')
				elif args[0] == '.': pwd = pwd
				elif args[0] == '..': pwd = pwd.parent
				else: pwd = pwd.joinpath(args[0])
			# Process ls
			elif cmd == "ls":
				pass
			else:
				raise ValueError("Unidentified command: %s" % cmd)
		# Process outputs
		else:
			size,file = line.split()
			if size == "dir": 
				size = 0
			else:
				size = int(size)
			if pwd in dirs:
				dirs[pwd].append((file,size))
			else:
				dirs[pwd] = [(file,size)]
	return dirs

def get_sizes(dirs:dict) -> dict:
	# Find the size of each directory's contents
	sizes = {dir:sum(size for file,size in dirs[dir]) for dir in dirs}

	# Find the total size of each directory's contents plus subdir sizes
	totalsizes = dict()
	for parent in dirs:
		totalsize = 0
		for dir in dirs:
			if (parent in dir.parents) or (parent is dir):
				totalsize += sizes[dir]
		totalsizes[parent] = totalsize

	return totalsizes

def solve_a(data)-> int:
	# Build the directory system
	dirs = build(data)
	ic(dirs)

	# Size the directories
	sizes = get_sizes(dirs)
	ic(sizes)

	# Report sum of all total sizes of at most 100000 
	return sum(sizes[dir] for dir in sizes if sizes[dir] <= 100000)

def solve_b(data:str)-> int:
	# Build the directory system
	dirs = build(data)

	# Size the directories
	sizes = get_sizes(dirs)

	# Get total size of root directory and minimum to be deleted
	used = sizes[Path('/')]
	unused = 70000000 - used
	required = 30000000
	mindel = required - unused
	
	# Find candidate to be deleted
	del_dir = Path('/')
	del_amt = sizes[Path('/')]
	for dir in sizes:
		if (sizes[dir] > mindel) and (sizes[dir] <= del_amt):
			del_dir = dir
			del_amt = sizes[dir]
			ic(del_dir,del_amt)
	return del_amt

if __name__ == "__main__":
	ic.disable()
	assert solve_a(testdata) == 95437
	aocd.submit(solve_a(aocd.data), part='a')
	assert(solve_b(testdata) == 24933642)
	aocd.submit(solve_b(aocd.data), part='b')