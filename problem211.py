limit = (64000000)
l = [1]*limit
from math import sqrt
# including 1
total=1

for i in range(2,limit):
    
    if l[i]==1:
        tt = i**2
        for ref in range(2*i,limit,i):
            po = 0
            j=ref
            while(j%i==0):
                po+=1
                j//=i
            l[ref]*= (tt**(po+1)-1)/(tt-1)
    else:
        ref = sqrt(l[i])
        if ref==int(ref):
            total+=i
print(total)
