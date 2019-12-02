"""

euler formula of partition 
p(n) = sum (k=1 to n)[ (-1)^k+1 *(p(n-1/2*k(3*k-1)) + p(n-1/2*k(3*k+1)) ) ]
 after k >sqrt(n) all term under p() becomes negative  p(- n) = 0

and p(n) = answer %1000000 
if p(n) == 0 
    return n

"""
import collections 
import math as m
partition = collections.deque()
# partition(0) = 1
partition.append(1)

i=1
def partitionCal(n):
    if n<0:
        return 0
    if n<len(partition):
        return partition[n]

while (True):
    partition_of_i = 0
    for k in range(1, int(m.sqrt(i)+1)):
        pn1 = i - (k*(3*k+1))//2
        pn2 = i - (k*(3*k-1))//2

        term1 = partitionCal(pn1)
        term2 = partitionCal(pn2)
        if (k+1)%2 == 0:
            partition_of_i += term1+term2
        else:
            partition_of_i -= (term1+term2)
    ref = partition_of_i%1000000
    if ref ==0:
        print(i)
        break
    partition.append(ref)
    i+=1        
    
#print(partition)
