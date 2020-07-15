limit = 10
import math as m 
s = int(m.log(limit,2))
l = [[0,2**i,2**(i+1)] for i in range(s+1)]
l[-1] = l[-1][:-1]
l[0] = [l[0],2]
for i in range(1,len(l)):
    l[i] = [l[i],l[i][-1]+l[i-1][1]]
print(l)
for i in range(len(l)-1):
    if l[i][1]<limit:
        l[i][0] = l[i][0][1:]
    else:
        break 
l[i][0]=l[i][0][1:]
print(l)
l.reverse()

total = 0 
print(l)
def getResult(index,res):
    global total
    if res==limit:
        total+=1
        return
    if index >=len(l) or res>limit or l[index][1]+res<limit:
        return
    for i in l[index][0]:
        getResult(index+1,res+i)

getResult(0,0)
print(total)
