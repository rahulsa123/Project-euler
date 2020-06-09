"""
115039000

real    2m52.140s
user    2m51.388s
sys 0m0.616s

biggest  group of 50 elements
sum([x**2 for x in range(51,101)]) == 295425
ref = contains counter for each value where it maintain the number of time subset lenght occurs

"""
from collections import Counter

ref=[Counter() for x in range(0,295425+1)]
limit = 50
for i in [x**2 for x in range(1,101)]:
    #print(i)
    for j in range(295425,i,-1):
        if len(ref[j-i])>0:
            for k in ref[j-i]:
                if k<limit:
                    ref[j][k+1]+=ref[j-i][k]
    ref[i][1]+=1
total=0
for j in range(1,295425+1):
    if ref[j][limit]==1:
        total+=j
print(total)


