import itertools as it
test=[True]*1000000
l=[0,2]
p=3
while(p*p<=1000000):
    if(test[p]):
        l.append(p)
        for i in range(p+p,1000000,p):
            test[i]=False
    p+=2
for i in range(p,1000000):
    if(test[i]):
        l.append(i)
def partition(num):
    total=num
    ways=[0]+[0 for _ in range(num)]
    ways[0]=1
    for i in range(1,num):
        if(l[i]>num):
            break
        for j in range(l[i],total+1):
            ways[j]=ways[j]+ways[j-l[i]]
 #   print(ways)
    for i in range(1,len(ways)):
        if((ways[i]+1)%1000000==0):
            print(i)
            break
    return ways[total]
for i in it.count(10):
    x=partition(i)
    print(i,x)
    if(x>=5000):
        print(i)
        break
    
