"""
using m,n method if n ==1 the max value of m will be m <=865

side of triangle
a =  m**2 - n**2
b = 2*m*n 
c = m**2 + n**2 

here in l{ [count of found solution , set of each max(a,b)]}

why not min (a,b)
in 132 there are two solution 
    11,60,61
    33,44,55
so if we check already find condition then it says already found because of 33 div 11 but
here i put 60,44
60 mod 44 != 0 so already found condition not satisfied



2.66 sec in python 
"""
import time as t 
t1 = t.time()
import math  
l = {x: [0,set()] for x in range(12, 1500000, 2)}
for m in range(2,866):
    for n in range(1+m%2,m,2):
        h = m**2+n**2
        b = 2*m*n 
        a = m**2 - n**2
        if h+b+a < 1500000:
            ref = h+b+a 
            if l[ref][0]>1:
                continue
            ref2 = max(a,b)
            same = False
            for i in l[ref][1]:
                if i%ref2==0:
                    same = True
                    break
            if same:
                continue
            l[ref][0]+=1
            l[ref][1].add(ref2)
            for i in range(ref+ref, 1500000, ref):
                l[i][0]+=1
                ref3 = ref2*i//ref 
                already = False
                for j in l[i][1]:
                    if j%ref3==0:
                        already = True
                        break
                if not already:
                    l[i][1].add(ref3)
count=0
for i in l:
    if l[i][0]==1:
        count+=1        
print(count, t.time()-t1)
