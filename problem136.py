"""
it take around 5 min to solve problem 136


"""
limit = 50*10**6
import numpy as np
a=np.zeros(shape=(limit+1), dtype=np.int8)
temp = (1,3)
for i in range(1,int(limit**.5)+1):
    # print(i)
    for j in range(i+(2 if i%4 in temp else 0),limit//i+1, 4):
    
        ref = 1
        if i!=j and i-(i+j)/4>0:
            ref+=1
        a[i*j]+=ref
co = 1
print(len(np.where(a[3:limit]==1)[0]))
