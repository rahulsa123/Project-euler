"""
take almost 3 min

"""
import math

#total = 0
l = []
M = 1
m = 2
#breakpoint()
while True:
    ref = M//2
    while m <= ref:
        for n in range(1 + m % 2, m, 2):
            if math.gcd(m, n) != 1:
                continue
            l.append(sorted([m ** 2 + n ** 2, 2 * m * n, m ** 2 - n ** 2]))
        m = m + 1
    total=0
    for i in range(len(l)):
        k = math.gcd(l[i][0], l[i][1])
        for temp in range(
            k if k == 1 else k + 1, M // l[i][0] + 1):
            a, b, c = [s * temp for s in l[i]]
            if a <= M:
                if b <= M:
                    total += a // 2
                    #s.add((a,b,c))
                ref = a - (b if b % 2 == 0 else b + 1) // 2 + 1
                if ref > 0:
                    total += ref
                        #s.add((a,b,c))
    if total>10**6:
        print(M,total)
        break
    #print(M,total)
    M += 1
