import math
t = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
temp = set()
result = 1
limit = 10**9
l = [] 
for i in t:
    l.append([1,i])
for i in l:
    ref = i[-1]
    #print(ref)
#    temp.add(ref)
    result+=1
    for power in range(2, int(math.log(limit,ref)+1)):
        i.append(i[-1]*ref)
        if(i[-1]<limit):
#            temp.add(i[-1])
            result+=1

def cal(row,total):
    if total>limit:
        return
    if row<len(l):
        for i in l[row]:
            cal(row+1, total*i)
    if total<= limit:
        temp.add(total)
cal(0, 1)
print(len(temp))

