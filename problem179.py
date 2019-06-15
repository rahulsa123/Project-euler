size=10**7-1
prime= [1]*(size+1)
p=2
l=[]
gcounter=0
while(p<=size):
    if(p!=2 and prime[p]==prime[p-1]):
        gcounter+=1
   #     print(p)
    if(prime[p]==1):
        l.append(p)
        for i in range(p+p,(size+1),p):
            ref = i
            power=0
            while(ref%p==0):
                ref/=p
                power+=1
    #        if(i==22):
            #    print(p,power)
            prime[i]*=(power+1)            
    p+=1
#for ind,item in enumerate(prime):
   # print(ind,item)
print(gcounter)


