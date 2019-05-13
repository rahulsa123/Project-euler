import time 
l=[]
for i in range(80):
    l.append([int(x) for x in input().split(",")])
t1 =time.time()
ref=[(0,0)]
ref2 =[]
for i in range(80):
    s =[]
    for j in range(80):
        s.append(0)
    ref2.append(s)
ref2[0][0]=1
def getAllValue(d):
    global ref,ref2
    #print(i,j,d)
    index =0
    while(index<len(ref)):
        i,j=ref[index][0],ref[index][1]
        t,b,le,r= False,False,False,False
        # true if left exist
        if(j!=79 and i>=0 and i<=79 and ref2[i][j+1]==0):
            d[l[i][j]+l[i][j+1]] = i,j+1
        else:
                le=True
        #right
        if(j!=0 and i>=0 and i<=79 and ref2[i][j-1]==0):
            d[l[i][j]+l[i][j-1]]=i,j-1
        else:
                r=True
        # true if bottom exist
        if(i!=79 and j>=0 and j<=79 and ref2[i+1][j]==0):
            d[l[i][j]+l[i+1][j]]=i+1,j
        else:
                b=True
        # true if top exist
        if(i!=0 and j>=0 and j<=79 and ref2[i-1][j]==0):
            d[l[i][j]+l[i-1][j]]=i-1,j
        else:
                t=True
        index+=1
        if(le and r and b and t):
            ref.remove(ref[index-1])
            index-=1
size = 2
while(ref2[79][79]!=1):
    # dict for strring value with index
    d=dict()
    getAllValue(d)
    #print(d)
    v,(i,j)=min(d.items())
    #print(len(ref))
    l[i][j]=v
    size+=1
    ref.append((i,j))
    ref2[i][j]=1
print(time.time()-t1)
