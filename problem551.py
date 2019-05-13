p=2
prime= []
ref=[True]*101
while(p*p<=100):
    if(ref[p]):
        prime.append(p)
        for i in range(p+p,101,p):
            ref[i]=False
    p+=1
for i in range(p,101):
    if(ref[i]):
        prime.append(i)
l=[]
for i in prime:
    ref=[]
    s=100
    res=0
    while(s>=i):
        res+=s//i
        s=s//i
    for j in range(res+1):
        ref.append(j)
    l.append(ref)
#print(prime)
#print(l)
counter=0
res1 =  1
for i in l:
    res1*=len(i)+1
def get(num, resultl,resultr):
    global counter,res1
    if(num<len(l) and resultl<res1//4):
        for i in l[num]:
            get(num+1,resultl*(i+1),resultr*(len(l[num])-i))
    else:
        print(resultl, resultr)
        if(resultl==resultr):
            counter+=1
            
for i in l[0]:
    get(num=1,resultr=i+1,resultl=len(l[0])-i)
    print(i)
print(counter)
"""
def get(num,resultl,resultr):
    if(num<len(l)):
        for i in l[num]:
            get(num+1,resultl*(i+1),resultr*(len(l[num])-i))
        else:
            if(resultl==resultr):
                print(resultl,resultr)
for i in l[0]:
    get(num=1,resultl=i+1,resultr=len(l[0])-i)
"""
