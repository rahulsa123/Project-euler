import itertools as it
def partition(num):
    l=[0]+[x for x in range(1,num)]
    total=num
    ways=[0]+[0 for _ in range(num)]
    ways[0]=1
    for i in range(1,num):
        for j in range(l[i],total+1):
            ways[j]=ways[j]+ways[j-l[i]]
 #   print(ways)
    for i in range(1,len(ways)):
        if((ways[i]+1)%1000000==0):
            print(i)
            break
    return ways[total]
print(partition(100))
"""
for i in it.count(10):
    print(i)
    if(partition(i)%1000000==0):
        print(i)
        break
    """
