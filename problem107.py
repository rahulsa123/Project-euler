l=[]
total=0
with open("network.txt") as f:
    for i in f.read().split("\n"):
        ref=[]
        for j in i.split(","):
            if(j==""):
                continue
            elif(j=="-"):
                ref.append(-999999)
            else:
                ref.append(int(j))
                total+=int(j)
        if(len(ref)!=0):
            l.append(ref)
#print(total)
seen=[False]*40
seen[0]=True
parent=[0]*40
end_total=0
print(l)
for _ in range(40):
    min_ref=999999
    ref_parent=0
    ref_child=0
    for index_i,i in enumerate(seen):
        if i: # for every seen element
            for index,j in enumerate(l[index_i]): # loop all the element
                if j>0 and min_ref>j and seen[index]==False: # not seen connected 
                    min_ref=j
                    ref_parent=index_i
                    ref_child=index
                    print(min_ref,ref_parent,ref_child)
    if(min_ref!=999999):
        seen[ref_child]=True
        parent[ref_child]=ref_parent
        end_total+=min_ref
#        print(ref_child)

print(total//2,end_total,seen)
