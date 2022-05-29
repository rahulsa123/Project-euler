"""
1412403576

real    0m4.180s
user    0m4.135s
sys 0m0.045s


"""


from prime import prime
import tqdm
import math as m
# limit
power = 800800
num = 800800
totalInLog = power * m.log2(num)

considerPrime = prime(2 * 10**7)


def f(p, q): return considerPrime[q] * m.log2(considerPrime[p]) + \
    considerPrime[p] * m.log2(considerPrime[q])


total = 0
for i in range(len(considerPrime) - 1):
    lower = i + 1
    higher = len(considerPrime) - 1
    ans = 0
    if f(i, lower) > totalInLog:
        break
    while(lower <= higher):
        mid = (lower + higher) // 2
        calInLog = f(i, mid)
        if calInLog <= totalInLog:
            ans = mid
            lower = mid + 1
        else:
            higher = mid - 1
    total += ans - i


print(total)
