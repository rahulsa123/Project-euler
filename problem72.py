l=[3,2]
while(True):
    for_new_addition= False
    length=len(l)
    i=0
    while(i!=length-1):
        if(l[i]+l[i+1]<12001):
            for_new_addition=True
            x1=l[i]+l[i+1]
            l.insert(i+1,x1)
            i+=2
            length+=1
          #  print(x1,x2,len(l))
        else:
           # print(l[i],l[i+1])
            i+=1
    print(l)
    if(not for_new_addition):
        break
print(len(l)-2)

