import sys  
limit = 10**2+1
prime = [0]*limit
result = 0
p = 2
l = [0]*limit
while(p<limit):
    if prime[p]==0:
        result += p
        l[p]=p
#        sys.stdout.write(str(p)+"\n")
        for i in range(p*p,limit,p):
            ref = i if prime[i]==0 else prime[i] 
            while(ref!=p and ref%p==0):
                ref//=p 
            prime[i]= ref 
    else:
        ref = p 
        t = 0
        while(ref%prime[p]==0):
            t+=1
            ref//=prime[p]
        result += t*prime[p]
        l[p]=t*prime[p]
    p+=1

#print(prime[100],result)
for index,val in enumerate(l):
    print(index,val)
