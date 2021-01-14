

def prime(n):
    sieveBond = (n)//2
    sieve = bytearray(sieveBond+1)
    sieve[0]=1
    crosslimit = int((n**0.5-1)/2)
    for i in range(1, crosslimit+1):
        if sieve[i]==0:
            for j in range(2*i*(i+1), sieveBond, 2*i+1):
                sieve[j] = 1
    # return
    return [2]+[2*i+1 for i in range(1, sieveBond) if sieve[i]==0]
# in place of this let do 6i +- 1 method


def prime_less_memory(n):
    sieveBond = (n//6)+1
    sieve = [0]*sieveBond
    crosslimit = int((n**0.5+1)/6)
    """
     here in array we store four value
        1. 0 means 6i+1 and 6i-1 both are prime
        2. 1 means 6i+1 is not prime
        3. -1 means 6i-1 is not prime
        4. 2 means 6i+1 and 6i-1 both are not prime
    """
    test1 = [0, 1]
    test2 = [0, 5]
    for i in range(1, crosslimit+1):
        if sieve[i] != 5 and sieve[i] != 6:
            # means 6i+1 is prime
            p = 6*i-1
            for j in range(p*p, n, 2*p):
                ref = j % 6
                if ref == 1 and sieve[j//6] in test2:
                    sieve[j//6] += ref
                if ref == 5 and (sieve[j//6+1] in test1):
                    sieve[j//6+1] += ref
        if sieve[i] != 1 and sieve[i] != 6:
            # means 6i+1 is prime
            p = 6*i+1
            for j in range(p*p, n, 2*p):
                ref = j % 6
                if ref == 1 and (sieve[j//6] in test2):
                    sieve[j//6] += ref
                if ref == 5 and (sieve[j//6+1] in test1):
                    sieve[j//6+1] += ref
    # return
    from collections import deque
    prime = deque([2, 3])
    # print(sieveBond)
    for i in range(1, sieveBond):
        if sieve[i] in test1:
            prime.append(6*i-1)
            # print(6*i-1)
        if sieve[i] in test2:
            prime.append(6*i+1)
    return list(prime)


def is_prime(n):

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number
    if n<2:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    if n < 2047:
        ref = [2]
    elif n < 1373653:
        ref = [2, 3]
    elif n < 9080191:
        ref = [31, 73]
    elif n < 25326001:
        ref = [2, 3, 5]
    elif n < 3215031751:
        ref = [2, 3, 5, 7]
    elif n < 4759123141:
        ref = [2, 7, 61]
    elif n < 1122004669633:
        ref = [2, 13, 23, 1662803]
    elif n < 2152302898747:
        ref = [2, 3, 5, 7, 11]
    elif n < 3474749660383:
        ref = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        ref = [2, 3, 5, 7, 11, 13, 17]
    else:
        ref = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for a in ref:
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def get_number(prime, limit):
    """
    pass list of prime and limit and it will genrate series of number
    """
    import numpy as np
    from collections import deque

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

