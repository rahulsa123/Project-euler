"""
two things found in series
1) next value of n is equal to present found value of m
2) next value of m is > 4 times of value of n

"""
import math
n = 1
count, total = 0,0
while(True):
	m=4*n+ (1 if n%2==0 else 0) #  2 condition (if else for make sure odd even case)
	while (True):
		if math.gcd(m,n)==1:
			a, b = 2*m*n, m**2-n**2
			if abs(b-2*a)==1 or abs(a-2*b)==1:
				total+=m**2+n**2
				count+=1
				n=m     # 1 condition
				#print(f"count ={count}, h= {m**2+n**2}, a= {a},b= {b},m= {m},n= {n}")
				break
		m+=2
	if count==12:
		break
print("ans ",total)
