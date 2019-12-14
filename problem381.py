"""
by simplification

((p-5)! * (9))% p

(p-5)! % p 

we know
(p-1)! % p = -1 mod p 

x*24 * (p-5)! = -1*x mod p 
find value of x
using divison "method"

http://mathonline.wikidot.com/examples-of-finding-remainders-using-wilson-s-theorem

"""
import array 
import time 
a = array.array("b")
limit = 10**8 
for i in range(limit):
    a.append(1)
    
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
    temp = l[-1]*-1
    for i in l[-2::-1]:
        temp2 = (temp * (i*-1))+ref 
        ref = temp
        temp = temp2
    temp*=-1
    temp = p+temp if temp<0 else temp
    return temp
print(remainder_of_p_1_fact(23,24))
t = time.time() 
p = 2 
total = 0
while p< limit:
    if a[p]==1:
        if p>=5:
            #calculation 
            total+= (9*remainder_of_p_1_fact(p,24))%p  
        for i in range(p*p,limit,p):
            a[i] = 0
    p+=1
print(total, t- time.time())
