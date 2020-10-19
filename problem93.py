"""

"""

import itertools

def cal(l,ref):
	if len(l)==1:
		if l[0]>0 and l[0] ==int(l[0]):
			ref.add(l[0])
		return
	for pick in [(0,1),(1,2),(2,3)]:
		if  pick[-1]>= len(l):
			break
		# here we select pick's element from l now apply all operation
		# add operation
		cal(l[:pick[0]]+[ (l[pick[0]] + l[pick[1]]) ] + l[pick[1]+1:], ref )		
		# sub operation
		cal(l[:pick[0]]+[ (l[pick[0]] - l[pick[1]]) ] + l[pick[1]+1:], ref )
		# mul operation
		cal(l[:pick[0]]+[ (l[pick[0]] * l[pick[1]]) ] + l[pick[1]+1:], ref )
		# div operation
		if l[pick[1]] !=0 : 
			cal(l[:pick[0]]+[ (l[pick[0]] / l[pick[1]]) ] + l[pick[1]+1:], ref )
max_found = 0
result  = [0,0,0,0]
for d in range(4, 10):
    for c in range(3, d):
        for b in range(2, c):
            for a in range(1, b):
            	ref = set()
            	for com in itertools.permutations([a,b,c,d]):
            		cal(list(com),ref)
            	temp = 0
            	while(temp+1 in ref):
            		temp+=1
            	if max_found < temp:
            		max_found = temp
            		result = a,b,c,d
print(result, max_found)            	