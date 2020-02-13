import math  
total = 0
l = [x**2 for x in range(10865)]
for m in range(1,10865):
    for n in range(m-1,-1,-2):
        if n==0:
            continue
        if math.gcd(m,n)==1:
            a,b,c = l[m]+l[n],2*m*n,l[m]-l[n]
            if abs(a-2*b)==1:
                print(a,a,2*b,m)
                total+=2*a+2*b 
            if abs(a-2*c)==1:
                print(a,a,2*c,m,n)
                total+=2*a+2*c
print(total)





"""
import math as m
import time 
result = 0
for i in range(1,333333332+1,4):
    # for a a a+1
    ref = (i+1)%4
    ref2 = (3*i+1)
    ref3 = (i-1)
    ref4 = m.sqrt(ref2*ref3)
    if i == 126500417:
        print(ref4)
    if ref4 == int(ref4):
        ref4 %=4
        if (ref*ref4)%4==0:
            print(i,i,i+1)
            result+=3*i+1    
    # for a a a-1
    ref = (i-1)%4
    ref2 = (3*i-1)
    ref3 = (i+1)
    ref4 = m.sqrt(ref2*ref3)

    if i == 126500417:
        print(ref4)
    if ref4 == int(ref4):
        ref4 %=4
        if (ref*ref4)%4==0:
            print(i, i, i-1)
            result+=3*i-1
print(result)"""
