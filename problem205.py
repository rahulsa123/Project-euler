total=0
p=[0]*37
for p0 in [1,2,3,4]:
	for p1 in [1,2,3,4]:
		for p2 in [1,2,3,4]:
			for p3 in [1,2,3,4]:
				for p4 in [1,2,3,4]:
					for p5 in [1,2,3,4]:
						for p6 in [1,2,3,4]:
							for p7 in [1,2,3,4]:
								for p8 in [1,2,3,4]:
									p[p0+p1+p2+p3+p4+p5+p6+p7+p8]+=1

#print(p)
c=[0]*37
for c0 in [1,2,3,4,5,6]:
	for c1 in [1,2,3,4,5,6]:
		for c2 in [1,2,3,4,5,6]:
			for c3 in [1,2,3,4,5,6]:
				for c4 in [1,2,3,4,5,6]:
					for c5 in [1,2,3,4,5,6]:
						c[c2+c3+c4+c5+c1+c0]+=1
#print(c)
count = 0
for i in range(9,37):
    for j in range(6,i):
        count+=p[i]*c[j]
print(round(count/(4**9*6**6),7))

