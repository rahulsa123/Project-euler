# p=(11/r)^4  to log11(p)=r*(1-log11(r)) maximum for 1 to 10
# now for 12 we starting checking r from 4 to 11 (very fast )

import math as m
su=0 
pre=2
for i in range(5,10000+1):
    ma=0
    for j in range(pre,i):
        if ma<(j*(1-m.log2(j)/m.log2(i))):
            ma = (j*(1-m.log2(j)/m.log2(i)))
        else:
            ref=j-1
            pre=j-1
            while(ref%2==0):
                ref/=2
            while(ref%5==0):
                ref/=5
            if(ref==1 or i%ref==0):
                su-=i
            else:
                su+=i
            print(i,j-1,ref)
            break
print(su)
