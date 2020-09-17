import requests
import bisect 
import time
url = "https://projecteuler.net/project/resources/p098_words.txt"
data = str(requests.get(url).content)[2:-1]

data = list(map(lambda x: x[1: -1], data.split(",")))

words = []
t1 = time.time()
for word in data:
	ref = "".join(sorted(word))
	index = bisect.bisect_left(words,[ref,word])
	# if word == "BOARD":
	# 	breakpoint()
	if index<len(words):
		if words[index][0]==ref:
			words[index].append(word)
			continue
	if index-1!= -1 and words[index-1][0]==ref:
		words[index-1].append(word)
		continue
	words.insert(index, [ref, word])

del data
# for word_len in sorted(words.keys(), reverse=True):
#     if len(words[word_len]) < 1:
#         continue
#     for r in range(int(10**(word_len*0.5-1))+1, int(10**(word_len**0.5))):


result = []
for number_of_digit in range(2,10):
	minimum = 10**(number_of_digit-1)
	maximum = 10**(number_of_digit)-1
	test = []
	for i in range(int(minimum**0.5),int(maximum**0.5)+1):
		ref = i**2
		
		if ref<minimum:
			continue
		if ref>maximum:
			break
		ref2 = "".join(sorted(str(ref)))
		index = bisect.bisect_left(test,[ref2,ref])
		if index<len(test):
			if test[index][0]==ref2:
				test[index].append(ref)
				continue
		if index-1!= -1 and test[index-1][0]==ref2:
			test[index-1].append(ref)
			continue
		test.insert(index, [ref2, ref])
	
	for i in test:
		if(len(i)>2):
			result.append(i)

maximum = 1
def check(word1, word2):
	global maximum
	unique_char = len(set(word1))
	for nums in result:
		if len(nums[0])<len(word1):
			# too small
			continue
		if len(nums[0])>len(word1):
			# too big
			break
		if len(set(nums[0]))==unique_char:
			for num in nums[1:]:
				char_dict = dict()
				match = False
				continueing = False
				num = str(num)
				for i in range(len(word1)):
					if word1[i] not in char_dict:
						char_dict[word1[i]] = num[i]
						continue
					if char_dict[word1[i]] != num[i]:
						continueing = True
						break
				if continueing:
					continue
				next_num = ""
				for char in word2:
					next_num +=char_dict[char]
				if int(next_num) in nums[1:]:
					match = True
				if match:
					maximum = max(maximum,int(num), int(next_num))
					return


for words_list in words:
	for first_word_index in range(1,len(words_list)-1):
		for second_word_index in range(first_word_index+1,len(words_list)):
			
			check(words_list[first_word_index],words_list[second_word_index])
	
print(maximum, time.time()-t1)