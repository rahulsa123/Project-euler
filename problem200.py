"""
229161792008

real	0m0.590s
user	0m0.531s
sys	0m0.037s

"""


from prime import prime ,is_prime
prime_list = prime(10**6)
ref_list = [[72,2,1]] # [value(p**3*q**2),prime (P**3), index value for q**2]

for i in prime_list[1:]:
	ref_list.append([i**3*4,i,0])

import heapq 
heapq.heapify(ref_list)
def checking(n):
	# first last digit replacement
	ref = n-(n%10) 
	prime_found = is_prime(ref+1) or is_prime(ref+3) or is_prime(ref+7) or is_prime(ref+9)
	if n%2==0 or n%5==0:
		return not prime_found
	# now check for all digits except last one
	ref = str(n)
	temp = list("0123456789")
	for i in range(len(ref)-1):
		for j in temp:
			if is_prime(int(ref[:i]+j+ref[i+1:])):
				return False
	return True


count = 1
ans = 0
while(count<=200):
	temp = heapq.heappop(ref_list)
	if "200" in str(temp[0]) and checking(temp[0]):
		ans = temp[0]
		count+=1
	temp[2]+=1 if prime_list[temp[2]+1]!=temp[1] else 2 # for distinct prime
	temp[0] = temp[1]**3 * prime_list[temp[2]]**2
	heapq.heappush(ref_list, temp)
print(ans)