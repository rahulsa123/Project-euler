from prime import prime, is_prime
from collections import deque
primeList = deque()


def getPrime():
    global primeList
    checkpimeList = prime(10**7 + 2)
    startingPoint = 10**14
    endingPoint = startingPoint + 10**7
    ref = [True] * (10**7)
    while len(primeList) < 10**5:
        for j in checkpimeList:
            if j > endingPoint**0.5:
                break
            start = j * (startingPoint // j)
            if start < startingPoint:
                start += j
            for k in range(start, endingPoint, j):
                ref[k - startingPoint] = False
        for j in range(len(ref)):
            if ref[j]:
                primeList.append(startingPoint + j)
            if len(primeList) == 10**5:
                break
        startingPoint = endingPoint
        endingPoint = startingPoint + 10**7
        ref = [True] * (10**7)


getPrime()


class Matrix:
    def __init__(self, size):
        self.size = size
        self.m = [[0] * size for _ in range(size)]

    def identity(self):
        for i in range(self.size):
            self.m[i][i] = 1

    def __mul__(self, a):
        res = Matrix(a.size)
        for i in range(a.size):
            for j in range(a.size):
                for k in range(a.size):
                    res.m[i][j] += self.m[i][k] * a.m[k][j]
                    res.m[i][j] %= 1234567891011
        return res


def fib(n):
    res = Matrix(2)
    res.identity()
    T = Matrix(2)
    T.m[0][0] = T.m[0][1] = T.m[1][0] = 1
    if n == 0:
        return 0
    if n <= 2:
        return 1
    n -= 2
    while n != 0:
        if (n & 1):
            res = res * T
        T = T * T
        n //= 2
    return (res.m[0][0] + res.m[0][1]) % 1234567891011


i = primeList[0] + 1
fn = fib(primeList[0])
fn1 = fib(primeList[0] + 1)
index = 1
total = fn % 1234567891011
while(index < len(primeList)):
    if i == primeList[index]:
        total += fn1
        total %= 1234567891011
        index += 1
    fn, fn1 = fn1 % 1234567891011, (fn + fn1) % 1234567891011
    i += 1
print(total)
