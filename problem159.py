limit = 10**6
l=[0]*limit
p = 2 
def digital_root(n):
    ref = sum([int(x) for x in str(n)])
    if ref%9==0:
        return 9 
    else:
        return ref%9
while(p*p<limit):
    if l[p]==0:
        l[p]= digital_root(p)
        for i in range(p*p,limit,p):
            l[i]=-1
    p+=1 
for i in range(p,limit):
    if l[i]==0:
        l[i]=digital_root(i)
total = 0
for i in range(2,limit):
    if l[i]!=-1:
        total+=l[i]
    else:
        l[i]=digital_root(i)
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                l[i]=max(l[j]+l[i//j],l[i])
        total+=l[i]
    if i==24:
        print(l[i])
print(total) 
