l=[]
for i in range(80):
    l.append([int(x) for x in input().split(",")])
for i in range(80):
    for j in range(80):
        if(j >0 and i==0):
            l[i][j]+=l[i][j-1]
        elif(i>0 and j==0):
            l[i][j]+=l[i-1][j]
        elif(i>0 and j>0):
            mi = min(l[i][j-1],l[i-1][j])
            l[i][j]+=mi
print(l[79][79])
