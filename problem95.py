sum_of_divisor=[True]*1000000
sum_of_divisor[1]=0
p=2
while(p<1000000):
    if(sum_of_divisor[p] is True):
        sum_of_divisor[p]=1
        for i in range(p+p,1000000,p):
            res=0
            power=0
            while(i%p**power==0):
                res+=p**power
                power+=1
            if(sum_of_divisor in [True,False]):
                sum_of_divisor[i]=res
            else:
                sum_of_divisor[i]*=res
    else:
        sum_of_divisor[p]-=p
    p+=1
print(sum_of_divisor[1184])

max_chain=0
min_element=28
for i in range(2,1000000):
    ref=sum_of_divisor[i]
    if(ref<1000000):
        l=[i]
        while(ref<1000000):
            if(ref==0 or ref==1):
                break
            if(ref not in l):
                l.append(ref)
            else:
                if(ref==i and max_chain<len(l)):
                    max_chain=len(l)
                    min_element=min(min(l),min_element)
                #print(l)
                break
            ref=sum_of_divisor[ref]
print(max_chain,min_element)
