"""
322303240771079935

real	0m53.198s
user	0m52.920s
sys	0m0.320s
"""


from prime import prime
import math
import array 
prime = array.array("I",prime(5097381))
def primeArray(LineNumber):
	ref = array.array("B",[1]*(LineNumber))
	endPoint = (LineNumber*(LineNumber+1))//2
	startPoint = endPoint-LineNumber+1
	for i in prime:
		if i**2 > endPoint:
			break
		for primeMul in range(i * math.ceil(startPoint/i), i*(endPoint//i)+1, i):
			ref[primeMul-startPoint] = 0
	return ref

def getResult(LineNumber):
	pre_pre_array = primeArray(LineNumber-2)
	pre_array = primeArray(LineNumber-1)
	cur_array = primeArray(LineNumber)
	next_array = primeArray(LineNumber+1)
	next_next_array = primeArray(LineNumber+2)

	#  set pre_array with number of prime neighbours from same row or from pre_pre_array
	for i in range(len(pre_array)):
		if pre_array[i]==0:
			continue
		# if i==1:
		# 	breakpoint()
		if i!=len(pre_pre_array) and pre_pre_array[i]>0:
			pre_array[i]+=1
		if i!=0:
			if pre_array[i-1]>0:
				pre_array[i]+=1
			if pre_pre_array[i-1]>0:
				pre_array[i]+=1
			pre_array[i]+=cur_array[i-1]
		if i<len(pre_array)-1 and pre_array[i+1]>0:
			pre_array[i]+=1
		if i+1<len(pre_pre_array) and pre_pre_array[i+1]>0:
			pre_array[i]+=1
		pre_array[i]+=cur_array[i]+cur_array[i+1]

	#  set next_array with number of prime neighbours from same row or from next_next_array
	for i in range(len(next_array)):
		if next_array[i]==0:
			continue
		if next_next_array[i]>0:
			next_array[i]+=1
		if i!=0:
			if next_array[i-1]>0:
				next_array[i]+=1
			if next_next_array[i-1]>0:
				next_array[i]+=1
			next_array[i]+=cur_array[i-1]
		if i==len(next_array)-1 and next_array[i+1]>0:
			next_array[i]+=1
		if  next_next_array[i+1]>0:
			next_array[i]+=1
		if i<len(cur_array):
			next_array[i]+=cur_array[i]
		if i<len(cur_array)-1:
			next_array[i]+=cur_array[i+1]

	endPoint = (LineNumber*(LineNumber+1))//2
	startPoint = endPoint-LineNumber+1
	# print(pre_array)
	# print(cur_array)
	# print(next_array)
	# print(next_next_array)
	s=0
	for i in range(len(cur_array)):
		if cur_array[i]==0:
			continue
		included = 0
		if i<len(pre_array):
			included+=pre_array[i]
		included+=next_array[i]+next_array[i+1]
		if i!=0:
			included+=cur_array[i-1]+pre_array[i-1]+next_array[i-1]

		if i!=len(cur_array)-1:
			included+=cur_array[i+1]
		if i<len(cur_array)-2:
			included+=pre_array[i+1]
		if included>2:
			s+=(startPoint+i)
			# print(startPoint+i)
	return s


print(getResult(5678027)+getResult(7208785))



