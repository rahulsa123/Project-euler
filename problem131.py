size=1000000
prime=[False]*2+[True]*2+[i for _ in range(int(size/2)-2) for i in [False, True]]
l=[2]
p=3
#print(prime)
while(p*p<=size):
    if(prime[p]):
        for i in range(p+p,size,p):
            prime[i]=False
    p+=2
#print(prime,l)
counter=0
squ =[x**3 for x in range(1,578)]
for i in range(1,len(squ)):
    for j in range(i-1,-1,-2):
        ref=squ[i]-squ[j]
       # print(ref%2==0)
        if(ref<size and prime[ref]):
            counter+=1
            break
    print(i+1)
print(counter)
