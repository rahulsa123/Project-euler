import array 
a = array.array("b")
limit = 10**8
for i in range(limit):
    a.append(1)
#print("com")
p = 2 
total = 0
while p*p <limit:
    if a[p] == 1:
        ref = p*p
        # first make all multiple of ref 0
        if ref<limit:
            a[ref]+=1
        for i in range(ref+p,limit,p):
            a[i]+=1
            if i%ref==0:
                a[i]+=1
    if a[p]==2:
#        print(p)
        total+=1 
    p+=1
for i in range(p,limit):
    if a[i]==2:
        #print(i)
        total+=1
print(total)
