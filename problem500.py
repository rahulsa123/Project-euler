"""

"""
import array 
a = array.array("b")

for i in range(500501):
    a.append(1)
prime = []
p = 2 
while p*p < 500501:
    if a[p]==1:
        prime.append([p,0])
        for i in range(p*p,500501,p):
            a[i]=0
    p+=1
for i in range(p,500501):
    if a[i]==1:
        prime.append([i,0])
del a 
print(prime)
