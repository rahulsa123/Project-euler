import math as m
counter=0
for i in range(5,12000+1):
    lower = m.ceil(i/3)
    upper=m.floor(i/2)
    for j in range(lower,upper+1):
        if(m.gcd(i,j)==1):
            counter+=1
print(counter)

