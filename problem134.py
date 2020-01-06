limit = 10**6+10
ref =[0]*limit 
prime = []
p=2 
while p*p<limit:
    if ref[p]==0:
        prime.append(p)
        for i in range(p*p,limit,p):
            ref[i]=1
    p+=1
for i in range(p,limit):
    if ref[i]==0:
        prime.append(i)
del ref
"""
example 5 and 7 

first break it 
x*10 + 5 = 0 mod 7 
now 5 mod 7 = 5
means x*10 mod 7 = 7-5 = 2 
10 mod 7 = 3
so equatino become 
x*3 = 2 mod 7 
solve using http://mathonline.wikidot.com/examples-of-finding-remainders-using-wilson-s-theorem for 1
x*3 = 1 mod 7 
then multiply 2 in both side 
"""
def remainder_of_p_1_fact(p,base):
    l = []
    rem = 1
    temp = p
    try:
        while(True):
            ref = temp//base
            l.append(ref)
            temp, base =base, temp - base*ref
            if base == 1:
                break
    except Exception as e:
        print(p,base)
        exit()
    ref = 1
    #print(l)
    while l[0]==0:
        l=l[1:]
    temp = l[-1]*-1
    for i in l[-2::-1]:
        temp2 = (temp * (i*-1))+ref
        ref = temp
        temp = temp2
    return temp
import math as m 
pre =  5
total = 0
import time  
t1 = time.time()
for i in prime[3:]: # pre = 5 i =7
    t = 10**m.ceil(m.log(pre,10)) # 10**(number of digit in pre) ref=10**1%7 =3
    ref = t %i # 10**(number of digit in pre) ref=10**1%7 =3
    ref1 = i- pre  # x*ref = ref1 mod i  ref1 = 7-5 =2 
    res = (ref1*remainder_of_p_1_fact(ref, i))%i
    total+=(res*t+pre)
    pre = i
print(total, time.time()-t1)
