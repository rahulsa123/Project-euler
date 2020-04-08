high_index = -1 
limit = 51
l = [-1]*(limit//2+1)
l[0]=1
s = set([1])
for i in range(2,limit):
    for j in range(i//2,0,-1):
        if i%2==0 and j==i//2:
            l[j]=2*l[j-1]
        else:
            l[j]+=l[j-1]
    for x in l[1:]:
        if x==-1:
            break
        s.add(x)
ref = [2**2,3**2,5**2,7**2,11**2,13**2,17**2,19**2,23**2] 
total=0
print(1 in s)
for i in s:
    for x in ref:
        if i%x==0:
            break 
    else:
        total+=i 
print(total)
