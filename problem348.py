"""
1004195061

real	1m47.447s
user	1m47.354s
sys	0m0.016s

"""

total = 0
count = 0
num = 10
from math import sqrt
cube = [x**3 for x in range(2000)]
while True:
	num_str = str(num)
	ref1,ref2 = int(num_str+num_str[::-1]), int(num_str+num_str[-2::-1])
	w1, w2 = 0 , 0
	for i in range(1,int(ref1**(1/3))):
		temp1 = sqrt(ref1-cube[i])
		if temp1== int(temp1):
			w1+=1
	for i in range(1,int(ref2**(1/3))):
		temp2 = sqrt(ref2-cube[i])
		if temp2== int(temp2):
			w2+=1
	if w1 == 4:
		total+=ref1
		count+=1
	if w2==4:
		total+=ref2
		count+=1
	if count==5:
		print(total)
		break
	num+=1


