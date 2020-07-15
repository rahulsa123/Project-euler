"""
7526965179680

real    0m3.388s
user    0m3.374s
sys 0m0.012s

"""

from Project_euler.prime import prime
from bitarray import bitarray
limit = 20000000
r = 15000000
lower_limit = limit-r
result=1
def psrime(n):
    sieveBond = (n-1)//2
    sieve = bitarray(sieveBond+1)
    sieve.setall(0)
    sieve[0]=1
    crosslimit = int((n**0.5-1)/2)
    for i in range(1, crosslimit+1):
        if sieve[i]==0:
            for j in range(2*i*(i+1), sieveBond, 2*i+1):
                sieve[j] = 1
    yield 2
    for i in range(1, sieveBond):
         if sieve[i]==0:
            yield 2*i+1
total = 0
for i in psrime(limit+1):
    ref1,ref2,ref3 = limit,lower_limit,r
    p1,p2,p3 = 0,0,0
    while ref1!=0:
        ref1//=i
        p1+=ref1
    while ref2!=0:
        ref2//=i
        p2+=ref2
    while ref3!=0:
        ref3//=i
        p3+=ref3
    
    if p1-p2-p3!=0:
        total+=i*(p1-p2-p3)
print(total)