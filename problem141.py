total = 0
import tqdm
for i in (range(2,10000)):
	
	
	for d in range(2,i):
		r = (i%d)**2%d
		q = int(i/d * i)
		if q**2 ==d*r or d**2 == q*r or r**2 ==d*q:
			total+=i**2
			print(i,num,d,q,r)
			break
	else:
		pass
print(total)