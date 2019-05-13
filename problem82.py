import time as t
import random as r
n=int(input())
l=[]
for i in range(n):
    s=[]
    for j in range(n):
        s.append(r.randint(1,10**9+1))
    l.append(s)
#first add col first in secon
print(len(l))
t1=t.time()
for j in range(1,n):
    for i in range(n):
        min = l[i][j-1]
        #check if upper is exist or not
        if(i>0):
            min = l[i-1][j]
        #check with left one
        if(min>l[i][j-1]):
            min = l[i][j-1]
        #check for lower col
        #print(min)
        ref=0
        for k in range(i+1,n):
            ref+=l[k][j]
            if(ref>min):
                break
            if(ref+l[k][j-1]<min):
                min=ref+l[k][j-1]
        l[i][j]+=min
        
m=l[0][n-1]
for i in range(n):
    if(m>l[i][n-1]):
        m=l[i][n-1]
print(m)


