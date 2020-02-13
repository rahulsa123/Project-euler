l = []
with open("primes1.txt","r") as f:
    for i in f.readlines():
        for j in map(int, i.strip().split()):
            l.append(j)
            if len(l)>=500500:
                break

num = 1
import bisect
for i in range(500500):
    num*=l[0]
    num%=500500507 
    t=l[0]**2 
    l.remove(l[0])
    if t<l[-1]:
        bisect.insort_left(l,t)
print(num)
