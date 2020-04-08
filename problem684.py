"""
1..9+19..99+199...999+...
    9/2(19+99)+9/2(199+999)+...
    9(59)+9(599)+9*5999
    9(60-1+600-1+6000-1....)
    9(60*(10**n-1)/9 - n)
    60*10**n-60 - n*9
now for extra calculaion
13 = 2*(10**step-1)-1   step = 13/9
     3*(10**step-1)-1
     4*(10**step-1)-1
    5*(10**step-1)-1
"""
total = 0
l = [0,1]
for i in range(2,91):
    l.append(l[-1]+l[-2])
#most_ref = 11111111111%(10**9+7)
def cal(n):
    if n<10:
        return (n*(1+n))//2
    total=45
    step = n//9-1
    if step!=0:
        total+=(60*pow(10,step,(10**9+7))-60-step*9)%(10**9+7)
    remain = 2
    for _ in range(n%9):
        total+=(remain*pow(10,step+1,(10**9+7))-1)%(10**9+7)
        remain+=1
        total%=(10**9+7)
    return total

result = 0
#count = 2
for i in range(2,91):
    #print(i)
    result+=cal(l[i])
    result%=(10**9+7)
print(result)

