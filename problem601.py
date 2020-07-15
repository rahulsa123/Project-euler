prime = [2,3,5,7,11,13,17,19,23,29,31]
l = [[2,0],[3,0],[5,0],[7,0],[11,0],[13,0],[17,0],[19,0],[23,0],[29,0],[31,0]]
i = 1
number1 = 1
number2 = 1*2
limit = 4**i 
# lamabda function for calculation
f = lambda limit,number1,number2:(limit//number1 - (1 if limit%number1==0 else 0))-(limit//number2 \
	- (1 if limit%number2==0 else 0)) -\
	 (1 if limit%(number1*number2)==0 else 0)

total = f(4**1,number1,number2)
for i in range(2,32):
	ref = i
	for p in range(len(prime)):
		if ref%prime[p]==0:
			power=0
			while ref%prime[p]==0:
				power+=1
				ref//=prime[p]
			l[p][1] = l[p][1] if l[p][1]>=power else power
		if ref==1:
			break
	limit = 4**i
	num1 = 1
	for ref in l:
		num1*=ref[0]**ref[1]
	ref = i+1
	number1 = num1
	for p in range(len(prime)):
		if ref%prime[p]==0:
			power=0
			while ref%prime[p]==0:
				power+=1
				ref//=prime[p]
			if l[p][1]<power:
				num1*=l[p][0]**(power-l[p][1])
		if ref==1:
			break
	number2 = num1
	total+=f(4**i,number1,number2)
print(total)