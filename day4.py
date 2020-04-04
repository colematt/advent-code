#!/usr/bin/python3

def isSixDigit(n):
	return len(str(n)) == 6

def hasDouble(n):
	n = str(n)
	
	# Check corner case that will cause out of bounds error with any()
	if len(n) < 2: return False
	
	# Check normal case with any()
	return any(n[i] == n[i+1] for i in range(len(n)-1))

def hasProperDouble(n):
	n = str(n)
	
	# Check corner cases that will cause out of bounds errors with any()
	if len(n) < 2: return False
	if n[0] == n[1] and n[0] != n[2] : return True
	if n[-1] == n[-2] and n[-1] != n[-3]: return True

	# Check normal case with any()
	return any(n[i] == n[i+1] and n[i] != n[i-1] and n[i] != n[i+2]
		for i in range(len(n) - 2))

def isMonotonic(n):
	n = str(n)
	return all(n[i] <= n[i+1] for i in range(len(n)-1))

assert(isSixDigit(123456))
assert not (isSixDigit(12345))
assert(hasDouble(122345))
assert not (hasDouble(123789))
assert(isMonotonic(111123))
assert(isMonotonic(135679))
assert not (isMonotonic(223450))

if __name__ == "__main__":
	# Get inputs
	start,stop = tuple(int(s) for s in input().split('-'))
	
	print("Number of passwords: ", 
		len(list(filter(lambda n: isMonotonic(n), 
				filter(lambda n: hasDouble(n), 
					filter(lambda n: isSixDigit(n), range(start,stop)))))))
					
	print("Number of proper passwords: ", 
			len(list(filter(lambda n: isMonotonic(n), 
					filter(lambda n: hasProperDouble(n), 
						filter(lambda n: isSixDigit(n), range(start,stop)))))))