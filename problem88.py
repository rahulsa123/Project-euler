"""
first find max num where it's squre and sum is equal to max_limit
a*a = a+a+(a*a-2*a) = 12000
let k is limit then eq
k**2 - 2*k + 2 = 12000
k = 110
then using recursion like
2*2*2*2
2*2*2*3
2*2*2*4 .....
"""
max_limit = 12000
result = dict()
def calculate(start, num, mul, sum):
    global result
    if mul-sum+num>max_limit:
        return
    if num>1:
        result.setdefault(mul - sum + num, mul)
        result[mul-sum+num]= min(result[mul - sum + num], mul)
    i=start
    while(True):
        if mul*i-(sum+i)+(num+1)>max_limit:
            return
        calculate(i, num+1, mul*i, sum+i)
        i+=1

for i in range(2,110+1):
    calculate(start=i, num=1, mul=i, sum=i)
total = 0
for i in set(result.values()):
    total += i
print(total)
