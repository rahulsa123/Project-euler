"""
1582

real    0m11.128s
user    0m11.030s
sys 0m0.033s


"""
import math
index  = 200
l= [[-1, set()] for i in range(index+1)]
l[1] = [0,[{1}]]

for i in range(2,index+1):
    # set min value which from i-1
    l[i] = [l[i-1][0] + 1, list(map(lambda x:x.union({i-1}),l[i-1][1]))]
    # search for min value
    for j in range(math.ceil(i/2), i-1):
        if l[j][0]+1<=l[i][0]:
            # check if i-j is in l[j][1]
            found = False
            for s in l[j][1]:
                if i-j in s or i-j == j:
                    found = True
                    break
            if found:
                if l[j][0]+1 < l[i][0]:
                    l[i][1].clear()
                l[i][0]=l[j][0]+1
                
                for s in l[j][1]:
                    ref = s.union({j})
                    con = False
                    # check if set already exist if then continue loop for j
                    for s2 in l[i][1]:
                        if s2.issuperset(ref):
                            con = True
                            break
                    if con:
                        continue
                    # check i-j in s or i-j==j for 4 where 4-2==2 and 4-2 not in s    
                    if i-j in s or i-j==j:
                        l[i][1].append(ref)
            else:
                # check is there subset avalaible in i-j 
                found = False
                for s1 in l[i-j][1]:
                    for s2 in l[j][1]:
                        # check if set already exist if then continue loop for j
                        if s2.issuperset(s1):
                            found = True
                            break
                if found and l[j][0]+2<=l[i][0]:
                    if l[j][0]+2 < l[i][0]:
                        l[i][1].clear()
                    l[i][0]=l[j][0]+2
                    
                    for s1 in l[i-j][1]:
                        for s2 in l[j][1]:
                            if s2.issuperset(s1):
                                l[i][1].append(s.union({j,i-j}))
res = 0
for i in range(2,201):
    res+= l[i][0]
print(res)