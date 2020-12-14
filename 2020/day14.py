#!/usr/bin/python3

def test():
	with open('inputs/input14-test.txt') as fin:
		lines = [line.rstrip() for line in fin.readlines()]
		print(lines)
		print()

def main():
	with open('inputs/input14.txt') as fin:
		lines = [line.rstrip() for line in fin.readlines()]
		print(lines)

if __name__ == '__main__':
	test()
	main()