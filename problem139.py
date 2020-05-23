"""
all primitive case where diffrence of two smallest edge is continue
"""
import math
limit = (100*10**6)//2
m_limit = int((limit)**0.5)
squre_list = [x**2 for x in range(0, m_limit+1)]
total = 0
# print(m_limit)
for m in range(2, m_limit+1):
    for n in range(1 + m % 2, m, 2):
        if math.gcd(m, n) != 1:
            continue
        if abs(squre_list[m]-squre_list[n]-2*m*n) == 1:
            total += limit//(m**2+m*n)

print(total)
