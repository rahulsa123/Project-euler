# less than 30sec

import time
t1=time.time()
size=10000000
prime= [True]*(size+1)
p=2
l=[]
while(p*p<=size/2):
    if(prime[p]==True):
        l.append(p)
        for i in range(p+p,(size//2+1),p):
            prime[i]=False
    p+=1
for i in range(p,(size//2+1)):
    if(prime[i]):
        l.append(i)
s= 0
#print(l)

for i in l:
    print(i)
    if(i>size**0.5):
        break
    for j in l[l.index(i)+1:]:
        ma = 0
        ref=i*j
        if(ref>size):
            break
        for k in range(size-(size%ref),0,-ref):
            tem=k
            while(tem%ref==0):
                tem/=ref
            while(tem%i==0):
                tem/=i
            while(tem%j==0):
                tem/=j
            if(tem==1):
                ma=k
                s+=ma
                break
       # print(i,j,k,tem)
    # print(i,j,ma)
print(time.time()-t1)
print(s)
