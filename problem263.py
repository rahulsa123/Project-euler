from collections import deque
from prime import prime

primes = prime(10**7    )
num = 0


def checkPractical(n):
    # print(n)
    if(n%3!=0 and n%5!=0):
        return False
    factor = [1, n]
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0):
            factor.append(i)
            factor.append(n//i)

    factor.sort()
    # print(factor)
    sumPosible = [False]*(n+1)
    sumPosible[0] = True
    for i in factor:
        for j in range(0, i):
            if (i+j > n):
                break
            if (sumPosible[j]):
                sumPosible[i+j] = True
    # print(sumPosible)
    return all(sumPosible)



for i in range(12, len(primes)-2):
    n = primes[i]+3
    if primes[i+1] == primes[i]+6 and primes[i+2] == primes[i]+12 \
        and primes[i-1] == primes[i]-6 and checkPractical(n) and checkPractical(n-4) and checkPractical(n-8) and checkPractical(n+4) and checkPractical(n+8):
        print(primes[i-1], primes[i], primes[i+1], primes[i+2])
print(num)
