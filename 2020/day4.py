#!/usr/bin/python3

import re

FIELDS = {'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}
MANDATORY = FIELDS - {'cid'}
EYES = {'amb','blu','brn','gry','grn','hzl','oth'}
HAIR = re.compile('^\#[0-9a-f]{6}$')
ID = re.compile ('^\d{9}$')

def validate_old(passport):
	# Returns true if and only if every key in MANDATORY is in passport.keys() 
	# and all keys in passport.keys() are in FIELDS
	return set(passport.keys()).issuperset(MANDATORY) and \
		set(passport.keys()).issubset(FIELDS)

def validate_new(passport):
	if not validate_old(passport):
		return False
	if not 1920 <= int(passport['byr']) <= 2002:
		return False
	if not 2010 <= int(passport['iyr']) <= 2020:
		return False
	if not 2020 <= int(passport['eyr']) <= 2030:
		return False
	if not ((passport['hgt'][-2:] == 'cm' and (150 <= int(passport['hgt'][:-2]) <= 193)) or \
		(passport['hgt'][-2:] == 'in' and (59 <= int(passport['hgt'][:-2]) <= 76))):
		return False
	if not HAIR.match(passport['hcl']): 
		return False
	if not passport['ecl'] in EYES:
		return False
	if not ID.match(passport['pid']):
		return False
	else:
		return True
	
def main():
	with open('input4.txt','r') as fin:
		passports = list(fin.read().split('\n\n'))
		passports = [dict(keyval.split(':') for keyval in passport.split()) 
			for passport in passports]
	print(len(list(filter(validate_old,passports))))
	print(len(list(filter(validate_new,passports))))

if __name__ == '__main__':
	main()