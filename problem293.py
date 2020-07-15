from functools import reduce
from itertools import combinations
from prime import is_prime
from collections import deque
import numpy as np
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23]
"""
find logic to reduce size of ref_array

"""


def get_number(prime, limit):
    
    ref_array = deque([1])
    prime_mul = np.zeros(len(prime), dtype=np.int64)
    while True:
        min_index = None
        min_value = -1
        for ref_index in range(len(prime)):
            if min_value == -1 or min_value > prime[ref_index]*ref_array[prime_mul[ref_index]]:
                min_value = prime[ref_index]*ref_array[prime_mul[ref_index]]
                min_index = deque([ref_index])
            elif min_value == prime[ref_index]*ref_array[prime_mul[ref_index]]:
                min_index.append(ref_index)
        if min_value >= limit:
            break
        ref_array.append(min_value)
        for ref_index in min_index:
            prime_mul[ref_index] += 1
        yield min_value


def getNearPrime(n):
	if n==2:
		return 3
	""" only for value greater than 6"""
	ref = n//6
	while True:
		temp = 6*ref
		if temp - 1 > n and is_prime(temp - 1):
			return 6*ref - 1
		if temp + 1 > n and is_prime(temp + 1):
			return temp + 1
		ref += 1

if __name__ == "__main__":
	""" for distinct value of M"""
	limit = 10**9
	M = set()
	for num in get_number([2], limit):
		tt = getNearPrime(num+1)
		M.add(tt - num)
	
	for com_num in range(2,len(prime)+1):
		ref = reduce(lambda x,y:x*y, prime[:com_num])
		M.add(getNearPrime(ref+1) - ref)
		for num in get_number(prime[:com_num], limit):
			if ref*num >= limit :
				break
			tt = getNearPrime(ref*num+1)
			M.add(tt - ref*num)
	print(sum(M))
