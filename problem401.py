import math as m
import sys
# sys.setrecursionlimit(10**6)
total = 0
"""
in 4 min 21 second

"""


limit = 10**15


def seriesSum(num):
    res1, res2, res3, temp = num, num + 1, 2 * num + 1, 6
    ref = m.gcd(res1, temp)
    res1 //= ref
    temp //= ref
    if temp != 1:
        ref = m.gcd(res2, temp)
        res2 //= ref
        temp //= ref
    if temp != 1:
        ref = m.gcd(res3, temp)
        res3 //= ref
        temp //= ref
    return (((res1 * res2) % 10**9) * res3) % 10**9


currNum = 1
while (currNum <= limit):
    if limit // currNum != limit // (currNum + 1):
        total += ((limit // currNum) * (pow(currNum, 2, 10**9))) % 10**9
        total %= 10**9
        currNum += 1
    else:
        ending = min(limit, limit // (limit // currNum))
        total += ((limit // currNum) * (seriesSum(ending) - seriesSum(currNum - 1))) % 10**9
        total %= 10**9
        currNum = ending + 1
print(total)
