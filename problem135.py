#import numpy as np
number = [1]*1000000
total=0
for i in range( 2,1000000):
    if number[i]==1:
        number[i]=2
        for t in range(i+i, 10**6,i):
            ref = 0
            j=t
            while(divmod(j,i)[1]==0):
                j/=i 
                ref+=1
            number[t]*=ref+1
    if number[i]>10:
        count = 0 
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                ref = i//j
                # check j as "a"  and find value of d 
                d = (ref+j)/4
                if d == int(d) and ref-d>0: # avoid a-d == 0  case 
                    count+=1
                if ref==j:
                    continue 
                if d==int(d) and j-d>0:
                    count+=1
        if count==10:
            total+=1
print(total)
