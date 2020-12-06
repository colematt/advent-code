#!/usr/bin/python3

def anyCount(groups) -> int:
	"""
	Find the sum of the count of answers by group, 
	where the anyone in the group had a particular answer
	"""
	sets = [set.union(*g) for g in groups]
	counts = [len(s) for s in sets]
	return sum(counts)

def allCount(groups):
	"""
	Find the sum of the count of answers by group, 
	where the entire group had the same answer
	"""
	sets = [set.intersection(*g) for g in groups]
	counts = [len(s) for s in sets]
	return sum(counts)

def main():
	with open('inputs/input6.txt') as fin:
		# Read the groups from the input file. Each group is a tuple of sets,
		# where each set is one person's answers.
		groups = [tuple(set(answers) for answers in group.split("\n")) 
					for group in fin.read().split('\n\n')]
		print(anyCount(groups))
		print(allCount(groups))		

if __name__ == '__main__':
	main()