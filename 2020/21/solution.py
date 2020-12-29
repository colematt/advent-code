#!/usr/bin/python3

import aocd
from icecream import ic
import itertools

def parse(lines):
	parsed = list()
	for line in lines:
		ingredients,_,allergens = line.partition('contains')
		ingredients = set(ingredients.rstrip(' (').split())
		allergens = tuple(allergens.rstrip(')').replace(',','').split())
		parsed.append((ingredients,allergens))
	return parsed

def reduce(parsed, submit=False):
	"""
	Return the dictionary of allergen to unrecognized ingredients.
	"""
	# Get the comprehensive sets of ingredients and allergens,
	# Set the value in reduced for each allergen to the comprehensive set
	# of ingredients
	ingr_set = set(itertools.chain.from_iterable([ing for ing,_ in parsed]))
	aller_set = set(itertools.chain.from_iterable([allg for _,allg in parsed]))
	reduced = {allergen:ingr_set for allergen in aller_set}

	# Reduce the potential dangerous ingredients by analyzing each food
	for ingredients,allergens in parsed:
		for allergen in allergens:
			reduced[allergen] = reduced[allergen] & ingredients

	# Submit the count of all safe ingredients appearing in each food
	count = 0
	safe = ingr_set.difference(
		set(itertools.chain.from_iterable(reduced.values())))
	for ingredients,_ in parsed:
		count += len(ingredients & safe)
	if submit:
		aocd.submit(count, year=2020, day=21, part='a')
	else:
		ic(count)

	return reduced

def solve(reduced, submit=False):
	solved = dict().fromkeys(reduced.keys())

	# While items remain in reduced ...
	while reduced:
		# Iterate across the item pairs to find solvable allergens
		for allergen, ingredients in reduced.items():
			# If a single ingredient remains for an allergen, it's solved
			if len(ingredients) == 1:
				# Update solved
				ingredient = reduced[allergen].pop()
				solved[allergen] = ingredient

				# Update all other allergens in reduced
				for allergen in reduced:
					reduced[allergen].discard(ingredient)

		# Eliminate solved allergens from reduced dictionary
		reduced = {k: v for k, v in reduced.items() if v}

	# Form the canonical list
	canonical = ",".join(value for _,value in sorted(solved.items()))
	if submit:
		aocd.submit(canonical, year=2020, day=21, part='b')
	else:
		ic(canonical)

def test():
	with open('test.txt', 'r') as fin:
		data = fin.read().splitlines()
	parsed = parse(data)
	reduced = reduce(parsed, submit=False)
	solved = solve(reduced)

def main():
	data = aocd.get_data(year=2020, day=21).splitlines()
	parsed = parse(data)
	reduced = reduce(parsed, submit=True)
	solved = solve(reduced, submit=True)

if __name__ == '__main__':
	test()
	main()