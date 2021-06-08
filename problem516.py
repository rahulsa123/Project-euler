
"""
939087315

real	15m44.484s
user	15m41.433s
sys	0m1.344s

"""
from prime import is_prime


l = [1]
limit = 10**12
p2,p3,p5 = [0]*3
prime = [2]
while(True):
	ref = min(l[p2]*2,l[p3]*3,l[p5]*5)
	if ref>limit:
		break
	l.append(ref)
	if ref+1<= limit and  is_prime(ref+1):
		prime.append(ref+1)
	if ref==l[p2]*2:
		p2+=1
	if ref==l[p3]*3:
		p3+=1
	if ref==l[p5]*5:
		p5+=1

import bisect
ans = sum(l)
temp = set()
sum_l = [1]
for i in l[1:]:
	sum_l.append(sum_l[-1]+i)
def calculate(val,index):
	global ans
	if  val>limit:
		return
	if val!=1 and val not in temp:
		sum_ele = limit/val
		sum_index = bisect.bisect_left(l,sum_ele)
		if l[sum_index]==sum_ele:
			sum_index+=1
		# print(val)
		ans+=(val*sum_l[sum_index-1])%4294967296
		temp.add(val)	
	
	if index==len(prime):
		return
	calculate(val*prime[index],index+1)
	calculate(val,index+1)
	

calculate(1,3)

print(ans%4294967296)

