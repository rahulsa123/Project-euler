"""
98792821

real    0m21.258s
user    0m21.248s
sys 0m0.008s

"""

from bitarray import bitarray
limit = 10**8
result=1
def prime(n):
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
for i in prime(limit+1):
    total_p=0
    ref = limit
    while ref!=0:
        total_p+=ref//i
        ref//=i
    result*=(1+pow(i,2*total_p,1000000009))
    # print(i,total_p)
    result%=1000000009
print(result)
