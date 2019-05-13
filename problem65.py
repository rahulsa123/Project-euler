import time as t
t1 = t.time()
l=[2]
k=1
for i  in range(33):
    l.append(1)
    l.append(2*k)
    k+=1
    l.append(1)
n = 1
d = l[-1]
l=l[:len(l)-1]
for i in l[::-1]:
    n=i*d+n
    n,d=d,n
print(sum([int(x) for x in str(d)]))
print(t.time()-t1)
