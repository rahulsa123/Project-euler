upper_limit = 10**10
squre_limit = int(upper_limit**0.5+1)
dict_number = {x:[] for x in range(squre_limit)}
p = 3 
for i in range(2,squre_limit,2):
    dict_number[i].append(2)
while p<squre_limit:
    if len(dict_number[p])==0:
        dict_number[p].append(p)
        for i in range(p+p,squre_limit,p):
            dict_number[i].append(p)
    p+=1
import math as m
total = 0
for i in range(2,squre_limit):
    ref = i**2 
    for j in dict_number[i]:
        ref*=(j-1)
        ref/=j 
    t = m.ceil(ref**(1/3))
    if t**3==ref:
        total+=i 
        print(i)
print(total)
