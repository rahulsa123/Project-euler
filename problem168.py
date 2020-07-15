'''
59206

real    0m0.059s
user    0m0.054s
sys 0m0.004s

here use reverse multiplication for calculation

'''


total=0
limit = 100
import math

def calculate(last_digit,mul,next_digit,ref,length,result,pre_z):
    if length>limit:
        return
    # checking next_digit == last_digit and remainder ==0 and pre_digit==0  and length!=1 means not taking 1,2,3,4..
    if next_digit==last_digit and ref==0 and pre_z!=0 and length!=1:
        global total
        #print(result[1:])
        total+=int(result[1:])
        if total>10**5:
            total-=10**5
    x=(next_digit*mul+ref)
    pre_z=next_digit
    next_digit=x%10
    ref=x//10
    if len(result)<6:
        result = str(next_digit)+ result
    calculate(last_digit,mul,next_digit,ref,length+1,result,pre_z)


for last_digit in range(1,10):
    for mul in range(1,10):
        calculate(last_digit,mul,next_digit=(last_digit*mul)%10,ref=(last_digit*mul)//10,length=1,result=str((last_digit*mul)%10)+str(last_digit),pre_z=last_digit)

print(total)