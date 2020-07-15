import numpy as np 
limit = 10**8+1 
l = np.zeros(limit,dtype=np.int32)
l[1]=1
total=0
for p in range(2,limit):
    if l[p]==0:
        l[p]=p+1
        for i in range(p+p,limit,p):
            power = 1
            while(divmod(i,p**(power+1))[1]==0):
                    power+=1
            if l[i]==0:
                l[i] = (p**(power+1)-1)/(p-1)
            else:
                l[i]*= (p**(power+1)-1)/(p-1)
print(sum(l))
                
