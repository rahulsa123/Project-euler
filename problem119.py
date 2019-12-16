import math 
import bisect 
l = {x:x for x in range(5,100)}
se = []
for power in range(2,100):
    for i in l:
        l[i]*=i 
        ref = l[i]
        s = 0
        Continue = False 
        while(ref!=0):
            s+=ref%10
            ref//=10
            if s>i:
                ref = 0
                Continue = True 
        if Continue:
            continue 
        elif(s!=1 and s==i):
            bisect.insort_left(se,l[i])

print(se[29])
