# duplicte is the big problem so using set 


size=100000000
sq=int(size**0.5)
l=[0]*(sq+1)
l[1]=1
squ=[x**2 for x in range(0,sq+1)]
palin = set()
su=0
len=0
for i in range(2,sq+1):
    l[i]=l[i-1]+squ[i]
    if(l[i]<size):
        s=str(l[i])
        if(s==s[::-1]):
            palin.add(l[i])
            len+=1
           # print("from 1 to ",i,"palin",s)
            su+=l[i]
    ref=l[i]
    for j in range(1,i-1):
        ref-=squ[j]
        if(ref<size):
            s=str(ref)
            if(s==s[::-1]):
                palin.add(ref)
                len+=1
          #      print("from",j+1,"to",i,"palin",s)
                su+=ref
print(sum(palin),len,su)
