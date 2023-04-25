"""
21210
2*3*5*7*1  is also counted

"""
from prime import get_number,prime
from collections import deque
import math as m
l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 
    67, 71, 73, 79, 83, 89, 97]
limit = 10**6
total = 0
test = []
prime = prime(limit//210)[25:]

def calculate(index,ref_list):
    

    temp = 1
    for i in ref_list:
        temp*=i 
    if temp>=limit:
        return
    # if len(ref_list) >3 then calculate all multiple
    if len(ref_list)>3:
        # increment total by 1 for current temp
        global total,test
        # print(temp)
        # input()
        total+=1
        for i in get_number(ref_list+prime,10**9):
            if temp*i<limit:
                # print(temp,i,ref_list,temp*i)
                # input()
                total+=1
                continue
            break
    for i in range(index,len(l)):
        calculate(i+1,ref_list+[l[i]])


