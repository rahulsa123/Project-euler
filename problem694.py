"""
1339784153569958487

real    0m33.182s
user    0m33.800s
sys 0m0.429s


"""
import numpy as np
from collections import deque
from prime import prime


limit = 10**6+1
test_limit = int(limit**(1/3)+1) 
# print(test_limit)
test = [[] for x in range(test_limit)]
total = limit-1
ref = []


def get_number(prime, limit):
    """
    passing list of primes and returning series of number where all prime factors are in the list
    example:-
        [2,3,5] , limit = 30
        2,3,5,6,8,9,10,12,15,16,18,20,25,27,30
    """
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


total = limit-1
for i in range(2, test_limit):
    # if i is prime or not
    if len(test[i]) == 0:
        test[i].append(i)
        # add prime i in each multiple of prime i
        for j in range(2*i, test_limit, i):
            test[j].append(i)
    # now check if i is start point or not
    temp = 1
    for j in test[i]:
        temp *= j
    if temp == i:
        temp = 1
        # get the starting cube full number with list of prime

        for j in test[i]:
            temp *= j**3
        print(temp, end=' ')
        # add all the multiple of cube full number
        total += (limit-1)//temp
        # now here get_numbers return series of numbers where prime factors are in list
        for mul in get_number(test[i], limit):
            ref = temp*mul
            if ref >= limit:
                break
            total += (limit-1)//ref
            print(ref, end=" ")
    test[i]=None
print(total)
