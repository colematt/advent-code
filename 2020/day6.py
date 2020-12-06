#!/usr/bin/python3

def union(groups) -> int:
	sets = [set.union(*g) for g in groups]
	counts = [len(s) for s in sets]
	return sum(counts)

def intersection(groups):
	sets = [set.intersection(*g) for g in groups]
	counts = [len(s) for s in sets]
	return sum(counts)

def main():
	with open('input6.txt') as fin:
		groups = [tuple(set(answers) for answers in group.split("\n")) for group in fin.read().split('\n\n')]
		print(groups)
		print(union(groups))
		print(intersection(groups))		

if __name__ == '__main__':
	main()