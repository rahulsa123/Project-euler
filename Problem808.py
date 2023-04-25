from prime import prime

primes  = prime(10**8)
result = 0
visited = [False]*(len(primes))
def searchPrimeSqureIndex(low, high, pSqure):
    if(low<=high):
        mid = low+(high-low)//2
        temp = primes[mid]**2
        if temp ==pSqure:
            return mid
        elif temp>pSqure:
            return searchPrimeSqureIndex(low, mid-1, pSqure)
        else:
            return searchPrimeSqureIndex(mid+1, high, pSqure)
    return -1


for i in range(len(primes)):
    if( not visited[i]):
        visited[i] = True
        pSqure = primes[i]**2
        pSqureReverse = 0
        temp = pSqure
        while temp!=0:
            pSqureReverse*=10
            pSqureReverse+=temp%10
            temp//=10
        if(pSqure<pSqureReverse):
            # print(primes[i], pSqure, pSqureReverse)
            index = searchPrimeSqureIndex(i+1, len(primes)-1, pSqureReverse)
            if index !=-1:
                visited[index] = True
                result += pSqure+pSqureReverse
print(result)
