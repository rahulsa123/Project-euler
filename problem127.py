import sys
limit = 120000
l=[set() for x in range(limit)]
for i in range(2, limit, 2):
    l[i].add(2)
p=3
while(p < limit):
    if len(l[p]) == 0:
        l[p].add(p)
        for i in range(p+p, limit, p):
            l[i].add(p)
    p += 2
# print(l[504])
# print(l[5],l[27],l[32])
co = 1
total = 0
def f(s1, s2, s3):
    num=1
    for i in s1:
        num*=i
    for i in s2:
        num*=i
    for i in s3:
        num*=i
    return num
for a in range(1, limit):
    for b in range(a+1, limit, 2 if a%2==0 else 1):
        if a + b >= limit:
            break
        #if a==2:
         #   print(b)
            #print("ddd",l[a]*l[b]*l[a+b]<a+b and math.gcd(l[a],l[b])==1 and  math.gcd(l[a+b],l[b])==1 and  math.gcd(l[a],l[b+a])==1)
        if ( l[a] == l[a]-l[b] == l[a]-l[a+b] and l[b]==l[b]-l[a+b] \
            and f(l[a],l[b],l[a+b])<a+b):
            sys.stdout.write(str(a)+" "+str(b)+"\n")
            total+=a+b
print(total)

