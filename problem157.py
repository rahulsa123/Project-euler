"""
53490

real	0m1.592s
user	0m1.583s
sys	0m0.009s


1/a + 1/b = p/10**n

1/(pa) + 1/(pb) = 1/10**n
p = 1 
all factors count


for 100
				number of factors
4 25.0 29     ->  2
4 5.0 45		> 6
2 25.0 54		>8
2 5.0 70		>8
1 100.0 101		>2
1 50.0 102		>8
1 25.0 104		>8
1 20.0 105		>8
1 10.0 110		>8
1 5.0 120		>16
1 4.0 125		>4
1 2.0 150		>12
1 1.0 200		>12
				-----
				102


"""



result = 20 # of 10
import time
t = time.time()
for power in range(2,10):
	l = [1]
	limit = 10**power
	pointer_2 = 0
	pointer_5 = 0
	while(l[-1]<limit):
		ref_2 = 2*l[pointer_2]
		ref_5 = 5*l[pointer_5]
		if ref_2<ref_5:
			if limit % ref_2 == 0:
				l.append(ref_2)
			pointer_2+=1 
		elif ref_5<ref_2:
			if limit % ref_5 == 0:
				l.append(ref_5)
			pointer_5+=1
		else:
			if limit % ref_5 == 0:
				l.append(ref_5)
			pointer_2+=1
			pointer_5+=1

	import math as m
	total = 0
	for i in range(l.index(2**(int(m.log10(limit))))+1):
		for j in range(i,len(l)):
			if m.gcd(l[i],l[j])==1:
				p = ((l[i]+l[j])*limit)/(l[i]*l[j])
				total+= 2
				for k in range(2,int(m.sqrt(p))+1):
					if p%k == 0:
						total+=2
	# print(power,total, time.time()-t)
	result+=total
print(result) 