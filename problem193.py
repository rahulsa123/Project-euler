"""
684465067343069

real	1m20.419s
user	1m20.246s
sys	0m0.092s

"""
def prime(n:int):
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
limit = 2**50
primes = prime(int(limit**0.5)+1)
total = 0
import sys
sys.setrecursionlimit(3*10**6)
def getCount(index,mul, count):
    global total
    if index==len(primes) and mul>=limit:
        return
    if index!=0:
        
        val = (limit-1)//mul *(1 if count%2==1 else -1)
        # print(f"{mul=} {val=}")
        total += val    
    for i in range(index,len(primes)):
        if primes[i]**2*mul<limit:
            getCount(i+1, primes[i]**2*mul,count+1)
        else:
            return
getCount(0, 1, 0)
print(limit-total-1)
# # primes = [2,3,5,7]
# count = 0
# for i in range(1,limit):
#     for j in primes:
#         if i%(j**2)==0:
#             break
#     else:
#         count+=1
# print(count)