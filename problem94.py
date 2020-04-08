import math  
total = 0
l = [x**2 for x in range(11000)]
for m in range(1,11000):
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

