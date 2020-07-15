import numpy as np
limit = 10**3+1
arr = np.zeros(limit)
for i in range(2,limit,2):
    arr[i]=1
print(i)
total = 2
p = 3
while(p<limit):
    if arr[p]==0:
        arr[p]=1
        for i in range(p+p,limit,p):
            arr[i]+=1
    total+=arr[p]
    p+=1
print(total, arr[30])
