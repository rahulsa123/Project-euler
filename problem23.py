import math as m
abundant=[12]
for i in range(13,28123-11):
    sf=1
    k=int(m.sqrt(i))
    for j in range(2,k+1):
        if(i%j==0):
            sf+= j+(i//j)
    if(k*k == i):
        sf-=k
    if(sf>i):
        abundant.append(i)
res=0
for i in range(1,28123+1):
    for j in abundant:
        if(i<j):
            res+=i
            #print(i)
            break
        else:
            if(i-j in abundant):
                #print(i,j-i)
                break
print(res)
