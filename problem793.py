import bisect
import heapq

l = [290797]
limit = 10**6+3
for i in range(limit-1):
    l.append(pow(l[-1],2,50515093))
l.sort()
# print(l)
low,high = 0,len(l)-1
ans = -1
totalNums = (len(l)*(len(l)-1))//2
midPosition1 = totalNums//2-(1 if totalNums%2==0 else 0)
midPosition2 = totalNums//2
# print(midPosition1,midPosition2)
def calculatePosition(mid):
    value = l[mid]*l[mid+1]
    position = 0
    for i in range(mid):
        position += bisect.bisect_right(l,value/l[i])-i-1

    return position

while(low<=high):
    mid = (low+high)//2
    position = calculatePosition(mid)
    if position<=midPosition1:
        ans = low
        low = mid+1
    elif position>=midPosition2:
        high = mid-1
    else:
        break
# print(ans)
position = calculatePosition(ans)
value = l[ans]*l[ans+1]
heap = [(value,ans,ans+1)] #[(l[i]*l[j],i,j)]
for i in range(ans):
    j = bisect.bisect_right(l,value/l[i])
    # position +=j-i-1
    if j<len(l):
        heapq.heappush(heap,(l[j]*l[i],i,j))

while(position<=midPosition2):
    
    if position==midPosition2:
        print(heap[0],position)
        break
    elif position == midPosition1:
        print(heap[0],position)
    _,i,j = heapq.heappop(heap)
    if j+1<len(l):
        heapq.heappush(heap,(l[i]*l[j+1],i,j+1))
    # if heap become empty or or ans * ans+1<heap[0]
    if len(heap)==0 or l[ans+1]*l[ans+2]<=heap[0][0]:
        ans+=1
        heapq.heappush(heap,(l[ans]*l[ans+1],ans,ans+1))
    position+=1




# test = []
# for i in range(len(l)-1):
#     for j in range(i+1,len(l)):
#         test.append(l[i]*l[j])
# test.sort()
# # print(test)
