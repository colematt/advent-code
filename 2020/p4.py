#!/usr/bin/env python3

from aocd import data, submit
from icecream import ic
ic.disable()
import re

FIELDS = {'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}
MANDATORY = FIELDS - {'cid'}
EYES = {'amb','blu','brn','gry','grn','hzl','oth'}
HAIR = re.compile('^\#[0-9a-f]{6}$') # pyright: ignore[reportInvalidStringEscapeSequence]
ID = re.compile ('^\d{9}$') # pyright: ignore[reportInvalidStringEscapeSequence]

testdata = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

def isValidA(passport:dict) -> bool:
    return set(passport.keys()).issuperset(MANDATORY) and \
        set(passport.keys()).issubset(FIELDS)


def solveA(data:str) -> int:
    # Input data
    passports = list(data.split("\n\n"))
    passports = [dict(keyval.split(':') for keyval in passport.split()) 
            for passport in passports]
    return len(list(filter(isValidA,passports)))


def isValidB(passport:dict) -> bool:
    if not isValidA(passport):
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
    

def solveB(data:str) -> int:
    passports = list(data.split("\n\n"))
    passports = [dict(keyval.split(':') for keyval in passport.split()) 
            for passport in passports]
    return len(list(filter(isValidB,passports)))


if __name__ == "__main__":
    assert(solveA(testdata) == 2)
    submit(str(solveA(data)), part='a')
    submit(str(solveB(data)), part='b')
