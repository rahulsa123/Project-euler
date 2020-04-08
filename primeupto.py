def prime(n):
    sieveBond = (n-1)//2 
    sieve = [False]+[True]*sieveBond 
    crosslimit = int((n**0.5-1)/2)
    for i in range(1,crosslimit+1):
        if sieve[i]:
            for j in range(2*i*(i+1),sieveBond, 2*i+1):
                sieve[j]=False 
    return
    return  [2]+[2*i+1 for i in range(1,sieveBond) if sieve[i]] 
# in place of this let do 6i +- 1 method
def prime_fast(n):
	sieveBond = (n//6)+1
	sieve = [0]*sieveBond 
	crosslimit = int((n**0.5+1)/6)
	"""
	 here in array we store four value
	 	1. 0 means 6i+1 and 6i-1 both are prime
	 	2. 1 means 6i+1 is not prime
	 	3. -1 means 6i-1 is not prime
	 	4. 2 means 6i+1 and 6i-1 both are not prime
	"""
	test1 = [0,1]
	test2 = [0,5]
	for i in range(1,crosslimit+1):
		if sieve[i]!=5 and sieve[i]!=6:
			# means 6i+1 is prime 
			p = 6*i-1
			for j in range(p*p,n,2*p):
				ref = j%6
				if ref == 1 and sieve[j//6] in test2:
					sieve[j//6]+=ref
				if ref == 5 and (sieve[j//6+1] in test1 ):
					sieve[j//6+1]+=ref  
		if sieve[i]!=1 and sieve[i]!=6:
			# means 6i+1 is prime 
			p = 6*i+1
			for j in range(p*p,n,2*p):
				ref = j%6
				if ref == 1 and (sieve[j//6] in test2 ):
					sieve[j//6]+=ref
				if ref == 5 and (sieve[j//6+1] in test1 ):
					sieve[j//6+1]+=ref
	return
	from collections import deque
	prime = deque([2,3])
	#print(sieveBond)
	for i in range(1,sieveBond):
		if sieve[i] in test1:
			prime.append(6*i-1)
			#print(6*i-1)
		if sieve[i] in test2:
			prime.append(6*i+1)
			#print(6*i+1)
		#print(i)
	for index, value in enumerate(sieve):
		pass
		#print(index, value)
	#print(prime)
	return list(prime)
pri = prime(10**8)
#test = prime_fast(10**8)
#print(len(pri), len(test), set(test).difference(set(pri)),set(pri).difference(set(test)))