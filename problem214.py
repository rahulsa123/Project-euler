"""
1677366278943

real    1m43.792s
user    1m43.145s
sys 0m0.874s
"""
limit = (40*10**6)
l = list(range(limit))
from math import sqrt

total=0
l[1]=0

for i in range(2,limit):
    if l[i]==i:
        l[i]=i-1
        for ref in range(2*i,limit,i):
            l[ref]*= (i-1)
            l[ref]//=i
        c = l[i]
        chain = 1
        while c!=0:
            c=l[c]
            chain+=1
            if chain>25:
                break
        if chain==25:
            total+=i
print(total)
